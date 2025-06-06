from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QLabel, QFrame, QGridLayout
from PyQt6.QtGui import QFont, QIcon, QDoubleValidator, QKeySequence
from PyQt6.QtCore import Qt, pyqtSignal
from threading import Thread
from openpyxl import load_workbook
import pandas as pd
import sys
from demo_database import Database

font = QFont("Cordia New", 16)

class Feedback_1_Window(QMainWindow):
    signal = pyqtSignal()
    def __init__(self, username=None):
        super().__init__()
        self.setWindowTitle("แบบบันทึกผลการทดสอบ")
        self.setWindowIcon(QIcon("icons/feedback.png"))

        # Create Central Widget
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # Create Tabs
        self.init_ui()

        # Update UI
        self.username = username
        self.path = "excel/%s.xlsx" % self.username
        self.sheet_name = "ทดสอบความแข็งแรง"
        update_ui = Thread(target=self.update_ui)
        update_ui.start()

    # Function To Create Feedback 1 UI
    def init_ui(self):
        # Create Table Labels
        self.แบบบันทึกผล = QLabel("ตารางบันทึกผลการทดสอบความแข็งแรงของกล้ามเนื้อบีบมือ")
        self.ครั้งที่ = QLabel("ครั้งที่")
        self.ก่อนเข้าร่วมโปรแกรม = QLabel("ก่อนเข้าร่วมโปรแกรมการออกกำลังกาย")
        self.หลังเข้าร่วมโปรแกรม = QLabel("หลังเข้าร่วมโปรแกรมการออกกำลังกาย 6 สัปดาห์")
        self.ครั้งที่_1 = QLabel("1")
        self.ครั้งที่_2 = QLabel("2")
        self.เลือก = QLabel("เลือกครั้งที่ดีที่สุด")
        self.ใส่ก่อน_1 = QLineEdit()
        self.ใส่ก่อน_2 = QLineEdit()
        self.ใส่หลัง_1 = QLineEdit()
        self.ใส่หลัง_2 = QLineEdit()
        self.ใส่เลือกก่อน = QLineEdit()
        self.ใส่เลือกหลัง = QLineEdit()
        self.ถัดไป = QPushButton("ตกลง")

        # Setting Font For Each Items
        self.แบบบันทึกผล.setFont(font)
        self.ครั้งที่.setFont(font)
        self.ก่อนเข้าร่วมโปรแกรม.setFont(font)
        self.หลังเข้าร่วมโปรแกรม.setFont(font)
        self.ครั้งที่_1.setFont(font)
        self.ครั้งที่_2.setFont(font)
        self.เลือก.setFont(font)
        self.ใส่ก่อน_1.setFont(font)
        self.ใส่ก่อน_2.setFont(font)
        self.ใส่หลัง_1.setFont(font)
        self.ใส่หลัง_2.setFont(font)
        self.ใส่เลือกก่อน.setFont(font)
        self.ใส่เลือกหลัง.setFont(font)
        self.ถัดไป.setFont(font)

        # Set Line Edit Compare Function
        self.ใส่ก่อน_1.textChanged.connect(self.text_change_1)
        self.ใส่ก่อน_2.textChanged.connect(self.text_change_1)
        self.ใส่หลัง_1.textChanged.connect(self.text_change_2)
        self.ใส่หลัง_2.textChanged.connect(self.text_change_2)

        # Set Button Connect Function
        self.ถัดไป.clicked.connect(self.update_excel)
        self.ถัดไป.setShortcut(QKeySequence("Return"))

        # Set Validator For Each Input
        self.ใส่ก่อน_1.setValidator(QDoubleValidator())
        self.ใส่ก่อน_2.setValidator(QDoubleValidator())
        self.ใส่หลัง_1.setValidator(QDoubleValidator())
        self.ใส่หลัง_2.setValidator(QDoubleValidator())
        self.ใส่เลือกก่อน.setValidator(QDoubleValidator())
        self.ใส่เลือกหลัง.setValidator(QDoubleValidator())

        # Set Alignment For Each Input
        self.ใส่ก่อน_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ใส่ก่อน_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ใส่หลัง_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ใส่หลัง_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ใส่เลือกก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ใส่เลือกหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create tab1 Layout
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(self.แบบบันทึกผล, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Create Table Layout
        table_layout = QGridLayout()
        table_layout.addWidget(self.ครั้งที่, 0, 0)
        table_layout.addWidget(self.ก่อนเข้าร่วมโปรแกรม, 0, 2)
        table_layout.addWidget(self.หลังเข้าร่วมโปรแกรม, 0, 4)
        table_layout.addWidget(self.ครั้งที่_1, 2, 0)
        table_layout.addWidget(self.ใส่ก่อน_1, 2, 2)
        table_layout.addWidget(self.ใส่หลัง_1, 2, 4)

        # Add a horizontal line
        line0 = QFrame()
        line0.setFrameShape(QFrame.Shape.HLine)
        line0.setFrameShadow(QFrame.Shadow.Sunken)
        table_layout.addWidget(line0, 1, 0, 1, 5)

        # Add a horizontal line
        line1 = QFrame()
        line1.setFrameShape(QFrame.Shape.HLine)
        line1.setFrameShadow(QFrame.Shadow.Sunken)
        table_layout.addWidget(line1, 3, 0, 1, 5)

        table_layout.addWidget(self.ครั้งที่_2, 4, 0)
        table_layout.addWidget(self.ใส่ก่อน_2, 4, 2)
        table_layout.addWidget(self.ใส่หลัง_2, 4, 4)

        # Add another horizontal line
        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setFrameShadow(QFrame.Shadow.Sunken)
        table_layout.addWidget(line2, 5, 0, 1, 5)

        table_layout.addWidget(self.เลือก, 6, 0)
        table_layout.addWidget(self.ใส่เลือกก่อน, 6, 2)
        table_layout.addWidget(self.ใส่เลือกหลัง, 6, 4)

        # Add a vertical line
        line_v1 = QFrame()
        line_v1.setFrameShape(QFrame.Shape.VLine)
        line_v1.setFrameShadow(QFrame.Shadow.Sunken)
        table_layout.addWidget(line_v1, 0, 1, 8, 1)

        # Add a vertical line
        line_v2 = QFrame()
        line_v2.setFrameShape(QFrame.Shape.VLine)
        line_v2.setFrameShadow(QFrame.Shadow.Sunken)
        table_layout.addWidget(line_v2, 0, 3, 8, 1)

        tab1_layout.addLayout(table_layout)
        tab1_layout.addWidget(self.ถัดไป)
        tab1_layout.addStretch(1)

        # Add Tabs
        self.widget.setLayout(tab1_layout)

    # Function to Compare Numbers
    def text_change_1(self):
        first = self.ใส่ก่อน_1.text()
        second = self.ใส่ก่อน_2.text()
        if str(first).isdigit() and str(second).isdigit():
            self.ใส่เลือกก่อน.setText(first if float(first) > float(second) else second)

    # Function to Compare Numbers
    def text_change_2(self):
        first = self.ใส่หลัง_1.text()
        second = self.ใส่หลัง_2.text()
        if str(first).isdigit() and str(second).isdigit():
            self.ใส่เลือกหลัง.setText(first if float(first) > float(second) else second)

    # Function to Update UI
    def update_ui(self):
        strength = Database.get_strength(self.username)
        if strength:
            self.ใส่ก่อน_1.setText(str(strength[2]) if strength[2] else "")
            self.ใส่หลัง_1.setText(str(strength[3]) if strength[3] else "")
            self.ใส่ก่อน_2.setText(str(strength[4]) if strength[4] else "")
            self.ใส่หลัง_2.setText(str(strength[5]) if strength[5] else "")
            self.ใส่เลือกก่อน.setText(str(strength[6]) if strength[6] else "")
            self.ใส่เลือกหลัง.setText(str(strength[7])  if strength[7] else "")

    # Function to Update Excel
    def update_excel(self):
        try:
            message = QMessageBox()
            message.setWindowTitle("แจ้งเตือน")
            message.setIcon(QMessageBox.Icon.Information)
            message.setText("บันทึกไฟล์ %s สำเร็จ" % self.username)
            
            Database.insert_strength(
                self.username, 
                beforeOne = self.ใส่ก่อน_1.text(), 
                afterOne = self.ใส่หลัง_1.text(),
                beforeTwo = self.ใส่ก่อน_2.text(), 
                afterTwo = self.ใส่หลัง_2.text(), 
                beforeBest = self.ใส่เลือกก่อน.text(), 
                afterBest = self.ใส่เลือกหลัง.text()
            )

            workbook = load_workbook(self.path)
            sheet = workbook[self.sheet_name]
            sheet["B3"] = self.ใส่ก่อน_1.text()
            sheet["C3"] = self.ใส่หลัง_1.text()
            sheet["B4"] = self.ใส่ก่อน_2.text()
            sheet["C4"] = self.ใส่หลัง_2.text()
            sheet["B5"] = self.ใส่เลือกก่อน.text()
            sheet["C5"] = self.ใส่เลือกหลัง.text()
            workbook.save(self.path)
            
            message.exec()
            self.close()
        except PermissionError:
            message.setIcon(QMessageBox.Icon.Warning)
            message.setText("โปรดปิดไฟล์ Excel ก่อนบันทึก")
            message.exec()

    # Autocall Function when Window Closed
    def closeEvent(self, event):
        self.signal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Feedback_1_Window("01")
    window.show()
    sys.exit(app.exec())
