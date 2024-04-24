import socket
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Button App')
        self.setGeometry(300, 300, 300, 300)
        self.button = QPushButton('Нажмите меня', self)
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('95.154.118.183', 1234))
        sock.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    buttonapp = ButtonApp()
    sys.exit(app.exec())
