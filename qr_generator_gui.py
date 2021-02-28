from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLineEdit, QPushButton, QTextEdit, QComboBox, QCheckBox, QSpinBox, QFileDialog, QMenu, QAction
import sys
from qr_generator import generator

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.setFixedSize(431, 357) 
        
        self.button1 = self.findChild(QPushButton, 'generate_1')
        self.button1.clicked.connect(self.generate_text)
        self.text_or_link = self.findChild(QLineEdit, "text_or_link")

        self.button2 = self.findChild(QPushButton, 'generate_2')
        self.button2.clicked.connect(self.generate_email)
        self.to_email = self.findChild(QLineEdit, "to_email")
        self.subject = self.findChild(QLineEdit, "subject")
        self.email_message = self.findChild(QTextEdit, "email_message")

        self.button3 = self.findChild(QPushButton, 'generate_3')
        self.button3.clicked.connect(self.generate_sms)
        self.to_phone = self.findChild(QLineEdit, "to_phone")
        self.sms_message = self.findChild(QTextEdit, "sms_message")


        self.button4 = self.findChild(QPushButton, 'generate_4')
        self.button4.clicked.connect(self.generate_wifi)
        self.ssid = self.findChild(QLineEdit, "ssid")
        self.passwd = self.findChild(QLineEdit, "password")
        self.encryption = self.findChild(QComboBox, "encryption")
        self.hidden = self.findChild(QCheckBox, "hidden")

        self.button5 = self.findChild(QPushButton, 'generate_5')
        self.button5.clicked.connect(self.generate_contact_details)
        self.name = self.findChild(QLineEdit, "name")
        self.org = self.findChild(QLineEdit, "org")
        self.tel = self.findChild(QLineEdit, "tel")
        self.email = self.findChild(QLineEdit, "email")
        self.cell = self.findChild(QLineEdit, "cell")
        self.fax = self.findChild(QLineEdit, "fax")
        self.street = self.findChild(QLineEdit, "street")
        self.city = self.findChild(QLineEdit, "city")
        self.region = self.findChild(QLineEdit, "region")
        self.postcode = self.findChild(QLineEdit, "postcode")
        self.country = self.findChild(QLineEdit, "country")
        self.url = self.findChild(QLineEdit, "url")

        self.bg=self.findChild(QComboBox, 'bg')
        self.fg=self.findChild(QComboBox, 'fg')
        self.border=self.findChild(QSpinBox, 'border')
        self.boxsize=self.findChild(QSpinBox, 'boxsize')
        self.qrversion=self.findChild(QComboBox, 'qrversion')

        self.logo=self.findChild(QPushButton, 'logo_2')
        self.logo_file='False'
        self.logo.clicked.connect(self.choose_logo)
        self.out_name=self.findChild(QLineEdit, 'output')
        self.filename='False'
    
        self.show()

    def generate_text(self): 
        if self.out_name.text():
            self.filename=self.out_name.text()
        else:
            self.filename='False'
        generator.generate_text(self.text_or_link.text(), self.qrversion.currentText(), self.boxsize.value(), self.border.value(), self.fg.currentText(), self.bg.currentText(), self.logo_file, self.filename)

    def generate_email(self):
        if self.out_name.text():
            self.filename=self.out_name.text()
        else:
            self.filename='False'
        generator.generate_email(self.to_email.text(), self.subject.text(), self.email_message.toPlainText(), self.qrversion.currentText(), self.boxsize.value(), self.border.value(), self.fg.currentText(), self.bg.currentText(), self.filename)
    
    def generate_sms(self):
        if self.out_name.text():
            self.filename=self.out_name.text()
        else:
            self.filename='False'
        generator.generate_sms(self.to_phone.text(), self.sms_message.toPlainText(), self.qrversion.currentText(), self.boxsize.value(), self.border.value(), self.fg.currentText(), self.bg.currentText(), self.filename)

    def generate_wifi(self):
        if self.out_name.text():
            self.filename=self.out_name.text()
        else:
            self.filename='False'

        if self.hidden.isChecked():
            hidden_='true'
        else:
            hidden_='false'
        generator.generate_wifi(self.ssid.text(), self.passwd.text(), self.encryption.currentText(), hidden_, self.qrversion.currentText(), self.boxsize.value(), self.border.value(), self.fg.currentText(), self.bg.currentText(), self.filename)
    
    def generate_contact_details(self):
        if self.out_name.text():
            self.filename=self.out_name.text()
        else:
            self.filename='False'
        generator.generate_contact_details(self.name.text(), self.org.text(), self.tel.text(), self.email.text(), self.cell.text(), self.fax.text(), self.street.text(), self.city.text(), self.region.text(), self.postcode.text(), self.country.text(), self.url.text, self.qrversion.currentText(), self.boxsize.value(), self.border.value(), self.fg.currentText(), self.bg.currentText(), self.filename)

    def choose_logo(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","PNG Files(*.png)", options=options)
        if fileName:
            self.logo.setText(fileName)
            self.logo.setToolTip(fileName)
            self.logo_file=fileName
        else:
            self.logo_file='False'
    

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = Ui()
app.exec_()