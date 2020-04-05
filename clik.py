##!/usr/bin/python   
# open chrome in windows 
import pyautogui as pg
import pyperclip as pc
import sys
import time


#def open_explor(str="chrome")
## This programe have 5 Jobs ## 
def open_explor(expname):
    ##打开浏览器
    pg.hotkey('win','r')
    pg.PAUSE=2
    pg.write(expname,interval=0.2,pause=0.2)
    pg.press('enter',interval=1) 

def open_new_url(url):
    ##新窗口打开地址
    pg.hotkey('ctrl','t')
    pg.PAUSE=1
    pg.getPointOnLine
    pg.write(url)
    pg.press('enter',interval=1)
    pg.PAUSE = 1

def max_windows():
    ##最大化窗口
    pg.keyDown('alt')
    pg.keyDown('space')
    pg.press('x',presses=1)
    pg.keyUp('space')
    pg.keyUp('alt')
    pg.PAUSE = 0.1

if __name__ == "__main__":
    
    print('==== 打开浏览器 Press Ctrl-C to quit====')
    time_start=time.time()
    #time.strftime("%Y-%m-%d %H:%M:%S",time_start)
    exp_name=' chrome'    #浏览器名称  前面加一个空格
    login_dir='www.zhibugongzuo.com/login' 
    job1_dir='www.zhibugongzuo.com'
    job2_dirs = (
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=129724224566fc2714a48723d741bf67c3e677660d83e0eee367d1b07a099457&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=63dd774c8e4bebd7273c8eb4f2d83eeb97cae0777b94214e188ab3ed0a9c2d9e&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=049c3f45aa680543e9c146a87e70fb11afe76e58060018a8d08a31e814bb5720&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=9e5fe9f6124634f4f08a318aa87875fc1ad137e9d7aa51138777b633df753243&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=170d44e93738220dd0418590e17d4e9461e58532e238a278e26bdd617a1b12cd&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=e1db726bf9a732b409a11dfd5683a88e0061084e5a728c58713bd38881a9380f&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=2e8d404e204c88a1c774e9dc50d33826a3f4d2d63af58992300050fbc39a09d9&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=4d8058f0c6224c1e38b0f3340002589b09505e728b111d3f7d8a74fd935ad2a4&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=20bbd8f9f3f098455043b937e2e6bf62b6e2037929b118ae8fb139554f3f61a2&template=1',
    '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=8fec49fc3a634bc87956816c0a04392d03d86c6f7af1479b37df4062e73b742d&template=1')
    job2_txt = '学习'
    job3_dir='  https://www.zhibugongzuo.com/study#/materialDetail/b30bbe82e55773d4cec1cce82fe339e6'
    job3_txt ='经过全国上下和广大人民群众艰苦努力，疫情防控取得阶段性重要成效，经济社会秩序加快恢复，彰显了中国共产党领导和中国特色社会主义制度的显著优势'
    job3_counter=20
    job4_dir='  https://www.zhibugongzuo.com/moments#/index'
    job4_txt = '经过全国上下和广大人民群众艰苦努力，疫情防控取得阶段性重要成效，经济社会秩序加快恢复，彰显了中国共产党领导和中国特色社会主义制度的显著优势'


    try:
        ## Run Chrome and SignIn
        
        open_explor(exp_name)
        
        #open_new_url(login_dir)
        max_windows()
        #pg.click()
        pg.write(login_dir)
        pg.press('enter')
        time.sleep(10)

        ### Start JOB1: SIGNIN +5 point ##
        open_new_url(job1_dir)
        pg.moveTo(1142,328,0.1)
        pg.click()
        pg.click()
        pg.click()
        pg.hotkey('ctrl','F4')

        ## Start JOB2: Reading +10 and Discuss +5 point ##
        for job2_dir in job2_dirs:
            open_new_url(job2_dir)
            pg.moveTo(304,193,0.0)
            pg.doubleClick()
            #pg.write(job2_txt,interval=0.01,pause=0.2)
            pc.copy(job2_txt)
            pg.hotkey('ctrl','v')
            #pc.paste()
            pg.moveTo(1024,668,0.0)
            pg.doubleClick()
            pg.PAUSE=2
            pg.hotkey('ctrl','F4')
        
        ## Start JOB4: Publish +2 point ##
        open_new_url(job4_dir)
        pg.moveTo(430,302,0.1)
        pg.doubleClick()
        #pg.write(job4_txt,interval=0.01,pause=0.2)
        pc.copy(job4_txt)
        pg.hotkey('ctrl','v')
        #pc.paste()
        pg.moveTo(935,392,0.1)
        pg.click()
        pg.PAUSE=2
        pg.hotkey('ctrl','F4')
        
        
        ## Start JOB3: Leaning Online +5 and Note  +2 point ##
        #time.sleep(1)
        open_new_url(job3_dir)
        pg.moveTo(323,289,0.1)
        pg.click()
        pg.moveTo(463,289,0.1)
        pg.click()
        #pg.write(job4_txt,interval=0.01,pause=0.2)
        pc.copy(job3_txt)
        pg.hotkey('ctrl','v')
        #pc.paste()
        pg.moveTo(1051,415,0.1)
        pg.click()
        pg.PAUSE=2
        time_2=time.time()
        for i in range (job3_counter):
            pg.middleClick()
            pg.move(0,400,duration=1)
            pg.middleClick()
            pg.middleClick()
            pg.move(0,-400,duration=1)
            pg.middleClick()
            #time.sleep(1)
            job3_counter-=1
        pg.hotkey('ctrl','F4')
        #pg.hotkey('ctrl','F4')

        ## Start JOB5: Practise +6 point ##
        time_end=time.time()
        
        pg.hotkey('alt','F4')
    except KeyboardInterrupt:
        print('\n')

    #time.strftime("%Y-%m-%d %H:%M:%S",time_end)
    time_count=time_end-time_start
    read_count=time_end-time_2
    print('Time totle cost:',time_count,'s /n.Reading cost:',read_count,'s')

    #return;




