# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\John\SkyDrive\Documents\REPOS\NODEERA\forms\CreateConstraintDlg.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateConstraintDlg(object):
    def setupUi(self, CreateConstraintDlg):
        CreateConstraintDlg.setObjectName("CreateConstraintDlg")
        CreateConstraintDlg.resize(591, 553)
        CreateConstraintDlg.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateConstraintDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CreateConstraintDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(CreateConstraintDlg)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbUnique = QtWidgets.QRadioButton(self.groupBox)
        self.rbUnique.setObjectName("rbUnique")
        self.gridLayout_2.addWidget(self.rbUnique, 0, 0, 1, 1)
        self.rbNodePropExists = QtWidgets.QRadioButton(self.groupBox)
        self.rbNodePropExists.setObjectName("rbNodePropExists")
        self.gridLayout_2.addWidget(self.rbNodePropExists, 0, 1, 1, 1)
        self.rbNodeKey = QtWidgets.QRadioButton(self.groupBox)
        self.rbNodeKey.setObjectName("rbNodeKey")
        self.gridLayout_2.addWidget(self.rbNodeKey, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(283, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 2)
        self.rbRelPropExists = QtWidgets.QRadioButton(self.groupBox)
        self.rbRelPropExists.setObjectName("rbRelPropExists")
        self.gridLayout_2.addWidget(self.rbRelPropExists, 1, 0, 1, 3)
        self.cbRelationships = QtWidgets.QComboBox(self.groupBox)
        self.cbRelationships.setMinimumSize(QtCore.QSize(200, 0))
        self.cbRelationships.setObjectName("cbRelationships")
        self.gridLayout_2.addWidget(self.cbRelationships, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(CreateConstraintDlg)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cbLabel = QtWidgets.QComboBox(self.frame)
        self.cbLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.cbLabel.setEditable(True)
        self.cbLabel.setObjectName("cbLabel")
        self.horizontalLayout.addWidget(self.cbLabel)
        spacerItem2 = QtWidgets.QSpacerItem(276, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(CreateConstraintDlg)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.cbProperty = QtWidgets.QComboBox(self.frame_2)
        self.cbProperty.setMinimumSize(QtCore.QSize(250, 0))
        self.cbProperty.setEditable(True)
        self.cbProperty.setObjectName("cbProperty")
        self.gridLayout.addWidget(self.cbProperty, 0, 1, 1, 3)
        self.pbAddToList = QtWidgets.QPushButton(self.frame_2)
        self.pbAddToList.setObjectName("pbAddToList")
        self.gridLayout.addWidget(self.pbAddToList, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(126, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(330, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 4)
        self.lstProperty = QtWidgets.QListWidget(self.frame_2)
        self.lstProperty.setObjectName("lstProperty")
        self.gridLayout.addWidget(self.lstProperty, 2, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 4, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(126, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.pbRemoveList = QtWidgets.QPushButton(self.frame_2)
        self.pbRemoveList.setObjectName("pbRemoveList")
        self.gridLayout.addWidget(self.pbRemoveList, 4, 1, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(244, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 3, 1, 2)
        self.verticalLayout.addWidget(self.frame_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateConstraintDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreateConstraintDlg)
        QtCore.QMetaObject.connectSlotsByName(CreateConstraintDlg)

    def retranslateUi(self, CreateConstraintDlg):
        _translate = QtCore.QCoreApplication.translate
        CreateConstraintDlg.setWindowTitle(_translate("CreateConstraintDlg", "Create Constraint"))
        self.label.setText(_translate("CreateConstraintDlg", "Create Constraint"))
        self.groupBox.setTitle(_translate("CreateConstraintDlg", "Constraint Type"))
        self.rbUnique.setText(_translate("CreateConstraintDlg", "Unique"))
        self.rbNodePropExists.setText(_translate("CreateConstraintDlg", "Node Property Exists"))
        self.rbNodeKey.setText(_translate("CreateConstraintDlg", "Node Key"))
        self.rbRelPropExists.setText(_translate("CreateConstraintDlg", "Relationship Property Exists For Relationship:"))
        self.label_2.setText(_translate("CreateConstraintDlg", "Enter or Select a Label:"))
        self.label_3.setText(_translate("CreateConstraintDlg", "Enter or Select a Property:"))
        self.pbAddToList.setToolTip(_translate("CreateConstraintDlg", "<html><head/><body><p>Click to add this property to the list.</p></body></html>"))
        self.pbAddToList.setText(_translate("CreateConstraintDlg", "Add To List"))
        self.label_4.setText(_translate("CreateConstraintDlg", "Property List:"))
        self.pbRemoveList.setToolTip(_translate("CreateConstraintDlg", "<html><head/><body><p>Select a property in the list and click to remove it.</p></body></html>"))
        self.pbRemoveList.setText(_translate("CreateConstraintDlg", "Remove From List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateConstraintDlg = QtWidgets.QDialog()
    ui = Ui_CreateConstraintDlg()
    ui.setupUi(CreateConstraintDlg)
    CreateConstraintDlg.show()
    sys.exit(app.exec_())

