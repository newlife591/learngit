# encoding:utf-8
##使用百度aip进行图像识别
##图片保存在.\out_img目录下
import requests
import json
from aip import AipOcr


def get_file_content(filePath):
    with open(filePath,'rb')as fp:
        return fp.read()

# client_id 为官网获取的AK， client_secret 为官网获取的SK
APP_ID='19131433'
API_KEY='kSvXEj1rR3xa9SI1vsKOaGFj'
SECRET_KEY='pyY7PrDGZClczOxniBhTqPmKfWzjMjg4'
#PNG_filePath = 'captcha.png'
PNG_filePath = '.\out_img\captcha-interferenceline.jpg'
OPTIONS = {
  'language_type':'KOR',
  'detect_direction':'true',
  'detect_language':'true'
  }

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

image=get_file_content(PNG_filePath)
Result=client.basicAccurate(image,OPTIONS)


if Result:
    print(Result)
    print(json.dumps(Result))

for word in Result['words_result']:
    captcha = (word['words'])
    captcha=captcha.replace(" ", "")
    print('识别结果：' + captcha)





