from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from demo_id_window import Lookup_Window

font = QFont("Cordia New", 16)

class ID_Button(QPushButton):
    def __init__(self):
        super().__init__()  

        # Setting Up ID Button
        self.setText("ค้นหาชื่อผู้ใช้")
        self.setFont(font)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(
            "QPushButton {border:none; color:blue; text-decoration: underline;}"
            "QPushButton:hover {color: red;}"
        )

        # Setting Up Connect Function
        self.clicked.connect(self.open_lookup_window)

    def open_lookup_window(self):
        self.lookup_window = Lookup_Window()
        self.lookup_window.show()