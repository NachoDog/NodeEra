# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\FormPropertyBox.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormPropertyBox(object):
    def setupUi(self, FormPropertyBox):
        FormPropertyBox.setObjectName("FormPropertyBox")
        FormPropertyBox.resize(1211, 649)
        FormPropertyBox.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormPropertyBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vSplitter = QtWidgets.QSplitter(FormPropertyBox)
        self.vSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.vSplitter.setObjectName("vSplitter")
        self.frmPreview = QtWidgets.QFrame(self.vSplitter)
        self.frmPreview.setFrameShape(QtWidgets.QFrame.Panel)
        self.frmPreview.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmPreview.setObjectName("frmPreview")
        self.frmInspector = QtWidgets.QFrame(self.vSplitter)
        self.frmInspector.setFrameShape(QtWidgets.QFrame.Box)
        self.frmInspector.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmInspector.setObjectName("frmInspector")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmInspector)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hSplitter = QtWidgets.QSplitter(self.frmInspector)
        self.hSplitter.setOrientation(QtCore.Qt.Vertical)
        self.hSplitter.setObjectName("hSplitter")
        self.frmOutline = QtWidgets.QFrame(self.hSplitter)
        self.frmOutline.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmOutline.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmOutline.setObjectName("frmOutline")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmOutline)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tvOutline = QtWidgets.QTreeWidget(self.frmOutline)
        self.tvOutline.setObjectName("tvOutline")
        self.tvOutline.headerItem().setText(0, "1")
        self.horizontalLayout_2.addWidget(self.tvOutline)
        self.frame_2 = QtWidgets.QFrame(self.frmOutline)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnAdd = QtWidgets.QPushButton(self.frame_2)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_3.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.frame_2)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout_3.addWidget(self.btnRemove)
        self.btnUp = QtWidgets.QPushButton(self.frame_2)
        self.btnUp.setObjectName("btnUp")
        self.verticalLayout_3.addWidget(self.btnUp)
        self.btnDown = QtWidgets.QPushButton(self.frame_2)
        self.btnDown.setObjectName("btnDown")
        self.verticalLayout_3.addWidget(self.btnDown)
        spacerItem = QtWidgets.QSpacerItem(20, 103, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frmMetaBox = QtWidgets.QFrame(self.hSplitter)
        self.frmMetaBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmMetaBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMetaBox.setObjectName("frmMetaBox")
        self.gridLayout = QtWidgets.QGridLayout(self.frmMetaBox)
        self.gridLayout.setObjectName("gridLayout")
        self.gridMetaBox = QtWidgets.QTableView(self.frmMetaBox)
        self.gridMetaBox.setObjectName("gridMetaBox")
        self.gridLayout.addWidget(self.gridMetaBox, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.hSplitter)
        self.verticalLayout.addWidget(self.vSplitter)
        self.frame = QtWidgets.QFrame(FormPropertyBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 43))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 43))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(540, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem2 = QtWidgets.QSpacerItem(540, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(FormPropertyBox)
        QtCore.QMetaObject.connectSlotsByName(FormPropertyBox)

    def retranslateUi(self, FormPropertyBox):
        _translate = QtCore.QCoreApplication.translate
        FormPropertyBox.setWindowTitle(_translate("FormPropertyBox", "Form Designer"))
        self.btnAdd.setText(_translate("FormPropertyBox", "Add"))
        self.btnRemove.setText(_translate("FormPropertyBox", "Remove"))
        self.btnUp.setText(_translate("FormPropertyBox", "Up"))
        self.btnDown.setText(_translate("FormPropertyBox", "Down"))
        self.btnClose.setText(_translate("FormPropertyBox", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormPropertyBox = QtWidgets.QDialog()
    ui = Ui_FormPropertyBox()
    ui.setupUi(FormPropertyBox)
    FormPropertyBox.show()
    sys.exit(app.exec_())
