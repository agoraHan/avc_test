#-*- coding:utf-8 -*-
from airtest.core.api import  *
from airtest.core.ios.ios import IOS
import pytest
from common import case_tag,verify_utils
from common.avc_ios import IOS_AVC
from common import avc_constance as ac
from common import pytest_utils
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

    #设置不同的网络检查网络质量回调是否符合预期
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.MANUAL, case_tag.FUNCTIONALITY)
    def test_checkNetworkQuality(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        pytest_utils.execute_manual_step("设置下行网络，丢包100%")
        assert  verify_utils.network_quality() == "Unkown"
        pytest_utils.execute_manual_step("设置下行网络，丢包0")
        assert verify_utils.network_quality() == "Good"
        pytest_utils.execute_manual_step("设置下行网络，丢包60%")
        assert verify_utils.network_quality() == "Bad"



