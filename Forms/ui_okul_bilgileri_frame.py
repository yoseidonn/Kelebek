# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yusuf/Belgeler/Projeler/Software/Kelebek/Kelebek BETA/Forms/okul_bilgileri_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(744, 426)
        Frame.setStyleSheet("QFrame{\n"
"border: none;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main = QtWidgets.QFrame(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.main)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.bilgiler = QtWidgets.QGroupBox(self.frame)
        self.bilgiler.setObjectName("bilgiler")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bilgiler)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.bilgiler)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.typeText_3 = QtWidgets.QLabel(self.frame_9)
        self.typeText_3.setObjectName("typeText_3")
        self.verticalLayout_5.addWidget(self.typeText_3)
        self.managerNameIn = QtWidgets.QLineEdit(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.managerNameIn.sizePolicy().hasHeightForWidth())
        self.managerNameIn.setSizePolicy(sizePolicy)
        self.managerNameIn.setMinimumSize(QtCore.QSize(350, 0))
        self.managerNameIn.setMaximumSize(QtCore.QSize(167000, 16777215))
        self.managerNameIn.setText("")
        self.managerNameIn.setPlaceholderText("")
        self.managerNameIn.setObjectName("managerNameIn")
        self.verticalLayout_5.addWidget(self.managerNameIn)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.typeText_2 = QtWidgets.QLabel(self.frame_12)
        self.typeText_2.setObjectName("typeText_2")
        self.verticalLayout_8.addWidget(self.typeText_2)
        self.schoolNameIn = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schoolNameIn.sizePolicy().hasHeightForWidth())
        self.schoolNameIn.setSizePolicy(sizePolicy)
        self.schoolNameIn.setMinimumSize(QtCore.QSize(350, 0))
        self.schoolNameIn.setMaximumSize(QtCore.QSize(167000, 16777215))
        self.schoolNameIn.setText("")
        self.schoolNameIn.setPlaceholderText("")
        self.schoolNameIn.setObjectName("schoolNameIn")
        self.verticalLayout_8.addWidget(self.schoolNameIn)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.typeText = QtWidgets.QLabel(self.frame_8)
        self.typeText.setObjectName("typeText")
        self.verticalLayout_11.addWidget(self.typeText)
        self.typeCombo = QtWidgets.QComboBox(self.frame_8)
        self.typeCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCombo.sizePolicy().hasHeightForWidth())
        self.typeCombo.setSizePolicy(sizePolicy)
        self.typeCombo.setObjectName("typeCombo")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.verticalLayout_11.addWidget(self.typeCombo)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame_7 = QtWidgets.QFrame(self.bilgiler)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_13 = QtWidgets.QFrame(self.frame_6)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.managerNameSaveBtn = QtWidgets.QPushButton(self.frame_13)
        self.managerNameSaveBtn.setObjectName("managerNameSaveBtn")
        self.horizontalLayout_3.addWidget(self.managerNameSaveBtn)
        self.managerNameDiscardBtn = QtWidgets.QPushButton(self.frame_13)
        self.managerNameDiscardBtn.setObjectName("managerNameDiscardBtn")
        self.horizontalLayout_3.addWidget(self.managerNameDiscardBtn)
        self.verticalLayout_9.addWidget(self.frame_13)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.schoolNameSaveBtn = QtWidgets.QPushButton(self.frame_14)
        self.schoolNameSaveBtn.setObjectName("schoolNameSaveBtn")
        self.horizontalLayout_9.addWidget(self.schoolNameSaveBtn)
        self.schoolNameDiscardBtn = QtWidgets.QPushButton(self.frame_14)
        self.schoolNameDiscardBtn.setObjectName("schoolNameDiscardBtn")
        self.horizontalLayout_9.addWidget(self.schoolNameDiscardBtn)
        self.verticalLayout_10.addWidget(self.frame_14)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_5 = QtWidgets.QFrame(self.frame_7)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.typeNameSaveBtn = QtWidgets.QPushButton(self.frame_11)
        self.typeNameSaveBtn.setObjectName("typeNameSaveBtn")
        self.horizontalLayout.addWidget(self.typeNameSaveBtn)
        self.typeNameDiscardBtn = QtWidgets.QPushButton(self.frame_11)
        self.typeNameDiscardBtn.setObjectName("typeNameDiscardBtn")
        self.horizontalLayout.addWidget(self.typeNameDiscardBtn)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.horizontalLayout_8.addWidget(self.bilgiler)
        self.verticalLayout_2.addWidget(self.frame)
        self.footer = QtWidgets.QGroupBox(self.main)
        self.footer.setObjectName("footer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table = QtWidgets.QTableWidget(self.footer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout_4.addWidget(self.table)
        self.verticalLayout_2.addWidget(self.footer)
        self.verticalLayout.addWidget(self.main)
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser, 0, QtCore.Qt.AlignTop)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.bilgiler.setTitle(_translate("Frame", "Okul Bilgileri"))
        self.typeText_3.setText(_translate("Frame", "Okul müdürü"))
        self.typeText_2.setText(_translate("Frame", "Okul adı"))
        self.typeText.setText(_translate("Frame", "Okul türü"))
        self.typeCombo.setItemText(0, _translate("Frame", "Lise"))
        self.typeCombo.setItemText(1, _translate("Frame", "Ortaokul"))
        self.managerNameSaveBtn.setText(_translate("Frame", "Kaydet"))
        self.managerNameDiscardBtn.setText(_translate("Frame", "İptal"))
        self.schoolNameSaveBtn.setText(_translate("Frame", "Kaydet"))
        self.schoolNameDiscardBtn.setText(_translate("Frame", "İptal"))
        self.typeNameSaveBtn.setText(_translate("Frame", "Kaydet"))
        self.typeNameDiscardBtn.setText(_translate("Frame", "İptal"))
        self.footer.setTitle(_translate("Frame", "İstatistikler"))
        self.textBrowser.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">NOT: İstatistiklerdeki salon sayısı salon adlarına verdiğiniz isimlere göre yanlış çıkabilir. Mevcut algoritma salon adlarında sadece &quot;/&quot; ayracı kullanımına göre çalışıyor.</span></p></body></html>"))
import resources_rc
