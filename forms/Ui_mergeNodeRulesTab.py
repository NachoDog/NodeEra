# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\Documents\NODEERA\V1\forms\mergeNodeRulesTab.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MergeNodeRulesTab(object):
    def setupUi(self, MergeNodeRulesTab):
        MergeNodeRulesTab.setObjectName("MergeNodeRulesTab")
        MergeNodeRulesTab.resize(1041, 784)
        self.verticalLayout = QtWidgets.QVBoxLayout(MergeNodeRulesTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.boxTemplate = QtWidgets.QGroupBox(MergeNodeRulesTab)
        self.boxTemplate.setObjectName("boxTemplate")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.boxTemplate)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblTemplate = QtWidgets.QLabel(self.boxTemplate)
        self.lblTemplate.setObjectName("lblTemplate")
        self.horizontalLayout_3.addWidget(self.lblTemplate)
        self.cboTemplate = QtWidgets.QComboBox(self.boxTemplate)
        self.cboTemplate.setMinimumSize(QtCore.QSize(204, 0))
        self.cboTemplate.setObjectName("cboTemplate")
        self.horizontalLayout_3.addWidget(self.cboTemplate)
        self.btnCreateTemplate = QtWidgets.QPushButton(self.boxTemplate)
        self.btnCreateTemplate.setObjectName("btnCreateTemplate")
        self.horizontalLayout_3.addWidget(self.btnCreateTemplate)
        spacerItem = QtWidgets.QSpacerItem(49, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.boxTemplate)
        self.tabMergeRules = QtWidgets.QTabWidget(MergeNodeRulesTab)
        self.tabMergeRules.setObjectName("tabMergeRules")
        self.tabMergeRules1 = QtWidgets.QWidget()
        self.tabMergeRules1.setObjectName("tabMergeRules1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabMergeRules1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBoxMatch = QtWidgets.QGroupBox(self.tabMergeRules1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMatch.sizePolicy().hasHeightForWidth())
        self.groupBoxMatch.setSizePolicy(sizePolicy)
        self.groupBoxMatch.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBoxMatch.setToolTip("")
        self.groupBoxMatch.setObjectName("groupBoxMatch")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxMatch)
        self.gridLayout.setObjectName("gridLayout")
        self.gridMatchRules = QtWidgets.QTableView(self.groupBoxMatch)
        self.gridMatchRules.setMinimumSize(QtCore.QSize(0, 0))
        self.gridMatchRules.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridMatchRules.setObjectName("gridMatchRules")
        self.gridLayout.addWidget(self.gridMatchRules, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.groupBoxMatch)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMatchRuleAdd = QtWidgets.QPushButton(self.frame_2)
        self.btnMatchRuleAdd.setToolTip("")
        self.btnMatchRuleAdd.setObjectName("btnMatchRuleAdd")
        self.horizontalLayout.addWidget(self.btnMatchRuleAdd)
        self.btnMatchRuleRemove = QtWidgets.QPushButton(self.frame_2)
        self.btnMatchRuleRemove.setToolTip("")
        self.btnMatchRuleRemove.setObjectName("btnMatchRuleRemove")
        self.horizontalLayout.addWidget(self.btnMatchRuleRemove)
        spacerItem1 = QtWidgets.QSpacerItem(759, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.groupBoxMatch)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnMatchRuleUp = QtWidgets.QToolButton(self.frame_5)
        self.btnMatchRuleUp.setObjectName("btnMatchRuleUp")
        self.verticalLayout_3.addWidget(self.btnMatchRuleUp)
        self.btnMatchRuleDown = QtWidgets.QToolButton(self.frame_5)
        self.btnMatchRuleDown.setObjectName("btnMatchRuleDown")
        self.verticalLayout_3.addWidget(self.btnMatchRuleDown)
        spacerItem2 = QtWidgets.QSpacerItem(20, 243, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout.addWidget(self.frame_5, 0, 1, 2, 1)
        self.verticalLayout_2.addWidget(self.groupBoxMatch)
        self.groupBox_Merge = QtWidgets.QGroupBox(self.tabMergeRules1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Merge.sizePolicy().hasHeightForWidth())
        self.groupBox_Merge.setSizePolicy(sizePolicy)
        self.groupBox_Merge.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_Merge.setToolTip("")
        self.groupBox_Merge.setObjectName("groupBox_Merge")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Merge)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridMergeRules = QtWidgets.QTableView(self.groupBox_Merge)
        self.gridMergeRules.setMinimumSize(QtCore.QSize(0, 0))
        self.gridMergeRules.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridMergeRules.setObjectName("gridMergeRules")
        self.gridLayout_2.addWidget(self.gridMergeRules, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_Merge)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddMergeRule = QtWidgets.QPushButton(self.frame_4)
        self.btnAddMergeRule.setToolTip("")
        self.btnAddMergeRule.setObjectName("btnAddMergeRule")
        self.horizontalLayout_2.addWidget(self.btnAddMergeRule)
        self.btnRemoveMergeRule = QtWidgets.QPushButton(self.frame_4)
        self.btnRemoveMergeRule.setToolTip("")
        self.btnRemoveMergeRule.setObjectName("btnRemoveMergeRule")
        self.horizontalLayout_2.addWidget(self.btnRemoveMergeRule)
        spacerItem3 = QtWidgets.QSpacerItem(497, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.groupBox_Merge)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnMergeRuleUp = QtWidgets.QToolButton(self.frame_6)
        self.btnMergeRuleUp.setObjectName("btnMergeRuleUp")
        self.verticalLayout_4.addWidget(self.btnMergeRuleUp)
        self.btnMergeRuleDown = QtWidgets.QToolButton(self.frame_6)
        self.btnMergeRuleDown.setObjectName("btnMergeRuleDown")
        self.verticalLayout_4.addWidget(self.btnMergeRuleDown)
        spacerItem4 = QtWidgets.QSpacerItem(20, 207, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.gridLayout_2.addWidget(self.frame_6, 0, 1, 2, 1)
        self.verticalLayout_2.addWidget(self.groupBox_Merge)
        self.tabMergeRules.addTab(self.tabMergeRules1, "")
        self.tabDescription = QtWidgets.QWidget()
        self.tabDescription.setObjectName("tabDescription")
        self.boxDescription = QtWidgets.QGroupBox(self.tabDescription)
        self.boxDescription.setGeometry(QtCore.QRect(10, 10, 491, 271))
        self.boxDescription.setObjectName("boxDescription")
        self.txtDescription = QtWidgets.QTextEdit(self.boxDescription)
        self.txtDescription.setGeometry(QtCore.QRect(10, 20, 471, 241))
        self.txtDescription.setReadOnly(True)
        self.txtDescription.setObjectName("txtDescription")
        self.tabMergeRules.addTab(self.tabDescription, "")
        self.verticalLayout.addWidget(self.tabMergeRules)

        self.retranslateUi(MergeNodeRulesTab)
        self.tabMergeRules.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MergeNodeRulesTab)

    def retranslateUi(self, MergeNodeRulesTab):
        _translate = QtCore.QCoreApplication.translate
        MergeNodeRulesTab.setWindowTitle(_translate("MergeNodeRulesTab", "Form"))
        self.boxTemplate.setTitle(_translate("MergeNodeRulesTab", "Node Template"))
        self.lblTemplate.setText(_translate("MergeNodeRulesTab", "Name:"))
        self.btnCreateTemplate.setText(_translate("MergeNodeRulesTab", "Create New Template"))
        self.groupBoxMatch.setTitle(_translate("MergeNodeRulesTab", "Match Rules"))
        self.btnMatchRuleAdd.setText(_translate("MergeNodeRulesTab", "Add"))
        self.btnMatchRuleRemove.setText(_translate("MergeNodeRulesTab", "Remove"))
        self.btnMatchRuleUp.setText(_translate("MergeNodeRulesTab", "UP"))
        self.btnMatchRuleDown.setText(_translate("MergeNodeRulesTab", "DN"))
        self.groupBox_Merge.setTitle(_translate("MergeNodeRulesTab", "Merge Rules"))
        self.btnAddMergeRule.setText(_translate("MergeNodeRulesTab", "Add"))
        self.btnRemoveMergeRule.setText(_translate("MergeNodeRulesTab", "Remove"))
        self.btnMergeRuleUp.setText(_translate("MergeNodeRulesTab", "UP"))
        self.btnMergeRuleDown.setText(_translate("MergeNodeRulesTab", "DN"))
        self.tabMergeRules.setTabText(self.tabMergeRules.indexOf(self.tabMergeRules1), _translate("MergeNodeRulesTab", "Mapping Rules"))
        self.boxDescription.setTitle(_translate("MergeNodeRulesTab", "Description"))
        self.tabMergeRules.setTabText(self.tabMergeRules.indexOf(self.tabDescription), _translate("MergeNodeRulesTab", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MergeNodeRulesTab = QtWidgets.QWidget()
    ui = Ui_MergeNodeRulesTab()
    ui.setupUi(MergeNodeRulesTab)
    MergeNodeRulesTab.show()
    sys.exit(app.exec_())

