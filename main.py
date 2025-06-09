#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import sys

from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
from ui_functions import request_cnpj

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTax - Sistema de Cadastro de Empresas")
        app_icon = QIcon(u"")
        self.setWindowIcon(app_icon)

        #################################################################################
        ## Exibir ou esconder o menu lateral;
        #################################################################################
        
        self.btn_toggle.clicked.connect(self.view_hide_menu)
        
        #################################################################################
        ## Exibir ou esconder o menu lateral;
        #################################################################################
        
        self.btn_home.clicked.connect(lambda: self.stc_pages.setCurrentWidget(self.pg_home))
        self.btn_register.clicked.connect(lambda: self.stc_pages.setCurrentWidget(self.pg_register))
        self.btn_contact.clicked.connect(lambda: self.stc_pages.setCurrentWidget(self.pg_contact))
        self.btn_about.clicked.connect(lambda: self.stc_pages.setCurrentWidget(self.pg_about))
        
        #################################################################################
        ## Exibir ou esconder o menu lateral;
        #################################################################################
        
        self.txt_cnpj.editingFinished.connect(self.consult_api)
        
    def view_hide_menu(self):
        width = self.frm_left_container.width()
        if width == 9:
            new_width = 200
        else:
            new_width = 9
            
        self.animation = QPropertyAnimation(self.frm_left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
            
    def consult_api(self):
        """ Consulta a API """
        
        fields = request_cnpj(self.txt_cnpj.text())
        print(fields)
        print(type(fields))
        
        self.txt_enterprise_name.setText(fields[1])
        self.txt_public_place.setText(fields[2])
        self.txt_number.setText(fields[3])
        self.txt_complement.setText(fields[4])
        self.txt_county.setText(fields[5])
        self.txt_district.setText(fields[6])
        self.txt_uf.setText(fields[7])
        self.txt_cep.setText(fields[8].replace('.', '').replace('-', ''))
        self.txt_phone.setText(fields[9].replace('-', '').replace('(', '').replace(')', ''))
        self.txt_email.setText(fields[10])
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
