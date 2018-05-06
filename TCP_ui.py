# -*- coding: utf-8 -*-
# @Author: Amberimzyj
# @Emial:  amberimzyj@outlook.com
# @Date:   2018-04-23 22:00:16
# @Last Modified by:   Amberimzyj
# @Last Modified time: 2018-05-04 13:58:22
# @License: MIT LICENSE
#-*- coding: utf-8 -*-
import socket
import time
from TCP_server1 import Ui_MainWindow
# from PyQt5 import QtWidgets
from PySide.QtCore import QTimer, QDateTime,QDate,QTime
from datetime import datetime
from PySide.QtGui import QApplication, QMainWindow, QHeaderView, QFont,QDateTimeEdit
import sys
import threading
import re
from PySide import QtGui, QtCore
import numpy as np
# import matplotlib as mpl
import matplotlib.pyplot as plt  # 调用绘图库
import _matplot
import _xlsx




# import TCP_Server


class Mywindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.result = []
        self.data1 = []
        self.data2 = []
        self.data3 = []
        self.data4 = []
        self.text = ""
        self.setTable2()
        self.clo = 0
        # self.dateTimeEdit = QDateTimeEdit(self)

        # self.dateEdit =  QDateTimeEdit(QDate.currentDate())
        # self.timeEdit =  QDateTimeEdit(QTime.currentTime())
        # self.dateTimeEdit = QtGui.QDateTimeEdit(QtCore.QDateTime.currentDateTime(), self)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        # self.dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        # self.dateEdit.setDisplayFormat("yyyy.M.d")
        # self.timeEdit.setDisplayFormat("H:mm")
        
        
        self.test1 = _matplot.Matplot()
        self.test1.set_diagram(1)
        self.horizontalLayout_8.addWidget(self.test1.canvas)
        self.test2 = _matplot.Matplot()
        self.test2.set_diagram(2)
        self.horizontalLayout_9.addWidget(self.test2.canvas)
        self.test3 = _matplot.Matplot()
        self.test3.set_diagram(3)
        self.horizontalLayout_10.addWidget(self.test3.canvas)
        self.test4 = _matplot.Matplot()
        self.test4.set_diagram(4)
        self.horizontalLayout_11.addWidget(self.test4.canvas)

        timer = QTimer(self)
        timer.timeout.connect(self.fresh1)
        timer.start(200)

        self.waitconnect()

    def fresh1(self):
        
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")



    def waitconnect(self):
        # 创建一个socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 监听端口
        s.bind(('0.0.0.0', 8088))
        s.listen(5)
        # setText('Waiting for connection...')
        self.s = s

    def tcplink(self):
        self.sock, self.addr = self.s.accept()
        self.text += 'Accept new connection from %s:%s...\r\n' % self.addr
        # sock.send(b'Welcome!')
        while not self.clo:
            try:
                data = self.sock.recv(1024)
            except OSError:
                break
            time.sleep(1)
            if not data or data.decode('GB2312') == 'exit':
                break
            # self.text += data.decode('GB2312')
            self.text += data.decode('GB2312')
            self.result = re.findall(r"\d+\.?\d*|F\d", data.decode('GB2312'))
            # for item in result:
            #     self.text += item + "\r\n"
            # sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
        # sock.close()
        self.text += 'Connection from %s:%s closed.' % self.addr
        


# 创建一个列表汇总显示各节点的测量值
    def setTable2(self):

        self.t1 = 0
        self.t2 = 0
        self.t3 = 0
        self.t4 = 0

        self.datat1 = [0]*100
        self.datah1 = [0]*100
        self.datal1 = [0]*100
        self.datat2 = [0]*100
        self.datah2 = [0]*100
        self.datal2 = [0]*100
        self.datat3 = [0]*100
        self.datah3 = [0]*100
        self.datal3 = [0]*100
        self.datat4 = [0]*100
        self.datah4 = [0]*100
        self.datal4 = [0]*100

        # 隐藏表头
        self.tableView_2.verticalHeader().hide()
        self.tableView_2.horizontalHeader().hide()
        # self.tableView_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.data_model = QtGui.QStandardItemModel()
        # self.tableView_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        # 设置每列的标题
        self.data_model.setItem(0, 0, QtGui.QStandardItem("测量参数"))
        self.data_model.setItem(0, 1, QtGui.QStandardItem("F1"))
        self.data_model.setItem(0, 2, QtGui.QStandardItem("F2"))
        self.data_model.setItem(0, 3, QtGui.QStandardItem("F3"))
        self.data_model.setItem(0, 4, QtGui.QStandardItem("F4"))
        self.data_model.setItem(1, 0, QtGui.QStandardItem("温度(℃)"))
        self.data_model.setItem(2, 0, QtGui.QStandardItem("湿度(%RH)"))
        self.data_model.setItem(3, 0, QtGui.QStandardItem("光照强度(lx)"))
        self.data_model.setItem(0, 0, QtGui.QStandardItem("测量参数"))
        self.data_model.setItem(1, 1, QtGui.QStandardItem("0"))
        self.data_model.setItem(2, 1, QtGui.QStandardItem("0"))
        self.data_model.setItem(3, 1, QtGui.QStandardItem("0"))
        self.data_model.setItem(1, 2, QtGui.QStandardItem("0"))
        self.data_model.setItem(2, 2, QtGui.QStandardItem("0"))
        self.data_model.setItem(3, 2, QtGui.QStandardItem("0"))
        self.data_model.setItem(1, 3, QtGui.QStandardItem("0"))
        self.data_model.setItem(2, 3, QtGui.QStandardItem("0"))
        self.data_model.setItem(3, 3, QtGui.QStandardItem("0"))
        self.data_model.setItem(1, 4, QtGui.QStandardItem("0"))
        self.data_model.setItem(2, 4, QtGui.QStandardItem("0"))
        self.data_model.setItem(3, 4, QtGui.QStandardItem("0"))

        # 设置参数水平居中
        self.data_model.item(0, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(0, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(0, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(0, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(0, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 4).setTextAlignment(QtCore.Qt.AlignCenter)

        # 设置表格的默认行高
        # self.tableView_2.verticalHeader().setDefaultSectionSize(60)
        self.data_model.item(0, 0).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(0, 1).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(0, 2).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(0, 3).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(0, 4).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(1, 0).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(2, 0).setFont(QFont("Times", 13, QFont.Black))
        self.data_model.item(3, 0).setFont(QFont("Times", 13, QFont.Black))

        # 设置自适应列宽
        self.tableView_2.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.tableView_2.verticalHeader().setResizeMode(QHeaderView.Stretch)

        # 关联tableView_2
        self.tableView_2.setModel(self.data_model)
        self.tableView_2.show()

        # self.buildDiagram()

    def showData(self):

        # 实时显示各节点测量数据
        for l1 in range(len(self.result)):
            if self.result[l1][0] == 'F':
                if self.result[l1][1] == '1':
                    self.datat1.pop(0)
                    self.datat1.append(float(self.result[l1+1]))
                    self.datah1.pop(0)
                    self.datah1.append(float(self.result[l1+2]))
                    self.datal1.pop(0)
                    self.datal1.append(float(self.result[l1+3]))
                    self.data_model.setItem(1, 1, QtGui.QStandardItem(self.result[l1+1]))
                    self.data_model.setItem(2, 1, QtGui.QStandardItem(self.result[l1+2]))
                    self.data_model.setItem(3, 1, QtGui.QStandardItem(self.result[l1+3]))
                    self.t1 = 0

                    time1=time.strftime('%Y-%m-%d %H:%M:%S')
                    self.datas1=[time1,self.result[l1+1],self.result[l1+2],self.result[l1+3]]
                    self.data1.append(self.datas1)

                if self.result[l1][1] == '2':
                    self.datat2.pop(0)
                    self.datat2.append(float(self.result[l1+1]))
                    self.datah2.pop(0)
                    self.datah2.append(float(self.result[l1+2]))
                    self.datal2.pop(0)
                    self.datal2.append(float(self.result[l1+3]))
                    self.data_model.setItem(1, 2, QtGui.QStandardItem(self.result[l1+1]))
                    self.data_model.setItem(2, 2, QtGui.QStandardItem(self.result[l1+2]))
                    self.data_model.setItem(3, 2, QtGui.QStandardItem(self.result[l1+3]))
                    self.t2 = 0

                    time2=time.strftime('%Y-%m-%d %H:%M:%S')
                    self.datas2=[time2,self.result[l1+1],self.result[l1+2],self.result[l1+3]]
                    self.data2.append(self.datas2)

                if self.result[l1][1] == '3':
                    self.datat3.pop(0)
                    self.datat3.append(float(self.result[l1+1]))
                    self.datah3.pop(0)
                    self.datah3.append(float(self.result[l1+2]))
                    self.datal3.pop(0)
                    self.datal3.append(float(self.result[l1+3]))
                    self.data_model.setItem(1, 3, QtGui.QStandardItem(self.result[l1+1]))
                    self.data_model.setItem(2, 3, QtGui.QStandardItem(self.result[l1+2]))
                    self.data_model.setItem(3, 3, QtGui.QStandardItem(self.result[l1+3]))
                    self.t3 = 0
                   
                    time3=time.strftime('%Y-%m-%d %H:%M:%S')
                    self.datas3=[time3,self.result[l1+1],self.result[l1+2],self.result[l1+3]]
                    self.data3.append(self.datas3)

                if self.result[l1][1] == '4':
                    self.datat4.pop(0)
                    self.datat4.append(float(self.result[l1+1]))
                    self.datah4.pop(0)
                    self.datah4.append(float(self.result[l1+2]))
                    self.datal4.pop(0)
                    self.datal4.append(float(self.result[l1+3]))
                    self.data_model.setItem(1, 4, QtGui.QStandardItem(self.result[l1+1]))
                    self.data_model.setItem(2, 4, QtGui.QStandardItem(self.result[l1+2]))
                    self.data_model.setItem(3, 4, QtGui.QStandardItem(self.result[l1+3]))
                    self.t4 = 0

                    time4=time.strftime('%Y-%m-%d %H:%M:%S')
                    self.datas4=[time4,self.result[l1+1],self.result[l1+2],self.result[l1+3]]
                    self.data4.append(self.datas4)
        
        # 设置水平居中
        self.data_model.item(1, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 4).setTextAlignment(QtCore.Qt.AlignCenter)

        # 设置字号和粗细
        self.data_model.item(1, 1).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 1).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 1).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(1, 2).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 2).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 2).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(1, 3).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 3).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 3).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(1, 4).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 4).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 4).setFont(QFont("Times", 12, QFont.Light))


        # elif not self.result[0] == "F4":
        #     self.t4 += 1


        self.test1._change(self.datal1,self.datat1,self.datah1)
        self.test1.set_diagram(1)
        self.test2._change(self.datal2,self.datat2,self.datah2)
        self.test2.set_diagram(2)
        self.test3._change(self.datal3,self.datat3,self.datah3)
        self.test3.set_diagram(3)
        self.test4._change(self.datal4,self.datat4,self.datah4)
        self.test4.set_diagram(4)
        self.result = []
        

    def fresh(self):
        self.t1 += 1  
        self.t2 += 1
        self.t3 += 1
        self.t4 += 1
        if self.t1 == 10:
            self.data_model.setItem(1, 1, QtGui.QStandardItem("0"))
            self.data_model.setItem(2, 1, QtGui.QStandardItem("0"))
            self.data_model.setItem(3, 1, QtGui.QStandardItem("0"))

        if self.t2 == 10:
            self.data_model.setItem(1, 2, QtGui.QStandardItem("0"))
            self.data_model.setItem(2, 2, QtGui.QStandardItem("0"))
            self.data_model.setItem(3, 2, QtGui.QStandardItem("0"))

        if self.t3 == 10:
            self.data_model.setItem(1, 3, QtGui.QStandardItem("0"))
            self.data_model.setItem(2, 3, QtGui.QStandardItem("0"))
            self.data_model.setItem(3, 3, QtGui.QStandardItem("0"))

        if self.t4 == 10:
            self.data_model.setItem(1, 4, QtGui.QStandardItem("0"))
            self.data_model.setItem(2, 4, QtGui.QStandardItem("0"))
            self.data_model.setItem(3, 4, QtGui.QStandardItem("0"))

         # 设置水平居中
        self.data_model.item(1, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 3).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(1, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(2, 4).setTextAlignment(QtCore.Qt.AlignCenter)
        self.data_model.item(3, 4).setTextAlignment(QtCore.Qt.AlignCenter)

        # 设置字号和粗细
        self.data_model.item(1, 1).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 1).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 1).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(1, 2).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 2).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 2).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(1, 3).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 3).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 3).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(1, 4).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(2, 4).setFont(QFont("Times", 12, QFont.Light))
        self.data_model.item(3, 4).setFont(QFont("Times", 12, QFont.Light))

        if self.text:
            self.textEdit_2.insertPlainText(self.text)
            self.text = ""
            v = self.textEdit_2.verticalScrollBar()
            v.setSliderPosition(v.maximum())
        if self.result:
            self.showData()
        

    def TCP_connect(self):
        self.clo = 0
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        # 等待一个新连接
        self.textEdit_2.insertPlainText('Waiting for connection...\r\n')
        # 接受一个新连接
        # 创建新线程来处理TCP连接
        timer = QTimer(self)
        timer.timeout.connect(self.fresh)
        timer.start(200)
        t = threading.Thread(target=self.tcplink)
        t.setDaemon(True)
        t.start()

    def TCP_disconnect(self):
        self.c1o = 1
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(False)
        if self.sock:
            self.sock.shutdown(2)
            self.sock.close()
        # self.textEdit_2.insertPlainText('Connection from %s:%s closed.\r\n' % self.addr)
        
   
    #保存各数据曲线
    def save_fig1(self):
        # self.pushButton_6.setEnabled(False)
        self.test1.figure.savefig("D:\study\The eighth term\graduation design\data\Line chart\F1.png")

    def save_fig2(self):
        # self.pushButton_6.setEnabled(False)
        self.test2.figure.savefig("D:\study\The eighth term\graduation design\data\Line chart\F2.png")

    def save_fig3(self):
        # self.pushButton_6.setEnabled(False)
        self.test3.figure.savefig("D:\study\The eighth term\graduation design\data\Line chart\F3.png")

    def save_fig4(self):
        # self.pushButton_6.setEnabled(False)
        self.test4.figure.savefig("D:\study\The eighth term\graduation design\data\Line chart\F4.png")

    #保存数据至excel
    def save_data(self):
        self.save=_xlsx.Xlsx()
        self.save.set_sheet1_data(self.data1)
        self.save.set_sheet2_data(self.data2)
        self.save.set_sheet3_data(self.data3)
        self.save.set_sheet4_data(self.data4)
        self.save.wb.save('D:\study\The eighth term\graduation design\data\Measured_data.xlsx')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mywindow()
    window.show()
    # window.textEdit_2.setHtml('<p>Accept new connection from ...</p>')
    sys.exit(app.exec_())
