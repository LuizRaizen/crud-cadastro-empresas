# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(797, 483)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, 0)
        self.frm_left_container = QFrame(self.centralwidget)
        self.frm_left_container.setObjectName(u"frm_left_container")
        self.frm_left_container.setMaximumSize(QSize(9, 16777215))
        self.frm_left_container.setFrameShape(QFrame.StyledPanel)
        self.frm_left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 20)
        self.frame = QFrame(self.frm_left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 6)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.frm_left_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_3)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox {\n"
"	text-align: left;\n"
"	background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pg_menu = QWidget()
        self.pg_menu.setObjectName(u"pg_menu")
        self.pg_menu.setGeometry(QRect(0, 0, 94, 343))
        self.verticalLayout_3 = QVBoxLayout(self.pg_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.btn_home = QPushButton(self.pg_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        font.setBold(False)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QToolBox {\n"
"	text-align: left;\n"
"	background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-align: left;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_register = QPushButton(self.pg_menu)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.btn_register.setFont(font1)
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_register)

        self.btn_contact = QPushButton(self.pg_menu)
        self.btn_contact.setObjectName(u"btn_contact")
        self.btn_contact.setMinimumSize(QSize(0, 30))
        self.btn_contact.setFont(font1)
        self.btn_contact.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_contact)

        self.btn_about = QPushButton(self.pg_menu)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(0, 30))
        self.btn_about.setFont(font1)
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_about)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.pg_menu, u"Menu")
        self.pg_info = QWidget()
        self.pg_info.setObjectName(u"pg_info")
        self.pg_info.setGeometry(QRect(0, 0, 143, 343))
        self.verticalLayout_4 = QVBoxLayout(self.pg_info)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.pg_info)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setTextFormat(Qt.RichText)

        self.verticalLayout_4.addWidget(self.label_3)

        self.toolBox.addItem(self.pg_info, u"Informa\u00e7\u00f5es")

        self.horizontalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frm_left_container)

        self.frm_main_container = QFrame(self.centralwidget)
        self.frm_main_container.setObjectName(u"frm_main_container")
        self.frm_main_container.setFrameShape(QFrame.StyledPanel)
        self.frm_main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.frm_header = QFrame(self.frm_main_container)
        self.frm_header.setObjectName(u"frm_header")
        self.frm_header.setFrameShape(QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.btn_toggle = QPushButton(self.frm_header)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.frm_header)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frm_header)

        self.frm_main = QFrame(self.frm_main_container)
        self.frm_main.setObjectName(u"frm_main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frm_main.sizePolicy().hasHeightForWidth())
        self.frm_main.setSizePolicy(sizePolicy3)
        self.frm_main.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frm_main.setFrameShape(QFrame.StyledPanel)
        self.frm_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frm_main)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, -1)
        self.stc_pages = QStackedWidget(self.frm_main)
        self.stc_pages.setObjectName(u"stc_pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_6.addWidget(self.logo)

        self.stc_pages.addWidget(self.pg_home)
        self.pg_register = QWidget()
        self.pg_register.setObjectName(u"pg_register")
        self.pg_register.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.pg_register)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.pg_register)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(10)
        self.label_5.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_9.addWidget(self.label_5)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.txt_number = QLineEdit(self.frame_4)
        self.txt_number.setObjectName(u"txt_number")

        self.gridLayout.addWidget(self.txt_number, 3, 0, 1, 2)

        self.txt_phone = QLineEdit(self.frame_4)
        self.txt_phone.setObjectName(u"txt_phone")

        self.gridLayout.addWidget(self.txt_phone, 5, 0, 1, 3)

        self.txt_complement = QLineEdit(self.frame_4)
        self.txt_complement.setObjectName(u"txt_complement")

        self.gridLayout.addWidget(self.txt_complement, 3, 2, 1, 2)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")

        self.gridLayout.addWidget(self.txt_cnpj, 1, 0, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")

        self.gridLayout.addWidget(self.txt_email, 5, 3, 1, 3)

        self.txt_public_place = QLineEdit(self.frame_4)
        self.txt_public_place.setObjectName(u"txt_public_place")

        self.gridLayout.addWidget(self.txt_public_place, 2, 0, 1, 5)

        self.txt_enterprise_name = QLineEdit(self.frame_4)
        self.txt_enterprise_name.setObjectName(u"txt_enterprise_name")

        self.gridLayout.addWidget(self.txt_enterprise_name, 1, 1, 1, 4)

        self.txt_district = QLineEdit(self.frame_4)
        self.txt_district.setObjectName(u"txt_district")

        self.gridLayout.addWidget(self.txt_district, 3, 4, 1, 1)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")

        self.gridLayout.addWidget(self.txt_uf, 4, 3, 1, 1)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")

        self.gridLayout.addWidget(self.txt_cep, 4, 4, 1, 1)

        self.txt_county = QLineEdit(self.frame_4)
        self.txt_county.setObjectName(u"txt_county")

        self.gridLayout.addWidget(self.txt_county, 4, 0, 1, 3)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(160, 40))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 120, 255);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setMargin(10)

        self.verticalLayout_8.addWidget(self.label_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        __qtablewidgetitem6.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem6.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        __qtablewidgetitem7.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem7.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        __qtablewidgetitem8.setBackground(QColor(148, 148, 148));
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderVIew::section {\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background-color: rgb(252, 252, 252);\n"
"}")

        self.horizontalLayout_7.addWidget(self.tableWidget)

        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 24, 74);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	font: 11pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(240k, 230, 230);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, -1)
        self.btn_generate = QPushButton(self.frame_2)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(120, 30))
        self.btn_generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_generate.setStyleSheet(u"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(49, 147, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_generate)

        self.btn_change = QPushButton(self.frame_2)
        self.btn_change.setObjectName(u"btn_change")
        self.btn_change.setMinimumSize(QSize(120, 30))
        self.btn_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_change.setStyleSheet(u"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_change)

        self.btn_remove = QPushButton(self.frame_2)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setMinimumSize(QSize(120, 30))
        self.btn_remove.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove.setStyleSheet(u"QPushButton::hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(199, 66, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_remove)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.stc_pages.addWidget(self.pg_register)
        self.pg_contact = QWidget()
        self.pg_contact.setObjectName(u"pg_contact")
        self.verticalLayout_10 = QVBoxLayout(self.pg_contact)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.pg_contact)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font2)
        self.label_7.setMargin(0)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_6 = QLabel(self.pg_contact)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.label_8 = QLabel(self.pg_contact)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_contact)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.pg_contact)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_10.addWidget(self.label_10)

        self.stc_pages.addWidget(self.pg_contact)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_11 = QVBoxLayout(self.pg_about)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.pg_about)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setMargin(10)

        self.verticalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.pg_about)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_12)

        self.stc_pages.addWidget(self.pg_about)

        self.verticalLayout_5.addWidget(self.stc_pages)


        self.verticalLayout.addWidget(self.frm_main)

        self.frm_footer = QFrame(self.frm_main_container)
        self.frm_footer.setObjectName(u"frm_footer")
        self.frm_footer.setFrameShape(QFrame.StyledPanel)
        self.frm_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_label = QLabel(self.frm_footer)
        self.lbl_label.setObjectName(u"lbl_label")

        self.horizontalLayout_3.addWidget(self.lbl_label)


        self.verticalLayout.addWidget(self.frm_footer)


        self.horizontalLayout.addWidget(self.frm_main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        self.stc_pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PyTax", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contact.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Usu\u00e1rio:</span><span style=\" color:#ffffff;\"> PyTax</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Sistema:</span><span style=\" color:#ffffff;\"> Cadastro</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Status:</span><span style=\" color:#ffffff;\"> Ativo</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Venc:</span><span style=\" color:#ffffff;\"> 12/12/2999</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_info), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.btn_toggle.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo4.png\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EMPRESAS", None))
        self.txt_number.setText("")
        self.txt_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_complement.setText("")
        self.txt_complement.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_cnpj.setText("")
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_public_place.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_enterprise_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.txt_district.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_county.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Formul\u00e1rio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">EMPRESAS</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(11) 951447350</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">contato@pytax.net</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">pytaxsolutions</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/Youtube.png\"/><span style=\" font-size:18pt; vertical-align:super;\">Pytax</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Este sistema faz consulta do CNPJ utilizando a API da Receita Federal e faz o. cadastro em um banco de dados SQLITE3. O objetivo deste sistema \u00e9 demonstrar conhecimentos em Python e QT no desenvolvimento de aplica\u00e7\u00f5es modernas e funcionais.</p></body></html>", None))
        self.lbl_label.setText(QCoreApplication.translate("MainWindow", u"Copyright 2023", None))
    # retranslateUi

