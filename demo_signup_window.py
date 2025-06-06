from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QCheckBox, QGridLayout, QMessageBox
from PyQt6.QtGui import QFont, QIcon, QKeySequence
from PyQt6.QtCore import Qt
from datetime import datetime
import sys
import os
from demo_database import Database

font = QFont("Cordia New", 16)

class SignUp_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("หน้าต่างลงทะเบียน")
        self.setWindowIcon(QIcon("icons/signup.png"))

        # Create Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Call Nescessary Functions
        self.create_elements()
        self.setting_font()
        self.set_function()
        self.setting_layout()

        self.central_widget.setLayout(self.main_layout)

        self.setGeometry(250, 25, 10, 10)
        print("หน้าจอลงทะเบียนพร้อมแล้ว")

    # Function To Create Nescessary Elements
    def create_elements(self):
        # Create Labels
        self.space = QLabel("       ")
        self.header = QLabel("โปรดกรอกข้อมูลสุขภาพทั่วไป")
        self.ข้อมูลทั่วไป = QLabel("ข้อมูลทั่วไป")
        self.ชื่อ = QLabel("หมายเลข HN :")
        self.ผู้ดูแล = QLabel("ชื่อผู้ดูแล :")
        self.เพศ = QLabel("เพศ")
        self.วันเกิด = QLabel("วัน/เดือน/ปีเกิด :")

        # Create Name Input
        self.ใส่ชื่อ = QLineEdit()
        self.ใส่ผู้ดูแล = QLineEdit()

        # Create Checkbox
        self.ชาย = QCheckBox("ชาย")
        self.หญิง = QCheckBox("หญิง")

        # Create Combobox
        self.date = QComboBox()
        self.month = QComboBox()
        self.year = QComboBox()

        # Create Weight
        self.weight_label = QLabel("น้ำหนัก (กิโลกรัม) :")
        self.weight_input = QLineEdit()

        # Create Height
        self.height_label = QLabel("ส่วนสูง (เซนติเมตร) :")
        self.height_input = QLineEdit()

        # Create Question Labels
        self.ข้อมูลด้านสุขภาพ = QLabel("ข้อมูลด้านสุขภาพ")
        self.ข้อ1 = QLabel("""1.ประวัติที่เกี่ยวข้องหรือมีความผิดปกติเกี่ยวกับระบบประสาท เช่น โรคหลอดเลือดสมอง พาร์กินสันโรคที่ทำให้กล้ามเนื้ออ่อนแรง ความเจ็บป่วยทางด้านจิตใจ \nเช่น โรคทางจิตแพทย์ ซึ่งถูกวินิจฉัยโดยแพทย์ มีปัญหาการรับสัมผัสของมือ (sensory) ที่ผิดปกติอย่างรุนแรง""")
        self.ข้อ2 = QLabel("2.ประวัติเกี่ยวกับความผิดปกติของช่วงการเคลื่อนไหวของนิ้วมือและข้อมือโดยไม่สามารถเคลื่อนไหวได้เต็มช่วงการเคลื่อนไหว")
        self.ข้อ3 = QLabel("3.โรคประจำตัว")
        self.ข้อ4 = QLabel("4.ประวัติการเจ็บป่วยที่ทำให้เกิดปัญหาในการใช้มือหรือแขน ได้แก่ ข้ออักเสบ มีข้อติดรูปที่รุนแรงจนส่งผลต่อการเคลื่อนไหวมือ มีแผลที่มือที่ทำให้เกิดปัญหาในการใส่ถุงมือ")
        self.ข้อ5 = QLabel("5.มีปัญหาบกพร่องทางการรับรู้ และความเข้าใจ (cognitive abnormalities) ที่ไม่สามารถทำตามคำสั่งได้")
        self.ข้อ6 = QLabel("6.มีปัญหามีสายตาที่ยังไม่ได้รับการแก้ไข")

        # Create 1st Answer
        self.ปกติ1 = QCheckBox("ปกติ")
        self.ไม่ปกติ1 = QCheckBox("ไม่ปกติ")
        self.ระบุ1 = QLineEdit()

        # Create 2nd Answer
        self.ปกติ2 = QCheckBox("ปกติ")
        self.ไม่ปกติ2 = QCheckBox("ไม่ปกติ")
        self.ระบุ2 = QLineEdit()

        # Create 3rd Answer
        self.ไม่มี3 = QCheckBox("ไม่มี")
        self.มี3 = QCheckBox("มี")
        self.ระบุ3 = QLineEdit()

        # Create 4th Answer
        self.ไม่มี4 = QCheckBox("ไม่มี")
        self.มี4 = QCheckBox("มี")
        self.ระบุ4 = QLineEdit()

        # Create 5th Answer
        self.ไม่มี5 = QCheckBox("ไม่มี")
        self.มี5 = QCheckBox("มี")
        self.ระบุ5 = QLineEdit()

        # Create 6th Answer
        self.ไม่มี6 = QCheckBox("ไม่มี")
        self.มี6 = QCheckBox("มี")
        self.ระบุ6 = QLineEdit()

        # Create User Id
        self.user_id_label = QLabel("ชื่อผู้ใช้")
        self.user_id_input = QLineEdit()

        # Create Signup Button
        self.button = QPushButton("ลงทะเบียน")

    # Function To Set Font For Each Elements
    def setting_font(self):
        # Set Labels Font
        self.space.setFont(font)
        self.header.setFont(QFont("Cordia New", 16, QFont.Weight.Bold))
        self.ข้อมูลทั่วไป.setFont(QFont("Cordia New", 16, QFont.Weight.Bold))
        self.ชื่อ.setFont(font)
        self.ผู้ดูแล.setFont(font)
        self.เพศ.setFont(font)
        self.วันเกิด.setFont(font)

        # Set Checkbox Font
        self.ชาย.setFont(font)
        self.หญิง.setFont(font)

        # Set Name Input Font
        self.ใส่ชื่อ.setFont(font)
        self.ใส่ผู้ดูแล.setFont(font)

        # Set Combobox Font
        self.date.setFont(font)
        self.month.setFont(font)
        self.year.setFont(font)

        # Set Weight Font
        self.weight_label.setFont(font)
        self.weight_input.setFont(font)

        # Set Height Font
        self.height_label.setFont(font)
        self.height_input.setFont(font)

        # Set Question Labels Font
        self.ข้อมูลด้านสุขภาพ.setFont(QFont("Cordia New", 16, QFont.Weight.Bold))
        self.ข้อ1.setFont(font)
        self.ข้อ2.setFont(font)
        self.ข้อ3.setFont(font)
        self.ข้อ4.setFont(font)
        self.ข้อ5.setFont(font)
        self.ข้อ6.setFont(font)

        # Set 1st Answer Font
        self.ปกติ1.setFont(font)
        self.ไม่ปกติ1.setFont(font)
        self.ระบุ1.setFont(font)

        # Set 2nd Answer Font
        self.ปกติ2.setFont(font)
        self.ไม่ปกติ2.setFont(font)
        self.ระบุ2.setFont(font)

        # Set 3rd Answer Font
        self.ไม่มี3.setFont(font)
        self.มี3.setFont(font)
        self.ระบุ3.setFont(font)

        # Set 4th Answer Font
        self.ไม่มี4.setFont(font)
        self.มี4.setFont(font)
        self.ระบุ4.setFont(font)

        # Set 5th Answer Font
        self.ไม่มี5.setFont(font)
        self.มี5.setFont(font)
        self.ระบุ5.setFont(font)

        # Set 6th Answer Font
        self.ไม่มี6.setFont(font)
        self.มี6.setFont(font)
        self.ระบุ6.setFont(font)

        # Set User Id Font
        self.user_id_label.setFont(font)
        self.user_id_input.setFont(font)

        # Set Signup Button Font
        self.button.setFont(font)
        self.button.setStyleSheet(
            "QPushButton { background-color : #000080 ; color : white ;}"
            "QPushButton:pressed { background-color : #0F52BA ; color : #F5FEFD }"
        )

    # Function To Set Nescessary Method
    def set_function(self):
        # Date Combobox
        date = [str(i) for i in range(1, 32)]
        date.insert(0, "วันที่")
        self.date.addItems(date)

        # Month Combobox
        month = ["เดือน", "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน","กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิยายน", "ธันวาคม"]
        self.month.addItems(month)

        # Year Combobox
        now = datetime.now().year
        year = [str(i) for i in range(now-100, now)]
        year.insert(0, "ปี")
        self.year.addItems(year)

        # Set PlaceHolder For Text Input
        self.ใส่ชื่อ.setPlaceholderText("โปรดใส่หมายเลข HN")
        self.ใส่ผู้ดูแล.setPlaceholderText("โปรดใส่ชื่อ-นามสกุล ผู้ดูแล")
        self.weight_input.setPlaceholderText("โปรดใส่น้ำหนัก (กิโลกรัม)")
        self.height_input.setPlaceholderText("โปรดใส่ส่วนสูง (เซนติเมตร)")

        # Set PlaceHolder For Questions
        self.ระบุ1.setPlaceholderText("ระบุ...........")
        self.ระบุ2.setPlaceholderText("ระบุ...........")
        self.ระบุ3.setPlaceholderText("ระบุ...........")
        self.ระบุ4.setPlaceholderText("ระบุ...........")
        self.ระบุ5.setPlaceholderText("ระบุ...........")
        self.ระบุ6.setPlaceholderText("ระบุ...........")

        # Button Connect Function
        self.button.clicked.connect(self.on_button_clicked)
        self.button.setShortcut(QKeySequence("Return"))

        # Create Checkbox Condtition
        self.ชาย.stateChanged.connect(self.male_function)
        self.หญิง.stateChanged.connect(self.female_function)
        self.ปกติ1.stateChanged.connect(self.normal_function_1)
        self.ไม่ปกติ1.stateChanged.connect(self.abnormal_function_1)
        self.ปกติ2.stateChanged.connect(self.normal_function_2)
        self.ไม่ปกติ2.stateChanged.connect(self.abnormal_function_2)
        self.ไม่มี3.stateChanged.connect(self.no_function_3)
        self.มี3.stateChanged.connect(self.yes_function_3)
        self.ไม่มี4.stateChanged.connect(self.no_function_4)
        self.มี4.stateChanged.connect(self.yes_function_4)
        self.ไม่มี5.stateChanged.connect(self.no_function_5)
        self.มี5.stateChanged.connect(self.yes_function_5)
        self.ไม่มี6.stateChanged.connect(self.no_function_6)
        self.มี6.stateChanged.connect(self.yes_function_6)

    # Function To Set Up Layout
    def setting_layout(self):
        # space = QSpacerItem(30, 10)
        # new_space = QSpacerItem(100, 10)
        # gender_space = QSpacerItem(160, 10)

        # Create Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.header, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.ข้อมูลทั่วไป)

        # Create Name Layout
        name_layout = QGridLayout()
        name_layout.addWidget(self.space, 0, 0)
        name_layout.addWidget(self.ชื่อ, 0, 1)
        name_layout.addWidget(self.ใส่ชื่อ, 0, 2)
        name_layout.addWidget(self.ผู้ดูแล, 1, 1)
        name_layout.addWidget(self.ใส่ผู้ดูแล, 1, 2)
        self.main_layout.addLayout(name_layout)

        # Create Gender Layout
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.space)
        gender_layout.addWidget(self.เพศ)
        gender_layout.addWidget(self.ชาย)
        gender_layout.addWidget(self.หญิง)
        # gender_layout.addWidget(gender_space)
        gender_layout.addWidget(self.วันเกิด)
        gender_layout.addWidget(self.date)
        gender_layout.addWidget(self.month)
        gender_layout.addWidget(self.year)
        self.main_layout.addLayout(gender_layout)

        # Weight and Height
        weight_layout = QHBoxLayout()
        weight_layout.addWidget(self.space)
        weight_layout.addWidget(self.weight_label)
        weight_layout.addWidget(self.weight_input)
        weight_layout.addWidget(self.space)
        weight_layout.addWidget(self.height_label)
        weight_layout.addWidget(self.height_input)
        self.main_layout.addLayout(weight_layout)
        self.main_layout.addWidget(self.ข้อมูลด้านสุขภาพ)

        # Create Question 1 Layout
        question1_layout = QHBoxLayout()
        question1_layout.addWidget(self.space, alignment=Qt.AlignmentFlag.AlignLeft)
        question1_layout.addWidget(self.ข้อ1)
        question1_layout.addStretch(1)
        self.main_layout.addLayout(question1_layout)

        # Create Answer 1 Layout
        answer1_layout = QHBoxLayout()
        answer1_layout.addWidget(self.space)
        answer1_layout.addWidget(self.space)
        answer1_layout.addWidget(self.ปกติ1)
        answer1_layout.addWidget(self.ไม่ปกติ1)
        answer1_layout.addWidget(self.ระบุ1)
        self.main_layout.addLayout(answer1_layout)

        # Create Question 2 Layout
        question2_layout = QHBoxLayout()
        question2_layout.addWidget(self.space, alignment=Qt.AlignmentFlag.AlignLeft)
        question2_layout.addWidget(self.ข้อ2)
        question2_layout.addStretch(1)
        self.main_layout.addLayout(question2_layout)

        # Create Answer 2 Layout
        answer2_layout = QHBoxLayout()
        answer2_layout.addWidget(self.space)
        answer2_layout.addWidget(self.space)
        answer2_layout.addWidget(self.ปกติ2)
        answer2_layout.addWidget(self.ไม่ปกติ2)
        answer2_layout.addWidget(self.ระบุ2)
        self.main_layout.addLayout(answer2_layout)

        # Create Question 3 Layout
        question3_layout = QHBoxLayout()
        question3_layout.addWidget(self.space)
        question3_layout.addWidget(self.ข้อ3)
        question3_layout.addStretch(1)
        self.main_layout.addLayout(question3_layout)

        # Create Answer 3 Layout
        answer3_layout = QHBoxLayout()
        answer3_layout.addWidget(self.space)
        answer3_layout.addWidget(self.space)
        answer3_layout.addWidget(self.ไม่มี3)
        answer3_layout.addWidget(self.มี3)
        answer3_layout.addWidget(self.space)
        answer3_layout.addWidget(self.ระบุ3)
        self.main_layout.addLayout(answer3_layout)

        # Create Question 4 Layout
        question4_layout = QHBoxLayout()
        question4_layout.addWidget(self.space)
        question4_layout.addWidget(self.ข้อ4)
        question4_layout.addStretch(1)
        self.main_layout.addLayout(question4_layout)

        # Create Answer 4 Layout
        answer4_layout = QHBoxLayout()
        answer4_layout.addWidget(self.space)
        answer4_layout.addWidget(self.space)
        answer4_layout.addWidget(self.ไม่มี4)
        answer4_layout.addWidget(self.มี4)
        answer4_layout.addWidget(self.space)
        answer4_layout.addWidget(self.ระบุ4)
        self.main_layout.addLayout(answer4_layout)

        # Create Question 5 Layout
        question5_layout = QHBoxLayout()
        question5_layout.addWidget(self.space)
        question5_layout.addWidget(self.ข้อ5)
        question5_layout.addStretch(1)
        self.main_layout.addLayout(question5_layout)

        # Create Answer 5 Layout
        answer5_layout = QHBoxLayout()
        answer5_layout.addWidget(self.space)
        answer5_layout.addWidget(self.space)
        answer5_layout.addWidget(self.ไม่มี5)
        answer5_layout.addWidget(self.มี5)
        answer5_layout.addWidget(self.space)
        answer5_layout.addWidget(self.ระบุ5)
        self.main_layout.addLayout(answer5_layout)

        # Create Question 6 Layout
        question6_layout = QHBoxLayout()
        question6_layout.addWidget(self.space)
        question6_layout.addWidget(self.ข้อ6)
        question6_layout.addStretch(1)
        self.main_layout.addLayout(question6_layout)

        # Create Answer 6 Layout
        answer6_layout = QHBoxLayout()
        answer6_layout.addWidget(self.space)
        answer6_layout.addWidget(self.space)
        answer6_layout.addWidget(self.ไม่มี6)
        answer6_layout.addWidget(self.มี6)
        answer6_layout.addWidget(self.space)
        answer6_layout.addWidget(self.ระบุ6)
        self.main_layout.addLayout(answer6_layout)
        
        self.main_layout.addWidget(self.button)

    # Function To Check Status
    def male_function(self):
        if self.ชาย.isChecked():
            self.หญิง.setChecked(False)

    # Function To Check Status
    def female_function(self):
        if self.หญิง.isChecked():
            self.ชาย.setChecked(False)

    # Function To Check Status
    def normal_function_1(self):
        if self.ปกติ1.isChecked():
            self.ไม่ปกติ1.setChecked(False)
            self.ระบุ1.clear()

    # Function To Check Status
    def abnormal_function_1(self):
        if self.ไม่ปกติ1.isChecked():
            self.ปกติ1.setChecked(False)

    # Function To Check Status
    def normal_function_2(self):
        if self.ปกติ2.isChecked():
            self.ไม่ปกติ2.setChecked(False)
            self.ระบุ2.clear()

    # Function To Check Status
    def abnormal_function_2(self):
        if self.ไม่ปกติ2.isChecked():
            self.ปกติ2.setChecked(False)

    # Function To Check Status
    def no_function_3(self):
        if self.ไม่มี3.isChecked():
            self.มี3.setChecked(False)
            self.ระบุ3.clear()

    # Function To Check Status
    def yes_function_3(self):
        if self.มี3.isChecked():
            self.ไม่มี3.setChecked(False)

    # Function To Check Status
    def no_function_4(self):
        if self.ไม่มี4.isChecked():
            self.มี4.setChecked(False)
            self.ระบุ4.clear()

    # Function To Check Status
    def yes_function_4(self):
        if self.มี4.isChecked():
            self.ไม่มี4.setChecked(False)

    # Function To Check Status
    def no_function_5(self):
        if self.ไม่มี5.isChecked():
            self.มี5.setChecked(False)
            self.ระบุ5.clear()

    # Function To Check Status
    def yes_function_5(self):
        if self.มี5.isChecked():
            self.ไม่มี5.setChecked(False)

    # Function To Check Status
    def no_function_6(self):
        if self.ไม่มี6.isChecked():
            self.มี6.setChecked(False)
            self.ระบุ6.clear()

    # Function To Check Status
    def yes_function_6(self):
        if self.มี6.isChecked():
            self.ไม่มี6.setChecked(False)

    # Function Toggled When Button Was Clicked
    def on_button_clicked(self):
        try:
            messagebox = QMessageBox()
            database = Database()
            existing_user = database.get_exist_user(self.ใส่ชื่อ.text())
            if not existing_user:
                data = self.prepare_data()
                all_filled = all(value != "" for value in data.values())
                if all_filled:
                    messagebox.setWindowTitle("ยืนยันข้อมูล")
                    messagebox.setText("โปรดยืนยันข้อมูลของท่าน")
                    messagebox.setIcon(QMessageBox.Icon.Information)
                    yes_button = messagebox.addButton("ยืนยัน", QMessageBox.ButtonRole.AcceptRole)
                    no_button = messagebox.addButton("ยกเลิก", QMessageBox.ButtonRole.RejectRole)
                    messagebox.exec()
                    if messagebox.clickedButton() == yes_button:
                        database.input_data(data)
                        messagebox.setWindowTitle("สำเร็จ")
                        messagebox.setText("สร้างบัญชี %s สำเร็จ" % data["name"])
                        messagebox.setIcon(QMessageBox.Icon.Information)
                        messagebox.removeButton(yes_button)
                        messagebox.removeButton(no_button)
                        messagebox.addButton("ตกลง", QMessageBox.ButtonRole.AcceptRole)
                        messagebox.exec()
                        self.close()
                        print("yes")
                    elif messagebox.clickedButton() == no_button:
                        print("No")
                else:
                    messagebox.setText(f"โปรดกรอกข้อมูลทั้งหมด")
                    messagebox.setWindowTitle("ตรวจสอบ")
                    messagebox.setIcon(QMessageBox.Icon.Warning)
                    messagebox.exec()
            else:
                messagebox.setText(f"ชื่อผู้ใช้มีในระบบแล้ว")
                messagebox.setWindowTitle("ตรวจสอบ")
                messagebox.setIcon(QMessageBox.Icon.Warning)
                messagebox.exec()

        except ValueError as e:
            messagebox.setText(f"น้ำหนักและส่วนสูงเป็นตัวเลข")
            messagebox.setWindowTitle("ตรวจสอบ")
            messagebox.setIcon(QMessageBox.Icon.Warning)
            messagebox.exec()

    # Function To Prepare Data
    def prepare_data(self):
        data = {
            "name": self.ใส่ชื่อ.text(),
            "accessor": self.ใส่ผู้ดูแล.text(),
            "gender": "ชาย" if self.ชาย.isChecked() else "หญิง" if self.หญิง.isChecked() else "",
            "birth": f"{self.date.currentText()}/{self.month.currentText()}/{self.year.currentText()}",
            "weight": float(self.weight_input.text()) if self.weight_input.text() != "" else "",
            "height": float(self.height_input.text()) if self.height_input.text() != "" else "",
            "ans1": "ปกติ" if self.ปกติ1.isChecked() else self.ระบุ1.text(),
            "ans2": "ปกติ" if self.ปกติ2.isChecked() else self.ระบุ2.text(),
            "ans3": "ไม่มี" if self.ไม่มี3.isChecked() else self.ระบุ3.text(),
            "ans4": "ไม่มี" if self.ไม่มี4.isChecked() else self.ระบุ4.text(),
            "ans5": "ไม่มี" if self.ไม่มี5.isChecked() else self.ระบุ5.text(),
            "ans6": "ไม่มี" if self.ไม่มี6.isChecked() else self.ระบุ6.text(),
        }
        return data

    # Autocall Function To Toggle When Window Closed
    def closeEvent(self, event):
        print("หน้าจอลงทะเบียนเสร็จสิ้น")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignUp_Window()
    window.show()
    sys.exit(app.exec())