from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, QMessageBox, QVBoxLayout, QPushButton, QLabel, QFrame, QGridLayout
from PyQt6.QtGui import QFont, QIcon, QKeySequence
from PyQt6.QtCore import Qt, pyqtSignal
from openpyxl import load_workbook
from threading import Thread
import pandas as pd
import numpy as np
import sys
from demo_database import Database

font = QFont("Cordia New", 14)

class Feedback_3_Window(QMainWindow):
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
        self.create_inputs()
        self.font_inputs()
        self.setting_function()
        self.setting_layout()

        # Update UI
        self.username = username
        self.path = "excel/%s.xlsx" % self.username
        self.sheet_name = "ความพึงพอใจ"
        update_ui = Thread(target=self.update_ui)
        update_ui.start()

        self.setGeometry(400, 25, 800, 800)

    # Function To Create Feedback 1 UI
    def init_ui(self):
        # Create Labels
        self.แบบประเมิน = QLabel("ตารางบันทึกผลทดสอบการใช้งานและความพึงพอใจของการใช้ถุงมือสัมผัสเทียม\n(ประเมินหลังสิ้นสุดโปรแกรมการออกกำลังกล้ามเนื้อมือ 6 สัปดาห์)")
        self.หัวข้อ = QLabel("หัวข้อ")
        self.คำถาม = QLabel("คำถาม")
        self.ไม่เห็นด้วยอย่างยิ่ง = QLabel("ไม่เห็นด้วยอย่างยิ่ง (1)")
        self.ไม่เห็นด้วย = QLabel("ไม่เห็นด้วย (2)")
        self.ไม่แน่ใจ = QLabel("ไม่แน่ใจ (3)")
        self.เห็นด้วย = QLabel("เห็นด้วย (4)")
        self.เห็นด้วยอย่างยิ่ง = QLabel("เห็นด้วยอย่างยิ่ง (5)")
        self.ข้อ1 = QLabel("1")
        self.ข้อ2 = QLabel("2")
        self.ข้อ3 = QLabel("3")
        self.ข้อ4 = QLabel("4")
        self.ข้อ5 = QLabel("5")
        self.ข้อ6 = QLabel("6")
        self.ข้อ7 = QLabel("7")
        self.ข้อ8 = QLabel("8")
        self.ข้อ9 = QLabel("9")
        self.ข้อ10 = QLabel("10")
        self.คำถาม1 = QLabel("ฉันคิดว่าฉันต้องการใช้ถุงมือนี้บ่อย ๆ")
        self.คำถาม2 = QLabel("ฉันคิดว่าถุงมือนี้มีความซับซ้อน (ใน\nการใช้งาน) โดยไม่จำเป็น")
        self.คำถาม3 = QLabel("ฉันคิดว่าถุงมือนี้ใช้ง่าย")
        self.คำถาม4 = QLabel("ฉันต้องคิดว่าต้องได้รับความช่วยเหลือ\nจึงจะสามารถใช้ถุงมือนี้ได้")
        self.คำถาม5 = QLabel("ฉันพบว่ามีหลายฟังก์ชันที่ทำงานได้ดี")
        self.คำถาม6 = QLabel("ฉันคิดว่าฟังก์ชันการทำงานของถุงมือนี้\nไม่สอดคล้องกัน")
        self.คำถาม7 = QLabel("ฉันคิดว่าคนส่วนใหญ่จะสามารถเรียนรู้\nการใช้งานถุงมือนี้ได้อย่าง\nรวดเร็ว")
        self.คำถาม8 = QLabel("ฉันพบว่าการใช้งานถุงมือนี้ยุ่งยากซับซ้อน")
        self.คำถาม9 = QLabel("ฉันจำเป็นต้องเรียนรู้หลายสิ่งก่อน\nจึงจะสามารถใช้งานถุงมือนี้ได้")
        self.คำถาม10 = QLabel("ฉันจำเป็นต้องเรียนรู้หลายสิ่งก่อน\nจึงจะสามารถใช้งานถุงมือนี้ได้")
        self.total1 = QLabel("")
        self.total2 = QLabel("")
        self.total3 = QLabel("")
        self.total4 = QLabel("")
        self.total5 = QLabel("")
        self.รวม = QLabel("รวม")
        self.button = QPushButton("ตกลง")

        # Setting Button Connect Funcion
        self.button.clicked.connect(self.update_excel)
        self.button.setShortcut(QKeySequence("Return"))

        # Setting Font
        self.แบบประเมิน.setFont(font)
        self.หัวข้อ.setFont(font)
        self.คำถาม.setFont(font)
        self.ไม่เห็นด้วยอย่างยิ่ง.setFont(font)
        self.ไม่เห็นด้วย.setFont(font)
        self.ไม่แน่ใจ.setFont(font)
        self.เห็นด้วย.setFont(font)
        self.เห็นด้วยอย่างยิ่ง.setFont(font)
        self.ข้อ1.setFont(font)
        self.ข้อ2.setFont(font)
        self.ข้อ3.setFont(font)
        self.ข้อ4.setFont(font)
        self.ข้อ5.setFont(font)
        self.ข้อ6.setFont(font)
        self.ข้อ7.setFont(font)
        self.ข้อ8.setFont(font)
        self.ข้อ9.setFont(font)
        self.ข้อ10.setFont(font)
        self.คำถาม1.setFont(font)
        self.คำถาม2.setFont(font)
        self.คำถาม3.setFont(font)
        self.คำถาม4.setFont(font)
        self.คำถาม5.setFont(font)
        self.คำถาม6.setFont(font)
        self.คำถาม7.setFont(font)
        self.คำถาม8.setFont(font)
        self.คำถาม9.setFont(font)
        self.คำถาม10.setFont(font)
        self.รวม.setFont(font)
        self.total1.setFont(font)
        self.total2.setFont(font)
        self.total3.setFont(font)
        self.total4.setFont(font)
        self.total5.setFont(font)
        self.button.setFont(font)

        # Set Alignment
        self.แบบประเมิน.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    # Function To Create Input
    def create_inputs(self):
        # Create Checkboxes 1
        self.num1_1 = QCheckBox()
        self.num1_2 = QCheckBox()
        self.num1_3 = QCheckBox()
        self.num1_4 = QCheckBox()
        self.num1_5 = QCheckBox()

        # Create Checkboxes 2
        self.num2_1 = QCheckBox()
        self.num2_2 = QCheckBox()
        self.num2_3 = QCheckBox()
        self.num2_4 = QCheckBox()
        self.num2_5 = QCheckBox()

        # Create Checkboxes 3
        self.num3_1 = QCheckBox()
        self.num3_2 = QCheckBox()
        self.num3_3 = QCheckBox()
        self.num3_4 = QCheckBox()
        self.num3_5 = QCheckBox()

        # Create Checkboxes 4
        self.num4_1 = QCheckBox()
        self.num4_2 = QCheckBox()
        self.num4_3 = QCheckBox()
        self.num4_4 = QCheckBox()
        self.num4_5 = QCheckBox()

        # Create Checkboxes 5
        self.num5_1 = QCheckBox()
        self.num5_2 = QCheckBox()
        self.num5_3 = QCheckBox()
        self.num5_4 = QCheckBox()
        self.num5_5 = QCheckBox()

        # Create Checkboxes 6
        self.num6_1 = QCheckBox()
        self.num6_2 = QCheckBox()
        self.num6_3 = QCheckBox()
        self.num6_4 = QCheckBox()
        self.num6_5 = QCheckBox()

        # Create Checkboxes 7
        self.num7_1 = QCheckBox()
        self.num7_2 = QCheckBox()
        self.num7_3 = QCheckBox()
        self.num7_4 = QCheckBox()
        self.num7_5 = QCheckBox()

        # Create Checkboxes 8
        self.num8_1 = QCheckBox()
        self.num8_2 = QCheckBox()
        self.num8_3 = QCheckBox()
        self.num8_4 = QCheckBox()
        self.num8_5 = QCheckBox()

        # Create Checkboxes 9
        self.num9_1 = QCheckBox()
        self.num9_2 = QCheckBox()
        self.num9_3 = QCheckBox()
        self.num9_4 = QCheckBox()
        self.num9_5 = QCheckBox()

        # Create Checkboxes 10
        self.num10_1 = QCheckBox()
        self.num10_2 = QCheckBox()
        self.num10_3 = QCheckBox()
        self.num10_4 = QCheckBox()
        self.num10_5 = QCheckBox()
        
    # Function To Set Font For Each Inputs
    def font_inputs(self):
        # Set Font For Checkboxes 1
        self.num1_1.setFont(font)
        self.num1_2.setFont(font)
        self.num1_3.setFont(font)
        self.num1_4.setFont(font)
        self.num1_5.setFont(font)

        # Set Font For Checkboxes 2
        self.num2_1.setFont(font)
        self.num2_2.setFont(font)
        self.num2_3.setFont(font)
        self.num2_4.setFont(font)
        self.num2_5.setFont(font)

        # Set Font For Checkboxes 3
        self.num3_1.setFont(font)
        self.num3_2.setFont(font)
        self.num3_3.setFont(font)
        self.num3_4.setFont(font)
        self.num3_5.setFont(font)

        # Set Font For Checkboxes 4
        self.num4_1.setFont(font)
        self.num4_2.setFont(font)
        self.num4_3.setFont(font)
        self.num4_4.setFont(font)
        self.num4_5.setFont(font)

        # Set Font For Checkboxes 5
        self.num5_1.setFont(font)
        self.num5_2.setFont(font)
        self.num5_3.setFont(font)
        self.num5_4.setFont(font)
        self.num5_5.setFont(font)

        # Set Font For Checkboxes 6
        self.num6_1.setFont(font)
        self.num6_2.setFont(font)
        self.num6_3.setFont(font)
        self.num6_4.setFont(font)
        self.num6_5.setFont(font)

        # Set Font For Checkboxes 7
        self.num7_1.setFont(font)
        self.num7_2.setFont(font)
        self.num7_3.setFont(font)
        self.num7_4.setFont(font)
        self.num7_5.setFont(font)

        # Set Font For Checkboxes 8
        self.num8_1.setFont(font)
        self.num8_2.setFont(font)
        self.num8_3.setFont(font)
        self.num8_4.setFont(font)
        self.num8_5.setFont(font)

        # Set Font For Checkboxes 9
        self.num9_1.setFont(font)
        self.num9_2.setFont(font)
        self.num9_3.setFont(font)
        self.num9_4.setFont(font)
        self.num9_5.setFont(font)

        # Set Font For Checkboxes 10
        self.num10_1.setFont(font)
        self.num10_2.setFont(font)
        self.num10_3.setFont(font)
        self.num10_4.setFont(font)
        self.num10_5.setFont(font)

    # Function to Set Callback
    def setting_function(self):
        # Set Callback For Checkboxes 1
        self.num1_1.stateChanged.connect(self.check_1_1)
        self.num1_2.stateChanged.connect(self.check_1_2)
        self.num1_3.stateChanged.connect(self.check_1_3)
        self.num1_4.stateChanged.connect(self.check_1_4)
        self.num1_5.stateChanged.connect(self.check_1_5)

        # Set Callback For Checkboxes 2
        self.num2_1.stateChanged.connect(self.check_2_1)
        self.num2_2.stateChanged.connect(self.check_2_2)
        self.num2_3.stateChanged.connect(self.check_2_3)
        self.num2_4.stateChanged.connect(self.check_2_4)
        self.num2_5.stateChanged.connect(self.check_2_5)

        # Set Callback For Checkboxes 3
        self.num3_1.stateChanged.connect(self.check_3_1)
        self.num3_2.stateChanged.connect(self.check_3_2)
        self.num3_3.stateChanged.connect(self.check_3_3)
        self.num3_4.stateChanged.connect(self.check_3_4)
        self.num3_5.stateChanged.connect(self.check_3_5)

        # Set Callback For Checkboxes 4
        self.num4_1.stateChanged.connect(self.check_4_1)
        self.num4_2.stateChanged.connect(self.check_4_2)
        self.num4_3.stateChanged.connect(self.check_4_3)
        self.num4_4.stateChanged.connect(self.check_4_4)
        self.num4_5.stateChanged.connect(self.check_4_5)

        # Set Callback For Checkboxes 5
        self.num5_1.stateChanged.connect(self.check_5_1)
        self.num5_2.stateChanged.connect(self.check_5_2)
        self.num5_3.stateChanged.connect(self.check_5_3)
        self.num5_4.stateChanged.connect(self.check_5_4)
        self.num5_5.stateChanged.connect(self.check_5_5)

        # Set Callback For Checkboxes 6
        self.num6_1.stateChanged.connect(self.check_6_1)
        self.num6_2.stateChanged.connect(self.check_6_2)
        self.num6_3.stateChanged.connect(self.check_6_3)
        self.num6_4.stateChanged.connect(self.check_6_4)
        self.num6_5.stateChanged.connect(self.check_6_5)

        # Set Callback For Checkboxes 7
        self.num7_1.stateChanged.connect(self.check_7_1)
        self.num7_2.stateChanged.connect(self.check_7_2)
        self.num7_3.stateChanged.connect(self.check_7_3)
        self.num7_4.stateChanged.connect(self.check_7_4)
        self.num7_5.stateChanged.connect(self.check_7_5)

        # Set Callback For Checkboxes 8
        self.num8_1.stateChanged.connect(self.check_8_1)
        self.num8_2.stateChanged.connect(self.check_8_2)
        self.num8_3.stateChanged.connect(self.check_8_3)
        self.num8_4.stateChanged.connect(self.check_8_4)
        self.num8_5.stateChanged.connect(self.check_8_5)

        # Set Callback For Checkboxes 9
        self.num9_1.stateChanged.connect(self.check_9_1)
        self.num9_2.stateChanged.connect(self.check_9_2)
        self.num9_3.stateChanged.connect(self.check_9_3)
        self.num9_4.stateChanged.connect(self.check_9_4)
        self.num9_5.stateChanged.connect(self.check_9_5)

        # Set Callback For Checkboxes 10
        self.num10_1.stateChanged.connect(self.check_10_1)
        self.num10_2.stateChanged.connect(self.check_10_2)
        self.num10_3.stateChanged.connect(self.check_10_3)
        self.num10_4.stateChanged.connect(self.check_10_4)
        self.num10_5.stateChanged.connect(self.check_10_5)

    # Function To Set Layout
    def setting_layout(self):
        # Create Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.แบบประเมิน, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Create Grid Layout
        grid_layout = QGridLayout()

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

        # Create V Line 5
        line_5 = QFrame()
        line_5.setFrameShape(QFrame.Shape.VLine)
        line_5.setFrameShadow(QFrame.Shadow.Sunken)

        # Create V Line 6
        line_6 = QFrame()
        line_6.setFrameShape(QFrame.Shape.VLine)
        line_6.setFrameShadow(QFrame.Shadow.Sunken)
        
        # Create H Line1
        line_h1 = QFrame()
        line_h1.setFrameShape(QFrame.Shape.HLine)
        line_h1.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line2
        line_h2 = QFrame()
        line_h2.setFrameShape(QFrame.Shape.HLine)
        line_h2.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line3
        line_h3 = QFrame()
        line_h3.setFrameShape(QFrame.Shape.HLine)
        line_h3.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line4
        line_h4 = QFrame()
        line_h4.setFrameShape(QFrame.Shape.HLine)
        line_h4.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line5
        line_h5 = QFrame()
        line_h5.setFrameShape(QFrame.Shape.HLine)
        line_h5.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line6
        line_h6 = QFrame()
        line_h6.setFrameShape(QFrame.Shape.HLine)
        line_h6.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line7
        line_h7 = QFrame()
        line_h7.setFrameShape(QFrame.Shape.HLine)
        line_h7.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line8
        line_h8 = QFrame()
        line_h8.setFrameShape(QFrame.Shape.HLine)
        line_h8.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line9
        line_h9 = QFrame()
        line_h9.setFrameShape(QFrame.Shape.HLine)
        line_h9.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line10
        line_h10 = QFrame()
        line_h10.setFrameShape(QFrame.Shape.HLine)
        line_h10.setFrameShadow(QFrame.Shadow.Sunken)

        # Create H Line11
        line_h11 = QFrame()
        line_h11.setFrameShape(QFrame.Shape.HLine)
        line_h11.setFrameShadow(QFrame.Shadow.Sunken)

        # 1st Row
        grid_layout.addWidget(self.หัวข้อ, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_1, 0, 1, 23, 1)
        grid_layout.addWidget(self.คำถาม, 0, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_2, 0, 3, 23, 1)
        grid_layout.addWidget(self.ไม่เห็นด้วยอย่างยิ่ง, 0, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_3, 0, 5, 23, 1)
        grid_layout.addWidget(self.ไม่เห็นด้วย, 0, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_4, 0, 7, 23, 1)
        grid_layout.addWidget(self.ไม่แน่ใจ, 0, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_5, 0, 9, 23, 1)
        grid_layout.addWidget(self.เห็นด้วย, 0, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(line_6, 0, 11, 23, 1)
        grid_layout.addWidget(self.เห็นด้วยอย่างยิ่ง, 0 ,12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 2nd Row
        grid_layout.addWidget(line_h1, 1, 0, 1, 15)

        # 3rd Row
        grid_layout.addWidget(self.ข้อ1, 2, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม1, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num1_1, 2, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num1_2, 2, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num1_3, 2, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num1_4, 2, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num1_5, 2, 12, alignment=Qt.AlignmentFlag.AlignHCenter)


        # 4th Row
        grid_layout.addWidget(line_h2, 3, 0, 1, 15)

        # 5th Row
        grid_layout.addWidget(self.ข้อ2, 4, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม2, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num2_1, 4, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num2_2, 4, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num2_3, 4, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num2_4, 4, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num2_5, 4, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 6th Row
        grid_layout.addWidget(line_h3, 5, 0, 1, 15)

        # 7th Row
        grid_layout.addWidget(self.ข้อ3, 6, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม3, 6, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num3_1, 6, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num3_2, 6, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num3_3, 6, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num3_4, 6, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num3_5, 6, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 8th Row
        grid_layout.addWidget(line_h4, 7, 0, 1, 15)

        # 9th Row
        grid_layout.addWidget(self.ข้อ4, 8, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม4, 8, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num4_1, 8, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num4_2, 8, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num4_3, 8, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num4_4, 8, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num4_5, 8, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 10th Row
        grid_layout.addWidget(line_h5, 9, 0, 1, 15)

        # 11th Row
        grid_layout.addWidget(self.ข้อ5, 10, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม5, 10, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num5_1, 10, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num5_2, 10, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num5_3, 10, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num5_4, 10, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num5_5, 10, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 12th Row
        grid_layout.addWidget(line_h6, 11, 0, 1, 15)

        # 13th Row
        grid_layout.addWidget(self.ข้อ6, 12, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม6, 12, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num6_1, 12, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num6_2, 12, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num6_3, 12, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num6_4, 12, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num6_5, 12, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 14th Row
        grid_layout.addWidget(line_h7, 13, 0, 1, 15)

        # 15th Row 
        grid_layout.addWidget(self.ข้อ7, 14, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม7, 14, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num7_1, 14, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num7_2, 14, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num7_3, 14, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num7_4, 14, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num7_5, 14, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 16th Row
        grid_layout.addWidget(line_h8, 15, 0, 1, 15)

        # 17th Row 
        grid_layout.addWidget(self.ข้อ8, 16, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม8, 16, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num8_1, 16, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num8_2, 16, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num8_3, 16, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num8_4, 16, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num8_5, 16, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 18th Row
        grid_layout.addWidget(line_h9, 17, 0, 1, 15)

        # 19th Row
        grid_layout.addWidget(self.ข้อ9, 18, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม9, 18, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num9_1, 18, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num9_2, 18, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num9_3, 18, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num9_4, 18, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num9_5, 18, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 20th Row
        grid_layout.addWidget(line_h10, 19, 0, 1, 15)

        # 21st Row
        grid_layout.addWidget(self.ข้อ10, 20, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.คำถาม10, 20, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num10_1, 20, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num10_2, 20, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num10_3, 20, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num10_4, 20, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.num10_5, 20, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        # 22nd Row
        grid_layout.addWidget(line_h11, 21, 0, 1, 15)

        # 23rd Row
        grid_layout.addWidget(self.รวม, 22, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.total1, 22, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.total2, 22, 6, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.total3, 22, 8, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.total4, 22, 10, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(self.total5, 22, 12, alignment=Qt.AlignmentFlag.AlignHCenter)

        grid_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_layout.addLayout(grid_layout)
        main_layout.addWidget(self.button)
        main_layout.addStretch(1)
        self.widget.setLayout(main_layout)

    # Function to check state 1
    def check_1_1(self):
        if self.num1_1.isChecked():
            self.num1_2.setChecked(False)
            self.num1_3.setChecked(False)
            self.num1_4.setChecked(False)
            self.num1_5.setChecked(False)
            self.cal()

    # Function to check state 1
    def check_1_2(self):
        if self.num1_2.isChecked():
            self.num1_1.setChecked(False)
            self.num1_3.setChecked(False)
            self.num1_4.setChecked(False)
            self.num1_5.setChecked(False)
            self.cal()

    # Function to check state 1
    def check_1_3(self):
        if self.num1_3.isChecked():
            self.num1_1.setChecked(False)
            self.num1_2.setChecked(False)
            self.num1_4.setChecked(False)
            self.num1_5.setChecked(False)
            self.cal()

    # Function to check state 1
    def check_1_4(self):
        if self.num1_4.isChecked():
            self.num1_1.setChecked(False)
            self.num1_2.setChecked(False)
            self.num1_3.setChecked(False)
            self.num1_5.setChecked(False)
            self.cal()

    # Function to check state 1
    def check_1_5(self):
        if self.num1_5.isChecked():
            self.num1_1.setChecked(False)
            self.num1_2.setChecked(False)
            self.num1_3.setChecked(False)
            self.num1_4.setChecked(False)
            self.cal()

    # Function to check state 2
    def check_2_1(self):
        if self.num2_1.isChecked():
            self.num2_2.setChecked(False)
            self.num2_3.setChecked(False)
            self.num2_4.setChecked(False)
            self.num2_5.setChecked(False)
            self.cal()

    # Function to check state 2
    def check_2_2(self):
        if self.num2_2.isChecked():
            self.num2_1.setChecked(False)
            self.num2_3.setChecked(False)
            self.num2_4.setChecked(False)
            self.num2_5.setChecked(False)
            self.cal()

    # Function to check state 2
    def check_2_3(self):
        if self.num2_3.isChecked():
            self.num2_1.setChecked(False)
            self.num2_2.setChecked(False)
            self.num2_4.setChecked(False)
            self.num2_5.setChecked(False)
            self.cal()

    # Function to check state 2
    def check_2_4(self):
        if self.num2_4.isChecked():
            self.num2_1.setChecked(False)
            self.num2_2.setChecked(False)
            self.num2_3.setChecked(False)
            self.num2_5.setChecked(False)
            self.cal()

    # Function to check state 2
    def check_2_5(self):
        if self.num2_5.isChecked():
            self.num2_1.setChecked(False)
            self.num2_2.setChecked(False)
            self.num2_3.setChecked(False)
            self.num2_4.setChecked(False)
            self.cal()

    # Function to check state 3
    def check_3_1(self):
        if self.num3_1.isChecked():
            self.num3_2.setChecked(False)
            self.num3_3.setChecked(False)
            self.num3_4.setChecked(False)
            self.num3_5.setChecked(False)
            self.cal()
    
    # Function to check state 3
    def check_3_2(self):
        if self.num3_2.isChecked():
            self.num3_1.setChecked(False)
            self.num3_3.setChecked(False)
            self.num3_4.setChecked(False)
            self.num3_5.setChecked(False)
            self.cal()

    # Function to check state 3
    def check_3_3(self):
        if self.num3_3.isChecked():
            self.num3_1.setChecked(False)
            self.num3_2.setChecked(False)
            self.num3_4.setChecked(False)
            self.num3_5.setChecked(False)
            self.cal()

    # Function to check state 3
    def check_3_4(self):
        if self.num3_4.isChecked():
            self.num3_1.setChecked(False)
            self.num3_2.setChecked(False)
            self.num3_3.setChecked(False)
            self.num3_5.setChecked(False)
            self.cal()

    # Function to check state 3
    def check_3_5(self):
        if self.num3_5.isChecked():
            self.num3_1.setChecked(False)
            self.num3_2.setChecked(False)
            self.num3_3.setChecked(False)
            self.num3_4.setChecked(False)
            self.cal()

    # Function to check state 4
    def check_4_1(self):
        if self.num4_1.isChecked():
            self.num4_2.setChecked(False)
            self.num4_3.setChecked(False)
            self.num4_4.setChecked(False)
            self.num4_5.setChecked(False)
            self.cal()

    # Function to check state 4
    def check_4_2(self):
        if self.num4_2.isChecked():
            self.num4_1.setChecked(False)
            self.num4_3.setChecked(False)
            self.num4_4.setChecked(False)
            self.num4_5.setChecked(False)
            self.cal()

    # Function to check state 4
    def check_4_3(self):
        if self.num4_3.isChecked():
            self.num4_1.setChecked(False)
            self.num4_2.setChecked(False)
            self.num4_4.setChecked(False)
            self.num4_5.setChecked(False)
            self.cal()

    # Function to check state 4
    def check_4_4(self):
        if self.num4_4.isChecked():
            self.num4_1.setChecked(False)
            self.num4_2.setChecked(False)
            self.num4_3.setChecked(False)
            self.num4_5.setChecked(False)
            self.cal()

    # Function to check state 4
    def check_4_5(self):
        if self.num4_5.isChecked():
            self.num4_1.setChecked(False)
            self.num4_2.setChecked(False)
            self.num4_3.setChecked(False)
            self.num4_4.setChecked(False)
            self.cal()

    # Function to check state 5
    def check_5_1(self):
        if self.num5_1.isChecked():
            self.num5_2.setChecked(False)
            self.num5_3.setChecked(False)
            self.num5_4.setChecked(False)
            self.num5_5.setChecked(False)
            self.cal()

    # Function to check state 5
    def check_5_2(self):
        if self.num5_2.isChecked():
            self.num5_1.setChecked(False)
            self.num5_3.setChecked(False)
            self.num5_4.setChecked(False)
            self.num5_5.setChecked(False)
            self.cal()

    # Function to check state 5
    def check_5_3(self):
        if self.num5_3.isChecked():
            self.num5_1.setChecked(False)
            self.num5_2.setChecked(False)
            self.num5_4.setChecked(False)
            self.num5_5.setChecked(False)
            self.cal()
    
    # Function to check state 5
    def check_5_4(self):
        if self.num5_4.isChecked():
            self.num5_1.setChecked(False)
            self.num5_2.setChecked(False)
            self.num5_3.setChecked(False)
            self.num5_5.setChecked(False)
            self.cal()

    # Function to check state 5
    def check_5_5(self):
        if self.num5_5.isChecked():
            self.num5_1.setChecked(False)
            self.num5_2.setChecked(False)
            self.num5_3.setChecked(False)
            self.num5_4.setChecked(False)
            self.cal()

    # Function to check state 6
    def check_6_1(self):
        if self.num6_1.isChecked():
            self.num6_2.setChecked(False)
            self.num6_3.setChecked(False)
            self.num6_4.setChecked(False)
            self.num6_5.setChecked(False)
            self.cal()

    # Function to check state 6
    def check_6_2(self):
        if self.num6_2.isChecked():
            self.num6_1.setChecked(False)
            self.num6_3.setChecked(False)
            self.num6_4.setChecked(False)
            self.num6_5.setChecked(False)
            self.cal()

    # Function to check state 6
    def check_6_3(self):
        if self.num6_3.isChecked():
            self.num6_1.setChecked(False)
            self.num6_2.setChecked(False)
            self.num6_4.setChecked(False)
            self.num6_5.setChecked(False)
            self.cal()

    # Function to check state 6
    def check_6_4(self):
        if self.num6_4.isChecked():
            self.num6_1.setChecked(False)
            self.num6_2.setChecked(False)
            self.num6_3.setChecked(False)
            self.num6_5.setChecked(False)
            self.cal()

    # Function to check state 6
    def check_6_5(self):
        if self.num6_5.isChecked():
            self.num6_1.setChecked(False)
            self.num6_2.setChecked(False)
            self.num6_3.setChecked(False)
            self.num6_4.setChecked(False)
            self.cal()

    # Function to check state 7
    def check_7_1(self):
        if self.num7_1.isChecked():
            self.num7_2.setChecked(False)
            self.num7_3.setChecked(False)
            self.num7_4.setChecked(False)
            self.num7_5.setChecked(False)
            self.cal()

    # Function to check state 7
    def check_7_2(self):
        if self.num7_2.isChecked():
            self.num7_1.setChecked(False)
            self.num7_3.setChecked(False)
            self.num7_4.setChecked(False)
            self.num7_5.setChecked(False)
            self.cal()

    # Function to check state 7
    def check_7_3(self):
        if self.num7_3.isChecked():
            self.num7_1.setChecked(False)
            self.num7_2.setChecked(False)
            self.num7_4.setChecked(False)
            self.num7_5.setChecked(False)
            self.cal()

    # Function to check state 7
    def check_7_4(self):
        if self.num7_4.isChecked():
            self.num7_1.setChecked(False)
            self.num7_2.setChecked(False)
            self.num7_3.setChecked(False)
            self.num7_5.setChecked(False)
            self.cal()

    # Function to check state 7
    def check_7_5(self):
        if self.num7_5.isChecked():
            self.num7_1.setChecked(False)
            self.num7_2.setChecked(False)
            self.num7_3.setChecked(False)
            self.num7_4.setChecked(False)
            self.cal()

    # Function to check state 8
    def check_8_1(self):
        if self.num8_1.isChecked():
            self.num8_2.setChecked(False)
            self.num8_3.setChecked(False)
            self.num8_4.setChecked(False)
            self.num8_5.setChecked(False)
            self.cal()

    # Function to check state 8
    def check_8_2(self):
        if self.num8_2.isChecked():
            self.num8_1.setChecked(False)
            self.num8_3.setChecked(False)
            self.num8_4.setChecked(False)
            self.num8_5.setChecked(False)
            self.cal()

    # Function to check state 8
    def check_8_3(self):
        if self.num8_3.isChecked():
            self.num8_1.setChecked(False)
            self.num8_2.setChecked(False)
            self.num8_4.setChecked(False)
            self.num8_5.setChecked(False)
            self.cal()

    # Function to check state 8
    def check_8_4(self):
        if self.num8_4.isChecked():
            self.num8_1.setChecked(False)
            self.num8_2.setChecked(False)
            self.num8_3.setChecked(False)
            self.num8_5.setChecked(False)
            self.cal()

    # Function to check state 8
    def check_8_5(self):
        if self.num8_5.isChecked():
            self.num8_1.setChecked(False)
            self.num8_2.setChecked(False)
            self.num8_3.setChecked(False)
            self.num8_4.setChecked(False)
            self.cal()

    # Function to check state 9
    def check_9_1(self):
        if self.num9_1.isChecked():
            self.num9_2.setChecked(False)
            self.num9_3.setChecked(False)
            self.num9_4.setChecked(False)
            self.num9_5.setChecked(False)
            self.cal()

    # Function to check state 9
    def check_9_2(self):
        if self.num9_2.isChecked():
            self.num9_1.setChecked(False)
            self.num9_3.setChecked(False)
            self.num9_4.setChecked(False)
            self.num9_5.setChecked(False)
            self.cal()

    # Function to check state 9
    def check_9_3(self):
        if self.num9_3.isChecked():
            self.num9_1.setChecked(False)
            self.num9_2.setChecked(False)
            self.num9_4.setChecked(False)
            self.num9_5.setChecked(False)
            self.cal()

    # Function to check state 9
    def check_9_4(self):
        if self.num9_4.isChecked():
            self.num9_1.setChecked(False)
            self.num9_2.setChecked(False)
            self.num9_3.setChecked(False)
            self.num9_5.setChecked(False)
            self.cal()

    # Function to check state 9
    def check_9_5(self):
        if self.num9_5.isChecked():
            self.num9_1.setChecked(False)
            self.num9_2.setChecked(False)
            self.num9_3.setChecked(False)
            self.num9_4.setChecked(False)
            self.cal()

    # Function to check state 10
    def check_10_1(self):
        if self.num10_1.isChecked():
            self.num10_2.setChecked(False)
            self.num10_3.setChecked(False)
            self.num10_4.setChecked(False)
            self.num10_5.setChecked(False)
            self.cal()

    # Function to check state 10
    def check_10_2(self):
        if self.num10_2.isChecked():
            self.num10_1.setChecked(False)
            self.num10_3.setChecked(False)
            self.num10_4.setChecked(False)
            self.num10_5.setChecked(False)
            self.cal()

    # Function to check state 10
    def check_10_3(self):
        if self.num10_3.isChecked():
            self.num10_1.setChecked(False)
            self.num10_2.setChecked(False)
            self.num10_4.setChecked(False)
            self.num10_5.setChecked(False)
            self.cal()

    # Function to check state 10
    def check_10_4(self):
        if self.num10_4.isChecked():
            self.num10_1.setChecked(False)
            self.num10_2.setChecked(False)
            self.num10_3.setChecked(False)
            self.num10_5.setChecked(False)
            self.cal()

    # Function to check state 10
    def check_10_5(self):
        if self.num10_5.isChecked():
            self.num10_1.setChecked(False)
            self.num10_2.setChecked(False)
            self.num10_3.setChecked(False)
            self.num10_4.setChecked(False)
            self.cal()

    # Function to Calculate First Row
    def cal(self):
        first_list = [self.num1_1, self.num2_1, self.num3_1, self.num4_1, self.num5_1, self.num6_1, self.num7_1, self.num8_1, self.num9_1, self.num10_1]
        first_value = [1 if num.isChecked() else 0 for num in first_list]
        total_1 = np.sum(first_value)
        self.total1.setText(str(total_1))

        second_list = [self.num1_2, self.num2_2, self.num3_2, self.num4_2, self.num5_2, self.num6_2, self.num7_2, self.num8_2, self.num9_2, self.num10_2]
        second_value = [1 if num.isChecked() else 0 for num in second_list]
        total_2 = np.sum(second_value)
        self.total2.setText(str(total_2))

        third_list = [self.num1_3, self.num2_3, self.num3_3, self.num4_3, self.num5_3, self.num6_3, self.num7_3, self.num8_3, self.num9_3, self.num10_3]
        third_value = [1 if num.isChecked() else 0 for num in third_list]
        total_3 = np.sum(third_value)
        self.total3.setText(str(total_3))

        fourth_list = [self.num1_4, self.num2_4, self.num3_4, self.num4_4, self.num5_4, self.num6_4, self.num7_4, self.num8_4, self.num9_4, self.num10_4]
        fourth_value = [1 if num.isChecked() else 0 for num in fourth_list]
        total_4 = np.sum(fourth_value)
        self.total4.setText(str(total_4))

        fifth_list = [self.num1_5, self.num2_5, self.num3_5, self.num4_5, self.num5_5, self.num6_5, self.num7_5, self.num8_5, self.num9_5, self.num10_5]
        fifth_value = [1 if num.isChecked() else 0 for num in fifth_list]
        total_5 = np.sum(fifth_value)
        self.total5.setText(str(total_5))    

    # Function to Update UI
    def update_ui(self):
        feedback = Database.get_feedback(self.username)
        if feedback:
            # Update data For Checkboxes 1
            self.num1_1.setChecked(True if feedback[2] == 1 else False)
            self.num1_2.setChecked(True if feedback[2] == 2 else False)
            self.num1_3.setChecked(True if feedback[2] == 3 else False)
            self.num1_4.setChecked(True if feedback[2] == 4 else False)
            self.num1_5.setChecked(True if feedback[2] == 5 else False)

            # Update data For Checkboxes 2
            self.num2_1.setChecked(True if feedback[3] == 1 else False)
            self.num2_2.setChecked(True if feedback[3] == 2 else False)
            self.num2_3.setChecked(True if feedback[3] == 3 else False)
            self.num2_4.setChecked(True if feedback[3] == 4 else False)
            self.num2_5.setChecked(True if feedback[3] == 5 else False)

            # Update data For Checkboxes 3
            self.num3_1.setChecked(True if feedback[4] == 1 else False)
            self.num3_2.setChecked(True if feedback[4] == 2 else False)
            self.num3_3.setChecked(True if feedback[4] == 3 else False)
            self.num3_4.setChecked(True if feedback[4] == 4 else False)
            self.num3_5.setChecked(True if feedback[4] == 5 else False)

            # Update data For Checkboxes 4
            self.num4_1.setChecked(True if feedback[5] == 1 else False)
            self.num4_2.setChecked(True if feedback[5] == 2 else False)
            self.num4_3.setChecked(True if feedback[5] == 3 else False)
            self.num4_4.setChecked(True if feedback[5] == 4 else False)
            self.num4_5.setChecked(True if feedback[5] == 5 else False)

            # Update data For Checkboxes 5
            self.num5_1.setChecked(True if feedback[6] == 1 else False)
            self.num5_2.setChecked(True if feedback[6] == 2 else False)
            self.num5_3.setChecked(True if feedback[6] == 3 else False)
            self.num5_4.setChecked(True if feedback[6] == 4 else False)
            self.num5_5.setChecked(True if feedback[6] == 5 else False)

            # Update data For Checkboxes 6
            self.num6_1.setChecked(True if feedback[7] == 1 else False)
            self.num6_2.setChecked(True if feedback[7] == 2 else False)
            self.num6_3.setChecked(True if feedback[7] == 3 else False)
            self.num6_4.setChecked(True if feedback[7] == 4 else False)
            self.num6_5.setChecked(True if feedback[7] == 5 else False)

            # Update data For Checkboxes 7
            self.num7_1.setChecked(True if feedback[8] == 1 else False)
            self.num7_2.setChecked(True if feedback[8] == 2 else False)
            self.num7_3.setChecked(True if feedback[8] == 3 else False)
            self.num7_4.setChecked(True if feedback[8] == 4 else False)
            self.num7_5.setChecked(True if feedback[8] == 5 else False)

            # Update data For Checkboxes 8
            self.num8_1.setChecked(True if feedback[9] == 1 else False)
            self.num8_2.setChecked(True if feedback[9] == 2 else False)
            self.num8_3.setChecked(True if feedback[9] == 3 else False)
            self.num8_4.setChecked(True if feedback[9] == 4 else False)
            self.num8_5.setChecked(True if feedback[9] == 5 else False)

            # Update data For Checkboxes 9
            self.num9_1.setChecked(True if feedback[10] == 1 else False)
            self.num9_2.setChecked(True if feedback[10] == 2 else False)
            self.num9_3.setChecked(True if feedback[10] == 3 else False)
            self.num9_4.setChecked(True if feedback[10] == 4 else False)
            self.num9_5.setChecked(True if feedback[10] == 5 else False)

            # Update data For Checkboxes 10
            self.num10_1.setChecked(True if feedback[11] == 1 else False)
            self.num10_2.setChecked(True if feedback[11] == 2 else False)
            self.num10_3.setChecked(True if feedback[11] == 3 else False)
            self.num10_4.setChecked(True if feedback[11] == 4 else False)
            self.num10_5.setChecked(True if feedback[11] == 5 else False)


    # Function to Update Excel
    def update_excel(self):
        try:
            message = QMessageBox()
            message.setWindowTitle("แจ้งเตือน")
            message.setIcon(QMessageBox.Icon.Information)
            message.setText("บันทึกไฟล์ %s สำเร็จ" % self.username) 

            buttons_1 = [self.num1_1, self.num1_2, self.num1_3, self.num1_4, self.num1_5]
            one = next((i + 1 for i, btn in enumerate(buttons_1) if btn.isChecked()), 0)

            buttons_2 = [self.num2_1, self.num2_2, self.num2_3, self.num2_4, self.num2_5]
            two = next((i + 1 for i, btn in enumerate(buttons_2) if btn.isChecked()), 0)

            buttons_3 = [self.num3_1, self.num3_2, self.num3_3, self.num3_4, self.num3_5]
            three = next((i + 1 for i, btn in enumerate(buttons_3) if btn.isChecked()), 0)

            buttons_4 = [self.num4_1, self.num4_2, self.num4_3, self.num4_4, self.num4_5]
            four = next((i + 1 for i, btn in enumerate(buttons_4) if btn.isChecked()), 0)

            buttons_5 = [self.num5_1, self.num5_2, self.num5_3, self.num5_4, self.num5_5]
            five = next((i + 1 for i, btn in enumerate(buttons_5) if btn.isChecked()), 0)

            buttons_6 = [self.num6_1, self.num6_2, self.num6_3, self.num6_4, self.num6_5]
            six = next((i + 1 for i, btn in enumerate(buttons_6) if btn.isChecked()), 0)

            buttons_7 = [self.num7_1, self.num7_2, self.num7_3, self.num7_4, self.num7_5]
            seven = next((i + 1 for i, btn in enumerate(buttons_7) if btn.isChecked()), 0)

            buttons_8 = [self.num8_1, self.num8_2, self.num8_3, self.num8_4, self.num8_5]
            eight = next((i + 1 for i, btn in enumerate(buttons_8) if btn.isChecked()), 0)

            buttons_9 = [self.num9_1, self.num9_2, self.num9_3, self.num9_4, self.num9_5]
            nine = next((i + 1 for i, btn in enumerate(buttons_9) if btn.isChecked()), 0)

            buttons_10 = [self.num10_1, self.num10_2, self.num10_3, self.num10_4, self.num10_5]
            ten = next((i + 1 for i, btn in enumerate(buttons_10) if btn.isChecked()), 0)

            Database.insert_feedback(
                self.username,
                one = one,
                two = two,
                three = three,
                four = four,
                five = five,
                six = six,
                seven = seven, 
                eight = eight,
                nine = nine,
                ten = ten,
                totalOne = self.total1.text(),
                totalTwo = self.total2.text(),
                totalThree = self.total3.text(),
                totalFour = self.total4.text(),
                totalFive = self.total5.text(),
            )

            workbook = load_workbook(self.path)
            sheet = workbook[self.sheet_name]

            sheet["C3"] = 1 if self.num1_1.isChecked() else ""
            sheet["D3"] = 1 if self.num1_2.isChecked() else ""
            sheet["E3"] = 1 if self.num1_3.isChecked() else ""
            sheet["F3"] = 1 if self.num1_4.isChecked() else ""
            sheet["G3"] = 1 if self.num1_5.isChecked() else ""

            sheet["C4"] = 1 if self.num2_1.isChecked() else ""
            sheet["D4"] = 1 if self.num2_2.isChecked() else ""
            sheet["E4"] = 1 if self.num2_3.isChecked() else ""
            sheet["F4"] = 1 if self.num2_4.isChecked() else ""
            sheet["G4"] = 1 if self.num2_5.isChecked() else ""

            sheet["C5"] = 1 if self.num3_1.isChecked() else ""
            sheet["D5"] = 1 if self.num3_2.isChecked() else ""
            sheet["E5"] = 1 if self.num3_3.isChecked() else ""
            sheet["F5"] = 1 if self.num3_4.isChecked() else ""
            sheet["G5"] = 1 if self.num3_5.isChecked() else ""

            sheet["C6"] = 1 if self.num4_1.isChecked() else ""
            sheet["D6"] = 1 if self.num4_2.isChecked() else ""
            sheet["E6"] = 1 if self.num4_3.isChecked() else ""
            sheet["F6"] = 1 if self.num4_4.isChecked() else ""
            sheet["G6"] = 1 if self.num4_5.isChecked() else ""

            sheet["C7"] = 1 if self.num5_1.isChecked() else ""
            sheet["D7"] = 1 if self.num5_2.isChecked() else ""
            sheet["E7"] = 1 if self.num5_3.isChecked() else ""
            sheet["F7"] = 1 if self.num5_4.isChecked() else ""
            sheet["G7"] = 1 if self.num5_5.isChecked() else ""

            sheet["C8"] = 1 if self.num6_1.isChecked() else ""
            sheet["D8"] = 1 if self.num6_2.isChecked() else ""
            sheet["E8"] = 1 if self.num6_3.isChecked() else ""
            sheet["F8"] = 1 if self.num6_4.isChecked() else ""
            sheet["G8"] = 1 if self.num6_5.isChecked() else ""

            sheet["C9"] = 1 if self.num7_1.isChecked() else ""
            sheet["D9"] = 1 if self.num7_2.isChecked() else ""
            sheet["E9"] = 1 if self.num7_3.isChecked() else ""
            sheet["F9"] = 1 if self.num7_4.isChecked() else ""
            sheet["G9"] = 1 if self.num7_5.isChecked() else ""

            sheet["C10"] = 1 if self.num8_1.isChecked() else ""
            sheet["D10"] = 1 if self.num8_2.isChecked() else ""
            sheet["E10"] = 1 if self.num8_3.isChecked() else ""
            sheet["F10"] = 1 if self.num8_4.isChecked() else ""
            sheet["G10"] = 1 if self.num8_5.isChecked() else ""

            sheet["C11"] = 1 if self.num9_1.isChecked() else ""
            sheet["D11"] = 1 if self.num9_2.isChecked() else ""
            sheet["E11"] = 1 if self.num9_3.isChecked() else ""
            sheet["F11"] = 1 if self.num9_4.isChecked() else ""
            sheet["G11"] = 1 if self.num9_5.isChecked() else ""

            sheet["C12"] = 1 if self.num10_1.isChecked() else ""
            sheet["D12"] = 1 if self.num10_2.isChecked() else ""
            sheet["E12"] = 1 if self.num10_3.isChecked() else ""
            sheet["F12"] = 1 if self.num10_4.isChecked() else ""
            sheet["G12"] = 1 if self.num10_5.isChecked() else ""

            sheet["C13"] = self.total1.text()
            sheet["D13"] = self.total2.text()
            sheet["E13"] = self.total3.text()
            sheet["F13"] = self.total4.text()
            sheet["G13"] = self.total5.text()

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
    window = Feedback_3_Window("01")
    window.show()
    sys.exit(app.exec())