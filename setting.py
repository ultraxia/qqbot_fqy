import random
import configparser
import os
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 小偶像名字
def idol_name():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        # idol name
        idol_name = cf.get('idol', 'name')
    return str(idol_name)


# ----------------------摩点微打赏设置----------------------


# 微打赏名称
def wds_name():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        modian_name = cf.get('modian', 'name')
    return str(modian_name)


# 微打赏网址 建议使用短地址t.cn
def wds_url():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        modian_url = cf.get('modian', 'url')
    return str(modian_url)


# 微打赏项目对应pro_id
def pro_id():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        pro_id = cf.get('modian', 'pro_id')
    return int(pro_id)


# ----------------------qq群设置----------------------

# qq群昵称
def groupid():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        group_name = cf.get('QQqun', 'name')
    return str(group_name)

# 欢迎信息
def welcome():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    # with open(file_path, 'r') as cfgfile:
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        # group_welcome
        words = cf.get('QQqun', 'welcome')
        msg = words.replace('\\n', '\n')
    return msg

# ----------------------微博设置----------------------

# 手机网页版微博地址
def weibo_url():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        weibo_url = cf.get('weibo', 'weiboURL')
    return str(weibo_url)

def weibo_id():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'setting.conf')
    cf = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as cfgfile:
        cf.readfp(cfgfile)
        weibo_id = cf.get('weibo', 'weiboID')
    return int(weibo_id)


