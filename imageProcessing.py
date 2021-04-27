# -*- coding:utf-8 -*-
import cv2
import numpy as np


def showRGBImage():
    """
    生成并显示三张纯蓝绿红尺寸为300X300的图片
    """
    # ----------------蓝色通道值---------------
    blue = np.zeros((300, 300, 3), dtype=np.uint8)
    blue[:, :, 0] = 255
    print("blue=\n", blue)
    cv2.imshow("blue", blue)
    # ----------------绿色通道值---------------
    green = np.zeros((300, 300, 3), dtype=np.uint8)
    green[:, :, 1] = 255
    print("red=\n", )
    cv2.imshow("green", green)
    # ----------------红色通道值---------------
    red = np.zeros((300, 300, 3), dtype=np.uint8)
    red[:, :, 2] = 255
    print("red=\n", red)
    cv2.imshow("red", red)
    cv2.waitKey()
    cv2.destroyAllWindows()


def changeImageRGB():
    """
    生成显示红绿蓝三色的300X300图片
    """
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    img[:, 0:100, 0] = 255
    img[:, 100:200, 1] = 255
    img[:, 200:300, 2] = 255
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def showRandomImage():
    img = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
    cv2.imshow("demo", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def setRandomImage():
    img = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
    for i in range(10, 100):
        for j in range(80, 100):
            img.itemset((i, j), 255)
    cv2.imshow("demo", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
