#-*- coding:utf-8 -*-
from airtest.core.api import *

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
        text("name")
        assert_exists(Template(r"resource/images/tpl1568034222130.png", record_pos=(0.345, -0.508), resolution=(750, 1334)), "修改成功")
        poco("back").click()

    def updateAvatar(self):
        btn_avatar = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child("Button")[0]
        btn_avatar.click()
        poco("相机").click()
        touch(Template(r"resource/images/tpl1568115823545.png", record_pos=(-0.005, 0.747), resolution=(750, 1334)))
        poco("使用照片").click()

    def getScreenSize(self):
        width,height = poco.get_screen_size()
        print("width:%s,height:%s"%(width,height))

    def getScreenshot(self,filename):
        snapshot(filename)

