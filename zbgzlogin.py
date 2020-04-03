#登录支部工作 获取验证码 并另存图片到.\easy_img 目录下
#
#

from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.keys import Keys
from aip import AipOcr
import os,time
import requests
import base64
from img_optimization import *
from baitu_rec import *






def main_login():
    
    uname='13718759896'
    pwd='820121'
    url ='http://www.zhibugongzuo.com/login'

    browser=webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(5)
    browser.maximize_window()

    #定位到 账号密码 页面 
    ZHMM=browser.find_element_by_xpath("//li[contains(text(),'账号密码')]")
    ZHMM.click()

    #填入用户名
    browser.find_element_by_id("uname").clear()
    browser.find_element_by_id("uname").send_keys(uname)
    browser.find_element_by_id("uname").send_keys(Keys.TAB)
    time.sleep(2)
    #填入密码
    browser.find_element_by_id("pwd").send_keys(pwd)
    browser.find_element_by_id("pwd").send_keys(Keys.TAB)
    time.sleep(2)
    #取验证码并保存
    png=browser.find_element_by_id("captcha-img")
    png.screenshot('.\easy_img\capt.png')
    #调用验证码处理函数进行图片处理
    img_main()
    #调用百度识别验证码
    str_code=baidu_rec_main(".\easy_img\capt-grey.jpg")
    #打印验证码
    print('code is:',str_code)
    #填入验证码
    browser.find_element_by_id("captcha").send_keys(str_code)
    #browser.find_element_by_id("captcha").send_keys(ENTER)
    time.sleep(3)
    DL=browser.find_element_by_xpath("//button[contains(text(),'登录')]")
    DL.click()
    time.sleep(3)
     

if  __name__ == "__main__":
    main_login()



