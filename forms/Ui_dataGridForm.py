# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\forms\dataGridForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(803, 489)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabData = QtWidgets.QWidget()
        self.tabData.setObjectName("tabData")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabData)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.tabData)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnExport = QtWidgets.QPushButton(self.frame)
        self.btnExport.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/RUN and DATA TAB/Export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExport.setIcon(icon)
        self.btnExport.setIconSize(QtCore.QSize(32, 32))
        self.btnExport.setObjectName("btnExport")
        self.horizontalLayout.addWidget(self.btnExport)
        self.btnBegin = QtWidgets.QPushButton(self.frame)
        self.btnBegin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/RUN and DATA TAB/GridStart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBegin.setIcon(icon1)
        self.btnBegin.setIconSize(QtCore.QSize(32, 32))
        self.btnBegin.setObjectName("btnBegin")
        self.horizontalLayout.addWidget(self.btnBegin)
        self.btnBack = QtWidgets.QPushButton(self.frame)
        self.btnBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/RUN and DATA TAB/GridBack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon2)
        self.btnBack.setIconSize(QtCore.QSize(32, 32))
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtWidgets.QPushButton(self.frame)
        self.btnForward.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/RUN and DATA TAB/GridForward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon3)
        self.btnForward.setIconSize(QtCore.QSize(32, 32))
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.btnEnd = QtWidgets.QPushButton(self.frame)
        self.btnEnd.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/RUN and DATA TAB/GridEnd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnd.setIcon(icon4)
        self.btnEnd.setIconSize(QtCore.QSize(32, 32))
        self.btnEnd.setObjectName("btnEnd")
        self.horizontalLayout.addWidget(self.btnEnd)
        spacerItem = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnRefresh = QtWidgets.QPushButton(self.frame)
        self.btnRefresh.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-circular-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon5)
        self.btnRefresh.setIconSize(QtCore.QSize(32, 32))
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.btnNew = QtWidgets.QPushButton(self.frame)
        self.btnNew.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/FILE/FILE/CreateNew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNew.setIcon(icon6)
        self.btnNew.setIconSize(QtCore.QSize(32, 32))
        self.btnNew.setObjectName("btnNew")
        self.horizontalLayout.addWidget(self.btnNew)
        self.btnDelete = QtWidgets.QPushButton(self.frame)
        self.btnDelete.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/FILE/FILE/DeleteFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon7)
        self.btnDelete.setIconSize(QtCore.QSize(32, 32))
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.gridCypherData = QtWidgets.QTableView(self.frame_2)
        self.gridCypherData.setObjectName("gridCypherData")
        self.gridCypherData.verticalHeader().setDefaultSectionSize(30)
        self.gridCypherData.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout.addWidget(self.gridCypherData)
        self.txtPosition = QtWidgets.QLineEdit(self.frame_2)
        self.txtPosition.setReadOnly(True)
        self.txtPosition.setObjectName("txtPosition")
        self.verticalLayout.addWidget(self.txtPosition)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tabData, "")
        self.tabLog = QtWidgets.QWidget()
        self.tabLog.setObjectName("tabLog")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabLog)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.tabLog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLog = QtWidgets.QTableView(self.frame_4)
        self.gridLog.setObjectName("gridLog")
        self.horizontalLayout_2.addWidget(self.gridLog)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnExportLog = QtWidgets.QPushButton(self.frame_5)
        self.btnExportLog.setObjectName("btnExportLog")
        self.verticalLayout_3.addWidget(self.btnExportLog)
        self.btnClearLog = QtWidgets.QPushButton(self.frame_5)
        self.btnClearLog.setObjectName("btnClearLog")
        self.verticalLayout_3.addWidget(self.btnClearLog)
        spacerItem2 = QtWidgets.QSpacerItem(20, 631, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tabLog, "")
        self.tabTrace = QtWidgets.QWidget()
        self.tabTrace.setObjectName("tabTrace")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabTrace)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.tabTrace)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textTrace = QtWidgets.QTextBrowser(self.frame_6)
        self.textTrace.setObjectName("textTrace")
        self.horizontalLayout_3.addWidget(self.textTrace)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnExportTrace = QtWidgets.QPushButton(self.frame_7)
        self.btnExportTrace.setObjectName("btnExportTrace")
        self.verticalLayout_4.addWidget(self.btnExportTrace)
        self.btnClearTrace = QtWidgets.QPushButton(self.frame_7)
        self.btnClearTrace.setObjectName("btnClearTrace")
        self.verticalLayout_4.addWidget(self.btnClearTrace)
        spacerItem3 = QtWidgets.QSpacerItem(20, 164, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.tabWidget.addTab(self.tabTrace, "")
        self.verticalLayout_6.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnExport.setToolTip(_translate("Dialog", "Export results"))
        self.btnBegin.setToolTip(_translate("Dialog", "Move to first row"))
        self.btnForward.setToolTip(_translate("Dialog", "Move Forward"))
        self.btnEnd.setToolTip(_translate("Dialog", "Move To Last Row"))
        self.btnRefresh.setToolTip(_translate("Dialog", "Refresh Data"))
        self.btnNew.setToolTip(_translate("Dialog", "Create a new Node based on the template"))
        self.btnDelete.setToolTip(_translate("Dialog", "Delete the selected row(s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), _translate("Dialog", "Data"))
        self.btnExportLog.setText(_translate("Dialog", "Export..."))
        self.btnClearLog.setText(_translate("Dialog", "Clear Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLog), _translate("Dialog", "Log"))
        self.btnExportTrace.setText(_translate("Dialog", "Export..."))
        self.btnClearTrace.setText(_translate("Dialog", "Clear Trace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTrace), _translate("Dialog", "Trace"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

