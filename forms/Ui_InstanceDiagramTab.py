# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\InstanceDiagramTab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InstanceDiagramTab(object):
    def setupUi(self, InstanceDiagramTab):
        InstanceDiagramTab.setObjectName("InstanceDiagramTab")
        InstanceDiagramTab.resize(1117, 636)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(InstanceDiagramTab)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frmDiagramer = QtWidgets.QFrame(InstanceDiagramTab)
        self.frmDiagramer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDiagramer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmDiagramer.setObjectName("frmDiagramer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmDiagramer)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frmButtonBar = QtWidgets.QFrame(self.frmDiagramer)
        self.frmButtonBar.setMinimumSize(QtCore.QSize(0, 80))
        self.frmButtonBar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frmButtonBar.setFrameShape(QtWidgets.QFrame.Box)
        self.frmButtonBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmButtonBar.setObjectName("frmButtonBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frmButtonBar)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmButton = QtWidgets.QFrame(self.frmButtonBar)
        self.frmButton.setFrameShape(QtWidgets.QFrame.Box)
        self.frmButton.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmButton.setObjectName("frmButton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmButton)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnShove = QtWidgets.QToolButton(self.frmButton)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-hand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnShove.setIcon(icon)
        self.btnShove.setIconSize(QtCore.QSize(32, 32))
        self.btnShove.setCheckable(True)
        self.btnShove.setObjectName("btnShove")
        self.horizontalLayout_2.addWidget(self.btnShove)
        self.btnPoint = QtWidgets.QToolButton(self.frmButton)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-cursor-pointer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPoint.setIcon(icon1)
        self.btnPoint.setIconSize(QtCore.QSize(32, 32))
        self.btnPoint.setCheckable(True)
        self.btnPoint.setObjectName("btnPoint")
        self.horizontalLayout_2.addWidget(self.btnPoint)
        self.btnNode = QtWidgets.QToolButton(self.frmButton)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-outline-of-a-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNode.setIcon(icon2)
        self.btnNode.setIconSize(QtCore.QSize(32, 33))
        self.btnNode.setCheckable(True)
        self.btnNode.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnNode.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnNode.setAutoRaise(False)
        self.btnNode.setObjectName("btnNode")
        self.horizontalLayout_2.addWidget(self.btnNode)
        self.btnRel = QtWidgets.QToolButton(self.frmButton)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-term.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRel.setIcon(icon3)
        self.btnRel.setIconSize(QtCore.QSize(32, 33))
        self.btnRel.setCheckable(True)
        self.btnRel.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btnRel.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btnRel.setObjectName("btnRel")
        self.horizontalLayout_2.addWidget(self.btnRel)
        self.btnTNode = QtWidgets.QToolButton(self.frmButton)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/NodeTemplate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTNode.setIcon(icon4)
        self.btnTNode.setIconSize(QtCore.QSize(32, 32))
        self.btnTNode.setCheckable(True)
        self.btnTNode.setObjectName("btnTNode")
        self.horizontalLayout_2.addWidget(self.btnTNode)
        self.btnTRel = QtWidgets.QToolButton(self.frmButton)
        self.btnTRel.setIcon(icon3)
        self.btnTRel.setIconSize(QtCore.QSize(32, 32))
        self.btnTRel.setCheckable(True)
        self.btnTRel.setObjectName("btnTRel")
        self.horizontalLayout_2.addWidget(self.btnTRel)
        spacerItem = QtWidgets.QSpacerItem(435, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnPrint = QtWidgets.QToolButton(self.frmButton)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/PRINT/PRINT/icons8-print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrint.setIcon(icon5)
        self.btnPrint.setIconSize(QtCore.QSize(32, 32))
        self.btnPrint.setObjectName("btnPrint")
        self.horizontalLayout_2.addWidget(self.btnPrint)
        self.btnPageSetup = QtWidgets.QToolButton(self.frmButton)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/PRINT/PRINT/icons8-property-script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPageSetup.setIcon(icon6)
        self.btnPageSetup.setIconSize(QtCore.QSize(32, 34))
        self.btnPageSetup.setObjectName("btnPageSetup")
        self.horizontalLayout_2.addWidget(self.btnPageSetup)
        self.pbRedraw = QtWidgets.QToolButton(self.frmButton)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-circular-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbRedraw.setIcon(icon7)
        self.pbRedraw.setIconSize(QtCore.QSize(32, 32))
        self.pbRedraw.setObjectName("pbRedraw")
        self.horizontalLayout_2.addWidget(self.pbRedraw)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnCopyNode = QtWidgets.QToolButton(self.frmButton)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-oval.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCopyNode.setIcon(icon8)
        self.btnCopyNode.setIconSize(QtCore.QSize(32, 32))
        self.btnCopyNode.setObjectName("btnCopyNode")
        self.horizontalLayout_2.addWidget(self.btnCopyNode)
        self.btnSyncDB = QtWidgets.QToolButton(self.frmButton)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/FILE/FILE/Synchronize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSyncDB.setIcon(icon9)
        self.btnSyncDB.setIconSize(QtCore.QSize(32, 32))
        self.btnSyncDB.setObjectName("btnSyncDB")
        self.horizontalLayout_2.addWidget(self.btnSyncDB)
        self.verticalLayout.addWidget(self.frmButton)
        self.frmMessage = QtWidgets.QFrame(self.frmButtonBar)
        self.frmMessage.setMinimumSize(QtCore.QSize(0, 20))
        self.frmMessage.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frmMessage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmMessage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmMessage.setObjectName("frmMessage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frmMessage)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblMessage = QtWidgets.QLabel(self.frmMessage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setMinimumSize(QtCore.QSize(400, 18))
        self.lblMessage.setMaximumSize(QtCore.QSize(600, 18))
        self.lblMessage.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblMessage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblMessage.setText("")
        self.lblMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblMessage.setObjectName("lblMessage")
        self.horizontalLayout_3.addWidget(self.lblMessage)
        spacerItem2 = QtWidgets.QSpacerItem(181, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnZoomOut = QtWidgets.QToolButton(self.frmMessage)
        self.btnZoomOut.setMinimumSize(QtCore.QSize(23, 16))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoomOut.setIcon(icon10)
        self.btnZoomOut.setObjectName("btnZoomOut")
        self.horizontalLayout_3.addWidget(self.btnZoomOut)
        self.zoomSlider = QtWidgets.QSlider(self.frmMessage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMaximum(50)
        self.zoomSlider.setPageStep(5)
        self.zoomSlider.setProperty("value", 25)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setObjectName("zoomSlider")
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.btnZoomIn = QtWidgets.QToolButton(self.frmMessage)
        self.btnZoomIn.setMinimumSize(QtCore.QSize(23, 16))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/DIAGRAM/DIAGRAM/icons8-zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoomIn.setIcon(icon11)
        self.btnZoomIn.setObjectName("btnZoomIn")
        self.horizontalLayout_3.addWidget(self.btnZoomIn)
        self.verticalLayout.addWidget(self.frmMessage)
        self.verticalLayout_2.addWidget(self.frmButtonBar)
        self.frmCanvas = QtWidgets.QFrame(self.frmDiagramer)
        self.frmCanvas.setFrameShape(QtWidgets.QFrame.Box)
        self.frmCanvas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmCanvas.setObjectName("frmCanvas")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frmCanvas)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addWidget(self.frmCanvas)
        self.verticalLayout_3.addWidget(self.frmDiagramer)

        self.retranslateUi(InstanceDiagramTab)
        QtCore.QMetaObject.connectSlotsByName(InstanceDiagramTab)

    def retranslateUi(self, InstanceDiagramTab):
        _translate = QtCore.QCoreApplication.translate
        InstanceDiagramTab.setWindowTitle(_translate("InstanceDiagramTab", "Form"))
        self.btnShove.setToolTip(_translate("InstanceDiagramTab", "Move Diagram"))
        self.btnShove.setText(_translate("InstanceDiagramTab", "Shove"))
        self.btnPoint.setToolTip(_translate("InstanceDiagramTab", "Select Items"))
        self.btnPoint.setText(_translate("InstanceDiagramTab", "Pointer"))
        self.btnNode.setToolTip(_translate("InstanceDiagramTab", "Add New Instance Node To Diagram"))
        self.btnNode.setText(_translate("InstanceDiagramTab", "Node"))
        self.btnRel.setToolTip(_translate("InstanceDiagramTab", "Add New Instance Relationship"))
        self.btnRel.setText(_translate("InstanceDiagramTab", "Relationship"))
        self.btnTNode.setToolTip(_translate("InstanceDiagramTab", "Add New Node Template"))
        self.btnTNode.setText(_translate("InstanceDiagramTab", "Node Template"))
        self.btnTRel.setToolTip(_translate("InstanceDiagramTab", "Add New Relationship Template"))
        self.btnTRel.setText(_translate("InstanceDiagramTab", "Relationship Template"))
        self.btnPrint.setToolTip(_translate("InstanceDiagramTab", "Print Diagram"))
        self.btnPrint.setText(_translate("InstanceDiagramTab", "Print"))
        self.btnPageSetup.setToolTip(_translate("InstanceDiagramTab", "Page Setup"))
        self.btnPageSetup.setText(_translate("InstanceDiagramTab", "Page Setup"))
        self.pbRedraw.setToolTip(_translate("InstanceDiagramTab", "Redraw Diagram"))
        self.pbRedraw.setText(_translate("InstanceDiagramTab", "ReDraw"))
        self.btnCopyNode.setToolTip(_translate("InstanceDiagramTab", "Copy Node from database..."))
        self.btnCopyNode.setText(_translate("InstanceDiagramTab", "Copy Node"))
        self.btnSyncDB.setToolTip(_translate("InstanceDiagramTab", "Syncronize Diagram and Graph Database"))
        self.btnSyncDB.setText(_translate("InstanceDiagramTab", "Sync DB..."))
        self.btnZoomOut.setText(_translate("InstanceDiagramTab", "Zoom Out"))
        self.zoomSlider.setToolTip(_translate("InstanceDiagramTab", "Zoom Diagram"))
        self.btnZoomIn.setText(_translate("InstanceDiagramTab", "Zoom In"))
import icons.icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InstanceDiagramTab = QtWidgets.QWidget()
    ui = Ui_InstanceDiagramTab()
    ui.setupUi(InstanceDiagramTab)
    InstanceDiagramTab.show()
    sys.exit(app.exec_())