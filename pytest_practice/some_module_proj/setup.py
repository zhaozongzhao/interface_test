# python 分发工具setuptools 能帮助我们更好的创建很分发
from setuptools import setup

setup(
    name = 'some_module',  #应用名
    version='0.0.1', # 版本号
    py_modules = ['some_module'],
    url = 'None',
    author = 'zzz',
    author_email = '3031371046@qq.com',
    # packages = ['some_module']
    # #  安装包内的python模块
)