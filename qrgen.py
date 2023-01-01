# quick-response code generator

import qrcode

# writing 
img = qrcode.make("https://www.youtube.com/watch?v=EfWlOmGEfvU&t=57s")
img.save("lbj_hype_plays.jpg")

img = qrcode.make("This could be a wifi password. Boston in 7. 2022 NBA Finals")
img.save("celtics.jpg")

# reading
# import cv2
# d = cv2.QRCodeDetector()
# val, points, straight_qrcode = d.detectAndDecode(cv2.imread("yoda.jpg"))
# print(val)