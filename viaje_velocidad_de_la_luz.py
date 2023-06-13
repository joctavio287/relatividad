import numpy as np, os, matplotlib.pyplot as plt
from PIL import Image
from core.config_builder import Parser, guarda_pkl, carga_pkl

# Importo las variables
variables = Parser(configuration='viaje_velocidad_de_la_luz').config()
img_path = os.path.join(variables['input_path'], 'playa.png')
imagen = np.asarray(Image.open(fp=img_path))
 
# 
colores = {0:'Reds', 1:'Greens', 2:'Blues'}
for i in range(3):
    plt.figure(tight_layout=True)
    plt.imshow(X=imagen[:,:,i], cmap=colores[i])
    plt.show(block=False)