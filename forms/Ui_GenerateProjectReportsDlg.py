# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\GenerateProjectReportsDlg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenerateProjectReportsDlg(object):
    def setupUi(self, GenerateProjectReportsDlg):
        GenerateProjectReportsDlg.setObjectName("GenerateProjectReportsDlg")
        GenerateProjectReportsDlg.setWindowModality(QtCore.Qt.WindowModal)
        GenerateProjectReportsDlg.resize(1074, 404)
        GenerateProjectReportsDlg.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(GenerateProjectReportsDlg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(GenerateProjectReportsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cbReportType = QtWidgets.QComboBox(self.frame_2)
        self.cbReportType.setObjectName("cbReportType")
        self.cbReportType.addItem("")
        self.gridLayout.addWidget(self.cbReportType, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(326, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.lblOutputDir = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOutputDir.sizePolicy().hasHeightForWidth())
        self.lblOutputDir.setSizePolicy(sizePolicy)
        self.lblOutputDir.setMinimumSize(QtCore.QSize(431, 20))
        self.lblOutputDir.setFrameShape(QtWidgets.QFrame.Box)
        self.lblOutputDir.setText("")
        self.lblOutputDir.setObjectName("lblOutputDir")
        self.gridLayout.addWidget(self.lblOutputDir, 1, 2, 1, 2)
        self.btnSelectDir = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSelectDir.sizePolicy().hasHeightForWidth())
        self.btnSelectDir.setSizePolicy(sizePolicy)
        self.btnSelectDir.setObjectName("btnSelectDir")
        self.gridLayout.addWidget(self.btnSelectDir, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(434, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 5, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(GenerateProjectReportsDlg)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneral = QtWidgets.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabGeneral)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.tabGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 180))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.txtTitle = QtWidgets.QLineEdit(self.frame_5)
        self.txtTitle.setMinimumSize(QtCore.QSize(500, 0))
        self.txtTitle.setObjectName("txtTitle")
        self.gridLayout_2.addWidget(self.txtTitle, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.txtHomeTitle = QtWidgets.QLineEdit(self.frame_5)
        self.txtHomeTitle.setMinimumSize(QtCore.QSize(500, 0))
        self.txtHomeTitle.setObjectName("txtHomeTitle")
        self.gridLayout_2.addWidget(self.txtHomeTitle, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.txtAuthor = QtWidgets.QLineEdit(self.frame_5)
        self.txtAuthor.setMinimumSize(QtCore.QSize(250, 0))
        self.txtAuthor.setObjectName("txtAuthor")
        self.gridLayout_2.addWidget(self.txtAuthor, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.frmImage = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmImage.sizePolicy().hasHeightForWidth())
        self.frmImage.setSizePolicy(sizePolicy)
        self.frmImage.setMinimumSize(QtCore.QSize(40, 40))
        self.frmImage.setMaximumSize(QtCore.QSize(40, 40))
        self.frmImage.setFrameShape(QtWidgets.QFrame.Box)
        self.frmImage.setText("")
        self.frmImage.setObjectName("frmImage")
        self.gridLayout_2.addWidget(self.frmImage, 3, 1, 1, 1)
        self.txtImageFile = QtWidgets.QLineEdit(self.frame_5)
        self.txtImageFile.setMinimumSize(QtCore.QSize(500, 0))
        self.txtImageFile.setReadOnly(True)
        self.txtImageFile.setObjectName("txtImageFile")
        self.gridLayout_2.addWidget(self.txtImageFile, 3, 2, 1, 1)
        self.btnLoadImage = QtWidgets.QPushButton(self.frame_5)
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.gridLayout_2.addWidget(self.btnLoadImage, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(204, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.txtFooter = QtWidgets.QLineEdit(self.frame_5)
        self.txtFooter.setMinimumSize(QtCore.QSize(500, 0))
        self.txtFooter.setObjectName("txtFooter")
        self.gridLayout_2.addWidget(self.txtFooter, 4, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabObjects = QtWidgets.QWidget()
        self.tabObjects.setObjectName("tabObjects")
        self.tabWidget.addTab(self.tabObjects, "")
        self.tabOutput = QtWidgets.QWidget()
        self.tabOutput.setObjectName("tabOutput")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabOutput)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtDisplayDoc = QtWidgets.QTextEdit(self.tabOutput)
        self.txtDisplayDoc.setObjectName("txtDisplayDoc")
        self.gridLayout_3.addWidget(self.txtDisplayDoc, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabOutput, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnGenerate = QtWidgets.QPushButton(self.frame_4)
        self.btnGenerate.setObjectName("btnGenerate")
        self.verticalLayout.addWidget(self.btnGenerate)
        self.btnViewBrowser = QtWidgets.QPushButton(self.frame_4)
        self.btnViewBrowser.setObjectName("btnViewBrowser")
        self.verticalLayout.addWidget(self.btnViewBrowser)
        self.btnPrint = QtWidgets.QPushButton(self.frame_4)
        self.btnPrint.setObjectName("btnPrint")
        self.verticalLayout.addWidget(self.btnPrint)
        self.btnMako = QtWidgets.QPushButton(self.frame_4)
        self.btnMako.setObjectName("btnMako")
        self.verticalLayout.addWidget(self.btnMako)
        spacerItem4 = QtWidgets.QSpacerItem(20, 210, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(GenerateProjectReportsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem6 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.frame)
        self.label_2.setBuddy(self.cbReportType)

        self.retranslateUi(GenerateProjectReportsDlg)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GenerateProjectReportsDlg)

    def retranslateUi(self, GenerateProjectReportsDlg):
        _translate = QtCore.QCoreApplication.translate
        GenerateProjectReportsDlg.setWindowTitle(_translate("GenerateProjectReportsDlg", "Generate Project Report"))
        self.label_2.setText(_translate("GenerateProjectReportsDlg", "Report Type:"))
        self.cbReportType.setItemText(0, _translate("GenerateProjectReportsDlg", "HTML"))
        self.label_3.setText(_translate("GenerateProjectReportsDlg", "Output Directory:"))
        self.btnSelectDir.setText(_translate("GenerateProjectReportsDlg", "Path..."))
        self.label.setText(_translate("GenerateProjectReportsDlg", "Header Title:"))
        self.txtTitle.setToolTip(_translate("GenerateProjectReportsDlg", "Title appears on the page header."))
        self.label_4.setText(_translate("GenerateProjectReportsDlg", "Home Page Title:"))
        self.txtHomeTitle.setToolTip(_translate("GenerateProjectReportsDlg", "Title of the Home page."))
        self.label_5.setText(_translate("GenerateProjectReportsDlg", "Author:"))
        self.txtAuthor.setToolTip(_translate("GenerateProjectReportsDlg", "Author appears on the Home page."))
        self.label_6.setText(_translate("GenerateProjectReportsDlg", "Image:"))
        self.txtImageFile.setToolTip(_translate("GenerateProjectReportsDlg", "Image file name"))
        self.btnLoadImage.setText(_translate("GenerateProjectReportsDlg", "Select Image..."))
        self.label_7.setText(_translate("GenerateProjectReportsDlg", "Footer:"))
        self.txtFooter.setToolTip(_translate("GenerateProjectReportsDlg", "Appears in page footer, typically used for Copyright or Classification."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("GenerateProjectReportsDlg", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabObjects), _translate("GenerateProjectReportsDlg", "Select Objects"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOutput), _translate("GenerateProjectReportsDlg", "Output"))
        self.btnGenerate.setText(_translate("GenerateProjectReportsDlg", "Generate"))
        self.btnViewBrowser.setText(_translate("GenerateProjectReportsDlg", "View in Browser"))
        self.btnPrint.setText(_translate("GenerateProjectReportsDlg", "Print..."))
        self.btnMako.setText(_translate("GenerateProjectReportsDlg", "Generate Mako"))
        self.btnClose.setText(_translate("GenerateProjectReportsDlg", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerateProjectReportsDlg = QtWidgets.QDialog()
    ui = Ui_GenerateProjectReportsDlg()
    ui.setupUi(GenerateProjectReportsDlg)
    GenerateProjectReportsDlg.show()
    sys.exit(app.exec_())

