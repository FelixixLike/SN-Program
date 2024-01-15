import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QTabWidget,QLineEdit, QStackedWidget, QScrollArea, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QTextEdit, QFormLayout
from  PyQt6.QtGui import QFont,  QPixmap, QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import matplotlib.pyplot as plt
from Style import style
import math


texto_pagina1 ="""
<center><h1>INTERPOLACIÓN</h1></center>
<br>
    <p>En algunas ocasiones, necesitamos estimar valores intermedios entre datos definidos por puntos. El método más común para lograrlo es la interpolación polinomial.</p>

    <p>La fórmula general para un polinomio de grado "n" es:</p>
    <p>F(x) = a0 + a1x + a2x^2 + a3x^3 + ... + anx^n</p>
    
    <p>Aquí, "F(x)" representa el valor estimado en el punto "x", y "a0, a1, a2, ..., an" son los coeficientes del polinomio que se determinan a partir de los puntos conocidos. Al resolver un sistema de ecuaciones que involucra los puntos y los coeficientes del polinomio, podemos encontrar los valores de los coeficientes y así obtener el polinomio de interpolación deseado.</p>
    
    <p>Dados <span style="color: red;">R+1</span> puntos, hay uno y solo un polinomio de grado "n" que pasa a través de todos los puntos.</p>
<br>
  <center><img src="imagenes/interpolacion.png"  height="300" alt="Imagen binario"></center>
  <br>
    <p>La interpolación polinomial consiste en determinar el polinomio único de grado "n" que se ajuste a n+1 puntos. Este polinomio, entonces, proporciona una fórmula para calcular valores intermedios.</p>

    <p>La interpolación polinomial es útil en diversas áreas, como la interpolación de datos en ciencia, ingeniería, gráficos por computadora y muchas otras disciplinas. Sin embargo, es importante tener en cuenta que la interpolación solo proporciona estimaciones dentro del rango de los puntos conocidos y no garantiza la precisión fuera de ese rango.</p>

"""

texto_pagina2 = """
<center><h1>Interpolación Lineal</h1></center>
<br>
  <p>La interpolación lineal es un método sencillo que consiste en unir dos puntos con una línea recta.</p>
  <p>La fórmula para la interpolación lineal es la siguiente:</p>
  <br>
  <center><img src="imagenes/interpolacion_lineal.png"  height="300" alt="Imagen binario"></center>
  <br>
  <pre>y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)</pre>
  <br>
  <p>En esta fórmula, f1(x) representa un polinomio de interpolación de primer orden.</p>
  <h2>Ejemplo: Estimación del logaritmo natural de 2 mediante interpolación lineal</h2>
  <p>En primer lugar, realizamos el cálculo utilizando la interpolación entre Ln(1) = 0 y Ln(6) = 1.791759. Luego, repetimos el procedimiento utilizando un intervalo más pequeño entre Ln(1) y Ln(4) = 1.386294.</p>
  <p>El valor verdadero de Ln(2) es 0.6931472.</p>
  <h3>Solución:</h3>
  <center>
  <p>a) Utilizando la ecuación anterior para Ln(2) desde Xo = 1 hasta X1 = 6:</p>
  <pre>f(2) = 0 + ((1.791759 - 0) / (6 - 1)) * (2 - 1) = 0.3583519</pre>
  <p>Calculando el error:</p>
  <pre>Et = (|0.6931472 - 0.3583519| / 0.6931472) * 100 = 48.3%</pre>
  <p>b) Utilizando un intervalo más pequeño desde Xo = 1 hasta X1 = 4:</p>
  <pre>f(2) = 0 + ((1.386294 - 0) / (4 - 1)) * (2 - 1) = 0.4620981</pre>
  <p>Calculando el error:</p>
  <pre>Et = (|0.6931472 - 0.4620981| / 0.6931472) * 100 = 33.3%</pre></center>
"""

texto_pagina3 = """
<center><h1>Interpolación Cuadrática</h1></center>
<br>
  <p>La interpolación cuadrática es una estrategia para mejorar la estimación al introducir curvatura en la línea que une los puntos de datos. Si se tienen 3 puntos, es posible ajustarlos mediante un polinomio de segundo grado, también conocido como polinomio cuadrático.</p>
  <p>La forma general de un polinomio cuadrático es:</p>
  <pre>f(x) = b0 + b1(x - x0) + b2(x - x0)(x - x1)</pre>
  <p>donde b0, b1 y b2 son los coeficientes del polinomio, x0 y x1 son las coordenadas x de los dos primeros puntos de datos, respectivamente.</p>
  <p>Para encontrar los coeficientes, se pueden utilizar técnicas de resolución de sistemas de ecuaciones o métodos numéricos.</p>
  <br>
  <center><img src="imagenes/interpolacion_cuadratica.png"  height="300" alt="Imagen binario"></center>
  <br>
  <h2>Ejemplo:</h2>
<p>Supongamos que tenemos los siguientes puntos de datos: (1, 0), (4, 1.386294), (6, 1.791759). Queremos estimar ln(2) utilizando interpolación cuadrática.</p>

<p>Solución:</p>
<p>Aplicando la fórmula de interpolación cuadrática, tenemos:</p>
<p>f(x) = b0 + b1(x - x0) + b2(x - x0)(x - x1)</p>
<p>Sustituyendo los valores de los puntos de datos, tenemos:</p>
<p>0 = b0 + b1(1 - 1) + b2(1 - 1)(1 - 4)</p>
<p>1.386294 = b0 + b1(4 - 1) + b2(4 - 1)(4 - 6)</p>
<p>1.791759 = b0 + b1(6 - 1) + b2(6 - 1)(6 - 4)</p>
<p>Simplificando las ecuaciones, obtenemos un sistema de tres ecuaciones con tres incógnitas (b0, b1, b2). Resolviendo el sistema, encontramos los valores de los coeficientes.</p>
<br><center>
<p>Una vez obtenidos los coeficientes, podemos calcular el valor estimado de f(x) sustituyendo x = 2 en la fórmula de interpolación cuadrática.</p>
<br><center>
<pre>f(2) = 0 + (0.4620981)(2-1) + (- 0.0518731)(2-1)(2-4) = 0.565844</pre>
  <p>Calculando el error:</p>
  <pre>Et = (|0.6931472 - 0.565844| / 0.6931472) * 100 = 18.4%</pre></center>
<p>La interpolación cuadrática permite obtener una mejor aproximación que la interpolación lineal cuando se necesita ajustar una curvatura en los datos. Sin embargo, es importante tener en cuenta que la interpolación cuadrática puede no ser precisa en todos los casos y se debe tener cuidado al extrapolar más allá de los puntos de datos utilizados en el ajuste.</p>
</center>
"""
texto_pagina4 ="""
<center><h1>Interpolación de Newton</h1></center>
<br>
  <h2>Forma general de los polinomios de interpolación de Newton</h2>
  <p>El análisis anterior puede generalizarse para ajustar un polinomio de grado n utilizando n+1 datos:</p>
  <p>fn(x) = b0 + b1(x - x0) + b2(x - x0)(x - x1) + ... + bn(x - x0)(x - x1)...(x - xn-1)</p>
  <p>Para un polinomio de grado n, se requieren n+1 puntos: [x0, f(x0)], [x1, f(x1)], ..., [xn, f(xn)]. Utilizamos estos datos y las siguientes ecuaciones para evaluar los coeficientes:</p>
  <p>b0 = f(x0)</p>
  <p>b1 = f[x1, x0]</p>
  <p>b2 = f[x2, x1, x0]</p>
  <p>...</p>
  <p>bn = f[xn, xn-1, ..., x0]</p>
  <h3>Ejemplo:</h3>
  <p>Aplicando al ln(2) como en los ejercicios anterioes, tendremos estos resultados:</p>
  <p>Supongamos que tenemos los siguientes puntos de datos: (1, 0), (4, 1.386294), (6, 1.791759), (5, 1.609438). Queremos estimar ln(2) utilizando interpolación general de Newton
  <center>
  <pre>f(2) = 0 + (0.4620981)(2-1) + (- 0.0518731)(2-1)(2-4) + (0.007865529)(x-1)(x-4)(x-6) = 0.6287674 </pre>
  <p>Calculando el error:</p>
  <pre>Et = (|0.6931472 - 0.565844| / 0.6931472) * 100 = 9.29%</pre></center>
  """

class Pagina_1(QMainWindow):
    def __init__(self):
        super(Pagina_1, self).__init__()
        self.interface()

    def interface(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina1)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

class Pagina_2(QMainWindow):
    def __init__(self):
        super(Pagina_2, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina2)
        text_edit.setReadOnly(True)
        text_edit.setFixedHeight(1100)


        # Configurar objeto de diseño horizontal para centrar la imagen
        h_layout = QHBoxLayout()
        h_layout.addWidget(Interpolacion_lineal())

        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        layout.addLayout(h_layout)

        # Añadir espacio flexible en el layout para que se expanda y se ajuste al tamaño de la ventana
        layout.addStretch()

        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)
        scroll_area.setWidgetResizable(True)  # Hacer que el contenido del scroll sea redimensionable
        self.setCentralWidget(scroll_area)

class Interpolacion_lineal(QMainWindow):

    def __init__(self):
        super(Interpolacion_lineal,self).__init__()
        self.interface()

    def interface(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        label_logaritmo = QLabel("Escoge el logaritmo a buscar: ")
        self.input_logaritmo = QLineEdit()
        self.input_logaritmo.setText("2")

        layout0 = QHBoxLayout()
        layout0.addWidget(label_logaritmo)
        layout0.addWidget(self.input_logaritmo)

        layout1 = QHBoxLayout()

        label_x0 = QLabel("X0:")
        self.input_x0 = QLineEdit()
        self.input_x0.setText("1")

        label_fx0 = QLabel("f(x0):")
        self.input_fx0 = QLineEdit()
        self.input_fx0.setText("0")

        layout1.addWidget(label_x0)
        layout1.addWidget(self.input_x0)
        layout1.addWidget(label_fx0)
        layout1.addWidget(self.input_fx0)

        layout2 = QHBoxLayout()

        label_x1 = QLabel("X1:")
        self.input_x1 = QLineEdit()
        self.input_x1.setText("6")

        label_fx1 = QLabel("f(x1):")
        self.input_fx1 = QLineEdit()
        self.input_fx1.setText("1.791759")

        layout2.addWidget(label_x1)
        layout2.addWidget(self.input_x1)
        layout2.addWidget(label_fx1)
        layout2.addWidget(self.input_fx1)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_interpolation)

        self.result_textedit = QTextEdit()
        self.result_textedit.setFixedHeight(100)
        self.result_textedit.setReadOnly(True)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout0)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(self.result_textedit)

        main_widget.setLayout(main_layout)

    def calculate_interpolation(self):
        try:
            x0 = float(self.input_x0.text())
            fx0 = float(self.input_fx0.text())
            x1 = float(self.input_x1.text())
            fx1 = float(self.input_fx1.text())
            x = int(self.input_logaritmo.text())
            if (x0 > x and x1 > x) or (x0 < x and x1 < x):

                self.result_textedit.setText("Esos valores no encierran el valor a buscar.")

            else:
                interpolation = fx0 + ((x - x0) / (x1 - x0)) * (fx1 - fx0)

                self.result_textedit.clear()
                self.result_textedit.setHtml(f"""
                <center>El valor interpolado de Ln({x}) es: {interpolation}
                <br>El error porcentual verdadero es = {round(((math.log(x) - interpolation) / math.log(x)) * 100, 2)}%
                """)
        except:
            self.result_textedit.setText("Ingrese valores válidos.")



class Pagina_3(QMainWindow):
    def __init__(self):
        super(Pagina_3, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina3)
        text_edit.setFixedHeight(1350)


        # Configurar objeto de diseño horizontal para centrar la imagen
        h_layout = QHBoxLayout()
        h_layout.addStretch()

        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        layout.addWidget(Interpolacion_cuadratica())

        # Añadir espacio flexible en el layout para que se expanda y se ajuste al tamaño de la ventana
        layout.addStretch()

        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)
        scroll_area.setWidgetResizable(True)  # Hacer que el contenido del scroll sea redimensionable
        self.setCentralWidget(scroll_area)

class Interpolacion_cuadratica(QMainWindow):

    def __init__(self):
        super(Interpolacion_cuadratica,self).__init__()
        self.interface()

    def interface(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        label_logaritmo = QLabel("Escoge el logaritmo a buscar: ")
        self.input_logaritmo = QLineEdit()
        self.input_logaritmo.setText("2")

        layout0 = QHBoxLayout()
        layout0.addWidget(label_logaritmo)
        layout0.addWidget(self.input_logaritmo)

        layout1 = QHBoxLayout()

        label_x0 = QLabel("X0:")
        self.input_x0 = QLineEdit()
        self.input_x0.setText("1")
        label_fx0 = QLabel("f(x0):")
        self.input_fx0 = QLineEdit()
        self.input_fx0.setText("0")

        layout1.addWidget(label_x0)
        layout1.addWidget(self.input_x0)
        layout1.addWidget(label_fx0)
        layout1.addWidget(self.input_fx0)

        layout2 = QHBoxLayout()

        label_x1 = QLabel("X1:")
        self.input_x1 = QLineEdit()
        self.input_x1.setText("4")
        label_fx1 = QLabel("f(x1):")
        self.input_fx1 = QLineEdit()
        self.input_fx1.setText("1.386294")

        layout2.addWidget(label_x1)
        layout2.addWidget(self.input_x1)
        layout2.addWidget(label_fx1)
        layout2.addWidget(self.input_fx1)

        label_x2 = QLabel("X2:")
        self.input_x2 = QLineEdit()
        self.input_x2.setText("6")
        label_fx2 = QLabel("f(x2):")
        self.input_fx2 = QLineEdit()
        self.input_fx2.setText("1.791759")

        layout3 = QHBoxLayout()
        layout3.addWidget(label_x2)
        layout3.addWidget(self.input_x2)
        layout3.addWidget(label_fx2)
        layout3.addWidget(self.input_fx2)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_interpolation)

        self.result_textedit = QTextEdit()
        self.result_textedit.setFixedHeight(100)
        self.result_textedit.setReadOnly(True)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout0)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(self.result_textedit)

        main_widget.setLayout(main_layout)

    def calculate_interpolation(self):
        try:
            x0 = float(self.input_x0.text())
            fx0 = float(self.input_fx0.text())
            x1 = float(self.input_x1.text())
            fx1 = float(self.input_fx1.text())
            x2 = float(self.input_x2.text())
            fx2 = float(self.input_fx2.text())
            x = int(self.input_logaritmo.text())

            if (x0 > x and x1 > x and x2 > x) or (x0 < x and x1 < x and x2 < x):
                self.result_textedit.setText("Los valores ingresados no encierran el valor a buscar.")
            else:
                interpolation = fx0 + ((fx1 - fx0) / (x1 - x0)) * (x - x0) + ((((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0)) * (x - x0) * (x-x1)

                self.result_textedit.setHtml(f"""<center>
                bo = {fx0} ; b1 = {((fx1 - fx0) / (x1 - x0))} ; b2 = {((((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0))}
                <br>El valor interpolado de Ln({x}) es: {interpolation}
                <br>El error porcentual verdadero es = {round(((math.log(x) - interpolation) / math.log(x)) * 100, 2)}%
                """)
        except:
            self.result_textedit.setText("Ingrese valores válidos.")


class Pagina_4(QMainWindow):
    def __init__(self):
        super(Pagina_4, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina4)
        text_edit.setFixedHeight(650)
        text_edit.setReadOnly(True)
        # Crear botón "Volver"
        button_volver = QPushButton("Volver")


        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        layout.addWidget(Interpolacion_general())

        # Añadir espacio flexible en el layout para que se expanda y se ajuste al tamaño de la ventana
        layout.addStretch()

        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)
        scroll_area.setWidgetResizable(True)  # Hacer que el contenido del scroll sea redimensionable
        self.setCentralWidget(scroll_area)

class Interpolacion_general(QMainWindow):

    def __init__(self):
        super(Interpolacion_general,self).__init__()
        self.interface()

    def interface(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        label_logaritmo = QLabel("Escoge el logaritmo a buscar: ")
        self.input_logaritmo = QLineEdit()
        self.input_logaritmo.setText("2")

        layout0 = QHBoxLayout()
        layout0.addWidget(label_logaritmo)
        layout0.addWidget(self.input_logaritmo)

        layout1 = QHBoxLayout()

        label_x0 = QLabel("X0:")
        self.input_x0 = QLineEdit()
        self.input_x0.setText("1")
        label_fx0 = QLabel("f(x0):")
        self.input_fx0 = QLineEdit()
        self.input_fx0.setText("0")

        layout1.addWidget(label_x0)
        layout1.addWidget(self.input_x0)
        layout1.addWidget(label_fx0)
        layout1.addWidget(self.input_fx0)

        layout2 = QHBoxLayout()

        label_x1 = QLabel("X1:")
        self.input_x1 = QLineEdit()
        self.input_x1.setText("4")
        label_fx1 = QLabel("f(x1):")
        self.input_fx1 = QLineEdit()
        self.input_fx1.setText("1.386294")

        layout2.addWidget(label_x1)
        layout2.addWidget(self.input_x1)
        layout2.addWidget(label_fx1)
        layout2.addWidget(self.input_fx1)

        label_x2 = QLabel("X2:")
        self.input_x2 = QLineEdit()
        self.input_x2.setText("6")
        label_fx2 = QLabel("f(x2):")
        self.input_fx2 = QLineEdit()
        self.input_fx2.setText("1.791759")

        layout3 = QHBoxLayout()
        layout3.addWidget(label_x2)
        layout3.addWidget(self.input_x2)
        layout3.addWidget(label_fx2)
        layout3.addWidget(self.input_fx2)

        label_x3 = QLabel("X3:")
        self.input_x3 = QLineEdit()
        self.input_x3.setText("5")
        label_fx3 = QLabel("f(x3):")
        self.input_fx3 = QLineEdit()
        self.input_fx3.setText("1.609438")

        layout4 = QHBoxLayout()
        layout4.addWidget(label_x3)
        layout4.addWidget(self.input_x3)
        layout4.addWidget(label_fx3)
        layout4.addWidget(self.input_fx3)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_interpolation)

        self.result_textedit = QTextEdit()
        self.result_textedit.setFixedHeight(100)
        self.result_textedit.setReadOnly(True)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout0)
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        main_layout.addLayout(layout4)
        main_layout.addWidget(self.calculate_button)
        main_layout.addWidget(self.result_textedit)

        main_widget.setLayout(main_layout)

    def calculate_interpolation(self):
        try:
            x0 = float(self.input_x0.text())
            fx0 = float(self.input_fx0.text())
            x1 = float(self.input_x1.text())
            fx1 = float(self.input_fx1.text())
            x2 = float(self.input_x2.text())
            fx2 = float(self.input_fx2.text())
            x3 = float(self.input_x3.text())
            fx3 = float(self.input_fx3.text())
            x = int(self.input_logaritmo.text())

            if (x0 > x and x1 > x and x2 > x and x3 > x) or (x0 < x and x1 < x and x2 < x and x3 < x):
                self.result_textedit.setText("Los valores ingresados no encierran el valor a buscar.")
            else:
                interpolation = fx0 + ((fx1 - fx0) / (x1 - x0)) * (x - x0) + (
                            (((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0)) * (x - x0) * (
                                            x - x1) + \
                                ((((((fx3 - fx2) / (x3 - x2)) -
                            ((fx2 - fx1) / (x2 - x1))) / (x3 - x1)) - ((((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0))) / (x3 - x0)) * (x - x0) * (
                                            x - x1) * (x - x2)

                self.result_textedit.setHtml(f"""<center>
                {((((((fx3 - fx2) / (x3 - x2)) - ((fx2 - fx1) / (x2 - x1))) / (x3 - x1)) - ((((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0))) / (x3 - x0))} <br>
                b0 = {fx0} ; b1 = {((fx1 - fx0) / (x1 - x0))} ; b2 = {((((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0))} ; b3 = {((((((fx3 - fx2) / (x3 - x2)) - ((fx2 - fx1) / (x2 - x1))) / (x3 - x1)) - ((((fx2 - fx1) / (x2 - x1)) - ((fx1 - fx0) / (x1 - x0))) / (x2 - x0))) / (x3 - x0))}
                <br>El valor interpolado de Ln({x}) es: {interpolation}
                <br>El error porcentual verdadero es = {round(((math.log(x) - interpolation) / math.log(x)) * 100, 2)}%
                """)
        except:
            self.result_textedit.setText("Ingrese valores válidos.")

