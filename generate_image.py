import cv2
import numpy as np
 

# https://mavic.ne.jp/machinevision-cameratype/
size_list = [[640,480],[1392,1040],[1628,1236],[2456,2058],[4008,2672],[4872,3248]]

#ブランク画像
header = "generate_image_"

for size in size_list:

  width = size[0]
  height = size[1]
  img = np.zeros((height, width, 3))
  cv2.imwrite(header + 'blank_' + str(width) + '_' + str(height) + '.png',img)

# white image
# https://qiita.com/miyamotok0105/items/b04fab6598f690fd60ba
for size in size_list:

  width = size[0]
  height = size[1]
  img = np.ones((height,width, 3),np.uint8)*255
  cv2.imwrite(header + 'white_' + str(width) + '_' + str(height) + '.png',img)
