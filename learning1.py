#!python
# open chrome in windows
import pyautogui as pg
import sys

#def open_explor(str="chrome")

print('==== 打开浏览器 Press Ctrl-C to quit====')
liulanqi_name = ' chrome'
mb_direct1 = '  https://www.zhibugongzuo.com/news#/workinfodetail?act_id=129724224566fc2714a48723d741bf67c3e677660d83e0eee367d1b07a099457&template=1'

try:
    #pg.dragTo(186, 348, 0.5, button='left')
    #pg.doubleClick()
    pg.hotkey('ctrl', 't')
    pg.PAUSE = 2
    pg.getPointOnLine
    pg.write(mb_direct1)
    pg.press('enter',interval=1)     
    pg.PAUSE=1
    pg.dragTo(304,193,0.5,button='left')
    pg.doubleClick()
