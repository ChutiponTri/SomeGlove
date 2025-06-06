from PyQt6.QtCore import QThread, pyqtSignal
from threading import Thread
import serial.tools.list_ports
import pydirectinput
import serial
import time
from demo_database import Database

def pydirectinput_delay(delay):
    pydirectinput.PAUSE = delay

class Controller(QThread):
    signal = pyqtSignal(float)
    value = None
    pressure_mqtt = []

    def __init__(self, username, pressure:list):
        super().__init__()
        self.username = username
        self.pressure = pressure
        self.game = "Admin"

    # Function to Create Necessary Variables
    def initialize_variables(self):  
        self.data1 = None
        self.connecting = True
        self.running = False
        self.ret = False
        available_ports = Controller.get_non_bluetooth_serial_ports()
        if available_ports:
            print("Non-Bluetooth Serial Ports:")
            for port, desc, hwid in available_ports:
                self.port = port
                print(f"Port: {port}, Description: {desc}, HWID: {hwid}")
        else:
            self.port = None
            print("No non-Bluetooth serial ports found.")

    # Funtion to Resume Emiting Data
    def resume(self):
        self.running = True

    # Functin to Stop Emiting Data
    def stop(self):
        self.running = False

    # Function to Disconnect
    def disconnect(self):
        self.ret = True
        if hasattr(self, "ser"):
            self.ser.close()
    
    # Function to Run Async Task
    def run(self):
        print("Start Connection")
        self.initialize_variables()
        self.connection(self.port)
        print("Finish Connection")
    
    # Function to Start Connection
    def connection(self, port):
        if self.port is not None:
            self.ser = serial.Serial(port, 115200)

            while True:
                if self.ret:
                    return
                try:
                    data = self.ser.readline()
                    data = float(data.decode())
                    self.pressure_mqtt.append(data)

                    if self.running:
                        Perform_GUI_Action.value = data
                        send = Thread(target=self.emit_data, args=(data,))
                        send.start()

                except Exception as e:
                    pass

    # Function to Emit Data to Main Thread
    def emit_data(self, data):
        self.pressure.append(data)
        Database.insert_data(self.username, data)

    # Function to Write Back to Sensor
    def write_back(self, mode, percent, delay):
        try:
            Perform_GUI_Action.percent = percent
            message = "%s,%d,%d" % (mode, percent, delay)
            if hasattr(self, "ser"):
                self.ser.write(message.encode())
                print("Write", message)
        except Exception as e:
            print("Write Back", e)

    # Function to get serial port
    @staticmethod
    def get_non_bluetooth_serial_ports():
        ports = serial.tools.list_ports.comports()
        non_bluetooth_ports = []
        
        for port, desc, hwid in sorted(ports):
            if "Bluetooth" not in desc and "BT" not in desc:
                non_bluetooth_ports.append((port, desc, hwid))
        
        return non_bluetooth_ports


class Perform_GUI_Action(QThread):
    value = None
    percent = None
    def __init__(self):
        super().__init__()

    # Function to Create Necessary Variables
    def initialize_variables(self):  
        self.data1 = None
        self.connecting = True
        self.running = False
        self.ret = False
        self.game = "Admin"
        self.maximum = 0
        self.threshold = 300

    # Funtion to Resume Emiting Data
    def resume(self):
        # time.sleep(4)
        self.running = True
        self.maximum = 0

    # Functin to Stop Emiting Data
    def stop(self):
        self.running = False

    # Function to Disconnect
    def disconnect(self):
        self.ret = True

    # Function to Run Async Task
    def run(self):
        print("Start Perform")
        self.initialize_variables()
        self.perform()
        print("Finish Perform")

    # Function to Perform GUI Action
    def perform(self):
        key = "up"
        while self.connecting:
            if self.ret:
                return
            
            if (self.value is not None) and (self.value > self.maximum) and self.running:
                self.maximum = self.value
            if (self.value is not None) and (self.maximum - self.value > 800) and self.running:
                self.maximum = self.value
            elif (self.percent is not None) and (self.percent < 60) and self.running:
                self.threshold = 300

            time.sleep(0.01)
            try:
                if self.game == "Admin" and self.running:
                    time.sleep(1)
                                
                elif self.game == "JetpackJoyride" and self.running:
                    pydirectinput_delay(0)
                    time.sleep(0.05)
                    if self.value is not None:
                        if self.value:  
                            if self.value > self.maximum - self.threshold:
                                key = 'up'
                                pydirectinput.press(key)
                            elif self.value < self.maximum - self.threshold:
                                key = 'up'
                                pydirectinput.keyDown(key)
                            else:
                                pydirectinput.keyUp(key)
                                # for key in ["down", "up"]:
                                    # pydirectinput.keyUp(key)
                else:
                    if self.running:
                        pydirectinput_delay(0.1)
                        time.sleep(0.05)
                        if self.value is not None:
                            if self.value:   
                                if self.value > self.maximum - self.threshold:
                                    key = 'down'
                                    # pydirectinput.press(key)
                                elif self.value < self.maximum - self.threshold:
                                    key = 'up'
                                    pydirectinput.press(key)
                # print(self.value, self.maximum, self.threshold)
                    
            except Exception as e:
                print(self.value, type(self.value))
                print("Action", e)
