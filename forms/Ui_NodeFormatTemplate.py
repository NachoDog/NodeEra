# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\Documents\ERIC\UI\NodeFormatTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NodeFormatTemplate(object):
    def setupUi(self, NodeFormatTemplate):
        NodeFormatTemplate.setObjectName("NodeFormatTemplate")
        NodeFormatTemplate.setWindowModality(QtCore.Qt.ApplicationModal)
        NodeFormatTemplate.resize(367, 411)
        NodeFormatTemplate.setSizeGripEnabled(False)
        NodeFormatTemplate.setModal(True)
        self.layoutWidget = QtWidgets.QWidget(NodeFormatTemplate)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 370, 331, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(self.layoutWidget)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.boxFillStyle = QtWidgets.QGroupBox(NodeFormatTemplate)
        self.boxFillStyle.setGeometry(QtCore.QRect(10, 70, 116, 99))
        self.boxFillStyle.setObjectName("boxFillStyle")
        self.formLayout_2 = QtWidgets.QFormLayout(self.boxFillStyle)
        self.formLayout_2.setObjectName("formLayout_2")
        self.rbNone = QtWidgets.QRadioButton(self.boxFillStyle)
        self.rbNone.setChecked(True)
        self.rbNone.setObjectName("rbNone")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rbNone)
        self.rbFill = QtWidgets.QRadioButton(self.boxFillStyle)
        self.rbFill.setObjectName("rbFill")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rbFill)
        self.rbPattern = QtWidgets.QRadioButton(self.boxFillStyle)
        self.rbPattern.setObjectName("rbPattern")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rbPattern)
        self.spinPattern = QtWidgets.QSpinBox(self.boxFillStyle)
        self.spinPattern.setMinimum(1)
        self.spinPattern.setMaximum(7)
        self.spinPattern.setObjectName("spinPattern")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinPattern)
        self.groupBox = QtWidgets.QGroupBox(NodeFormatTemplate)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 341, 152))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frmView = QtWidgets.QFrame(self.groupBox)
        self.frmView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmView.setObjectName("frmView")
        self.gridLayout_3.addWidget(self.frmView, 0, 0, 3, 1)
        self.btnFillColor = QtWidgets.QPushButton(self.groupBox)
        self.btnFillColor.setObjectName("btnFillColor")
        self.gridLayout_3.addWidget(self.btnFillColor, 0, 1, 1, 1)
        self.btnLineColor = QtWidgets.QPushButton(self.groupBox)
        self.btnLineColor.setObjectName("btnLineColor")
        self.gridLayout_3.addWidget(self.btnLineColor, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(NodeFormatTemplate)
        self.label.setGeometry(QtCore.QRect(9, 9, 65, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(NodeFormatTemplate)
        self.label_2.setGeometry(QtCore.QRect(9, 35, 64, 16))
        self.label_2.setObjectName("label_2")
        self.boxLineStyle = QtWidgets.QGroupBox(NodeFormatTemplate)
        self.boxLineStyle.setGeometry(QtCore.QRect(205, 10, 120, 191))
        self.boxLineStyle.setObjectName("boxLineStyle")
        self.formLayout = QtWidgets.QFormLayout(self.boxLineStyle)
        self.formLayout.setObjectName("formLayout")
        self.rbNoLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbNoLine.setObjectName("rbNoLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.rbNoLine)
        self.rbSolidLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbSolidLine.setObjectName("rbSolidLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rbSolidLine)
        self.rbDashLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDashLine.setObjectName("rbDashLine")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.rbDashLine)
        self.rbDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDotLine.setObjectName("rbDotLine")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.rbDotLine)
        self.rbDashDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDashDotLine.setObjectName("rbDashDotLine")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.rbDashDotLine)
        self.rbDashDotDotLine = QtWidgets.QRadioButton(self.boxLineStyle)
        self.rbDashDotDotLine.setObjectName("rbDashDotDotLine")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.rbDashDotDotLine)
        self.lblLineWidth = QtWidgets.QLabel(self.boxLineStyle)
        self.lblLineWidth.setObjectName("lblLineWidth")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblLineWidth)
        self.spinLineWidth = QtWidgets.QSpinBox(self.boxLineStyle)
        self.spinLineWidth.setMinimum(1)
        self.spinLineWidth.setMaximum(10)
        self.spinLineWidth.setObjectName("spinLineWidth")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinLineWidth)
        self.spinHeight = QtWidgets.QSpinBox(NodeFormatTemplate)
        self.spinHeight.setGeometry(QtCore.QRect(90, 10, 42, 22))
        self.spinHeight.setMinimum(25)
        self.spinHeight.setMaximum(200)
        self.spinHeight.setObjectName("spinHeight")
        self.spinWidth = QtWidgets.QSpinBox(NodeFormatTemplate)
        self.spinWidth.setGeometry(QtCore.QRect(90, 40, 42, 22))
        self.spinWidth.setMinimum(50)
        self.spinWidth.setMaximum(200)
        self.spinWidth.setProperty("value", 100)
        self.spinWidth.setObjectName("spinWidth")
        self.label.setBuddy(self.spinHeight)
        self.label_2.setBuddy(self.spinWidth)
        self.lblLineWidth.setBuddy(self.spinLineWidth)

        self.retranslateUi(NodeFormatTemplate)
        self.okButton.clicked.connect(NodeFormatTemplate.accept)
        self.cancelButton.clicked.connect(NodeFormatTemplate.reject)
        QtCore.QMetaObject.connectSlotsByName(NodeFormatTemplate)

    def retranslateUi(self, NodeFormatTemplate):
        _translate = QtCore.QCoreApplication.translate
        NodeFormatTemplate.setWindowTitle(_translate("NodeFormatTemplate", "Format Node Instance"))
        self.okButton.setText(_translate("NodeFormatTemplate", "&OK"))
        self.cancelButton.setText(_translate("NodeFormatTemplate", "&Cancel"))
        self.boxFillStyle.setTitle(_translate("NodeFormatTemplate", "Fill Style"))
        self.rbNone.setText(_translate("NodeFormatTemplate", "None"))
        self.rbFill.setText(_translate("NodeFormatTemplate", "Solid"))
        self.rbPattern.setText(_translate("NodeFormatTemplate", "Pattern"))
        self.groupBox.setTitle(_translate("NodeFormatTemplate", "Sample Node Formatting"))
        self.btnFillColor.setText(_translate("NodeFormatTemplate", "Fill Color"))
        self.btnLineColor.setText(_translate("NodeFormatTemplate", "Line Color"))
        self.label.setText(_translate("NodeFormatTemplate", "Node Heght:"))
        self.label_2.setText(_translate("NodeFormatTemplate", "Node Width:"))
        self.boxLineStyle.setTitle(_translate("NodeFormatTemplate", "Line Style"))
        self.rbNoLine.setText(_translate("NodeFormatTemplate", "No Line"))
        self.rbSolidLine.setText(_translate("NodeFormatTemplate", "Solid"))
        self.rbDashLine.setText(_translate("NodeFormatTemplate", "Dash"))
        self.rbDotLine.setText(_translate("NodeFormatTemplate", "Dot"))
        self.rbDashDotLine.setText(_translate("NodeFormatTemplate", "Dash Dot"))
        self.rbDashDotDotLine.setText(_translate("NodeFormatTemplate", "Dash Dot Dot"))
        self.lblLineWidth.setText(_translate("NodeFormatTemplate", "Line Width: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NodeFormatTemplate = QtWidgets.QDialog()
    ui = Ui_NodeFormatTemplate()
    ui.setupUi(NodeFormatTemplate)
    NodeFormatTemplate.show()
    sys.exit(app.exec_())

