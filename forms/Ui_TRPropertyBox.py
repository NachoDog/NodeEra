# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\TRPropertyBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TRPropertyBox(object):
    def setupUi(self, TRPropertyBox):
        TRPropertyBox.setObjectName("TRPropertyBox")
        TRPropertyBox.setWindowModality(QtCore.Qt.ApplicationModal)
        TRPropertyBox.resize(1033, 543)
        TRPropertyBox.setSizeGripEnabled(True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(TRPropertyBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblHeader = QtWidgets.QLabel(TRPropertyBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setObjectName("lblHeader")
        self.verticalLayout_5.addWidget(self.lblHeader)
        self.frame_2 = QtWidgets.QFrame(TRPropertyBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtRelTemplateName = QtWidgets.QLineEdit(self.frame_2)
        self.txtRelTemplateName.setObjectName("txtRelTemplateName")
        self.horizontalLayout.addWidget(self.txtRelTemplateName)
        spacerItem = QtWidgets.QSpacerItem(142, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tabRelTemplate = QtWidgets.QTabWidget(TRPropertyBox)
        self.tabRelTemplate.setObjectName("tabRelTemplate")
        self.tabDefinition = QtWidgets.QWidget()
        self.tabDefinition.setObjectName("tabDefinition")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabDefinition)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.tabDefinition)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.cboRelName = QtWidgets.QComboBox(self.frame_5)
        self.cboRelName.setMinimumSize(QtCore.QSize(181, 0))
        self.cboRelName.setMaximumSize(QtCore.QSize(181, 16777215))
        self.cboRelName.setEditable(True)
        self.cboRelName.setObjectName("cboRelName")
        self.gridLayout.addWidget(self.cboRelName, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(354, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.cmbFromTemplate = QtWidgets.QComboBox(self.frame_5)
        self.cmbFromTemplate.setMinimumSize(QtCore.QSize(181, 0))
        self.cmbFromTemplate.setMaximumSize(QtCore.QSize(181, 16777215))
        self.cmbFromTemplate.setObjectName("cmbFromTemplate")
        self.gridLayout.addWidget(self.cmbFromTemplate, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setMinimumSize(QtCore.QSize(40, 0))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.cmbFromCardinality = QtWidgets.QComboBox(self.frame_5)
        self.cmbFromCardinality.setMinimumSize(QtCore.QSize(80, 0))
        self.cmbFromCardinality.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cmbFromCardinality.setEditable(False)
        self.cmbFromCardinality.setObjectName("cmbFromCardinality")
        self.cmbFromCardinality.addItem("")
        self.cmbFromCardinality.addItem("")
        self.cmbFromCardinality.addItem("")
        self.cmbFromCardinality.addItem("")
        self.gridLayout.addWidget(self.cmbFromCardinality, 1, 3, 1, 1)
        self.editFromToType = QtWidgets.QLineEdit(self.frame_5)
        self.editFromToType.setMinimumSize(QtCore.QSize(200, 0))
        self.editFromToType.setFrame(False)
        self.editFromToType.setReadOnly(True)
        self.editFromToType.setObjectName("editFromToType")
        self.gridLayout.addWidget(self.editFromToType, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(354, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.cmbToTemplate = QtWidgets.QComboBox(self.frame_5)
        self.cmbToTemplate.setMinimumSize(QtCore.QSize(181, 0))
        self.cmbToTemplate.setMaximumSize(QtCore.QSize(181, 16777215))
        self.cmbToTemplate.setObjectName("cmbToTemplate")
        self.gridLayout.addWidget(self.cmbToTemplate, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.cmbToCardinality = QtWidgets.QComboBox(self.frame_5)
        self.cmbToCardinality.setMinimumSize(QtCore.QSize(80, 0))
        self.cmbToCardinality.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cmbToCardinality.setEditable(False)
        self.cmbToCardinality.setObjectName("cmbToCardinality")
        self.cmbToCardinality.addItem("")
        self.cmbToCardinality.addItem("")
        self.cmbToCardinality.addItem("")
        self.cmbToCardinality.addItem("")
        self.gridLayout.addWidget(self.cmbToCardinality, 2, 3, 1, 1)
        self.editToFromType = QtWidgets.QLineEdit(self.frame_5)
        self.editToFromType.setMinimumSize(QtCore.QSize(200, 0))
        self.editToFromType.setFrame(False)
        self.editToFromType.setReadOnly(True)
        self.editToFromType.setObjectName("editToFromType")
        self.gridLayout.addWidget(self.editToFromType, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(354, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 5, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.groupBox_Properties = QtWidgets.QGroupBox(self.tabDefinition)
        self.groupBox_Properties.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_Properties.setToolTip("")
        self.groupBox_Properties.setObjectName("groupBox_Properties")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_Properties)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_Properties)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridProps = QtWidgets.QTableView(self.frame_4)
        self.gridProps.setMinimumSize(QtCore.QSize(0, 0))
        self.gridProps.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridProps.setObjectName("gridProps")
        self.horizontalLayout_5.addWidget(self.gridProps)
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.groupBox_Properties)
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
        self.btnSetDefaultNull = QtWidgets.QPushButton(self.frame)
        self.btnSetDefaultNull.setObjectName("btnSetDefaultNull")
        self.horizontalLayout_2.addWidget(self.btnSetDefaultNull)
        spacerItem5 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_6.addWidget(self.frame)
        self.verticalLayout_4.addWidget(self.groupBox_Properties)
        self.tabRelTemplate.addTab(self.tabDefinition, "")
        self.tabConstraint = QtWidgets.QWidget()
        self.tabConstraint.setObjectName("tabConstraint")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tabConstraint)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridConstraints = QtWidgets.QTableView(self.groupBox)
        self.gridConstraints.setObjectName("gridConstraints")
        self.verticalLayout_8.addWidget(self.gridConstraints)
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnAddConstraint = QtWidgets.QPushButton(self.frame_6)
        self.btnAddConstraint.setObjectName("btnAddConstraint")
        self.horizontalLayout_6.addWidget(self.btnAddConstraint)
        self.btnRemoveConstraint = QtWidgets.QPushButton(self.frame_6)
        self.btnRemoveConstraint.setObjectName("btnRemoveConstraint")
        self.horizontalLayout_6.addWidget(self.btnRemoveConstraint)
        spacerItem6 = QtWidgets.QSpacerItem(672, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabRelTemplate.addTab(self.tabConstraint, "")
        self.tabDescription = QtWidgets.QWidget()
        self.tabDescription.setObjectName("tabDescription")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabDescription)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.tabDescription)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editDescription = QtWidgets.QPlainTextEdit(self.tabDescription)
        self.editDescription.setMaximumSize(QtCore.QSize(16777215, 75))
        self.editDescription.setObjectName("editDescription")
        self.verticalLayout.addWidget(self.editDescription)
        self.label_3 = QtWidgets.QLabel(self.tabDescription)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.brwsrGeneratedDesc = QtWidgets.QTextBrowser(self.tabDescription)
        self.brwsrGeneratedDesc.setObjectName("brwsrGeneratedDesc")
        self.verticalLayout.addWidget(self.brwsrGeneratedDesc)
        self.tabRelTemplate.addTab(self.tabDescription, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbTemplateDefaultFormat = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbTemplateDefaultFormat.setMinimumSize(QtCore.QSize(110, 0))
        self.rbTemplateDefaultFormat.setObjectName("rbTemplateDefaultFormat")
        self.horizontalLayout_3.addWidget(self.rbTemplateDefaultFormat)
        self.rbTemplateCustomFormat = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbTemplateCustomFormat.setMinimumSize(QtCore.QSize(110, 0))
        self.rbTemplateCustomFormat.setObjectName("rbTemplateCustomFormat")
        self.horizontalLayout_3.addWidget(self.rbTemplateCustomFormat)
        self.btnDefineTemplateFormat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDefineTemplateFormat.setObjectName("btnDefineTemplateFormat")
        self.horizontalLayout_3.addWidget(self.btnDefineTemplateFormat)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(453, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbInstanceDefaultFormat = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbInstanceDefaultFormat.setMinimumSize(QtCore.QSize(110, 0))
        self.rbInstanceDefaultFormat.setObjectName("rbInstanceDefaultFormat")
        self.horizontalLayout_4.addWidget(self.rbInstanceDefaultFormat)
        self.rbInstanceCustomFormat = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbInstanceCustomFormat.setMinimumSize(QtCore.QSize(110, 0))
        self.rbInstanceCustomFormat.setObjectName("rbInstanceCustomFormat")
        self.horizontalLayout_4.addWidget(self.rbInstanceCustomFormat)
        self.btnDefineInstanceFormat = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDefineInstanceFormat.setObjectName("btnDefineInstanceFormat")
        self.horizontalLayout_4.addWidget(self.btnDefineInstanceFormat)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(453, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 241, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 2, 0, 1, 1)
        self.tabRelTemplate.addTab(self.tab, "")
        self.tabDataGrid = QtWidgets.QWidget()
        self.tabDataGrid.setObjectName("tabDataGrid")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabDataGrid)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dataTabFrame = QtWidgets.QFrame(self.tabDataGrid)
        self.dataTabFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataTabFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataTabFrame.setObjectName("dataTabFrame")
        self.gridLayout_3.addWidget(self.dataTabFrame, 0, 0, 1, 1)
        self.tabRelTemplate.addTab(self.tabDataGrid, "")
        self.verticalLayout_5.addWidget(self.tabRelTemplate)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem12 = QtWidgets.QSpacerItem(71, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem12)
        self.okButton = QtWidgets.QPushButton(TRPropertyBox)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(TRPropertyBox)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.hboxlayout)
        self.label.setBuddy(self.txtRelTemplateName)
        self.label_2.setBuddy(self.editDescription)

        self.retranslateUi(TRPropertyBox)
        self.tabRelTemplate.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TRPropertyBox)
        TRPropertyBox.setTabOrder(self.txtRelTemplateName, self.tabRelTemplate)
        TRPropertyBox.setTabOrder(self.tabRelTemplate, self.cboRelName)
        TRPropertyBox.setTabOrder(self.cboRelName, self.cmbFromTemplate)
        TRPropertyBox.setTabOrder(self.cmbFromTemplate, self.cmbToTemplate)
        TRPropertyBox.setTabOrder(self.cmbToTemplate, self.gridProps)
        TRPropertyBox.setTabOrder(self.gridProps, self.btnPropUp)
        TRPropertyBox.setTabOrder(self.btnPropUp, self.btnPropDown)
        TRPropertyBox.setTabOrder(self.btnPropDown, self.btnPropAdd)
        TRPropertyBox.setTabOrder(self.btnPropAdd, self.btnPropRemove)
        TRPropertyBox.setTabOrder(self.btnPropRemove, self.gridConstraints)
        TRPropertyBox.setTabOrder(self.gridConstraints, self.btnAddConstraint)
        TRPropertyBox.setTabOrder(self.btnAddConstraint, self.btnRemoveConstraint)
        TRPropertyBox.setTabOrder(self.btnRemoveConstraint, self.editDescription)
        TRPropertyBox.setTabOrder(self.editDescription, self.brwsrGeneratedDesc)
        TRPropertyBox.setTabOrder(self.brwsrGeneratedDesc, self.rbTemplateDefaultFormat)
        TRPropertyBox.setTabOrder(self.rbTemplateDefaultFormat, self.rbTemplateCustomFormat)
        TRPropertyBox.setTabOrder(self.rbTemplateCustomFormat, self.btnDefineTemplateFormat)
        TRPropertyBox.setTabOrder(self.btnDefineTemplateFormat, self.rbInstanceDefaultFormat)
        TRPropertyBox.setTabOrder(self.rbInstanceDefaultFormat, self.rbInstanceCustomFormat)
        TRPropertyBox.setTabOrder(self.rbInstanceCustomFormat, self.btnDefineInstanceFormat)
        TRPropertyBox.setTabOrder(self.btnDefineInstanceFormat, self.okButton)
        TRPropertyBox.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, TRPropertyBox):
        _translate = QtCore.QCoreApplication.translate
        TRPropertyBox.setWindowTitle(_translate("TRPropertyBox", "Relationship Template"))
        self.lblHeader.setText(_translate("TRPropertyBox", "Relationship Template"))
        self.label.setText(_translate("TRPropertyBox", "Relationship Template Name:"))
        self.label_6.setText(_translate("TRPropertyBox", "Relationship Type:"))
        self.label_4.setText(_translate("TRPropertyBox", "From Node Template:"))
        self.label_7.setText(_translate("TRPropertyBox", "has"))
        self.cmbFromCardinality.setItemText(0, _translate("TRPropertyBox", "0:1"))
        self.cmbFromCardinality.setItemText(1, _translate("TRPropertyBox", "0:M"))
        self.cmbFromCardinality.setItemText(2, _translate("TRPropertyBox", "1:1"))
        self.cmbFromCardinality.setItemText(3, _translate("TRPropertyBox", "1:M"))
        self.label_5.setText(_translate("TRPropertyBox", "To Node Template:"))
        self.label_8.setText(_translate("TRPropertyBox", "has"))
        self.cmbToCardinality.setItemText(0, _translate("TRPropertyBox", "0:1"))
        self.cmbToCardinality.setItemText(1, _translate("TRPropertyBox", "0:M"))
        self.cmbToCardinality.setItemText(2, _translate("TRPropertyBox", "1:1"))
        self.cmbToCardinality.setItemText(3, _translate("TRPropertyBox", "1:M"))
        self.groupBox_Properties.setTitle(_translate("TRPropertyBox", "Properties"))
        self.btnPropUp.setText(_translate("TRPropertyBox", "UP"))
        self.btnPropDown.setText(_translate("TRPropertyBox", "DN"))
        self.btnPropAdd.setText(_translate("TRPropertyBox", "Add"))
        self.btnPropRemove.setText(_translate("TRPropertyBox", "Remove"))
        self.btnSetDefaultNull.setText(_translate("TRPropertyBox", "Set Default Null"))
        self.tabRelTemplate.setTabText(self.tabRelTemplate.indexOf(self.tabDefinition), _translate("TRPropertyBox", "Definition"))
        self.groupBox.setTitle(_translate("TRPropertyBox", "Constraints"))
        self.btnAddConstraint.setText(_translate("TRPropertyBox", "Add"))
        self.btnRemoveConstraint.setText(_translate("TRPropertyBox", "Remove"))
        self.tabRelTemplate.setTabText(self.tabRelTemplate.indexOf(self.tabConstraint), _translate("TRPropertyBox", "Constraints"))
        self.label_2.setText(_translate("TRPropertyBox", "Description:"))
        self.label_3.setText(_translate("TRPropertyBox", "Generated Description:"))
        self.tabRelTemplate.setTabText(self.tabRelTemplate.indexOf(self.tabDescription), _translate("TRPropertyBox", "Description"))
        self.groupBox_2.setTitle(_translate("TRPropertyBox", "Relationship Template Format"))
        self.rbTemplateDefaultFormat.setText(_translate("TRPropertyBox", "Default Format"))
        self.rbTemplateCustomFormat.setText(_translate("TRPropertyBox", "Custom Format"))
        self.btnDefineTemplateFormat.setText(_translate("TRPropertyBox", "Define Format"))
        self.groupBox_3.setTitle(_translate("TRPropertyBox", "Relationship Instance Format"))
        self.rbInstanceDefaultFormat.setText(_translate("TRPropertyBox", "Default Format"))
        self.rbInstanceCustomFormat.setText(_translate("TRPropertyBox", "Custom Format"))
        self.btnDefineInstanceFormat.setText(_translate("TRPropertyBox", "Define Format"))
        self.tabRelTemplate.setTabText(self.tabRelTemplate.indexOf(self.tab), _translate("TRPropertyBox", "Formats"))
        self.tabRelTemplate.setTabText(self.tabRelTemplate.indexOf(self.tabDataGrid), _translate("TRPropertyBox", "Data"))
        self.okButton.setText(_translate("TRPropertyBox", "&OK"))
        self.cancelButton.setText(_translate("TRPropertyBox", "&Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TRPropertyBox = QtWidgets.QDialog()
    ui = Ui_TRPropertyBox()
    ui.setupUi(TRPropertyBox)
    TRPropertyBox.show()
    sys.exit(app.exec_())