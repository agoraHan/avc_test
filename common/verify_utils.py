#-*- coding:utf-8 -*-
from PIL import Image
from PIL import ImageChops
import cv2 as cv
import numpy as np
import pytesseract
def compare_images(path_one, path_two):
    """
    比较图片
    :param path_one: 第一张图片的路径
    :param path_two: 第二张图片的路径
    :return: 不相同返回 success
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            return "ERROR:替换头像不成功！"
        else:
            return "Success"
    except ValueError as e:
        return "{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!")

