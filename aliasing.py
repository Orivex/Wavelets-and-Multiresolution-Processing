import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

image = np.zeros((100, 100))
image[:, ::2] = 1.0  

aliased_image = image[::2, ::2]

smoothed_image = gaussian_filter(image, sigma=1.0)

decimated_image = smoothed_image[::2, ::2]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image, cmap='gray', interpolation='nearest')
axes[0].set_title("Original (100x100)\n")

axes[1].imshow(aliased_image, cmap='gray', interpolation='nearest')
axes[1].set_title("Naive Downsampling (50x50)\nALIASING")

axes[2].imshow(decimated_image, cmap='gray', interpolation='nearest')
axes[2].set_title("Proper Decimation (50x50)\n ANTI-ALIASING")

plt.tight_layout()

plt.savefig("images/aliasing.png", format="png", bbox_inches="tight")

plt.show()