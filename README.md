python 环境 python3.x

需要安装的插件：

pip install pytest

pip install airtest 

pip install pocoui

pip install PIL

brew install tesseract（并在脚本声明tesseract所在的路径，e.g:pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/4.1.0/bin/tesseract'）

IOS设备连接方法:http://airtest.netease.com/docs/docs_AirtestIDE-zh_CN/1_quick_start/3_get_started_with_iOS_test.html

执行：python -m pytest testcase/ios/test_function.py  -s -v -k test_xx(指定运行某条case）
