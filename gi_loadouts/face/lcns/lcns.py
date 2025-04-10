
################################################################################
## Form generated from reading UI file 'lcns.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QSizePolicy


class Ui_lcns:
    def setupUi(self, lcns):
        if not lcns.objectName():
            lcns.setObjectName("lcns")
        lcns.setWindowModality(Qt.WindowModality.ApplicationModal)
        lcns.resize(600, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lcns.sizePolicy().hasHeightForWidth())
        lcns.setSizePolicy(sizePolicy)
        lcns.setMinimumSize(QSize(600, 630))
        lcns.setMaximumSize(QSize(600, 630))
        font = QFont()
        font.setFamilies(["IBM Plex Sans"])
        font.setPointSize(10)
        lcns.setFont(font)
        self.icon = QLabel(lcns)
        self.icon.setObjectName("icon")
        self.icon.setGeometry(QRect(225, 65, 150, 150))
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(150, 150))
        self.icon.setMaximumSize(QSize(150, 150))
        self.icon.setPixmap(QPixmap(":/pmon/imgs/pmon/8.webp"))
        self.icon.setScaledContents(True)
        self.head = QLabel(lcns)
        self.head.setObjectName("head")
        self.head.setGeometry(QRect(50, 225, 500, 30))
        sizePolicy.setHeightForWidth(self.head.sizePolicy().hasHeightForWidth())
        self.head.setSizePolicy(sizePolicy)
        self.head.setMinimumSize(QSize(500, 30))
        self.head.setMaximumSize(QSize(500, 30))
        font1 = QFont()
        font1.setFamilies(["IBM Plex Sans"])
        font1.setPointSize(20)
        self.head.setFont(font1)
        self.head.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vers = QLabel(lcns)
        self.vers.setObjectName("vers")
        self.vers.setGeometry(QRect(50, 265, 500, 15))
        sizePolicy.setHeightForWidth(self.vers.sizePolicy().hasHeightForWidth())
        self.vers.setSizePolicy(sizePolicy)
        self.vers.setMinimumSize(QSize(500, 15))
        self.vers.setMaximumSize(QSize(500, 15))
        self.vers.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.body = QLabel(lcns)
        self.body.setObjectName("body")
        self.body.setGeometry(QRect(50, 350, 500, 160))
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setMinimumSize(QSize(500, 160))
        self.body.setMaximumSize(QSize(500, 160))
        self.body.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.body.setWordWrap(True)
        self.comp = QLabel(lcns)
        self.comp.setObjectName("comp")
        self.comp.setGeometry(QRect(50, 285, 500, 15))
        sizePolicy.setHeightForWidth(self.comp.sizePolicy().hasHeightForWidth())
        self.comp.setSizePolicy(sizePolicy)
        self.comp.setMinimumSize(QSize(500, 15))
        self.comp.setMaximumSize(QSize(500, 15))
        self.comp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(lcns)

        QMetaObject.connectSlotsByName(lcns)
    # setupUi

    def retranslateUi(self, lcns):
        lcns.setWindowTitle(QCoreApplication.translate("lcns", "Dialog", None))
        self.icon.setText("")
        self.head.setText(QCoreApplication.translate("lcns", "<html><head/><body><p><span style=\" font-weight:700;\">Loadouts for Genshin Impact</span></p></body></html>", None))
        self.vers.setText(QCoreApplication.translate("lcns", "Version v0.0.0", None))
        self.body.setText(QCoreApplication.translate("lcns", "<html><head/><body><p align=\"justify\">This program is free software: you can redistribute it and/or modify it under the terms of the <span style=\" font-weight:700;\">GNU General Public License</span> as published by the <a href=\"https://www.fsf.org/\"><span style=\" font-weight:700; text-decoration: underline; color:#498058;\">Free Software Foundation</span></a><span style=\" font-weight:700;\">,</span> either <span style=\" font-weight:700;\">version 3</span> of the License, or (at your option) any <span style=\" font-weight:700;\">later version</span>.</p><p align=\"justify\">This program is distributed in the hope that it will be useful, but <span style=\" font-weight:700;\">without any warranty</span>; without even the implied warranty of <span style=\" font-weight:700;\">merchantability</span> or <span style=\" font-weight:700;\">fitness for a particular purpose</span>. See the <a href=\"https://github.com/gridhead/gi-loadouts/blob/main/LICENSE\"><span style=\" font-weight:700; text-decoration: underl"
                        "ine; color:#498058;\">GNU General Public License</span></a> for more details.</p><p align=\"justify\">\u00a9 All rights to <a href=\"https://genshin.hoyoverse.com/\"><span style=\" font-weight:700; text-decoration: underline; color:#498058;\">Genshin Impact</span></a> assets used in this project are reserved by <a href=\"https://www.mihoyo.com/\"><span style=\" font-weight:700; text-decoration: underline; color:#498058;\">miHoYo Ltd.</span></a> and <span style=\" font-weight:700;\">Cognosphere Pte</span>., Ltd. Other properties belong to their respective owners.</p></body></html>", None))
        self.comp.setText(QCoreApplication.translate("lcns", "This version is compatible with Genshin Impact 5.0", None))
    # retranslateUi

