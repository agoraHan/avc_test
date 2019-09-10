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

    def tearDown(self):
        pass

    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM)
    def test_updateNickname(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC()
        avc.updateNickname()

    @pytest.mark.tags(case_tag.iOS,case_tag.MEDIUM)
    def test_updateAvatar(self):
        avc = self.avc
        avc.startAVC()
        poco("mine").click()
        path1 = "resource/screenshot/test.jpg"
        avc.getScreenshot(filename=path1)
        path2 = "resource/screenshot/test1.jpg"
        avc.updateAvatar()
        avc.getScreenshot(filename=path2)
        assert verify_utils.compare_images(path1,path2) == "Success"
