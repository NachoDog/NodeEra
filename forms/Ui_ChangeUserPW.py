# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\ChangeUserPW.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeUserPW(object):
    def setupUi(self, ChangeUserPW):
        ChangeUserPW.setObjectName("ChangeUserPW")
        ChangeUserPW.resize(364, 259)
        ChangeUserPW.setSizeGripEnabled(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(ChangeUserPW)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(ChangeUserPW)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.editUserID = QtWidgets.QLineEdit(self.groupBox)
        self.editUserID.setObjectName("editUserID")
        self.gridLayout.addWidget(self.editUserID, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editPW = QtWidgets.QLineEdit(self.groupBox)
        self.editPW.setObjectName("editPW")
        self.gridLayout.addWidget(self.editPW, 1, 1, 1, 1)
        self.btnCurrentShow = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCurrentShow.sizePolicy().hasHeightForWidth())
        self.btnCurrentShow.setSizePolicy(sizePolicy)
        self.btnCurrentShow.setMinimumSize(QtCore.QSize(0, 0))
        self.btnCurrentShow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnCurrentShow.setObjectName("btnCurrentShow")
        self.gridLayout.addWidget(self.btnCurrentShow, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(ChangeUserPW)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 85))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.editNewPW = QtWidgets.QLineEdit(self.groupBox_2)
        self.editNewPW.setObjectName("editNewPW")
        self.gridLayout_2.addWidget(self.editNewPW, 0, 1, 1, 1)
        self.btnNewShow = QtWidgets.QPushButton(self.groupBox_2)
        self.btnNewShow.setMinimumSize(QtCore.QSize(0, 0))
        self.btnNewShow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnNewShow.setObjectName("btnNewShow")
        self.gridLayout_2.addWidget(self.btnNewShow, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.editRepeatPW = QtWidgets.QLineEdit(self.groupBox_2)
        self.editRepeatPW.setObjectName("editRepeatPW")
        self.gridLayout_2.addWidget(self.editRepeatPW, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 3)
        self.frame = QtWidgets.QFrame(ChangeUserPW)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.btnReset = QtWidgets.QPushButton(self.frame)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout_3.addWidget(self.btnReset, 0, 1, 1, 1)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout_3.addWidget(self.btnClose, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 1, 1, 2)
        self.label.setBuddy(self.editUserID)
        self.label_2.setBuddy(self.editPW)
        self.label_3.setBuddy(self.editNewPW)
        self.label_4.setBuddy(self.editRepeatPW)

        self.retranslateUi(ChangeUserPW)
        QtCore.QMetaObject.connectSlotsByName(ChangeUserPW)
        ChangeUserPW.setTabOrder(self.editUserID, self.editPW)
        ChangeUserPW.setTabOrder(self.editPW, self.btnCurrentShow)
        ChangeUserPW.setTabOrder(self.btnCurrentShow, self.editNewPW)
        ChangeUserPW.setTabOrder(self.editNewPW, self.btnNewShow)
        ChangeUserPW.setTabOrder(self.btnNewShow, self.editRepeatPW)
        ChangeUserPW.setTabOrder(self.editRepeatPW, self.btnReset)
        ChangeUserPW.setTabOrder(self.btnReset, self.btnClose)

    def retranslateUi(self, ChangeUserPW):
        _translate = QtCore.QCoreApplication.translate
        ChangeUserPW.setWindowTitle(_translate("ChangeUserPW", "Reset Password"))
        self.groupBox.setTitle(_translate("ChangeUserPW", "Current User/Password"))
        self.label.setText(_translate("ChangeUserPW", "User ID:"))
        self.label_2.setText(_translate("ChangeUserPW", "Password:"))
        self.btnCurrentShow.setText(_translate("ChangeUserPW", "Show"))
        self.groupBox_2.setTitle(_translate("ChangeUserPW", "New Password"))
        self.label_3.setText(_translate("ChangeUserPW", "New Password: "))
        self.btnNewShow.setText(_translate("ChangeUserPW", "Show"))
        self.label_4.setText(_translate("ChangeUserPW", "Repeat Password:"))
        self.btnReset.setText(_translate("ChangeUserPW", "Reset Password"))
        self.btnClose.setText(_translate("ChangeUserPW", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangeUserPW = QtWidgets.QDialog()
    ui = Ui_ChangeUserPW()
    ui.setupUi(ChangeUserPW)
    ChangeUserPW.show()
    sys.exit(app.exec_())
