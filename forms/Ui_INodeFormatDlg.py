# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\INodeFormatDlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_INodeFormat(object):
    def setupUi(self, INodeFormat):
        INodeFormat.setObjectName("INodeFormat")
        INodeFormat.setWindowModality(QtCore.Qt.ApplicationModal)
        INodeFormat.resize(396, 517)
        INodeFormat.setSizeGripEnabled(False)
        INodeFormat.setModal(True)
        self.gridLayout_5 = QtWidgets.QGridLayout(INodeFormat)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(INodeFormat)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.spinHeight = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinHeight.setMinimum(25)
        self.spinHeight.setMaximum(200)
        self.spinHeight.setObjectName("spinHeight")
        self.gridLayout_3.addWidget(self.spinHeight, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinWidth = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinWidth.setMinimum(50)
        self.spinWidth.setMaximum(200)
        self.spinWidth.setProperty("value", 100)
        self.spinWidth.setObjectName("spinWidth")
        self.gridLayout_3.addWidget(self.spinWidth, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(114, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.boxLineStyle = QtWidgets.QGroupBox(INodeFormat)
        self.boxLineStyle.setObjectName("boxLineStyle")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.boxLineStyle)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbNoLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbNoLine.setObjectName("rbNoLine")
        self.gridLayout_2.addWidget(self.rbNoLine, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 2)
        self.rbSolidLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbSolidLine.setObjectName("rbSolidLine")
        self.gridLayout_2.addWidget(self.rbSolidLine, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 2)
        self.rbDashLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDashLine.setObjectName("rbDashLine")
        self.gridLayout_2.addWidget(self.rbDashLine, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 2)
        self.rbDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDotLine.setObjectName("rbDotLine")
        self.gridLayout_2.addWidget(self.rbDotLine, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 1, 1, 2)
        self.rbDashDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDashDotLine.setObjectName("rbDashDotLine")
        self.gridLayout_2.addWidget(self.rbDashDotLine, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 1, 1, 2)
        self.rbDashDotDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDashDotDotLine.setObjectName("rbDashDotDotLine")
        self.gridLayout_2.addWidget(self.rbDashDotDotLine, 5, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 5, 2, 1, 2)
        self.lblLineWidth = QtWidgets.QLabel(self.boxLineStyle)
        self.lblLineWidth.setObjectName("lblLineWidth")
        self.gridLayout_2.addWidget(self.lblLineWidth, 6, 0, 1, 1)
        self.spinLineWidth = QtWidgets.QSpinBox(self.boxLineStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinLineWidth.sizePolicy().hasHeightForWidth())
        self.spinLineWidth.setSizePolicy(sizePolicy)
        self.spinLineWidth.setMinimum(1)
        self.spinLineWidth.setMaximum(10)
        self.spinLineWidth.setObjectName("spinLineWidth")
        self.gridLayout_2.addWidget(self.spinLineWidth, 6, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 6, 3, 1, 1)
        self.gridLayout_5.addWidget(self.boxLineStyle, 0, 2, 2, 1)
        self.boxFillStyle = QtWidgets.QGroupBox(INodeFormat)
        self.boxFillStyle.setObjectName("boxFillStyle")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.boxFillStyle)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rbNone = QtWidgets.QRadioButton(self.boxFillStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbNone.sizePolicy().hasHeightForWidth())
        self.rbNone.setSizePolicy(sizePolicy)
        self.rbNone.setChecked(True)
        self.rbNone.setObjectName("rbNone")
        self.gridLayout_4.addWidget(self.rbNone, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 1, 1, 1)
        self.rbFill = QtWidgets.QRadioButton(self.boxFillStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbFill.sizePolicy().hasHeightForWidth())
        self.rbFill.setSizePolicy(sizePolicy)
        self.rbFill.setObjectName("rbFill")
        self.gridLayout_4.addWidget(self.rbFill, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 1, 1, 1, 1)
        self.rbPattern = QtWidgets.QRadioButton(self.boxFillStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbPattern.sizePolicy().hasHeightForWidth())
        self.rbPattern.setSizePolicy(sizePolicy)
        self.rbPattern.setObjectName("rbPattern")
        self.gridLayout_4.addWidget(self.rbPattern, 2, 0, 1, 1)
        self.spinPattern = QtWidgets.QSpinBox(self.boxFillStyle)
        self.spinPattern.setMinimum(1)
        self.spinPattern.setMaximum(7)
        self.spinPattern.setObjectName("spinPattern")
        self.gridLayout_4.addWidget(self.spinPattern, 2, 1, 1, 1)
        self.gridLayout_5.addWidget(self.boxFillStyle, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(114, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(INodeFormat)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.frmView = QtWidgets.QFrame(self.groupBox)
        self.frmView.setMinimumSize(QtCore.QSize(150, 150))
        self.frmView.setMaximumSize(QtCore.QSize(150, 150))
        self.frmView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmView.setObjectName("frmView")
        self.gridLayout.addWidget(self.frmView, 0, 0, 3, 1)
        self.btnFillColor = QtWidgets.QPushButton(self.groupBox)
        self.btnFillColor.setObjectName("btnFillColor")
        self.gridLayout.addWidget(self.btnFillColor, 0, 1, 1, 1)
        self.btnLineColor = QtWidgets.QPushButton(self.groupBox)
        self.btnLineColor.setObjectName("btnLineColor")
        self.gridLayout.addWidget(self.btnLineColor, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 2, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 2, 0, 1, 3)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem12 = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem12)
        self.okButton = QtWidgets.QPushButton(INodeFormat)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(INodeFormat)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem13)
        self.gridLayout_5.addLayout(self.hboxlayout, 3, 0, 1, 3)
        self.label.setBuddy(self.spinHeight)
        self.label_2.setBuddy(self.spinWidth)
        self.lblLineWidth.setBuddy(self.spinLineWidth)

        self.retranslateUi(INodeFormat)
        self.okButton.clicked.connect(INodeFormat.accept)
        self.cancelButton.clicked.connect(INodeFormat.reject)
        QtCore.QMetaObject.connectSlotsByName(INodeFormat)
        INodeFormat.setTabOrder(self.spinHeight, self.spinWidth)
        INodeFormat.setTabOrder(self.spinWidth, self.rbNone)
        INodeFormat.setTabOrder(self.rbNone, self.rbFill)
        INodeFormat.setTabOrder(self.rbFill, self.rbPattern)
        INodeFormat.setTabOrder(self.rbPattern, self.spinPattern)
        INodeFormat.setTabOrder(self.spinPattern, self.rbNoLine)
        INodeFormat.setTabOrder(self.rbNoLine, self.rbSolidLine)
        INodeFormat.setTabOrder(self.rbSolidLine, self.rbDashLine)
        INodeFormat.setTabOrder(self.rbDashLine, self.rbDotLine)
        INodeFormat.setTabOrder(self.rbDotLine, self.rbDashDotLine)
        INodeFormat.setTabOrder(self.rbDashDotLine, self.rbDashDotDotLine)
        INodeFormat.setTabOrder(self.rbDashDotDotLine, self.spinLineWidth)
        INodeFormat.setTabOrder(self.spinLineWidth, self.btnFillColor)
        INodeFormat.setTabOrder(self.btnFillColor, self.btnLineColor)
        INodeFormat.setTabOrder(self.btnLineColor, self.okButton)
        INodeFormat.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, INodeFormat):
        _translate = QtCore.QCoreApplication.translate
        INodeFormat.setWindowTitle(_translate("INodeFormat", "Instance Node Format Editor"))
        self.groupBox_2.setTitle(_translate("INodeFormat", "Node Size"))
        self.label.setText(_translate("INodeFormat", "Height"))
        self.label_2.setText(_translate("INodeFormat", "Width"))
        self.boxLineStyle.setTitle(_translate("INodeFormat", "Line Style"))
        self.rbNoLine.setText(_translate("INodeFormat", "No Line"))
        self.rbSolidLine.setText(_translate("INodeFormat", "Solid"))
        self.rbDashLine.setText(_translate("INodeFormat", "Dash"))
        self.rbDotLine.setText(_translate("INodeFormat", "Dot"))
        self.rbDashDotLine.setText(_translate("INodeFormat", "Dash Dot"))
        self.rbDashDotDotLine.setText(_translate("INodeFormat", "Dash Dot Dot"))
        self.lblLineWidth.setText(_translate("INodeFormat", "Line Width: "))
        self.boxFillStyle.setTitle(_translate("INodeFormat", "Fill Style"))
        self.rbNone.setText(_translate("INodeFormat", "None"))
        self.rbFill.setText(_translate("INodeFormat", "Solid"))
        self.rbPattern.setText(_translate("INodeFormat", "Pattern"))
        self.groupBox.setTitle(_translate("INodeFormat", "Instance Node Preview"))
        self.btnFillColor.setText(_translate("INodeFormat", "Fill Color"))
        self.btnLineColor.setText(_translate("INodeFormat", "Line Color"))
        self.okButton.setText(_translate("INodeFormat", "&OK"))
        self.cancelButton.setText(_translate("INodeFormat", "&Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    INodeFormat = QtWidgets.QDialog()
    ui = Ui_INodeFormat()
    ui.setupUi(INodeFormat)
    INodeFormat.show()
    sys.exit(app.exec_())
