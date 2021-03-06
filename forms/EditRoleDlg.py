# -*- coding: utf-8 -*-

"""
Module implementing EditRoleDlg.
 
Copyright 2018-2020 SingerLinks Consulting LLC 

This file is part of NodeEra.

NodeEra is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

NodeEra is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with NodeEra. If not, see <https://www.gnu.org/licenses/>.
 
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QApplication
from core.helper import Helper
from .Ui_EditRoleDlg import Ui_EditRoleDlg


class EditRoleDlg(QDialog, Ui_EditRoleDlg):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, mode=None, roleName=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(EditRoleDlg, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.roleName=roleName
        self.mode=mode
        self.helper = Helper()
        self.initUI()

    def initUI(self, ):
        self.txtRoleName.setText(self.roleName)
        self.txtRoleName.setReadOnly(True)   
        
        # populate the user combo box
        self.cbUserName.addItems(self.parent.schemaModel.instanceList("User"))   
        # populate role users in the list box
        roleUsers = self.parent.schemaModel.getRoleUsers(roleName=self.roleName)
        for roleUser in roleUsers:
            self.lstRoleUsers.addItem(roleUser)

    
    @pyqtSlot()
    def on_dlgBtnBox_accepted(self):
        """
        User clicks Close
        """
        QDialog.accept(self)
    
    @pyqtSlot()
    def on_dlgBtnBox_rejected(self):
        """
        User clicks something that generates the reject
        """
        QDialog.reject(self)
    
    @pyqtSlot()
    def on_btnAddUser_clicked(self):
        """
        Give the user selected from the combobox the role
        """
        addUser = self.cbUserName.currentText()
        currentUsers = [str(self.lstRoleUsers.item(i).text()) for i in range(self.lstRoleUsers.count())]
        if addUser in currentUsers:
            # error, the user already has the selected role
            self.helper.displayErrMsg("Edit Role", "The role already has this user.")
        else:
            # give the role the user
            QApplication.setOverrideCursor(Qt.WaitCursor)
            rc, msg = self.parent.schemaModel.addUserRole(userName=addUser, role=self.roleName)
            if rc:
                self.lstRoleUsers.addItem(addUser)
            else:
                self.helper.displayErrMsg("Add User to Role Error", msg)
            QApplication.restoreOverrideCursor()                
    
    @pyqtSlot()
    def on_btnRemoveUsers_clicked(self):
        """
        Remove the selected user from the list of users in the role
        """
        if self.lstRoleUsers.currentItem() == None:
            self.helper.displayErrMsg("Remove User From Role","You must select a user to remove.")
            return
            
        removeUser = self.lstRoleUsers.currentItem().text()
        QApplication.setOverrideCursor(Qt.WaitCursor)
        rc, msg = self.parent.schemaModel.removeUserRole(userName=removeUser, role=self.roleName)
        if rc:
            self.lstRoleUsers.takeItem(self.lstRoleUsers.currentRow())
        else:
            self.helper.displayErrMsg("Remove User from Role Error", msg)
        QApplication.restoreOverrideCursor() 
