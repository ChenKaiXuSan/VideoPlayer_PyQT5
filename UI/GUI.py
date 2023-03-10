# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import pyqtSignal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1254, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.attention_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.attention_text.setEnabled(True)
        self.attention_text.setMinimumSize(QtCore.QSize(500, 100))
        self.attention_text.setObjectName("attention_text")
        self.verticalLayout_2.addWidget(self.attention_text)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.head_btn = QtWidgets.QPushButton(self.centralwidget)
        self.head_btn.setCheckable(True)
        self.head_btn.setObjectName("head_btn")
        self.verticalLayout_2.addWidget(self.head_btn)
        self.shoulder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.shoulder_btn.setCheckable(True)
        self.shoulder_btn.setObjectName("shoulder_btn")
        self.verticalLayout_2.addWidget(self.shoulder_btn)
        self.wrist_btn = QtWidgets.QPushButton(self.centralwidget)
        self.wrist_btn.setCheckable(True)
        self.wrist_btn.setObjectName("wrist_btn")
        self.verticalLayout_2.addWidget(self.wrist_btn)
        self.lumbar_pelvis_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lumbar_pelvis_btn.setCheckable(True)
        self.lumbar_pelvis_btn.setObjectName("lumbar_pelvis_btn")
        self.verticalLayout_2.addWidget(self.lumbar_pelvis_btn)
        self.foot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.foot_btn.setCheckable(True)
        self.foot_btn.setObjectName("foot_btn")
        self.verticalLayout_2.addWidget(self.foot_btn)
        self.focus_unkonwn_btn = QtWidgets.QPushButton(self.centralwidget)
        self.focus_unkonwn_btn.setCheckable(True)
        self.focus_unkonwn_btn.setObjectName("focus_unkonwn_btn")
        self.verticalLayout_2.addWidget(self.focus_unkonwn_btn)
        self.disease_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.disease_text.setEnabled(True)
        self.disease_text.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.disease_text.setFont(font)
        self.disease_text.setMouseTracking(False)
        self.disease_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.disease_text.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.disease_text.setLineWidth(0)
        self.disease_text.setObjectName("disease_text")
        self.verticalLayout_2.addWidget(self.disease_text)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.asd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.asd_btn.setEnabled(True)
        self.asd_btn.setAcceptDrops(False)
        self.asd_btn.setCheckable(True)
        self.asd_btn.setChecked(False)
        self.asd_btn.setAutoRepeat(False)
        self.asd_btn.setAutoDefault(False)
        self.asd_btn.setDefault(False)
        self.asd_btn.setFlat(False)
        self.asd_btn.setObjectName("asd_btn")
        self.verticalLayout_2.addWidget(self.asd_btn)
        self.non_asd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.non_asd_btn.setCheckable(True)
        self.non_asd_btn.setChecked(False)
        self.non_asd_btn.setObjectName("non_asd_btn")
        self.verticalLayout_2.addWidget(self.non_asd_btn)
        self.disease_unknown_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disease_unknown_btn.setCheckable(True)
        self.disease_unknown_btn.setObjectName("disease_unknown_btn")
        self.verticalLayout_2.addWidget(self.disease_unknown_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMinimumSize(QtCore.QSize(100, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(28, 498, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 4, 3, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setEnabled(True)
        self.wgt_video.setMinimumSize(QtCore.QSize(700, 700))
        self.wgt_video.setObjectName("wgt_video")
        self.verticalLayout_5.addWidget(self.wgt_video)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.verticalLayout.addWidget(self.stop_button)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setObjectName("next_button")
        self.verticalLayout.addWidget(self.next_button)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.attention_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">What part of the body do you focus on?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#ff0000;\">(single choice)</span></p></body></html>"))
        self.head_btn.setText(_translate("MainWindow", "head (頭)"))
        self.shoulder_btn.setText(_translate("MainWindow", "shoulder (cervical) 肩（頚胸椎）"))
        self.wrist_btn.setText(_translate("MainWindow", "wrist (腕)"))
        self.lumbar_pelvis_btn.setText(_translate("MainWindow", "lumbar, pelvis (腰椎・骨盤)"))
        self.foot_btn.setText(_translate("MainWindow", "foot　(足)"))
        self.focus_unkonwn_btn.setText(_translate("MainWindow", "don\'t know"))
        self.disease_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:20pt;\">Guess which disease is in the video?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:20pt; color:#ff0000;\">(single choice)</span></p></body></html>"))
        self.asd_btn.setText(_translate("MainWindow", "ASD"))
        self.non_asd_btn.setText(_translate("MainWindow", "non ASD"))
        self.disease_unknown_btn.setText(_translate("MainWindow", "don\'t know"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#ff0000;\">current:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#ff0000;\">total:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; color:#ff0000;\">remain:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; color:#ff0000;\"><br /></p></body></html>"))
        self.wgt_video.setWhatsThis(_translate("MainWindow", "video player"))
        self.start_button.setText(_translate("MainWindow", "start"))
        self.stop_button.setText(_translate("MainWindow", "stop"))
        self.next_button.setText(_translate("MainWindow", "next"))

class myVideoWidget(QVideoWidget):
    doubleClickedItem = pyqtSignal(str)  # 创建双击信号
    def __init__(self,parent=None):
        super(QVideoWidget,self).__init__(parent)
    def mouseDoubleClickEvent(self,QMouseEvent):     #双击事件
        self.doubleClickedItem.emit("double clicked")