class DrawPic():
    def delete_first_lines(self, filename, count):
        fin = open(filename, 'r')
        a = fin.readlines()
        fout = open(filename, 'w')
        b = ''.join(a[count:])
        fout.write(b)
        fout.close()
    def replace_space(self,filename):
        fin = open(filename, 'r')
        a = fin.readlines()
        with open(filename, 'w') as w:
            for l in a:
                w.write(l.replace(' ', ''))

    def drawPicture(self, filename):
        # 导入必要的模块
        import numpy as np
        import matplotlib.pyplot as plt
        import csv
        # 产生测试数据
        ii = 0
        # filename = 'result.txt'
        x = []
        y = []
        z = []
        with open(filename) as f:
            reader = csv.DictReader(f, delimiter=';')
            item = reader
            for i in reader:
                # print(i)
                if int(i['Type']) == 101:
                    x.append(float(i['t']))  # x是时间
                    y.append(float(i['DistX']))  # y是距离
                    z.append(float(i['v'])) #z是速度
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        # 设置标题
        ax1.set_title('Scatter Plot')
        # 设置X轴标签
        plt.xlabel('Time(s)')
        # 设置Y轴标签
        plt.ylabel('Distance(m)')
        # 画散点图
        ax1.scatter(x, y, c=z, cmap=plt.cm.hot, marker='.')
        # ax1.scatter(x,y,c=z,cmap='gray',marker = '.')
        # 设置图标
        plt.legend('x1')
        # 显示所画的图
        plt.show()

    def __init__(self,filename):
        self.delete_first_lines(filename, 13)
        self.replace_space(filename)
        self.drawPicture(filename)
        print("替换完成")
