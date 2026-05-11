"""Remove white background from PNG image, making it transparent."""
from PIL import Image
import numpy as np

img = Image.open('media/products/caperpngpic.png').convert('RGBA')
data = np.array(img)

# Make white/near-white pixels transparent (threshold: R>230, G>230, B>230)
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
white_mask = (r > 230) & (g > 230) & (b > 230)
data[:,:,3][white_mask] = 0  # Set alpha to 0 for white pixels

# Smooth edges - make near-white pixels semi-transparent
near_white = (r > 200) & (g > 200) & (b > 200) & ~white_mask
data[:,:,3][near_white] = 128

result = Image.fromarray(data)
result.save('media/products/caperpngpic.png')
print('Done! White background removed from caperpngpic.png')
