# Andrés Felipe Martínez González

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QMessageBox, QToolButton
from PyQt6 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt6.QtGui import QMovie, QIcon

from Hoja_1 import Hoja_1
from Hoja_2 import Hoja_2
from Hoja_3 import Hoja_3
from Hoja_4 import Hoja_4
from Hoja_5 import Hoja_5

# Crear reproductores multimedia
fondo = QMediaPlayer()
player = QMediaPlayer()
# Cargar archivos de sonido
url = QUrl.fromLocalFile('sonidos/clicked.mp3')
content = QMediaContent(url)
player.setMedia(content)
url = QUrl.fromLocalFile("sonidos/fondo.mp3")
content = QMediaContent(url)
fondo.setMedia(content)
fondo.play()

# X_L
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.interface()
    def interface(self):
        self.setWindowIcon(QIcon("imagenes/buho.png"))
        self.setWindowTitle("Sistemas Númericos")
        # Establecer tamaño de ventana
        self.setGeometry(0, 0, 1280, 800)
        self.showMaximized()

        # Crear etiqueta de fondo con archivo GIF
        background_label = QLabel(self)
        movie = QMovie('imagenes/intro.gif')
        background_label.setMovie(movie)
        movie.start()
        background_label.setScaledContents(True)



        # Crear botón de inicio
        start_button = QPushButton('Iniciar', self)
        start_button.clicked.connect(self.open_main_window)
        # Establecer estilo del botón
        start_button.setStyleSheet(
            'background-color: #00ff00; color: white; font-size: 20px; border-radius: 10px; padding: 10px;')

        # Crear diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(background_label)
        layout.addWidget(start_button)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        # Establecer estilo de la ventana
        self.setStyleSheet('background-color: black;')

    def open_main_window(self):
        # Abrir ventana principal
        player.play()
        fondo.stop()
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.interface()

    def interface(self):
        self.setWindowIcon(QIcon("imagenes/icon.ico"))
        self.setWindowTitle("Sistemas Numéricos")
        self.setGeometry(0, 0, 700, 700)
        # Mostrar la ventana en pantalla completa
        self.showMaximized()
        # Crear widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Crear botón de About
        about_button = QToolButton(self)
        about_button.setIcon(QIcon('imagenes/about.png'))
        about_button.setIconSize(about_button.sizeHint())
        about_button.setFixedSize(about_button.sizeHint())
        about_button.clicked.connect(self.informar)

        # Agregar etiqueta con título centrado
        title_label = QLabel("SISTEMAS NUMÉRICOS", self)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; color: #333; padding: 20px 0; font-weight: bold;")


        # Crear botones para cada opción de índice
        index_button_1 = QPushButton("1. Modelo matemático simple", self)
        index_button_1.clicked.connect(self.modelo_matematico_simple)
        index_button_1.setStyleSheet("height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        index_button_2 = QPushButton("2. Aproximaciones y errores de redondeo", self)
        index_button_2.clicked.connect(self.aproximaciones_y_errores)
        index_button_2.setStyleSheet("height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        index_button_3 = QPushButton("3. Interpolación", self)
        index_button_3.clicked.connect(self.interpolacion)
        index_button_3.setStyleSheet("height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        index_button_4 = QPushButton("4. Raices de ecuaciones", self)
        index_button_4.clicked.connect(self.raices_de_ecuaciones)
        index_button_4.setStyleSheet("height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        index_button_5 = QPushButton("5. Sistemas de ecuaciones no lineales", self)
        index_button_5.clicked.connect(self.sistemas_de_ecuaciones_no_lineales)
        index_button_5.setStyleSheet("height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        # Crear layout vertical
        layout = QVBoxLayout()

        # Añadir botones y etiqueta de título al diseño
        layout.addWidget(about_button)
        layout.addWidget(title_label)
        layout.addWidget(index_button_1)
        layout.addWidget(index_button_2)
        layout.addWidget(index_button_3)
        layout.addWidget(index_button_4)
        layout.addWidget(index_button_5)

        # Establecer el layout como el layout del widget central
        central_widget.setLayout(layout)

    def informar(self):

        message_box = QMessageBox(self)
        message_box.setWindowTitle('Acerca de:')
        message_box.setWindowIcon(QIcon('imagenes/about.png'))
        # Establecer el texto centrado
        message = '''<div>
    Desarrollado por el estudiante Andrés Felipe Martínez González - Ing Sistemas.
</div>
<br>
<div>
    En colaboración del Estudiante Brayan Torres Velez - Ing sistemas y el Licenciado WILDER ANGARITA OSORIO, Ciencias básicas.
</div>
<br>
<center>
    <div>
        CORPORACIÓN UNIVERSITARIA DEL META
    </div>
    <div>
        2023 - V1.0
    </div>
</center>
''' 
        message_box.setText(message)
        message_box.exec()

    def modelo_matematico_simple(self):
        player.play()
        self.welcome_window = Hoja_1()
        self.welcome_window.show()

    def aproximaciones_y_errores(self):
        player.play()
        self.welcome_window = Hoja_2()
        self.welcome_window.show()


    def interpolacion(self):
        "Función de Interpolación"
        player.play()
        self.welcome_window = Hoja_3()
        self.welcome_window.show()

    def raices_de_ecuaciones(self):
        "Función de Raices de ecuaciones"
        player.play()
        self.welcome_window = Hoja_4()
        self.welcome_window.show()

    def sistemas_de_ecuaciones_no_lineales(self):
        "Función de Sistemas de ecuaciones no lineales"
        player.play()
        self.welcome_window = Hoja_5()
        self.welcome_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = WelcomeWindow()
    ventana.show()
    sys.exit(app.exec())

# Andrés Felipe Martínez González