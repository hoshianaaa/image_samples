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

# write circle
# https://qiita.com/miyamotok0105/items/b04fab6598f690fd60ba
for size in size_list:

  width = size[0]
  height = size[1]
  img = np.ones((height,width, 3),np.uint8)*255
  cv2.circle(img,
           center=(int(width/2), int(height/2)),
           radius=150,
           color=(0, 0, 0),
           thickness=-1,
           lineType=cv2.LINE_4,
           shift=0)
  cv2.imwrite(header + 'circle_' + str(width) + '_' + str(height) + '.png',img)


# write circle
# https://qiita.com/miyamotok0105/items/b04fab6598f690fd60ba
for size in size_list:

  width = size[0]
  height = size[1]
  center_x = int(width/2)
  center_y = int(height/2)
  rect_w_half = 100
  rect_h_half = 150
  img = np.ones((height, width, 3),np.uint8)*255
  cv2.rectangle(img,
              pt1=(center_x - rect_w_half, center_y - rect_h_half),
              pt2=(center_x + rect_w_half, center_y + rect_h_half),
              color=(0, 0, 0),
              thickness=-1,
              lineType=cv2.LINE_4,
              shift=0)
  cv2.imwrite(header + 'rectangle_' + str(width) + '_' + str(height) + '.png',img)
