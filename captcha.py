#!/usr/bin/env python
import time
import pyautogui as do
def findOnScreen(image):
    return do.locateOnScreen(image)[0:2]

def lvalue(image, directory):
    leftValue = {}
    for i in do.locateAllOnScreen(
                directory
                +str(image)+'.png'):
        leftValue.update([(i[0],image)])
    return leftValue


def getCaptcha(directory, images):
    captcha = {}
    for image in images:
        captcha.update(lvalue(image, directory))
        print captcha
    return ' '.join(
                map(
                    str
                    ,[captcha[key] for key in sorted(captcha)]
                    )
                )

time.sleep(2)
images = [0,1,2,3,4,5,6,7,8,9,10,11]

expr =  str(
            getCaptcha('./library/pnr/', images)
                .replace('10', '-')
                .replace('11', '+')
                .replace(' ', '')
        )

result = eval(expr)
print expr, ' = ',result

