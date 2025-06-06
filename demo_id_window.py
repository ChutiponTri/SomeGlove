from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import QThread, Qt
import sys
from demo_database import Database

font = QFont("Cordia New", 16)

class Lookup_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("รายชื่อผู้ใช้")
        self.setWindowIcon(QIcon("icons/id_look.png"))

        # Create Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create Labels
        header = QLabel("รายชื่อผู้ใช้")

        # Create Button
        button = QPushButton("ยืนยัน")

        # Set Button Connect Function
        button.clicked.connect(self.close)

        # Setting Font
        header.setFont(QFont("Cordia New", 30, QFont.Weight.Bold))
        button.setFont(font)

        # Create Layout
        layout = QVBoxLayout()
        layout.addWidget(header, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Create Label For Each Files
        users = Database.get_all_usernames()
        if users:
            for file in users:
                user = QLabel(file)
                user.setFont(font)
                layout.addWidget(user)
        layout.addStretch(1)
        layout.addWidget(button)
        
        self.central_widget.setLayout(layout)
        self.setMinimumSize(300, 300)
        print("HN Check Window is Ready")

    # Autocall Function To Toggle When Window Closed
    def closeEvent(self, event):
        print("HN Check Window is Closed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Lookup_Window()
    window.show()
    sys.exit(app.exec())