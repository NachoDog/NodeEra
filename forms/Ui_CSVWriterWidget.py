# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jsing\OneDrive\Documents\DEV_LAPTOP_LOCAL_REPO\NODEERA\forms\CSVWriterWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(388, 270)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmFile = QtWidgets.QFrame(self.frame)
        self.frmFile.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmFile.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmFile.setObjectName("frmFile")
        self.gridLayout = QtWidgets.QGridLayout(self.frmFile)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frmFile)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.txtCSVFileName = QtWidgets.QLineEdit(self.frmFile)
        self.txtCSVFileName.setReadOnly(True)
        self.txtCSVFileName.setObjectName("txtCSVFileName")
        self.gridLayout.addWidget(self.txtCSVFileName, 0, 1, 1, 4)
        self.btnSaveCSVFile = QtWidgets.QPushButton(self.frmFile)
        self.btnSaveCSVFile.setObjectName("btnSaveCSVFile")
        self.gridLayout.addWidget(self.btnSaveCSVFile, 0, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(27, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 7, 1, 1)
        self.chkWriteHeader = QtWidgets.QCheckBox(self.frmFile)
        self.chkWriteHeader.setObjectName("chkWriteHeader")
        self.gridLayout.addWidget(self.chkWriteHeader, 1, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.frmFile)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.cmbDelimiter = QtWidgets.QComboBox(self.frmFile)
        self.cmbDelimiter.setEditable(True)
        self.cmbDelimiter.setObjectName("cmbDelimiter")
        self.cmbDelimiter.addItem("")
        self.cmbDelimiter.addItem("")
        self.cmbDelimiter.addItem("")
        self.cmbDelimiter.addItem("")
        self.cmbDelimiter.addItem("")
        self.gridLayout.addWidget(self.cmbDelimiter, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frmFile)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2)
        self.cmbQuoteChar = QtWidgets.QComboBox(self.frmFile)
        self.cmbQuoteChar.setEditable(True)
        self.cmbQuoteChar.setObjectName("cmbQuoteChar")
        self.cmbQuoteChar.addItem("")
        self.cmbQuoteChar.addItem("")
        self.cmbQuoteChar.addItem("")
        self.cmbQuoteChar.addItem("")
        self.gridLayout.addWidget(self.cmbQuoteChar, 3, 3, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frmFile)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 2)
        self.cmbUseQuotes = QtWidgets.QComboBox(self.frmFile)
        self.cmbUseQuotes.setEditable(True)
        self.cmbUseQuotes.setObjectName("cmbUseQuotes")
        self.cmbUseQuotes.addItem("")
        self.cmbUseQuotes.addItem("")
        self.cmbUseQuotes.addItem("")
        self.cmbUseQuotes.addItem("")
        self.gridLayout.addWidget(self.cmbUseQuotes, 4, 2, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 5, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.frmFile)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 2)
        self.cmbDoubleQuote = QtWidgets.QComboBox(self.frmFile)
        self.cmbDoubleQuote.setEditable(True)
        self.cmbDoubleQuote.setObjectName("cmbDoubleQuote")
        self.cmbDoubleQuote.addItem("")
        self.cmbDoubleQuote.addItem("")
        self.gridLayout.addWidget(self.cmbDoubleQuote, 5, 2, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 5, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.frmFile)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 3)
        self.cmbEscapeCharacter = QtWidgets.QComboBox(self.frmFile)
        self.cmbEscapeCharacter.setEditable(True)
        self.cmbEscapeCharacter.setObjectName("cmbEscapeCharacter")
        self.cmbEscapeCharacter.addItem("")
        self.cmbEscapeCharacter.addItem("")
        self.cmbEscapeCharacter.addItem("")
        self.cmbEscapeCharacter.addItem("")
        self.cmbEscapeCharacter.addItem("")
        self.gridLayout.addWidget(self.cmbEscapeCharacter, 6, 3, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 5, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.frmFile)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 3)
        self.cmbLineTerminator = QtWidgets.QComboBox(self.frmFile)
        self.cmbLineTerminator.setEditable(True)
        self.cmbLineTerminator.setObjectName("cmbLineTerminator")
        self.cmbLineTerminator.addItem("")
        self.cmbLineTerminator.addItem("")
        self.cmbLineTerminator.addItem("")
        self.gridLayout.addWidget(self.cmbLineTerminator, 7, 3, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 7, 5, 1, 2)
        self.verticalLayout.addWidget(self.frmFile)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_3.setBuddy(self.txtCSVFileName)
        self.label_6.setBuddy(self.cmbDelimiter)
        self.label_7.setBuddy(self.cmbQuoteChar)
        self.label_8.setBuddy(self.cmbUseQuotes)
        self.label_9.setBuddy(self.cmbDoubleQuote)
        self.label_10.setBuddy(self.cmbEscapeCharacter)
        self.label_11.setBuddy(self.cmbLineTerminator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "File Name:"))
        self.btnSaveCSVFile.setText(_translate("Form", "Select File Name ..."))
        self.chkWriteHeader.setText(_translate("Form", "Output Header Column Names"))
        self.label_6.setToolTip(_translate("Form", "The character used between fields."))
        self.label_6.setText(_translate("Form", "Delimiter:"))
        self.cmbDelimiter.setItemText(0, _translate("Form", ","))
        self.cmbDelimiter.setItemText(1, _translate("Form", "/"))
        self.cmbDelimiter.setItemText(2, _translate("Form", "#"))
        self.cmbDelimiter.setItemText(3, _translate("Form", "|"))
        self.cmbDelimiter.setItemText(4, _translate("Form", "Enter a character"))
        self.label_7.setToolTip(_translate("Form", "The character used to quote text fields"))
        self.label_7.setText(_translate("Form", "Quote Character:"))
        self.cmbQuoteChar.setItemText(0, _translate("Form", "None"))
        self.cmbQuoteChar.setItemText(1, _translate("Form", "\'"))
        self.cmbQuoteChar.setItemText(2, _translate("Form", "\""))
        self.cmbQuoteChar.setItemText(3, _translate("Form", "Enter a Character"))
        self.label_8.setToolTip(_translate("Form", "Defines when quotes will be used on text fields."))
        self.label_8.setText(_translate("Form", "Use Quotes:"))
        self.cmbUseQuotes.setItemText(0, _translate("Form", "All"))
        self.cmbUseQuotes.setItemText(1, _translate("Form", "Minimal"))
        self.cmbUseQuotes.setItemText(2, _translate("Form", "Non-Numeric"))
        self.cmbUseQuotes.setItemText(3, _translate("Form", "None"))
        self.label_9.setToolTip(_translate("Form", "True will double the quote character when it appears inside a quoted string.  False will use the escape character."))
        self.label_9.setText(_translate("Form", "Doube Quote:"))
        self.cmbDoubleQuote.setItemText(0, _translate("Form", "TRUE"))
        self.cmbDoubleQuote.setItemText(1, _translate("Form", "FALSE"))
        self.label_10.setToolTip(_translate("Form", "The character used between fields."))
        self.label_10.setText(_translate("Form", "Escape Character:"))
        self.cmbEscapeCharacter.setItemText(0, _translate("Form", "None"))
        self.cmbEscapeCharacter.setItemText(1, _translate("Form", "/"))
        self.cmbEscapeCharacter.setItemText(2, _translate("Form", "#"))
        self.cmbEscapeCharacter.setItemText(3, _translate("Form", "|"))
        self.cmbEscapeCharacter.setItemText(4, _translate("Form", "Enter a character"))
        self.label_11.setToolTip(_translate("Form", "The character used between fields."))
        self.label_11.setText(_translate("Form", "Line Terminator:"))
        self.cmbLineTerminator.setItemText(0, _translate("Form", "\\r\\n"))
        self.cmbLineTerminator.setItemText(1, _translate("Form", "\\r"))
        self.cmbLineTerminator.setItemText(2, _translate("Form", "\\n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())