








from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
logo = Image.open('Logo.png')
logo_array = np.array(logo)
plt.imshow(logo_array)
plt.axis('off')  # 不显示坐标轴
plt.show()