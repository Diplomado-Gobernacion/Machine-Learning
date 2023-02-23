from PIL import Image
#from numpy import asarray
import numpy as np

imagen = Image.open('../images/koala.jpg')

#print(imagen.format)
#print(imagen.mode)
#print(imagen.size)

imagen_numpy = np.asarray(imagen)
print(type(imagen_numpy))

## Convertirla de en imagen PIL
imagen2 = Image.fromarray(imagen_numpy)

imagen.show()
imagen2.show()