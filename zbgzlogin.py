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





#def get_captcha():
  


uname='13718759896'
pwd='820121'
url ='http://www.zhibugongzuo.com/login'

browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(url)
browser.maximize_window()

#定位到 账号密码 页面 
a=browser.find_element_by_xpath("//li[contains(text(),'账号密码')]")
a.click()
'''
browser.find_element_by_id("uname").clear()
browser.find_element_by_id("uname").send_keys(uname)
browser.find_element_by_id("uname").send_keys(Keys.TAB)
time.sleep(2)
browser.find_element_by_id("pwd").send_keys(pwd)
browser.find_element_by_id("pwd").send_keys(Keys.ENTER)
time.sleep(2)
'''
png=browser.find_element_by_id("captcha-img")
png.screenshot('.\easy_img\capt.png')


img=Image.open('.\easy_img\capt.png')
img = img.convert('L')         # P模式转换为L模式(灰度模式默认阈值127)
count=160                  # 设定阈值
table=[]
for i in range(256):
        if i<count:
            table.append(0)
        else:
            table.append(1)
    
img=img.point(table,'1')
img.save('.\easy_img\captcha.png')   # 保存处理后的验证码
time.sleep(2)



'''


'''




#browser.quit()



