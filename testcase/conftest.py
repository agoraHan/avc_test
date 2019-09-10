import pytest
# from pathlib import Path
# import json

devices = {"device": "WY1"}

def pytest_addoption(parser):
    parser.addoption("--device", action="store", default=devices['device'], help="qr for primary device")

@pytest.fixture
def device(request):
    return request.config.getoption("--device")


