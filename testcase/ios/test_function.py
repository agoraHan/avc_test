#-*- coding:utf-8 -*-
from airtest.core.api import  *
import pytest
from common import case_tag,verify_utils
from common.avc_ios import IOS_AVC
from poco.drivers.ios import iosPoco
poco = iosPoco()
class TestIOS:

    def setup(self):
        self.avc = IOS_AVC()
        self.channel_name = "AVCAUTO"
        self.password = "avctest"
        self.packageName = "io.agora.videocall"

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
        path1 = "resource/screenshot/getAppVersion_a.jpg"
        path2 = "resource/screenshot/getAppVersion_b.jpg"
        avc.getScreenshot(path1)
        width,height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1,path2,0,5/6*height,width,height)
        version = avc.getWordsInImage(path2)
        assert version == "V3.1.8 Build 488"

    '''
    nickname长度 <= 18
    '''
    @pytest.mark.parametrize("nickname",["1234567890","qwertyuiopasdfghjk","Q WERTYUIOPASDFGHJ","KLZXCVVBNM","l;'zxv c bnm,./","~!@#$%^&*())_+"])
    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_updateNickname_01(self,nickname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname()
        path1 = "resource/screenshot/test_updateNickname_01a.jpg"
        path2 = "resource/screenshot/test_updateNickname_01b.jpg"
        text(nickname)
        avc.getScreenshot(path1)
        width,height= avc.getImageSize(path1)
        avc.getCustomizeImage(path1,path2,1/2*width,1/6*height,width,1.5/6*height)
        words = avc.getWordsInImage(path2)
        cur_nickname = nickname
        assert words == cur_nickname +" >"
        poco("back").click()

    '''
    nickname长度 > 18
    '''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_updateNickname_02(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.updateNickname()
        path1 = "resource/screenshot/test_updateNickname_02a.jpg"
        path2 = "resource/screenshot/test_updateNickname_02b.jpg"
        text("1234567890123456789")
        avc.getScreenshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 1/2*width, 1 / 6 * height, width, 1.5 / 6 * height)
        words = avc.getWordsInImage(path2)
        assert words == "123456789012345678 >"
        poco("back").click()

    '''
    更换头像
    '''
    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM,case_tag.AUTOMATED,case_tag.FUNCTIONALITY)
    def test_updateAvatar(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        path1 = "resource/screenshot/test_updateAvatar_a.jpg"
        path2 = "resource/screenshot/test_updateAvatar_b.jpg"
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
        path = "resource/screenshot/test_roomName_01_a.jpg"
        path1 = "resource/screenshot/test_roomName_01_b.jpg"
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
        path = "resource/screenshot/test_roomName_02_a.jpg"
        path1 = "resource/screenshot/test_roomName_02_b.jpg"
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
        touch([100, 100])
        path = "resource/screenshot/test_password_a.jpg"
        path1 = "resource/screenshot/test_password_b.jpg"
        avc.getScreenshot(path)
        width,height = avc.getImageSize(path)
        avc.getCustomizeImage(path, path1, 1/5*width, 4/9*height, width, 7/9*height)
        pwd = avc.getWordsInImage(path1)
        assert len(pwd) <= 18

    "进退房间"
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinLeaveChannel(self):
        avc = self.avc
        roomName = self.channel_name
        password = self.password
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.setRoomName(roomName)
        avc.setPassword(password)
        touch([100, 100])
        avc.joinChannel()
        sleep(2)
        avc.leaveChannel()

    @pytest.mark.parametrize("msg", [ "1234567890123456789"])
    def test_uploadLog(self,msg):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.sendMessage()
        text(msg)
