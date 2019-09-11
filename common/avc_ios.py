#-*- coding:utf-8 -*-
from .avc_common import Common_AVC
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

class IOS_AVC(Common_AVC):
    def __init__(self):
        self.interval =2

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



