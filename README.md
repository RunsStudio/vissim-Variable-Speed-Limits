---
tag: VISSIM
categories: 交通工程
author: 藏龙御景
date: 2020-1-22 10:56:23
---

# 在VISSIM中实现可变限速

一个简单的案例，用Python实现，当t=1000的时候事故发生，封闭四条高速路车道，同时开始限速，t=2000的时候事故撤销，总共仿真5000秒。

仿真结束后处理车辆轨迹数据文件（*.fzp），通过对每辆车里程、在路网中的时间绘制时空图。
在对轨迹数据文件进行处理时，可能会有BUG，替换不完整，这时候需要手工处理一下FZP文件。

效果图如下：

![NOVSL_2LaneClosed](NOVSL_2LaneClosed.png)
**封闭2车道+无VSL**



![NoVSL_4LaneClosed](README\NoVSL_4LaneClosed.png)
**封闭4车道+无VSL**

![VSL_2LaneClosed](README\VSL_2LaneClosed.png)
**封闭2车道+有VSL**
![VSL_4LaneClosed](README\VSL_4LaneClosed.png)
**封闭4车道+有VSL**


文档有待更新



