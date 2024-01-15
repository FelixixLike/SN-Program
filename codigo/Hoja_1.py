from Vent_H1 import *

# Crear reproductores multimedia
regresar = QMediaPlayer()
# Cargar archivos de sonido
url = QUrl.fromLocalFile('sonidos/return.mp3')
content = QMediaContent(url)
regresar.setMedia(content)



class Hoja_1(QMainWindow):
    def __init__(self):
        super(Hoja_1, self).__init__()
        self.interface()

    def interface(self):
        self.setWindowIcon(QIcon("imagenes/buho.png"))
        self.setWindowTitle("Modelo matemático simple")
        # Establecer tamaño de ventana
        self.setGeometry(0, 0, 500, 500)
        self.showFullScreen()

        scroll_area = QScrollArea(self)

        # Boton devolver
        self.button1 = QPushButton('Volver')
        self.button1.clicked.connect(self.retun_page_inicio)
        self.button1.setStyleSheet(
            "height: 60px; font-size: 24px; background-color: #3498db; color: #fff; border: none; border-radius: 5px; padding: 0 20px;")

        # Crear diseño vertical
        layout_main = QVBoxLayout()
        layout_main.addWidget(Pagina_1())
        layout_main.addWidget(self.button1)

        central_widget = QWidget()

        central_widget.setLayout(layout_main)
        scroll_area.setWidget(central_widget)
        scroll_area.setWidgetResizable(True)
        self.setCentralWidget(scroll_area)
        self.setStyleSheet(style)

    def retun_page_inicio(self):
        regresar.play()
        self.close()


