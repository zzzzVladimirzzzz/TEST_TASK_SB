from UI.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')