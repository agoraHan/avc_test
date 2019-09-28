#-*- coding:utf-8 -*-
from airtest.core.api import  *
from airtest.core.ios.ios import IOS
import pytest
from common import case_tag,verify_utils
from common.avc_ios import IOS_AVC
from common import avc_constance as ac
from poco.drivers.ios import iosPoco
poco = iosPoco()
class TestIOS:

    def setup(self):
        self.avc = IOS_AVC()
        self.channel_name = "AVCAUTO"
        self.password = "avctest"
        self.packageName = ac.Package_Name.ios_packageName
        self.screeshot_path = "resource/screenshot/"
    def tearDown(self):
        pass

    '''
    获取版本号
    '''
    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_getAppVersion(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        path1 = self.screeshot_path+"getAppVersion_a.jpg"
        path2 = self.screeshot_path+"getAppVersion_b.jpg"
        avc.getScreenshot(path1)
        width,height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1,path2,0,6/7*height,width,height)
        version = avc.getWordsInImage(path2)
        assert version == "V3.1.8 Build 488"

    '''
    nickname长度 <= 18
    '''
    @pytest.mark.parametrize("nickname",["1234567890","qwertyuiopasdfghjk","QWERTYUIOPASDFGHJ","KLZXCVVBNM","l;'zxv c bnm,./","~!@#$%^&()_+"])
    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_updateNickname_01(self,nickname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname(nickname)
        path1 = self.screeshot_path+"test_updateNickname_01a.jpg"
        path2 = self.screeshot_path+"test_updateNickname_01b.jpg"
        avc.getScreenshot(path1)
        width,height= avc.getImageSize(path1)
        avc.getCustomizeImage(path1,path2,1/3*width,1/6*height,width,1.5/6*height)
        words = avc.getWordsInImage(path2)
        cur_nickname = nickname
        assert words == cur_nickname +" >"
        avc.back()

    '''
    nickname长度 > 18
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateNickname_02(self,nickname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname(nickname)
        path1 = self.screeshot_path+"test_updateNickname_02a.jpg"
        path2 = self.screeshot_path+"test_updateNickname_02b.jpg"
        text("1234567890123456789")
        avc.getScreenshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 1/2*width, 1 / 6 * height, width, 1.5 / 6 * height)
        words = avc.getWordsInImage(path2)
        assert words == "123456789012345678 >"


    '''
    更换头像
    '''
    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_updateAvatar(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        path1 = self.screeshot_path+"test_updateAvatar_a.jpg"
        path2 = self.screeshot_path+"test_updateAvatar_b.jpg"
        avc.getScreenshot(filename=path1)
        avc.updateAvatar()
        avc.getScreenshot(filename=path2)
        assert verify_utils.compare_images(path1,path2) == "Success"

    '''
    英文房间名自动大写
    '''
    @pytest.mark.parametrize("roomName",["abcd"])
    @pytest.mark.tags(case_tag.iOS,case_tag.HIGH,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_roomName_01(self,roomName):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setRoomName(roomName)
        touch([100,100])
        path = self.screeshot_path+"test_roomName_01_a.jpg"
        path1 = self.screeshot_path+"test_roomName_01_b.jpg"
        avc.getScreenshot(path)
        width,height=avc.getImageSize(path)
        avc.getCustomizeImage(path,path1,1/5*width,1/3*height,width,1/2*height)
        room_name = avc.getWordsInImage(path1)
        assert  room_name == "ABCD"

    '''
    房间名不能超过18
    '''
    @pytest.mark.parametrize("roomName",["QWERTYUIOPASDFGHJKL","qwertyuiopdashjk","zxcvbnmm","ZXCVBNM<>?!@#$%^&*(","1234567890123456789"])
    @pytest.mark.tags(case_tag.iOS,case_tag.HIGH,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_roomName_02(self,roomName):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setRoomName(roomName)
        touch([100, 100])
        path = self.screeshot_path+"test_roomName_02_a.jpg"
        path1 = self.screeshot_path+"test_roomName_02_b.jpg"
        avc.getScreenshot(path)
        width,height=avc.getImageSize(path)
        avc.getCustomizeImage(path,path1,1/5*width,1/3*height,width,1/2*height)
        room_name = avc.getWordsInImage(path1)
        assert  len(room_name) <= 18

    '''
    密码不能超过18
    '''
    @pytest.mark.parametrize("password", ["1ACV21-_","Tasd_VBG00","qwertyuiopasdfghk","zxcvbm","QWERTYUIOPASDFGHJKL", "ZXCVBNM", "1234567890123456789",",./!@#$%^&*()-+"])
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_password(self, password):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setPassword(password)
        path = self.screeshot_path+"test_password_a.jpg"
        path1 = self.screeshot_path+"test_password_b.jpg"
        avc.getScreenshot(path)
        width,height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1/5*width, 4/9*height, width, 5/9*height)
        pwd = avc.getWordsInImage(path1)
        assert len(pwd) <= 18

    '''输入的房间密码正确可以正常进入会议'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannelWithiCorrectPassword(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(self.channel_name,self.password)
        avc.leaveChannel()

    '''输入的房间密码不正确无法进入会议'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannelWithIncorrectPassword(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(self.channel_name,"error")
        assert poco("Room join failed, incorrect password, ").exists()


    "设置不同的分辨率进入房间"
    @pytest.mark.parametrize("resolution",[ac.Video_Resolution.video_240P,ac.Video_Resolution.video_360P,ac.Video_Resolution.video_480p])
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinChannelWithDifferentReslotion(self,resolution):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.setVideoResolution(resolution=resolution)
        avc.back()
        avc.joinChannel(self.channel_name,self.password)
        sleep(2)
        avc.leaveChannel()

    #查看与会者列表人数
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_checkParticipants(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(self.channel_name,self.password)
        avc.goToParticipantList()
        path = self.screeshot_path+"test_checkParticipants_a.jpg"
        path1 = self.screeshot_path+"test_checkParticipants_b.jpg"
        avc.getScreenshot(filename=path)
        width,height = avc.getImageSize(path)
        avc.getCustomizeImage(path,path1,1/3*width,1/20*height,2/3*width,1/8*height)
        avc.getNumberOfParticipants(path1)
        assert avc.getNumberOfParticipants(path1) == 1

    #会议中发送消息
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_sendMsg(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(self.channel_name,self.password)
        msg= ["qwertyuiopabcdefghijklzxcvbnm","QWERTYUIOPASDFGHJKLZXCVBNM","~!@#$%^&*()_____+~！@￥……（）：「」【】：《》？、。\，","测试消息发送","👌"]
        avc.sendMessage(msg)
        avc.back()
        #todo:校验有多个 用户在会议中 远端是否可以接收到消息



