# Form implementation generated from reading ui file 'voting.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 581)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(651, 581))
        MainWindow.setMaximumSize(QtCore.QSize(651, 581))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 651, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(651, 581))
        self.stackedWidget.setMaximumSize(QtCore.QSize(651, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.application_label = QtWidgets.QLabel(parent=self.page)
        self.application_label.setGeometry(QtCore.QRect(170, 0, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.application_label.setFont(font)
        self.application_label.setObjectName("application_label")
        self.firstname_label = QtWidgets.QLabel(parent=self.page)
        self.firstname_label.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.firstname_label.setFont(font)
        self.firstname_label.setObjectName("firstname_label")
        self.lastname_label = QtWidgets.QLabel(parent=self.page)
        self.lastname_label.setGeometry(QtCore.QRect(250, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lastname_label.setFont(font)
        self.lastname_label.setObjectName("lastname_label")
        self.age_label = QtWidgets.QLabel(parent=self.page)
        self.age_label.setGeometry(QtCore.QRect(20, 150, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.age_label.setFont(font)
        self.age_label.setObjectName("age_label")
        self.age_number = QtWidgets.QSpinBox(parent=self.page)
        self.age_number.setGeometry(QtCore.QRect(80, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.age_number.setFont(font)
        self.age_number.setObjectName("age_number")
        self.citizen_label = QtWidgets.QLabel(parent=self.page)
        self.citizen_label.setGeometry(QtCore.QRect(20, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.citizen_label.setFont(font)
        self.citizen_label.setObjectName("citizen_label")
        self.citizen_input = QtWidgets.QComboBox(parent=self.page)
        self.citizen_input.setGeometry(QtCore.QRect(140, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.citizen_input.setFont(font)
        self.citizen_input.setObjectName("citizen_input")
        self.citizen_input.addItem("")
        self.citizen_input.setItemText(0, "")
        self.citizen_input.addItem("")
        self.citizen_input.setItemText(1, "Yes")
        self.citizen_input.addItem("")
        self.citizen_input.setItemText(2, "No")
        self.registered_label = QtWidgets.QLabel(parent=self.page)
        self.registered_label.setGeometry(QtCore.QRect(20, 340, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.registered_label.setFont(font)
        self.registered_label.setObjectName("registered_label")
        self.registered_input = QtWidgets.QComboBox(parent=self.page)
        self.registered_input.setGeometry(QtCore.QRect(210, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.registered_input.setFont(font)
        self.registered_input.setObjectName("registered_input")
        self.registered_input.addItem("")
        self.registered_input.setItemText(0, "")
        self.registered_input.addItem("")
        self.registered_input.setItemText(1, "Yes")
        self.registered_input.addItem("")
        self.registered_input.setItemText(2, "No")
        self.state_label = QtWidgets.QLabel(parent=self.page)
        self.state_label.setGeometry(QtCore.QRect(20, 230, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.state_label.setFont(font)
        self.state_label.setObjectName("state_label")
        self.address_label = QtWidgets.QLabel(parent=self.page)
        self.address_label.setGeometry(QtCore.QRect(210, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.zip_label = QtWidgets.QLabel(parent=self.page)
        self.zip_label.setGeometry(QtCore.QRect(470, 230, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.zip_label.setFont(font)
        self.zip_label.setObjectName("zip_label")
        self.state_input = QtWidgets.QLineEdit(parent=self.page)
        self.state_input.setGeometry(QtCore.QRect(80, 230, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.state_input.setFont(font)
        self.state_input.setObjectName("state_input")
        self.submit_button = QtWidgets.QPushButton(parent=self.page)
        self.submit_button.setGeometry(QtCore.QRect(170, 430, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.output_label = QtWidgets.QLabel(parent=self.page)
        self.output_label.setGeometry(QtCore.QRect(120, 470, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_label.setFont(font)
        self.output_label.setText("")
        self.output_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.output_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output_label.setWordWrap(True)
        self.output_label.setObjectName("output_label")
        self.firstname_input = QtWidgets.QLineEdit(parent=self.page)
        self.firstname_input.setGeometry(QtCore.QRect(130, 89, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstname_input.setFont(font)
        self.firstname_input.setObjectName("firstname_input")
        self.lastname_input = QtWidgets.QLineEdit(parent=self.page)
        self.lastname_input.setGeometry(QtCore.QRect(370, 90, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastname_input.setFont(font)
        self.lastname_input.setObjectName("lastname_input")
        self.address_input = QtWidgets.QLineEdit(parent=self.page)
        self.address_input.setGeometry(QtCore.QRect(300, 229, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.address_input.setFont(font)
        self.address_input.setObjectName("address_input")
        self.zip_input = QtWidgets.QLineEdit(parent=self.page)
        self.zip_input.setGeometry(QtCore.QRect(510, 230, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.zip_input.setFont(font)
        self.zip_input.setObjectName("zip_input")
        self.continue_button = QtWidgets.QPushButton(parent=self.page)
        self.continue_button.setGeometry(QtCore.QRect(550, 510, 91, 31))
        self.continue_button.setObjectName("continue_button")
        self.clear_button = QtWidgets.QPushButton(parent=self.page)
        self.clear_button.setGeometry(QtCore.QRect(10, 510, 91, 31))
        self.clear_button.setObjectName("clear_button")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.voteballot_label = QtWidgets.QLabel(parent=self.page_2)
        self.voteballot_label.setGeometry(QtCore.QRect(140, 0, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.voteballot_label.setFont(font)
        self.voteballot_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.voteballot_label.setObjectName("voteballot_label")
        self.id_label = QtWidgets.QLabel(parent=self.page_2)
        self.id_label.setGeometry(QtCore.QRect(120, 90, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.id_name = QtWidgets.QLineEdit(parent=self.page_2)
        self.id_name.setGeometry(QtCore.QRect(210, 90, 261, 31))
        self.id_name.setObjectName("id_name")
        self.candidates_label = QtWidgets.QLabel(parent=self.page_2)
        self.candidates_label.setGeometry(QtCore.QRect(240, 160, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.candidates_label.setFont(font)
        self.candidates_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.candidates_label.setObjectName("candidates_label")
        self.edward_button = QtWidgets.QRadioButton(parent=self.page_2)
        self.edward_button.setGeometry(QtCore.QRect(180, 210, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edward_button.setFont(font)
        self.edward_button.setObjectName("edward_button")
        self.bianca_button = QtWidgets.QRadioButton(parent=self.page_2)
        self.bianca_button.setGeometry(QtCore.QRect(180, 270, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bianca_button.setFont(font)
        self.bianca_button.setObjectName("bianca_button")
        self.felicia_button = QtWidgets.QRadioButton(parent=self.page_2)
        self.felicia_button.setGeometry(QtCore.QRect(180, 330, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.felicia_button.setFont(font)
        self.felicia_button.setObjectName("felicia_button")
        self.submit_button2 = QtWidgets.QPushButton(parent=self.page_2)
        self.submit_button2.setGeometry(QtCore.QRect(200, 380, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.submit_button2.setFont(font)
        self.submit_button2.setObjectName("submit_button2")
        self.output_label2 = QtWidgets.QLabel(parent=self.page_2)
        self.output_label2.setGeometry(QtCore.QRect(170, 430, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_label2.setFont(font)
        self.output_label2.setText("")
        self.output_label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output_label2.setWordWrap(True)
        self.output_label2.setObjectName("output_label2")
        self.totalvotes_label = QtWidgets.QLabel(parent=self.page_2)
        self.totalvotes_label.setGeometry(QtCore.QRect(50, 500, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalvotes_label.setFont(font)
        self.totalvotes_label.setText("")
        self.totalvotes_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.totalvotes_label.setObjectName("totalvotes_label")
        self.restart_button = QtWidgets.QPushButton(parent=self.page_2)
        self.restart_button.setGeometry(QtCore.QRect(560, 510, 75, 23))
        self.restart_button.setObjectName("restart_button")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.application_label.setText(_translate("MainWindow", "VOTING APPLICATION"))
        self.firstname_label.setText(_translate("MainWindow", "First Name:"))
        self.lastname_label.setText(_translate("MainWindow", "Last Name:"))
        self.age_label.setText(_translate("MainWindow", "Age:"))
        self.citizen_label.setText(_translate("MainWindow", "U.S. Citizen?"))
        self.registered_label.setText(_translate("MainWindow", "Registered to vote?"))
        self.state_label.setText(_translate("MainWindow", "State: "))
        self.address_label.setText(_translate("MainWindow", "Address:"))
        self.zip_label.setText(_translate("MainWindow", "Zip:"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT APPLICATION"))
        self.continue_button.setText(_translate("MainWindow", "Continue"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.voteballot_label.setText(_translate("MainWindow", "VOTING BALLOT"))
        self.id_label.setText(_translate("MainWindow", "ID:"))
        self.candidates_label.setText(_translate("MainWindow", "CANDIDATES"))
        self.edward_button.setText(_translate("MainWindow", "Edward"))
        self.bianca_button.setText(_translate("MainWindow", "Bianca"))
        self.felicia_button.setText(_translate("MainWindow", "Felicia"))
        self.submit_button2.setText(_translate("MainWindow", "SUBMIT VOTE"))
        self.restart_button.setText(_translate("MainWindow", "Restart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
