# encoding:utf-8
##使用百度aip进行图像识别
##图片保存在.\out_img目录下
import requests
import json
from aip import AipOcr


def get_file_content(filePath):
    with open(filePath,'rb')as fp:
        return fp.read()

def baidu_rec_main(PNG_filePath):

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    APP_ID='19131433'
    API_KEY='kSvXEj1rR3xa9SI1vsKOaGFj'
    SECRET_KEY='pyY7PrDGZClczOxniBhTqPmKfWzjMjg4'
    #PNG_filePath = 'captcha.png'
    #PNG_filePath = '.\out_img\captcha-clearBorder.jpg'   #传入需要进行识别的图片名
    OPTIONS = {
    'language_type':'ENG',
    'detect_direction':'true',
    'detect_language':'true'
    }

    client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

    image=get_file_content(PNG_filePath)
    Result=client.basicAccurate(image,OPTIONS)


    if Result:
        #print(Result)
        print(json.dumps(Result))
        print('---------------')
    
    dict1=Result['words_result']    
    captcha=''
    for word in dict1:
        print(word,'\n')
        capt = (word['words'])
        captcha=captcha+capt
    print('===>'+captcha)


    captcha=captcha.replace(" ", "") #去除掉空格
     #循环去除标点符号
    for i in ',.。;；？?<>-+()!@#$%^&*[]{}:':
        captcha=captcha.replace(i,"")
            
    print('识别结果：' + captcha)
    Answer_str=captcha
    print("answer is:",Answer_str)

           
    return Answer_str

if __name__ == "__main__":
    str_1=baidu_rec_main(".\easy_img\capt-grey.jpg")
    print(str_1)






