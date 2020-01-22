# -*- coding: utf-8 -*-
import numpy as np
from OpenVissim import OpenVissim  # 导入自定义问题接口
from DrawPic import DrawPic
###########
## Author:  藏龙御景
## Date:    2020-01-22 
###########
dir = "C:\\Users\\Run\\Desktop\\VISSIMCOM_VSL\\"
accidentStartTime = 1000
accidentEndTime = 2000
totalPeriod = 5000
openVissim = OpenVissim(filename=dir + "vsl.inp")
openVissim.runSimulation(accidentStartTime, accidentEndTime, totalPeriod, flagVSL=False)
drawPic = DrawPic(filename=dir + "vsl.fzp")
openVissim.runSimulation(accidentStartTime, accidentEndTime, totalPeriod, flagVSL=True)
drawPic = DrawPic(filename=dir + "vsl.fzp")
