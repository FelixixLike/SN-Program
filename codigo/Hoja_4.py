
from Vent_H4 import *

# Crear reproductores multimedia
regresar = QMediaPlayer()
# Cargar archivos de sonido
url = QUrl.fromLocalFile('sonidos/return.mp3')
content = QMediaContent(url)
regresar.setMedia(content)

player = QMediaPlayer()
# Cargar archivos de sonido
url = QUrl.fromLocalFile('sonidos/clicked.mp3')
content = QMediaContent(url)
player.setMedia(content)

class Hoja_4(QMainWindow):
    def __init__(self):
        super(Hoja_4, self).__init__()
        self.interface()

    def interface(self):
        self.setWindowIcon(QIcon("imagenes/buho.png"))
        self.setWindowTitle("Raices de ecuaciones")
        # Establecer tamaño de ventana
        self.setGeometry(0,0,500,500)
        self.showFullScreen()

        # Crear QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Crear páginas
        self.page1 = Pagina_1()
        self.page2 = Pagina_2()
        self.page3 = Pagina_3()


        # Agregar páginas al QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # Crear botones para cambiar de página
        self.button1 = QPushButton('Explicación')
        self.button1.clicked.connect(self.change_to_page1)

        self.button2 = QPushButton('Metodo Cerrado')
        self.button2.clicked.connect(self.change_to_page2)

        self.button3 = QPushButton('Metodo Abierto')
        self.button3.clicked.connect(self.change_to_page3)

        self.button_s = QPushButton('Volver')
        self.button_s.clicked.connect(self.retun_page_inicio)
        self.button_s.setStyleSheet(
            "height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        # Crear diseño Horizontal
        buttons = QHBoxLayout()
        buttons.addWidget(self.button1)
        buttons.addWidget(self.button2)
        buttons.addWidget(self.button3)

        # Crear diseño vertical
        layout = QVBoxLayout()
        layout.addLayout(buttons)
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.button_s)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet(style)

    def change_to_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)
        player.play()

    def change_to_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)
        player.play()

    def change_to_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)
        player.play()

    def retun_page_inicio(self):
        regresar.play()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana =Hoja_4()
    ventana.show()
    sys.exit(app.exec())