import time
import pyautogui as do

"""
Better
Goto All
select all
goto print
select download to pdf
wait
click download pdf here
press enter
page dn 10 times
click next page
repeat
"""

def linkedpwn():
    while(not do.locateCenterOnScreen('/home/amar/Pictures/all.png')):
        time.sleep(0.5)
    x, y = do.locateCenterOnScreen('/home/amar/Pictures/all.png')
    do.click(x-10, y)

    time.sleep(0.2)
    x, y = do.locateCenterOnScreen('/home/amar/Pictures/anchor.png')
    do.click(x-5, y)

    time.sleep(0.2)
    do.moveRel(0,60)
    do.click()
    time.sleep(15)

    while(not do.locateCenterOnScreen('/home/amar/Pictures/download_pdf.png')):
        time.sleep(0.5)
    x,y = do.locateCenterOnScreen('/home/amar/Pictures/download_pdf.png')
    do.click(x+35, y)

    time.sleep(6)
    do.press('enter')

    time.sleep(1)
    for i in range(0,10):
        do.press('pgdn')

    time.sleep(1)
    x, y = do.locateCenterOnScreen('/home/amar/Pictures/next.png')

    do.click(x,y)

time.sleep(2)
for i in range(0,36):
    linkedpwn()
