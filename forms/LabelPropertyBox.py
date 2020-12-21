# -*- coding: utf-8 -*-

"""
Module implementing LabelPropertyBox.
    Copyright: SingerLinks Consulting LLC dba NodeEra Software 2018-2019 - all rights reserved
    Confidential Material - Do Not Distribute - SingerLinks Consulting dba NodeEra Software
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from forms.Ui_LabelPropertyBox import Ui_Dialog
from core.helper import Helper

class LabelPropertyBox(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, mode=None, objectDict=None, designModel=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LabelPropertyBox, self).__init__(parent)
        self.helper = Helper()
        self.setupUi(self)
        self.designModel = designModel
        self.modelData = self.designModel.modelData
        self.objectDict = objectDict
        self.mode = mode
        #populate ui data from object
        self.populateUIfromObject()
            
        if self.mode == "NEW":
            # set focus to name
            pass
        else: 
            # disable name entry and set focus to description
            self.editName.setEnabled(False)
            self.editDescription.setFocus()
    
    def populateUIfromObject(self, ):
        if self.objectDict is not None:
            self.editName.insert(str(self.objectDict["name"]))
            self.editDescription.appendPlainText(self.objectDict["desc"])
            
    @pyqtSlot()
    def on_okButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.validate():
            self.apply()
            QDialog.accept(self)
    
    @pyqtSlot()
    def on_cancelButton_clicked(self):
        """
        Slot documentation goes here.
        """
        QDialog.reject(self)
    
    def validate(self):
        if self.objectDict is None:
            self.objectDict = {}
        name = self.editName.text()
        if self.helper.NoTextValueError(name, "Must enter a Name"):
            self.editName.setFocus()
            return False
        if self.mode == 'NEW':
            if self.helper.DupObjectError(designModel = self.designModel, objName=name, topLevel = "Label", txtMsg = "A Label named {} already exists".format(name)):
                self.editName.setFocus()
                return False
        return True

        
    def apply(self, ):
        self.objectDict["name"] = self.editName.text()
        desc = self.editDescription.toPlainText()
        if desc is not None:
            self.objectDict["desc"] = desc