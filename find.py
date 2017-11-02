#!/usr/bin/env python
import time
import pyautogui as do

def findOnScreen(image):
    return do.locateOnScreen(image)[0:2]

def uvalue(image, directory):
    upValue = []
    for i in do.locateAllOnScreen(
                directory
                +str(image)):
        upValue.append(i[1])
#        print image
    return upValue


time.sleep(2)

images = [
        'extra_search.png'
        , 'job_icon.png'
        , 'people_icon.png'
        , 'group_icon.png'
        ,'company.png'
        , 'group.png'
        , 'school.png'
        , 'showcase.png'
        ]
db_dir = './'
search = 'search.png'
cell_space = 60
dist_from_curr = 10
org_x, org_y = findOnScreen(db_dir+search)
up_values = []

# we initially move to the suggestion cell beneath the search bar
do.moveTo(org_x, org_y+cell_space)
curr = do.position()


for image in images:
    up_values.append(uvalue(image, db_dir))

all_values = []
for up_value_array in up_values:
    for up_value in up_value_array:
        all_values.append(up_value)

all_values = sorted(all_values)


for y_value in all_values:
    # if our current y postion and the  company,job,showcase etc y postion are in the same cell
    if max(y_value, curr[1]) - min(y_value, curr[1]) <= 60:
        # we move down the next cell
        do.moveRel(0, 60)
    else:
        do.moveTo(curr)
    curr = do.position()

