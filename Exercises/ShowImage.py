import matplotlib.pyplot as plt
from skimage import io

img = io.imread("/Assert/img/pexels-kevin-ku-92347-577585.jpg")
plt.imshow(img)
plt.show()

plt.imshow(
    img[
        3200:3700,
        2600:3400,
    ]
)
plt.show()
