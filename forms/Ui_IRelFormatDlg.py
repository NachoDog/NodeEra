# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\IRelFormatDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IRelFormatDlg(object):
    def setupUi(self, IRelFormatDlg):
        IRelFormatDlg.setObjectName("IRelFormatDlg")
        IRelFormatDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        IRelFormatDlg.resize(326, 379)
        IRelFormatDlg.setSizeGripEnabled(False)
        IRelFormatDlg.setModal(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(IRelFormatDlg)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.boxLineStyle = QtWidgets.QGroupBox(IRelFormatDlg)
        self.boxLineStyle.setObjectName("boxLineStyle")
        self.gridLayout = QtWidgets.QGridLayout(self.boxLineStyle)
        self.gridLayout.setObjectName("gridLayout")
        self.rbSolidLine = QtWidgets.QRadioButton(self.boxLineStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbSolidLine.sizePolicy().hasHeightForWidth())
        self.rbSolidLine.setSizePolicy(sizePolicy)
        self.rbSolidLine.setObjectName("rbSolidLine")
        self.gridLayout.addWidget(self.rbSolidLine, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 3)
        self.rbDashLine = QtWidgets.QRadioButton(self.boxLineStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbDashLine.sizePolicy().hasHeightForWidth())
        self.rbDashLine.setSizePolicy(sizePolicy)
        self.rbDashLine.setObjectName("rbDashLine")
        self.gridLayout.addWidget(self.rbDashLine, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 3)
        self.rbDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbDotLine.sizePolicy().hasHeightForWidth())
        self.rbDotLine.setSizePolicy(sizePolicy)
        self.rbDotLine.setObjectName("rbDotLine")
        self.gridLayout.addWidget(self.rbDotLine, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 3)
        self.rbDashDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbDashDotLine.sizePolicy().hasHeightForWidth())
        self.rbDashDotLine.setSizePolicy(sizePolicy)
        self.rbDashDotLine.setObjectName("rbDashDotLine")
        self.gridLayout.addWidget(self.rbDashDotLine, 3, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 2, 2, 3)
        spacerItem4 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 3, 2, 2)
        self.rbDashDotDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbDashDotDotLine.sizePolicy().hasHeightForWidth())
        self.rbDashDotDotLine.setSizePolicy(sizePolicy)
        self.rbDashDotDotLine.setObjectName("rbDashDotDotLine")
        self.gridLayout.addWidget(self.rbDashDotDotLine, 5, 0, 1, 3)
        self.lblLineWidth = QtWidgets.QLabel(self.boxLineStyle)
        self.lblLineWidth.setObjectName("lblLineWidth")
        self.gridLayout.addWidget(self.lblLineWidth, 6, 0, 1, 1)
        self.spinLineWidth = QtWidgets.QSpinBox(self.boxLineStyle)
        self.spinLineWidth.setMinimum(1)
        self.spinLineWidth.setMaximum(10)
        self.spinLineWidth.setObjectName("spinLineWidth")
        self.gridLayout.addWidget(self.spinLineWidth, 6, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 4, 1, 1)
        self.gridLayout_3.addWidget(self.boxLineStyle, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 1, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(IRelFormatDlg)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frmView = QtWidgets.QFrame(self.groupBox)
        self.frmView.setMinimumSize(QtCore.QSize(88, 88))
        self.frmView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmView.setObjectName("frmView")
        self.gridLayout_2.addWidget(self.frmView, 0, 0, 2, 1)
        self.btnLineColor = QtWidgets.QPushButton(self.groupBox)
        self.btnLineColor.setObjectName("btnLineColor")
        self.gridLayout_2.addWidget(self.btnLineColor, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 2, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem9 = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem9)
        self.okButton = QtWidgets.QPushButton(IRelFormatDlg)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(IRelFormatDlg)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem10)
        self.gridLayout_3.addLayout(self.hboxlayout, 2, 0, 1, 3)
        self.lblLineWidth.setBuddy(self.spinLineWidth)

        self.retranslateUi(IRelFormatDlg)
        self.okButton.clicked.connect(IRelFormatDlg.accept)
        self.cancelButton.clicked.connect(IRelFormatDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(IRelFormatDlg)
        IRelFormatDlg.setTabOrder(self.rbSolidLine, self.rbDashLine)
        IRelFormatDlg.setTabOrder(self.rbDashLine, self.rbDotLine)
        IRelFormatDlg.setTabOrder(self.rbDotLine, self.rbDashDotLine)
        IRelFormatDlg.setTabOrder(self.rbDashDotLine, self.rbDashDotDotLine)
        IRelFormatDlg.setTabOrder(self.rbDashDotDotLine, self.spinLineWidth)
        IRelFormatDlg.setTabOrder(self.spinLineWidth, self.btnLineColor)
        IRelFormatDlg.setTabOrder(self.btnLineColor, self.okButton)
        IRelFormatDlg.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, IRelFormatDlg):
        _translate = QtCore.QCoreApplication.translate
        IRelFormatDlg.setWindowTitle(_translate("IRelFormatDlg", "Instance Relationship Format Editor"))
        self.boxLineStyle.setTitle(_translate("IRelFormatDlg", "Line Style"))
        self.rbSolidLine.setText(_translate("IRelFormatDlg", "Solid"))
        self.rbDashLine.setText(_translate("IRelFormatDlg", "Dash"))
        self.rbDotLine.setText(_translate("IRelFormatDlg", "Dot"))
        self.rbDashDotLine.setText(_translate("IRelFormatDlg", "Dash Dot"))
        self.rbDashDotDotLine.setText(_translate("IRelFormatDlg", "Dash Dot Dot"))
        self.lblLineWidth.setText(_translate("IRelFormatDlg", "Line Width: "))
        self.groupBox.setTitle(_translate("IRelFormatDlg", "Instance Relationship Preview"))
        self.btnLineColor.setText(_translate("IRelFormatDlg", "Line Color"))
        self.okButton.setText(_translate("IRelFormatDlg", "&OK"))
        self.cancelButton.setText(_translate("IRelFormatDlg", "&Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IRelFormatDlg = QtWidgets.QDialog()
    ui = Ui_IRelFormatDlg()
    ui.setupUi(IRelFormatDlg)
    IRelFormatDlg.show()
    sys.exit(app.exec_())
