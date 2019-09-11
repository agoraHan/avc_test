#-*- coding:utf-8 -*-
from airtest.core.api import *
from PIL import Image
from PIL import ImageChops
import cv2 as cv
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'
connect_device("ios:///http://127.0.0.1:8100")
# connect_device("Android:///")
from poco.drivers.ios import iosPoco
poco = iosPoco()
auto_setup(__file__)

class IOS_AVC:
    def __init__(self):
        self.interval = 2


    def setCurrentDevice(self,device):
        set_current(device)

    def startAVC(self):
        start_app("io.agora.videocall")
        wait(Template(r"resource/images/tpl1568100069708.png", record_pos=(0.003, -0.54), resolution=(750, 1334)),5)
        sleep(self.interval)

    def updateNickname(self):
        poco("mine").click()
        btn_nickName = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child("Button")[1]
        btn_nickName.click()
        poco("TextField").click()
        poco("全选").click()
        poco("剪切").click()


    def updateAvatar(self):
        btn_avatar = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child("Button")[0]
        btn_avatar.click()
        poco("相机").click()
        touch(Template(r"resource/images/tpl1568115823545.png", record_pos=(-0.005, 0.747), resolution=(750, 1334)))
        poco("使用照片").click()

    def setRoomName(self,roomName):
        # touch(Template(r"resource/images/tpl1568185999017.png", record_pos=(0.023, -0.149), resolution=(750, 1334)))
        poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("TextField")[0].click()
        text(roomName, enter=False)

    def setPassword(self,password):
        poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("TextField")[1].click()
        text(password,enter=False)

    def joinChannel(self):
        poco("加入").click()
        wait(Template(r"resource/images/tpl1568189862382.png", record_pos=(0.0, 0.811), resolution=(750, 1334)))

    def leaveChannel(self):
        poco("hang up").click()
        wait(Template(r"resource/images/tpl1568100069708.png", record_pos=(0.003, -0.54), resolution=(750, 1334)),5)

    def muteVideoInchannel(self):
        poco("video on").click()

    def unmuteVideoInchannel(self):
        poco("video off").click()

    def muteAudioInchannel(self):
        poco("audio on").click()

    def unmuteAudioInchannel(self):
        poco("audio off").click()


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
