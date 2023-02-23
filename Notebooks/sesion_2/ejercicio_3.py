from PIL import Image
import numpy as np

imagen = Image.open('../images/koala.jpg')
imagen = imagen.convert('L')
im = np.array(imagen)
img1 = Image.fromarray(im)
img1.show()

im = np.asarray(imagen.resize((150, 150)))
img2 = Image.fromarray(im)
img2.show()