import cv2
import numpy as np
 

# https://mavic.ne.jp/machinevision-cameratype/
size_list = [[640,480],[1392,1040],[1628,1236],[2456,2058],[4008,2672],[4872,3248]]

#ブランク画像
header = "generate_image_"

for size in size_list:

  width = size[0]
  height = size[1]
  blank = np.zeros((height, width, 3))
  cv2.imwrite(header + 'blank_' + str(width) + '_' + str(height) + '.png',blank)
