#-*- coding:utf-8 -*-
from .avc_common import Common_AVC
from airtest.core.api import *
from PIL import Image
import cv2 as cv
from datetime import datetime
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/bin/tesseract'
connect_device("ios:///http://127.0.0.1:8100")
# connect_device("Android:///")
from common import avc_constance as ac
from poco.drivers.ios import iosPoco
poco = iosPoco()
auto_setup(__file__)

class IOS_AVC(Common_AVC):
    def __init__(self):
        self.interval =2

    def goMine(self):
        poco("mine").click()

    def back(self):
        poco("back").click()

    def updateNickname(self,nickname):
        btn_nickName = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child("Button")[1]
        btn_nickName.click()
        poco("TextField").click()
        poco("全选").click()
        poco("剪切").click()
        text(nickname)

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
        touch(Template('resource/images/tpl1568100069708.png'))

    def joinChannel(self,roomName,password):
        self.setRoomName(roomName)
        self.setPassword(password)
        poco("加入").click()
        wait(Template(r"resource/images/tpl1568189862382.png", record_pos=(0.0, 0.811), resolution=(750, 1334)))
        print(">>>>>>>>>>Join Channel Success>>>>>>>>")

    def leaveChannel(self):
        poco("hang up").click()
        print(">>>>>>>>>>Leave Channel Success>>>>>>>>")

    def muteVideoInchannel(self):
        if poco("video off").exists():
            print("video already mute")
        else:
            poco("video on").click()

    def unmuteVideoInchannel(self):
        if poco("video on").exists():
            print("video already unmute")
        else:
            poco("video off").click()

    def muteAudioInchannel(self):
        if  poco("audio off").exists():
            print("audio already mute")
        else:
            poco("audio on").click()

    def unmuteAudioInchannel(self):
        if poco("audio on").exists():
            print("audio already unmute")
        else:
            poco("audio off").click()

    def setVideoResolution(self,resolution):
        '''
        :param resotion: 0:240P, 1:360P(默认),  2:480P
        '''

        if resolution == ac.Video_Resolution.video_240P:
            poco("240P").click()
        elif resolution == ac.Video_Resolution.video_360P:
            poco("360P").click()
        elif resolution == ac.Video_Resolution.video_480p:
            poco("480P").click()
        else:
            raise ValueError("[Fail] Resolution is not supported : %s" % resolution)

    def preMuteVideo(self):
        if poco("video off").exists():
           print("video already mute")
        else:
            poco("video join").click()

    def preUnmuteVideo(self):
        if poco("video join").exists():
           print("video already unmute")
        else:
            poco("video off").click()

    def preMuteAudio(self):
        if poco("audio off").exists():
            print("audio already muted")
        else:
            poco("audio join").click()

    def preUnmuteAudio(self):
        if poco("audio join").exists():
            print("audio already unmute")
        else:
            poco("audio off").click()

    def sendMessage(self,msg):
        poco("message").click()
        poco("TextField").click()
        text(msg)

    def copyHistroyMessageAndSend(self):
        touch([100,100])
        poco("TextView").long_click(duration=2)
        poco("拷贝").click()
        for i in range(2):
            poco("TextField").click()
        poco("粘贴").click()
        poco("Send").click()


    def goToParticipantList(self):
        poco("participants").click()


    def goSettingInChannel(self):
        poco("Button").click()
        sleep(self.interval)

    def applyToHost(self):
        if poco("放弃主持人权限").exists():
            print("You are already the host")
        else:
            poco("申请成为主持人").click()
            assert poco("放弃主持人权限").exists()

    def giveUpHost(self):
        if poco("申请成为主持人").exists():
            print("You are not the host")
        else:
            poco("放弃主持人权限").click()
            assert poco("无").exists()

    def changeRoomPassword(self,pwd):
        if poco("申请成为主持人").exists() or poco("放弃主持人权限").exists():
            poco("房间密码").click()
            poco("TextField").click()
            poco("全选").click()
            poco("剪切").click()
            text(pwd)
        else:
            raise TimeoutError("You are not the host!")

    def uploadLog(self):
        '''
            网络不好，上传时间会变长，可能会失败
        '''
        poco("上传日志").click()
        time = str(datetime.utcnow())
        wait(Template(r"resource/images/tpl1568205469989.png", record_pos=(0.003, -0.489), resolution=(750, 1334)))
        print("日志上传时间:%s" % time)

