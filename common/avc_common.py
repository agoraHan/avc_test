#-*- coding:utf-8 -*-
from airtest.core.api import *
from PIL import Image
import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'
connect_device("ios:///http://127.0.0.1:8100")
# connect_device("Android:///")
from poco.drivers.ios import iosPoco
poco = iosPoco()
auto_setup(__file__)

class Common_AVC:
    def __init__(self):
        self.interval = 2

    def setCurrentDevice(self,device):
        set_current(device)

    def startAVC(self,packageName):
        start_app(packageName)
        wait(Template(r"resource/images/tpl1568100069708.png", record_pos=(0.003, -0.54), resolution=(750, 1334)),5)
        sleep(self.interval)

    def getScreenSize(self):
        width,height = poco.get_screen_size()
        return width,height

    def getScreenshot(self,filename):
        snapshot(filename)

    def getImageSize(self,img_path):
        img = Image.open(img_path)
        width = img.size[0]
        height = img.size[1]
        print("width:%s,height:%s" % (width, height))
        return width,height

    def getCustomizeImage(self,origin_image_path, new_image_path, left, upper, right, lower):
        """
        :param origin_image_path: 原始图片的路径
        :param new_image_path: 图片裁剪后的路径
        :param left: 左 坐标
        :param upper: 上 坐标
        :param right: 右 坐标
        :param lower: 下 坐标
        :return:
        """
        img = Image.open(origin_image_path)
        cropped = img.crop((left, upper, right, lower))
        cropped.save(new_image_path)

    def getWordsInImage(self,image_path):
        '''
        :param image_path: 图片路径
        :return: 返回识别的文本内容
        '''
        '''
        部分内容会识别出错："^"->"*","Q"->"[","c"-"e"
        '''
        img = cv.imread(image_path)
        text = pytesseract.image_to_string(Image.fromarray(img))
        return text
