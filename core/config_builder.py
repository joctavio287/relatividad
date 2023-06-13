import yaml, argparse, os, pickle

def guarda_pkl(path:str, dic:dict, reescribir:bool=False):
    '''
    Para salvar un diccionario en formato pickle.\n
    INPUT\n
    path:str -> path del diccionario a guardar.
    dic:dict -> diccionario a guardar.
    reescribir:bool -> si reescribimos o no.
    '''
    isfile = os.path.isfile(path)
    if isfile:
        if not reescribir:
            print('Este archivo ya existe, para sobreescribirlo usar el argumento rewrite = True.')
            return
    try:
        with open(file = path, mode = "wb") as archive:
            pickle.dump(file = archive, obj=dic)
        texto = f'Diccionario guardado en: {path}.'
        if isfile:
            texto += f'Atención: se reescribió el archivo {path}'
    except:
        print('Algo fallo cuando se guardaba')
    return

def carga_pkl(path:str):
    '''
    Para cargar un diccionario en formato pickle.\n
    INPUT\n
    path:str -> path del diccionario a leer.
    '''
    isfile = os.path.isfile(path)
    if not isfile:
        print(f'El archivo {path} no existe')
        return
    try:
        with open(file = path, mode = "rb") as archive:
            data = pickle.load(file = archive)
        return data
    except:
        print('Algo fallo')
    return

class Parser:
    '''
    La idea de esta clase es armar un diccionario con variables de interés para una dada configuración.
    '''
    def __init__(self, configuration:str = None) -> None:

        # diccionario donde están todos las configuraciones yamls #TODO #FIXME 
        self.file_path = 'core/parameters/'

        # lista de todas las configuraciones
        self.parameters_list = ', '.join([param.removesuffix('.yaml') for param in os.listdir(self.file_path) if param.endswith('.yaml')])

        # nombre de la configuración
        self.configuration = configuration

    def config(self):

        # en caso de que se corra internamente el programa
        if self.configuration:

            # Construimos las variables de la configuracion
            dic = Parser.configuration_builder(self.file_path, self.configuration)
            return dic

        # si se corre desde la consola (cmd)
        else:
            # crea un parser desde el que se puede elegir la configuración
            parser = argparse.ArgumentParser()

            # crea los argumentos (en help se indica qué hace cada argumento)
            parser.add_argument(
            "config", 
            help = f"Elegir la configuración con la cual correr el modelo: {self.parameters_list}", 
            type = str)

            parser.add_argument(
            "-v", 
            "--verbose", 
            action = "store_true", 
            help = "aumentar la verbosidad")

            args = parser.parse_args()
            
            # Si se pide verbosidad se printea lo siguiente
            if args.verbose:
                print(f"El parámetro elegido es {args.config}.")
            else:
                print(args.config)
            
            # Construimos el diccionario con la dada configuración
            dic = Parser.configuration_builder(self.file_path, args.config)
            return dic
    
    @staticmethod
    def configuration_builder(filepath, config):
        '''
        Loads yaml file
        '''
        file_descriptor = open(filepath + f'{config}'+ '.yaml', "r") 
        data = yaml.load(file_descriptor, Loader = yaml.Loader)
        file_descriptor.close()
        return data

    @staticmethod
    def yaml_dump(filepath, data):
        '''
        Dumps into yaml file
        '''
        file_descriptor = open(filepath, "r") 
        data = yaml.dump(file_descriptor, Dumper = yaml.Dumper)
        file_descriptor.close()
        return data

if __name__ == '__main__':
    p = Parser('default')
    p.config()