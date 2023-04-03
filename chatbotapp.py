from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from chatbotappbackend import Chatbot
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        chatbot = Chatbot()

        self.setMinimumSize(900,700)

        self.chatbot_interface = QTextEdit(self)
        self.chatbot_interface.setGeometry(20,20,500,420)
        self.chatbot_interface.setReadOnly(True)

        self.usersearchbar = QLineEdit(self)
        self.usersearchbar.setGeometry(20,460,500,40)
        self.input_field.returnPressed.connect(self.enter_message)

        self.sendbutton = QPushButton("Enter" , self)
        self.sendbutton.setGeometry(500,460,100,40)
        self.sendbutton.clicked.connect(self.enter_message)

        self.show()

    def enter_message(self):
        user_input = self.input_field.text().strip()
        self.chatbot_interface.append(f"<p style='color#333333'>User:  {user_input}</p>")
        self.input_field.clear()
    
        thread = threading.Thread(target=self.wait_for_response, args=(user_input, ) )
        thread.start()

    def wait_for_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chatbot_interface.append(f"<p style='color#333333'; background-color: #E9E9E9'> Maya: {response}</p>")



chatbotapp = QApplication(sys.argv)
chatbotwindow = MainWindow()
sys.exit(chatbotapp.exec())

