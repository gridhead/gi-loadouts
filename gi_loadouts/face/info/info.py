
################################################################################
## Form generated from reading UI file 'info.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QSizePolicy


class Ui_info:
    def setupUi(self, info):
        if not info.objectName():
            info.setObjectName("info")
        info.setWindowModality(Qt.WindowModality.ApplicationModal)
        info.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(info.sizePolicy().hasHeightForWidth())
        info.setSizePolicy(sizePolicy)
        info.setMinimumSize(QSize(600, 800))
        info.setMaximumSize(QSize(600, 800))
        font = QFont()
        font.setFamilies(["IBM Plex Sans"])
        font.setPointSize(10)
        info.setFont(font)
        self.icon = QLabel(info)
        self.icon.setObjectName("icon")
        self.icon.setGeometry(QRect(225, 65, 150, 150))
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(150, 150))
        self.icon.setMaximumSize(QSize(150, 150))
        self.icon.setPixmap(QPixmap(":/pmon/imgs/pmon/8.webp"))
        self.icon.setScaledContents(True)
        self.head = QLabel(info)
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
        self.vers = QLabel(info)
        self.vers.setObjectName("vers")
        self.vers.setGeometry(QRect(50, 265, 500, 15))
        sizePolicy.setHeightForWidth(self.vers.sizePolicy().hasHeightForWidth())
        self.vers.setSizePolicy(sizePolicy)
        self.vers.setMinimumSize(QSize(500, 15))
        self.vers.setMaximumSize(QSize(500, 15))
        self.vers.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.body = QLabel(info)
        self.body.setObjectName("body")
        self.body.setGeometry(QRect(50, 350, 500, 285))
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setMinimumSize(QSize(500, 285))
        self.body.setMaximumSize(QSize(500, 285))
        self.body.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.body.setWordWrap(True)
        self.comp = QLabel(info)
        self.comp.setObjectName("comp")
        self.comp.setGeometry(QRect(50, 285, 500, 15))
        sizePolicy.setHeightForWidth(self.comp.sizePolicy().hasHeightForWidth())
        self.comp.setSizePolicy(sizePolicy)
        self.comp.setMinimumSize(QSize(500, 15))
        self.comp.setMaximumSize(QSize(500, 15))
        self.comp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.updt = QPushButton(info)
        self.updt.setObjectName("updt")
        self.updt.setGeometry(QRect(225, 685, 150, 25))
        sizePolicy.setHeightForWidth(self.updt.sizePolicy().hasHeightForWidth())
        self.updt.setSizePolicy(sizePolicy)
        self.updt.setMinimumSize(QSize(150, 25))
        self.updt.setMaximumSize(QSize(150, 25))

        self.retranslateUi(info)

        QMetaObject.connectSlotsByName(info)
    # setupUi

    def retranslateUi(self, info):
        info.setWindowTitle(QCoreApplication.translate("info", "Dialog", None))
        self.icon.setText("")
        self.head.setText(QCoreApplication.translate("info", "<html><head/><body><p><span style=\" font-weight:700;\">Loadouts for Genshin Impact</span></p></body></html>", None))
        self.vers.setText(QCoreApplication.translate("info", "Version v0.0.0", None))
        self.body.setText(QCoreApplication.translate("info", "<html><head/><body><p align=\"justify\">This is a desktop application that allows travelers to manage their custom equipment of artifacts and weapons for playable characters and makes it convenient for travelers to calculate the associated statistics based on their equipment using the semantic understanding of how the gameplay works. Travelers can create their bespoke loadouts consisting of characters, artifacts and weapons and share them with their fellow travelers. Supported file formats include a human-readable <span style=\" font-weight:700;\">Yet Another Markup Language (YAML)</span> serialization format and a JSON-based <span style=\" font-weight:700;\">Genshin Open Object Definition (GOOD)</span> serialization format.</p><p align=\"justify\">This project is currently in its beta phase and we are committed to delivering a quality experience with every release we make. If you are excited about the direction of this project and want to contribute to the efforts, we would greatly appreciate it if you help u"
                        "s boost the project visibility by <span style=\" font-weight:700;\">starring the project repository</span>, address the releases by <span style=\" font-weight:700;\">reporting the experienced errors</span>, choose the direction by <span style=\" font-weight:700;\">proposing the intended features</span>, enhance the usability by <span style=\" font-weight:700;\">documenting the project repository</span>, improve the codebase by <span style=\" font-weight:700;\">opening the pull requests</span> and finally, persist our efforts by <span style=\" font-weight:700;\">sponsoring the development members</span>.</p></body></html>", None))
        self.comp.setText(QCoreApplication.translate("info", "This version is compatible with Genshin Impact 0.0 Phase 0", None))
        self.updt.setText(QCoreApplication.translate("info", "CHECK FOR UPDATES", None))
    # retranslateUi

