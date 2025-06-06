from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QMessageBox
from PyQt6.QtGui import QFont, QIcon, QPixmap, QKeySequence
from PyQt6.QtCore import Qt
from multiprocessing import freeze_support
import sys
import os
from demo_game_selection import GameSelection
from demo_signup_button import SignUp_Button    
from demo_id_button import ID_Button
from demo_database import Database

font = QFont("Cordia New", 16)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Glove")
        self.setWindowIcon(QIcon("icons/glove.png"))

        # Create Database
        database = Database()

        # Create Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create Labels
        label = QLabel("Smart Glove")
        image = QLabel("")
        pixmap = QPixmap("icons/someglove.png")
        image.setPixmap(pixmap)

        # Create Input Text
        self.text_input = QLineEdit()

        # Create Buttons
        login_button = QPushButton("เข้าสู่ระบบ")
        signup_button = SignUp_Button()
        id_button = ID_Button()

        # Setting Button Connect Function
        login_button.clicked.connect(self.on_login)
        login_button.setShortcut(QKeySequence("Return"))

        # Create Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)

        # Setting Fonts
        label.setFont(QFont("Cordia New", 32, QFont.Weight.Bold))
        login_button.setFont(font)
        self.text_input.setFont(font)

        # Setting PlaceHolder Text
        self.text_input.setPlaceholderText("โปรดใส่ข้อมูลชื่อผู้ใช้")

        # Create Button Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(signup_button)
        button_layout.addWidget(separator)
        button_layout.addWidget(id_button)

        # Create Main Layout
        layout = QVBoxLayout()
        # layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(image, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.text_input)
        layout.addWidget(login_button)
        layout.addLayout(button_layout)

        # Setting Layout
        central_widget.setLayout(layout)

        self.setGeometry(400,100,600,600)

        print("Login Window is Ready")

    # Function To Call When Button was Clicked
    def on_login(self):
        file_name = "%s.xlsx" % self.text_input.text()
        messagebox = QMessageBox()
        messagebox.setWindowTitle("กล่องข้อความ")
        if self.text_input.text() != "":
            if file_name in os.listdir("excel"):
                self.hide()
                Database.create_current_user()
                Database.current_user(self.text_input.text())
                self.game_selection_window = GameSelection()
                self.game_selection_window.signal.connect(self.on_selection_window_close)
                self.game_selection_window.show()
                print("Found User %s" % self.text_input.text())

            else:
                messagebox.setText("ไม่พบข้อมูลของ %s" % self.text_input.text())
                messagebox.setIcon(QMessageBox.Icon.Warning)
                messagebox.exec()
        else:
            messagebox.setText("โปรดกรอกข้อมูลชื่อผู้ใช้")
            messagebox.setIcon(QMessageBox.Icon.Warning)
            messagebox.exec()

    # Close Signal Function
    def on_selection_window_close(self):
        self.show()

    # Autocall Function To Toggle When Window Closed
    def closeEvent(self, event):
        print("Login Window is Closed")

if __name__ == '__main__':
    freeze_support()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())