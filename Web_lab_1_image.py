import socket
import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class ImageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image App')
        self.setGeometry(300, 300, 300, 300)
        self.label = QLabel(self)
        self.label.setFixedSize(300, 300)
        self.images = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg']
        self.show_random_image()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', 1234))
        self.sock.listen(1)
        self.sock.settimeout(0.1)
        self.show()

    def show_random_image(self):
        image = random.choice(self.images)
        pixmap = QPixmap(image)
        self.label.setPixmap(pixmap)

    def run(self):
        while True:
            try:
                # Проверить, есть ли входящие соединения
                conn, addr = self.sock.accept()

                # Получить сообщение
                data = conn.recv(1024)

                # Сменить картинку
                self.show_random_image()

                # Закрыть соединение
                conn.close()
            except socket.timeout:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    imageapp = ImageApp()
    imageapp.run()
    sys.exit(app.exec())
