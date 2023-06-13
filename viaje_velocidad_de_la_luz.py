import numpy as np, os, matplotlib.pyplot as plt
from PIL import Image
from core.config_builder import Parser, guarda_pkl, carga_pkl

def angulo_a_rango_pixel(angulo:float, imagen:np.ndarray, unidades:str='rad'):
    '''
    Transforma ángulos a rangos de np.ndarray (píxeles en la imagen).\n
    INPUT\n
    angulo:float --> ángulo de la imagen

    '''
    if unidades=='rad':
        angulo_por_pixel = (2*np.pi)/imagen.shape[1]
        return imagen[:,:int(angulo//angulo_por_pixel),:]
    elif unidades=='deg':
        angulo_por_pixel = (2*np.pi)/imagen.shape[1]
        return imagen[:,:int(angulo//angulo_por_pixel),:]
    else:
        print("Esas unidades no existen. Sólo se pueden usar 'deg' o 'rad'")

# Importo las variables
variables = Parser(configuration='viaje_velocidad_de_la_luz').config()
img_path = os.path.join(variables['input_path'], 'playa.png')
imagen = np.asarray(Image.open(fp=img_path))


colores = {0:'Reds', 1:'Greens', 2:'Blues'}
for i in range(3):
    plt.figure(tight_layout=True)
    plt.imshow(X=angulo_a_rango_pixel(np.pi*2, imagen=imagen)[:,:,i], cmap=colores[i])
    plt.show(block=False)