# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\SkyDrive\Documents\REPOS\NODEERA\forms\RelPropertyBox.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RelPropertyBox(object):
    def setupUi(self, RelPropertyBox):
        RelPropertyBox.setObjectName("RelPropertyBox")
        RelPropertyBox.setWindowModality(QtCore.Qt.ApplicationModal)
        RelPropertyBox.resize(718, 471)
        RelPropertyBox.setSizeGripEnabled(True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(RelPropertyBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblHeader = QtWidgets.QLabel(RelPropertyBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setObjectName("lblHeader")
        self.verticalLayout_5.addWidget(self.lblHeader)
        self.frame_2 = QtWidgets.QFrame(RelPropertyBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.editName = QtWidgets.QLineEdit(self.frame_2)
        self.editName.setObjectName("editName")
        self.horizontalLayout_3.addWidget(self.editName)
        spacerItem = QtWidgets.QSpacerItem(142, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.rbDefaultFormat = QtWidgets.QRadioButton(self.frame_2)
        self.rbDefaultFormat.setObjectName("rbDefaultFormat")
        self.horizontalLayout_3.addWidget(self.rbDefaultFormat)
        self.rbCustomFormat = QtWidgets.QRadioButton(self.frame_2)
        self.rbCustomFormat.setObjectName("rbCustomFormat")
        self.horizontalLayout_3.addWidget(self.rbCustomFormat)
        self.btnDefineFormat = QtWidgets.QPushButton(self.frame_2)
        self.btnDefineFormat.setObjectName("btnDefineFormat")
        self.horizontalLayout_3.addWidget(self.btnDefineFormat)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tabRelationship = QtWidgets.QTabWidget(RelPropertyBox)
        self.tabRelationship.setObjectName("tabRelationship")
        self.tabDefinition = QtWidgets.QWidget()
        self.tabDefinition.setObjectName("tabDefinition")
        self.groupBox_Properties = QtWidgets.QGroupBox(self.tabDefinition)
        self.groupBox_Properties.setGeometry(QtCore.QRect(0, 10, 591, 281))
        self.groupBox_Properties.setMinimumSize(QtCore.QSize(0, 180))
        self.groupBox_Properties.setToolTip("")
        self.groupBox_Properties.setObjectName("groupBox_Properties")
        self.gridProps = QtWidgets.QTableView(self.groupBox_Properties)
        self.gridProps.setGeometry(QtCore.QRect(10, 23, 521, 201))
        self.gridProps.setMinimumSize(QtCore.QSize(0, 0))
        self.gridProps.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridProps.setObjectName("gridProps")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_Properties)
        self.frame_3.setGeometry(QtCore.QRect(540, 20, 45, 201))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnPropUp = QtWidgets.QToolButton(self.frame_3)
        self.btnPropUp.setObjectName("btnPropUp")
        self.verticalLayout_3.addWidget(self.btnPropUp)
        self.btnPropDown = QtWidgets.QToolButton(self.frame_3)
        self.btnPropDown.setObjectName("btnPropDown")
        self.verticalLayout_3.addWidget(self.btnPropDown)
        spacerItem1 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_Properties)
        self.frame_4.setGeometry(QtCore.QRect(0, 210, 174, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.frame = QtWidgets.QFrame(self.groupBox_Properties)
        self.frame.setGeometry(QtCore.QRect(10, 230, 573, 43))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnPropAdd = QtWidgets.QPushButton(self.frame)
        self.btnPropAdd.setToolTip("")
        self.btnPropAdd.setObjectName("btnPropAdd")
        self.horizontalLayout_2.addWidget(self.btnPropAdd)
        self.btnPropRemove = QtWidgets.QPushButton(self.frame)
        self.btnPropRemove.setToolTip("")
        self.btnPropRemove.setObjectName("btnPropRemove")
        self.horizontalLayout_2.addWidget(self.btnPropRemove)
        spacerItem2 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.tabRelationship.addTab(self.tabDefinition, "")
        self.tabSourceTarget = QtWidgets.QWidget()
        self.tabSourceTarget.setObjectName("tabSourceTarget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSourceTarget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.boxSourceTarget = QtWidgets.QGroupBox(self.tabSourceTarget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxSourceTarget.sizePolicy().hasHeightForWidth())
        self.boxSourceTarget.setSizePolicy(sizePolicy)
        self.boxSourceTarget.setMinimumSize(QtCore.QSize(0, 180))
        self.boxSourceTarget.setToolTip("")
        self.boxSourceTarget.setObjectName("boxSourceTarget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.boxSourceTarget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridSourceTarget = QtWidgets.QTableView(self.boxSourceTarget)
        self.gridSourceTarget.setMinimumSize(QtCore.QSize(0, 0))
        self.gridSourceTarget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridSourceTarget.setObjectName("gridSourceTarget")
        self.gridLayout_4.addWidget(self.gridSourceTarget, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.boxSourceTarget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSTUp = QtWidgets.QToolButton(self.frame_5)
        self.btnSTUp.setObjectName("btnSTUp")
        self.verticalLayout.addWidget(self.btnSTUp)
        self.btnSTDown = QtWidgets.QToolButton(self.frame_5)
        self.btnSTDown.setObjectName("btnSTDown")
        self.verticalLayout.addWidget(self.btnSTDown)
        spacerItem3 = QtWidgets.QSpacerItem(20, 121, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_4.addWidget(self.frame_5, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.boxSourceTarget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.boxSourceTarget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSTAdd = QtWidgets.QPushButton(self.frame_6)
        self.btnSTAdd.setToolTip("")
        self.btnSTAdd.setObjectName("btnSTAdd")
        self.horizontalLayout.addWidget(self.btnSTAdd)
        self.btnSTRemove = QtWidgets.QPushButton(self.frame_6)
        self.btnSTRemove.setToolTip("")
        self.btnSTRemove.setObjectName("btnSTRemove")
        self.horizontalLayout.addWidget(self.btnSTRemove)
        spacerItem4 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_4.addWidget(self.frame_6, 3, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.boxSourceTarget)
        self.tabRelationship.addTab(self.tabSourceTarget, "")
        self.tabDescription = QtWidgets.QWidget()
        self.tabDescription.setObjectName("tabDescription")
        self.label_2 = QtWidgets.QLabel(self.tabDescription)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 57, 16))
        self.label_2.setObjectName("label_2")
        self.editDescription = QtWidgets.QPlainTextEdit(self.tabDescription)
        self.editDescription.setGeometry(QtCore.QRect(10, 30, 581, 75))
        self.editDescription.setMaximumSize(QtCore.QSize(16777215, 75))
        self.editDescription.setObjectName("editDescription")
        self.label_3 = QtWidgets.QLabel(self.tabDescription)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_3.setObjectName("label_3")
        self.brwsrGeneratedDesc = QtWidgets.QTextBrowser(self.tabDescription)
        self.brwsrGeneratedDesc.setGeometry(QtCore.QRect(10, 140, 581, 151))
        self.brwsrGeneratedDesc.setObjectName("brwsrGeneratedDesc")
        self.tabRelationship.addTab(self.tabDescription, "")
        self.tabDataGrid = QtWidgets.QWidget()
        self.tabDataGrid.setObjectName("tabDataGrid")
        self.gridMacros = QtWidgets.QTableView(self.tabDataGrid)
        self.gridMacros.setGeometry(QtCore.QRect(9, 9, 481, 281))
        self.gridMacros.setObjectName("gridMacros")
        self.frmButtons = QtWidgets.QFrame(self.tabDataGrid)
        self.frmButtons.setGeometry(QtCore.QRect(500, 10, 95, 270))
        self.frmButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmButtons.setObjectName("frmButtons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmButtons)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnRunQuery = QtWidgets.QPushButton(self.frmButtons)
        self.btnRunQuery.setObjectName("btnRunQuery")
        self.verticalLayout_2.addWidget(self.btnRunQuery)
        spacerItem5 = QtWidgets.QSpacerItem(20, 218, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.tabRelationship.addTab(self.tabDataGrid, "")
        self.verticalLayout_5.addWidget(self.tabRelationship)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem6 = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem6)
        self.okButton = QtWidgets.QPushButton(RelPropertyBox)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(RelPropertyBox)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem7)
        self.verticalLayout_5.addLayout(self.hboxlayout)
        self.label.setBuddy(self.editName)
        self.label_2.setBuddy(self.editDescription)

        self.retranslateUi(RelPropertyBox)
        self.tabRelationship.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RelPropertyBox)
        RelPropertyBox.setTabOrder(self.editName, self.editDescription)
        RelPropertyBox.setTabOrder(self.editDescription, self.gridProps)
        RelPropertyBox.setTabOrder(self.gridProps, self.btnPropAdd)
        RelPropertyBox.setTabOrder(self.btnPropAdd, self.btnPropUp)
        RelPropertyBox.setTabOrder(self.btnPropUp, self.btnPropDown)
        RelPropertyBox.setTabOrder(self.btnPropDown, self.okButton)
        RelPropertyBox.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, RelPropertyBox):
        _translate = QtCore.QCoreApplication.translate
        RelPropertyBox.setWindowTitle(_translate("RelPropertyBox", "Dialog"))
        self.lblHeader.setText(_translate("RelPropertyBox", "Relationship Template"))
        self.label.setText(_translate("RelPropertyBox", "Relationship Name:"))
        self.rbDefaultFormat.setText(_translate("RelPropertyBox", "Default Format"))
        self.rbCustomFormat.setText(_translate("RelPropertyBox", "Custom Format"))
        self.btnDefineFormat.setText(_translate("RelPropertyBox", "Define Format"))
        self.groupBox_Properties.setTitle(_translate("RelPropertyBox", "Properties"))
        self.btnPropUp.setText(_translate("RelPropertyBox", "UP"))
        self.btnPropDown.setText(_translate("RelPropertyBox", "DN"))
        self.btnPropAdd.setText(_translate("RelPropertyBox", "Add"))
        self.btnPropRemove.setText(_translate("RelPropertyBox", "Remove"))
        self.tabRelationship.setTabText(self.tabRelationship.indexOf(self.tabDefinition), _translate("RelPropertyBox", "Definition"))
        self.boxSourceTarget.setTitle(_translate("RelPropertyBox", "Source and Target Nodes"))
        self.btnSTUp.setText(_translate("RelPropertyBox", "UP"))
        self.btnSTDown.setText(_translate("RelPropertyBox", "DN"))
        self.btnSTAdd.setText(_translate("RelPropertyBox", "Add"))
        self.btnSTRemove.setText(_translate("RelPropertyBox", "Remove"))
        self.tabRelationship.setTabText(self.tabRelationship.indexOf(self.tabSourceTarget), _translate("RelPropertyBox", "Source/Target"))
        self.label_2.setText(_translate("RelPropertyBox", "Description:"))
        self.label_3.setText(_translate("RelPropertyBox", "Generated Description:"))
        self.tabRelationship.setTabText(self.tabRelationship.indexOf(self.tabDescription), _translate("RelPropertyBox", "Description"))
        self.btnRunQuery.setText(_translate("RelPropertyBox", "Run Query"))
        self.tabRelationship.setTabText(self.tabRelationship.indexOf(self.tabDataGrid), _translate("RelPropertyBox", "Macros"))
        self.okButton.setText(_translate("RelPropertyBox", "&OK"))
        self.cancelButton.setText(_translate("RelPropertyBox", "&Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RelPropertyBox = QtWidgets.QDialog()
    ui = Ui_RelPropertyBox()
    ui.setupUi(RelPropertyBox)
    RelPropertyBox.show()
    sys.exit(app.exec_())

