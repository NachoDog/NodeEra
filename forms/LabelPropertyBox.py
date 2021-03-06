# -*- coding: utf-8 -*-

"""
Module implementing LabelPropertyBox.
 
Copyright 2018-2020 SingerLinks Consulting LLC 

This file is part of NodeEra.

NodeEra is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

NodeEra is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with NodeEra. If not, see <https://www.gnu.org/licenses/>.
 
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
