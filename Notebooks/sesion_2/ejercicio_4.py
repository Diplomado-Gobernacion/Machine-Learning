from PIL import Image
import numpy as np

imagen = Image.open('../images/koala.jpg')
im = np.array(imagen)

im_trim = im[30:250, 250:550]

img = Image.fromarray(im_trim)
img.show()

