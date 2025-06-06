from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QLabel, QFrame, QGridLayout
from PyQt6.QtGui import QFont, QIcon, QDoubleValidator, QKeySequence
from PyQt6.QtCore import Qt, pyqtSignal
from threading import Thread
from openpyxl import load_workbook
import pandas as pd
import sys
from demo_database import Database

font = QFont("Cordia New", 16)

class Feedback_2_Window(QMainWindow):
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
        self.create_text_input()
        self.font_text_input()
        self.alignment_text_input()
        self.validation_text_input()
        self.setting_layout()

        # Update UI
        self.username = username
        self.path = "excel/%s.xlsx" % self.username
        self.sheet_name = "ทดสอบการประเมินทำงาน"
        update_ui = Thread(target=self.update_ui)
        update_ui.start()

    # Function To Create Feedback 1 UI
    def init_ui(self):
        # Create Labels
        self.แบบบันทึกผล = QLabel("แบบบันทึกผลการทดสอบการประเมินทำงานของมือ Jebsen-Taylor Hand Function Test")
        self.งานที่ใช้ = QLabel("งานที่ใช้ในการทดสอบ")
        self.ก่อนเข้าร่วม = QLabel("ก่อนเข้าร่วมโปรแกรมการออกกำลังกาย (นาที)")
        self.หลังเข้าร่วม = QLabel("หลังเข้าร่วมโปรแกรมการออกกำลังกาย 6 สัปดาห์ (นาที)")
        self.แขนซ้าย_1 = QLabel("แขนข้างซ้าย")
        self.แขนขวา_1 = QLabel("แขนข้างขวา")
        self.แขนซ้าย_2 = QLabel("แขนข้างซ้าย")
        self.แขนขวา_2 = QLabel("แขนข้างขวา")
        self.ข้อ1 = QLabel("1.เขียนตัวหนังสือ 1 ประโยค (24 ตัวอักษร)")
        self.ข้อ2 = QLabel("2.กลับการ์ดขนาด 7.6x12.7 ซม")
        self.ข้อ3 = QLabel("3.หยิบของชิ้นเล็ก (เช่น คลิปหนีบกระดาษ เหรียญ \nหรือฝาขวดน้ำ) และนำไปใส่กล่อง")
        self.ข้อ4 = QLabel("4.จำลองการรับประทานอาหาร (เช่น การตักเมล็ดถั่ว\nด้วยช้อน)")
        self.ข้อ5 = QLabel("5.ต่อตัวหมาก (การทดสอบ eye-hand coordination)")
        self.ข้อ6 = QLabel("6.ยกกระป๋องเปล่าขนาดใหญ่")
        self.ข้อ7 = QLabel("7.เคลื่อนกระป๋องที่มีน้ำหนัก 450 กรัม")
        self.button = QPushButton("ตกลง")

        # Setting Button Connect Function
        self.button.clicked.connect(self.update_excel)
        self.button.setShortcut(QKeySequence("Return"))

        # Setting Font
        self.แบบบันทึกผล.setFont(font)
        self.งานที่ใช้.setFont(font)
        self.ก่อนเข้าร่วม.setFont(font)
        self.หลังเข้าร่วม.setFont(font)
        self.แขนซ้าย_1.setFont(font)
        self.แขนขวา_1.setFont(font)
        self.แขนซ้าย_2.setFont(font)
        self.แขนขวา_2.setFont(font)
        self.ข้อ1.setFont(font)
        self.ข้อ2.setFont(font)
        self.ข้อ3.setFont(font)
        self.ข้อ4.setFont(font)
        self.ข้อ5.setFont(font)
        self.ข้อ6.setFont(font)
        self.ข้อ7.setFont(font)
        self.button.setFont(font)

    # Function To Create Text Input
    def create_text_input(self):
        # Create question 1 input
        self.ข้อ1ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ1ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ1ใส่ขวาก่อน = QLineEdit()
        self.ข้อ1ใส่ขวาหลัง = QLineEdit()

        # Create question 2 input
        self.ข้อ2ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ2ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ2ใส่ขวาก่อน = QLineEdit()
        self.ข้อ2ใส่ขวาหลัง = QLineEdit()

        # Create question 3 input
        self.ข้อ3ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ3ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ3ใส่ขวาก่อน = QLineEdit()
        self.ข้อ3ใส่ขวาหลัง = QLineEdit()

        # Create question 4 input
        self.ข้อ4ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ4ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ4ใส่ขวาก่อน = QLineEdit()
        self.ข้อ4ใส่ขวาหลัง = QLineEdit()

        # Create question 5 input
        self.ข้อ5ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ5ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ5ใส่ขวาก่อน = QLineEdit()
        self.ข้อ5ใส่ขวาหลัง = QLineEdit()

        # Create question 6 input
        self.ข้อ6ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ6ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ6ใส่ขวาก่อน = QLineEdit()
        self.ข้อ6ใส่ขวาหลัง = QLineEdit()

        # Create question 7 input
        self.ข้อ7ใส่ซ้ายก่อน = QLineEdit()
        self.ข้อ7ใส่ซ้ายหลัง = QLineEdit()
        self.ข้อ7ใส่ขวาก่อน = QLineEdit()
        self.ข้อ7ใส่ขวาหลัง = QLineEdit()

    # Function To Set Font For Text Input
    def font_text_input(self):
        # Create question 1 input
        self.ข้อ1ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ1ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ1ใส่ขวาก่อน.setFont(font)
        self.ข้อ1ใส่ขวาหลัง.setFont(font)

        # Create question 2 input
        self.ข้อ2ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ2ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ2ใส่ขวาก่อน.setFont(font)
        self.ข้อ2ใส่ขวาหลัง.setFont(font)

        # Create question 3 input
        self.ข้อ3ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ3ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ3ใส่ขวาก่อน.setFont(font)
        self.ข้อ3ใส่ขวาหลัง.setFont(font)

        # Create question 4 input
        self.ข้อ4ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ4ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ4ใส่ขวาก่อน.setFont(font)
        self.ข้อ4ใส่ขวาหลัง.setFont(font)

        # Create question 5 input
        self.ข้อ5ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ5ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ5ใส่ขวาก่อน.setFont(font)
        self.ข้อ5ใส่ขวาหลัง.setFont(font)

        # Create question 6 input
        self.ข้อ6ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ6ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ6ใส่ขวาก่อน.setFont(font)
        self.ข้อ6ใส่ขวาหลัง.setFont(font)

        # Create question 7 input
        self.ข้อ7ใส่ซ้ายก่อน.setFont(font)
        self.ข้อ7ใส่ซ้ายหลัง.setFont(font)
        self.ข้อ7ใส่ขวาก่อน.setFont(font)
        self.ข้อ7ใส่ขวาหลัง.setFont(font)

    # Function To Set Alignment For Text Input
    def alignment_text_input(self):
        # Create question 1 Aligment
        self.ข้อ1ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ1ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ1ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ1ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create question 2 Aligment
        self.ข้อ2ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ2ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ2ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ2ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create question 3 Aligment
        self.ข้อ3ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ3ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ3ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ3ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create question 4 Aligment
        self.ข้อ4ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ4ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ4ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ4ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create question 5 Aligment
        self.ข้อ5ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ5ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ5ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ5ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create question 6 Aligment
        self.ข้อ6ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ6ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ6ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ6ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create question 7 Aligment
        self.ข้อ7ใส่ซ้ายก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ7ใส่ซ้ายหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ7ใส่ขวาก่อน.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ข้อ7ใส่ขวาหลัง.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    # Function To Set Validation For Text Input
    def validation_text_input(self):
        # Create question 1 input
        self.ข้อ1ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ1ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ1ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ1ใส่ขวาหลัง.setValidator(QDoubleValidator())

        # Create question 2 input
        self.ข้อ2ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ2ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ2ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ2ใส่ขวาหลัง.setValidator(QDoubleValidator())

        # Create question 3 input
        self.ข้อ3ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ3ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ3ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ3ใส่ขวาหลัง.setValidator(QDoubleValidator())

        # Create question 4 input
        self.ข้อ4ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ4ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ4ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ4ใส่ขวาหลัง.setValidator(QDoubleValidator())

        # Create question 5 input
        self.ข้อ5ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ5ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ5ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ5ใส่ขวาหลัง.setValidator(QDoubleValidator())

        # Create question 6 input
        self.ข้อ6ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ6ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ6ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ6ใส่ขวาหลัง.setValidator(QDoubleValidator())

        # Create question 7 input
        self.ข้อ7ใส่ซ้ายก่อน.setValidator(QDoubleValidator())
        self.ข้อ7ใส่ซ้ายหลัง.setValidator(QDoubleValidator())
        self.ข้อ7ใส่ขวาก่อน.setValidator(QDoubleValidator())
        self.ข้อ7ใส่ขวาหลัง.setValidator(QDoubleValidator())

    # Function To Setup Layout
    def setting_layout(self):
        # Create Main Layout 
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.แบบบันทึกผล, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Create Grid Layout
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.งานที่ใช้, 0, 0)

        # Create V Line 1
        line_1 = QFrame()
        line_1.setFrameShape(QFrame.Shape.VLine)
        line_1.setFrameShadow(QFrame.Shadow.Sunken)

        # Create V Line 2
        line_2 = QFrame()
        line_2.setFrameShape(QFrame.Shape.VLine)
        line_2.setFrameShadow(QFrame.Shadow.Sunken)

        # Create V Line 3
        line_3 = QFrame()
        line_3.setFrameShape(QFrame.Shape.VLine)
        line_3.setFrameShadow(QFrame.Shadow.Sunken)

        # Create V Line 4
        line_4 = QFrame()
        line_4.setFrameShape(QFrame.Shape.VLine)
        line_4.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 1
        line_h1 = QFrame()
        line_h1.setFrameShape(QFrame.Shape.HLine)
        line_h1.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 2
        line_h2 = QFrame()
        line_h2.setFrameShape(QFrame.Shape.HLine)
        line_h2.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 3
        line_h3 = QFrame()
        line_h3.setFrameShape(QFrame.Shape.HLine)
        line_h3.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 4
        line_h4 = QFrame()
        line_h4.setFrameShape(QFrame.Shape.HLine)
        line_h4.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 5
        line_h5 = QFrame()
        line_h5.setFrameShape(QFrame.Shape.HLine)
        line_h5.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 6
        line_h6 = QFrame()
        line_h6.setFrameShape(QFrame.Shape.HLine)
        line_h6.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 7
        line_h7 = QFrame()
        line_h7.setFrameShape(QFrame.Shape.HLine)
        line_h7.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 8
        line_h8 = QFrame()
        line_h8.setFrameShape(QFrame.Shape.HLine)
        line_h8.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line 9
        line_h9 = QFrame()
        line_h9.setFrameShape(QFrame.Shape.HLine)
        line_h9.setFrameShadow(QFrame.Shadow.Sunken)

        # 1st Row
        grid_layout.addWidget(line_1, 0, 1, 20, 1)
        grid_layout.addWidget(self.ก่อนเข้าร่วม, 0, 2, 1, 3)
        grid_layout.addWidget(line_2, 0, 5, 20, 1)
        grid_layout.addWidget(self.หลังเข้าร่วม, 0, 6, 1, 3)

        # 2nd Horizontal Line
        grid_layout.addWidget(line_h1, 1, 1, 1, 9)

        # 3rd Row
        grid_layout.addWidget(self.แขนซ้าย_1, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_3, 2, 3, 18, 1)
        grid_layout.addWidget(self.แขนขวา_1, 2, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.แขนซ้าย_2, 2, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_4, 2, 7, 18, 1)
        grid_layout.addWidget(self.แขนขวา_2, 2, 8, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 4th Horizontal Line
        grid_layout.addWidget(line_h2, 3, 0, 1, 10)

        # 5th Row
        grid_layout.addWidget(self.ข้อ1, 4, 0)
        grid_layout.addWidget(self.ข้อ1ใส่ซ้ายก่อน, 4, 2)
        grid_layout.addWidget(self.ข้อ1ใส่ขวาก่อน, 4, 4)
        grid_layout.addWidget(self.ข้อ1ใส่ซ้ายหลัง, 4, 6)
        grid_layout.addWidget(self.ข้อ1ใส่ขวาหลัง, 4, 8)

        # 6th Horizontal Line
        grid_layout.addWidget(line_h3, 5, 0, 1, 10)

        # 7th Row
        grid_layout.addWidget(self.ข้อ2, 6, 0)
        grid_layout.addWidget(self.ข้อ2ใส่ซ้ายก่อน, 6, 2)
        grid_layout.addWidget(self.ข้อ2ใส่ขวาก่อน, 6, 4)
        grid_layout.addWidget(self.ข้อ2ใส่ซ้ายหลัง, 6, 6)
        grid_layout.addWidget(self.ข้อ2ใส่ขวาหลัง, 6, 8)

        # 8th Horizontal Line
        grid_layout.addWidget(line_h4, 7, 0, 1, 10)

        # 9th Row
        grid_layout.addWidget(self.ข้อ3, 8, 0)
        grid_layout.addWidget(self.ข้อ3ใส่ซ้ายก่อน, 8, 2)
        grid_layout.addWidget(self.ข้อ3ใส่ขวาก่อน, 8, 4)
        grid_layout.addWidget(self.ข้อ3ใส่ซ้ายหลัง, 8, 6)
        grid_layout.addWidget(self.ข้อ3ใส่ขวาหลัง, 8, 8)

        # 10th Horizontal Line
        grid_layout.addWidget(line_h5, 9, 0, 1, 10)

        # 11th Row
        grid_layout.addWidget(self.ข้อ4, 10, 0)
        grid_layout.addWidget(self.ข้อ4ใส่ซ้ายก่อน, 10, 2)
        grid_layout.addWidget(self.ข้อ4ใส่ขวาก่อน, 10, 4)
        grid_layout.addWidget(self.ข้อ4ใส่ซ้ายหลัง, 10, 6)
        grid_layout.addWidget(self.ข้อ4ใส่ขวาหลัง, 10, 8)

        # 12th Horizontal Line
        grid_layout.addWidget(line_h6, 11, 0, 1, 10)

        # 13th Row
        grid_layout.addWidget(self.ข้อ5, 12, 0)
        grid_layout.addWidget(self.ข้อ5ใส่ซ้ายก่อน, 12, 2)
        grid_layout.addWidget(self.ข้อ5ใส่ขวาก่อน, 12, 4)
        grid_layout.addWidget(self.ข้อ5ใส่ซ้ายหลัง, 12, 6)
        grid_layout.addWidget(self.ข้อ5ใส่ขวาหลัง, 12, 8)

        # 14th Horizontal Line
        grid_layout.addWidget(line_h7, 13, 0, 1, 10)

        # 15th Row
        grid_layout.addWidget(self.ข้อ6, 14, 0)
        grid_layout.addWidget(self.ข้อ6ใส่ซ้ายก่อน, 14, 2)
        grid_layout.addWidget(self.ข้อ6ใส่ขวาก่อน, 14, 4)
        grid_layout.addWidget(self.ข้อ6ใส่ซ้ายหลัง, 14, 6)
        grid_layout.addWidget(self.ข้อ6ใส่ขวาหลัง, 14, 8)

        # 16th Horizontal Line
        grid_layout.addWidget(line_h8, 15, 0, 1, 10)

        # 17th Row
        grid_layout.addWidget(self.ข้อ7, 16, 0)
        grid_layout.addWidget(self.ข้อ7ใส่ซ้ายก่อน, 16, 2)
        grid_layout.addWidget(self.ข้อ7ใส่ขวาก่อน, 16, 4)
        grid_layout.addWidget(self.ข้อ7ใส่ซ้ายหลัง, 16, 6)
        grid_layout.addWidget(self.ข้อ7ใส่ขวาหลัง, 16, 8)

        main_layout.addLayout(grid_layout)
        main_layout.addWidget(self.button)
        main_layout.addStretch(1)

        # Set Layout
        self.widget.setLayout(main_layout)

    # Function to Update UI
    def update_ui(self):
        # if self.username is not None:
        #     df = pd.read_excel(self.path, sheet_name=self.sheet_name)

        #     # Create question 1 input
        #     self.ข้อ1ใส่ซ้ายก่อน.setText(str(df.iloc[2, 1]) if not pd.isna(df.iloc[2, 1]) else "")
        #     self.ข้อ1ใส่ขวาก่อน.setText(str(df.iloc[2, 2]) if not pd.isna(df.iloc[2, 2]) else "")
        #     self.ข้อ1ใส่ซ้ายหลัง.setText(str(df.iloc[2, 3]) if not pd.isna(df.iloc[2, 3]) else "")
        #     self.ข้อ1ใส่ขวาหลัง.setText(str(df.iloc[2, 4]) if not pd.isna(df.iloc[2, 4]) else "")

        #     # Create question 2 input
        #     self.ข้อ2ใส่ซ้ายก่อน.setText(str(df.iloc[3, 1]) if not pd.isna(df.iloc[3, 1]) else "")
        #     self.ข้อ2ใส่ขวาก่อน.setText(str(df.iloc[3, 2]) if not pd.isna(df.iloc[3, 2]) else "")
        #     self.ข้อ2ใส่ซ้ายหลัง.setText(str(df.iloc[3, 3]) if not pd.isna(df.iloc[3, 3]) else "")
        #     self.ข้อ2ใส่ขวาหลัง.setText(str(df.iloc[3, 4]) if not pd.isna(df.iloc[3, 4]) else "")

        #     # Create question 3 input
        #     self.ข้อ3ใส่ซ้ายก่อน.setText(str(df.iloc[4, 1]) if not pd.isna(df.iloc[4, 1]) else "")
        #     self.ข้อ3ใส่ขวาก่อน.setText(str(df.iloc[4, 2]) if not pd.isna(df.iloc[4, 2]) else "")
        #     self.ข้อ3ใส่ซ้ายหลัง.setText(str(df.iloc[4, 3]) if not pd.isna(df.iloc[4, 3]) else "")
        #     self.ข้อ3ใส่ขวาหลัง.setText(str(df.iloc[4, 4]) if not pd.isna(df.iloc[4, 4]) else "")

        #     # Create question 4 input
        #     self.ข้อ4ใส่ซ้ายก่อน.setText(str(df.iloc[5, 1]) if not pd.isna(df.iloc[5, 1]) else "")
        #     self.ข้อ4ใส่ขวาก่อน.setText(str(df.iloc[5, 2]) if not pd.isna(df.iloc[5, 2]) else "")
        #     self.ข้อ4ใส่ซ้ายหลัง.setText(str(df.iloc[5, 3]) if not pd.isna(df.iloc[5, 3]) else "")
        #     self.ข้อ4ใส่ขวาหลัง.setText(str(df.iloc[5, 4]) if not pd.isna(df.iloc[5, 4]) else "")

        #     # Create question 5 input
        #     self.ข้อ5ใส่ซ้ายก่อน.setText(str(df.iloc[6, 1]) if not pd.isna(df.iloc[6, 1]) else "")
        #     self.ข้อ5ใส่ขวาก่อน.setText(str(df.iloc[6, 2]) if not pd.isna(df.iloc[6, 2]) else "")
        #     self.ข้อ5ใส่ซ้ายหลัง.setText(str(df.iloc[6, 3]) if not pd.isna(df.iloc[6, 3]) else "")
        #     self.ข้อ5ใส่ขวาหลัง.setText(str(df.iloc[6, 4]) if not pd.isna(df.iloc[6, 4]) else "")

        #     # Create question 6 input
        #     self.ข้อ6ใส่ซ้ายก่อน.setText(str(df.iloc[7, 1]) if not pd.isna(df.iloc[7, 1]) else "")
        #     self.ข้อ6ใส่ขวาก่อน.setText(str(df.iloc[7, 2]) if not pd.isna(df.iloc[7, 2]) else "")
        #     self.ข้อ6ใส่ซ้ายหลัง.setText(str(df.iloc[7, 3]) if not pd.isna(df.iloc[7, 3]) else "")
        #     self.ข้อ6ใส่ขวาหลัง.setText(str(df.iloc[7, 4]) if not pd.isna(df.iloc[7, 4]) else "")

        #     # Create question 7 input
        #     self.ข้อ7ใส่ซ้ายก่อน.setText(str(df.iloc[8, 1]) if not pd.isna(df.iloc[8, 1]) else "")
        #     self.ข้อ7ใส่ขวาก่อน.setText(str(df.iloc[8, 2]) if not pd.isna(df.iloc[8, 2]) else "")
        #     self.ข้อ7ใส่ซ้ายหลัง.setText(str(df.iloc[8, 3]) if not pd.isna(df.iloc[8, 3]) else "")
        #     self.ข้อ7ใส่ขวาหลัง.setText(str(df.iloc[8, 4]) if not pd.isna(df.iloc[8, 4]) else "")

        process = Database.get_process(self.username)
        if process:
            # Create question 1 input
            self.ข้อ1ใส่ซ้ายก่อน.setText(str(process[2]) if process[2] else "")
            self.ข้อ1ใส่ขวาก่อน.setText(str(process[3]) if process[3] else "")
            self.ข้อ1ใส่ซ้ายหลัง.setText(str(process[4]) if process[4] else "")
            self.ข้อ1ใส่ขวาหลัง.setText(str(process[5]) if process[5] else "")

            # Create question 2 input
            self.ข้อ2ใส่ซ้ายก่อน.setText(str(process[6]) if process[6] else "")
            self.ข้อ2ใส่ขวาก่อน.setText(str(process[7]) if process[7] else "")
            self.ข้อ2ใส่ซ้ายหลัง.setText(str(process[8]) if process[8] else "")
            self.ข้อ2ใส่ขวาหลัง.setText(str(process[9]) if process[9] else "")

            # Create question 3 input
            self.ข้อ3ใส่ซ้ายก่อน.setText(str(process[10]) if process[10] else "")
            self.ข้อ3ใส่ขวาก่อน.setText(str(process[11]) if process[11] else "")
            self.ข้อ3ใส่ซ้ายหลัง.setText(str(process[12]) if process[12] else "")
            self.ข้อ3ใส่ขวาหลัง.setText(str(process[13]) if process[13] else "")

            # Create question 4 input
            self.ข้อ4ใส่ซ้ายก่อน.setText(str(process[14]) if process[14] else "")
            self.ข้อ4ใส่ขวาก่อน.setText(str(process[15]) if process[15] else "")
            self.ข้อ4ใส่ซ้ายหลัง.setText(str(process[16]) if process[16] else "")
            self.ข้อ4ใส่ขวาหลัง.setText(str(process[17]) if process[17] else "")

            # Create question 5 input
            self.ข้อ5ใส่ซ้ายก่อน.setText(str(process[18]) if process[18] else "")
            self.ข้อ5ใส่ขวาก่อน.setText(str(process[19]) if process[19] else "")
            self.ข้อ5ใส่ซ้ายหลัง.setText(str(process[20]) if process[20] else "")
            self.ข้อ5ใส่ขวาหลัง.setText(str(process[21]) if process[21] else "")

            # Create question 6 input
            self.ข้อ6ใส่ซ้ายก่อน.setText(str(process[22]) if process[22] else "")
            self.ข้อ6ใส่ขวาก่อน.setText(str(process[23]) if process[23] else "")
            self.ข้อ6ใส่ซ้ายหลัง.setText(str(process[24]) if process[24] else "")
            self.ข้อ6ใส่ขวาหลัง.setText(str(process[25]) if process[25] else "")

            # Create question 7 input
            self.ข้อ7ใส่ซ้ายก่อน.setText(str(process[26]) if process[26] else "")
            self.ข้อ7ใส่ขวาก่อน.setText(str(process[27]) if process[27] else "")
            self.ข้อ7ใส่ซ้ายหลัง.setText(str(process[28]) if process[28] else "")
            self.ข้อ7ใส่ขวาหลัง.setText(str(process[29]) if process[29] else "")

    # Function to Update Excel
    def update_excel(self):
        try:
            message = QMessageBox()
            message.setWindowTitle("แจ้งเตือน")
            message.setIcon(QMessageBox.Icon.Information)
            message.setText("บันทึกไฟล์ %s สำเร็จ" % self.username)
            
            Database.insert_process(
                self.username,

                oneBeforeLeft = self.ข้อ1ใส่ซ้ายก่อน.text(),
                oneBeforeRight = self.ข้อ1ใส่ขวาก่อน.text(),
                oneAfterLeft = self.ข้อ1ใส่ซ้ายหลัง.text(),
                oneAfterRight = self.ข้อ1ใส่ขวาหลัง.text(),

                twoBeforeLeft = self.ข้อ2ใส่ซ้ายก่อน.text(),
                twoBeforeRight = self.ข้อ2ใส่ขวาก่อน.text(),
                twoAfterLeft = self.ข้อ2ใส่ซ้ายหลัง.text(),
                twoAfterRight = self.ข้อ2ใส่ขวาหลัง.text(),

                threeBeforeLeft = self.ข้อ3ใส่ซ้ายก่อน.text(),
                threeBeforeRight = self.ข้อ3ใส่ขวาก่อน.text(),
                threeAfterLeft = self.ข้อ3ใส่ซ้ายหลัง.text(),
                threeAfterRight = self.ข้อ3ใส่ขวาหลัง.text(),

                fourBeforeLeft = self.ข้อ4ใส่ซ้ายก่อน.text(),
                fourBeforeRight = self.ข้อ4ใส่ขวาก่อน.text(),
                fourAfterLeft = self.ข้อ4ใส่ซ้ายหลัง.text(),
                fourAfterRight = self.ข้อ4ใส่ขวาหลัง.text(),

                fiveBeforeLeft = self.ข้อ5ใส่ซ้ายก่อน.text(),
                fiveBeforeRight = self.ข้อ5ใส่ขวาก่อน.text(),
                fiveAfterLeft = self.ข้อ5ใส่ซ้ายหลัง.text(),
                fiveAfterRight = self.ข้อ5ใส่ขวาหลัง.text(),

                sixBeforeLeft = self.ข้อ6ใส่ซ้ายก่อน.text(),
                sixBeforeRight = self.ข้อ6ใส่ขวาก่อน.text(),
                sixAfterLeft = self.ข้อ6ใส่ซ้ายหลัง.text(),
                sixAfterRight = self.ข้อ6ใส่ขวาหลัง.text(),

                sevenBeforeLeft = self.ข้อ7ใส่ซ้ายก่อน.text(),
                sevenBeforeRight = self.ข้อ7ใส่ขวาก่อน.text(),
                sevenAfterLeft = self.ข้อ7ใส่ซ้ายหลัง.text(),
                sevenAfterRight = self.ข้อ7ใส่ขวาหลัง.text(),
            )

            workbook = load_workbook(self.path)
            sheet = workbook[self.sheet_name]
            sheet["B4"] = self.ข้อ1ใส่ซ้ายก่อน.text()
            sheet["C4"] = self.ข้อ1ใส่ขวาก่อน.text()
            sheet["D4"] = self.ข้อ1ใส่ซ้ายหลัง.text()
            sheet["E4"] = self.ข้อ1ใส่ขวาหลัง.text()

            sheet["B5"] = self.ข้อ2ใส่ซ้ายก่อน.text()
            sheet["C5"] = self.ข้อ2ใส่ขวาก่อน.text()
            sheet["D5"] = self.ข้อ2ใส่ซ้ายหลัง.text()
            sheet["E5"] = self.ข้อ2ใส่ขวาหลัง.text()

            sheet["B6"] = self.ข้อ3ใส่ซ้ายก่อน.text()
            sheet["C6"] = self.ข้อ3ใส่ขวาก่อน.text()
            sheet["D6"] = self.ข้อ3ใส่ซ้ายหลัง.text()
            sheet["E6"] = self.ข้อ3ใส่ขวาหลัง.text()

            sheet["B7"] = self.ข้อ4ใส่ซ้ายก่อน.text()
            sheet["C7"] = self.ข้อ4ใส่ขวาก่อน.text()
            sheet["D7"] = self.ข้อ4ใส่ซ้ายหลัง.text()
            sheet["E7"] = self.ข้อ4ใส่ขวาหลัง.text()

            sheet["B8"] = self.ข้อ5ใส่ซ้ายก่อน.text()
            sheet["C8"] = self.ข้อ5ใส่ขวาก่อน.text()
            sheet["D8"] = self.ข้อ5ใส่ซ้ายหลัง.text()
            sheet["E8"] = self.ข้อ5ใส่ขวาหลัง.text()

            sheet["B9"] = self.ข้อ6ใส่ซ้ายก่อน.text()
            sheet["C9"] = self.ข้อ6ใส่ขวาก่อน.text()
            sheet["D9"] = self.ข้อ6ใส่ซ้ายหลัง.text()
            sheet["E9"] = self.ข้อ6ใส่ขวาหลัง.text()

            sheet["B10"] = self.ข้อ7ใส่ซ้ายก่อน.text()
            sheet["C10"] = self.ข้อ7ใส่ขวาก่อน.text()
            sheet["D10"] = self.ข้อ7ใส่ซ้ายหลัง.text()
            sheet["E10"] = self.ข้อ7ใส่ขวาหลัง.text()

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
    window = Feedback_2_Window("01")
    window.show()
    sys.exit(app.exec())