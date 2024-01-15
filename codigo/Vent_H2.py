import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QTabWidget,QLineEdit, QStackedWidget, QScrollArea, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QTextEdit, QFormLayout
from  PyQt6.QtGui import QFont,  QPixmap, QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import matplotlib.pyplot as plt
from Style import style



texto_pagina1 = """
<center><h2>EXACTITUD Y PRECISIÓN</h2></center>
<br>
<p>La exactitud y la precisión son conceptos importantes en el ámbito científico y técnico.</p>
<p><strong>Exactitud:</strong> se refiere a la proximidad del valor medido o calculado al valor verdadero de una magnitud o variable. Es decir, la exactitud mide qué tan cercano está el resultado obtenido al valor que se esperaba obtener en una medición o cálculo determinado.</p>
<p>Un ejemplo de exactitud sería si se midiera la longitud de una mesa y se obtuviera un resultado de 1 metro, y luego se comparara con la medida verdadera de 1.01 metros, se puede decir que la medida es bastante exacta, ya que el resultado es cercano al valor verdadero.</p>
<p><strong>Precisión:</strong> se refiere a la repetibilidad de los resultados de una medición o cálculo. Es decir, la precisión mide qué tan cercanos son los valores obtenidos entre sí. Si los valores obtenidos están muy cerca entre sí, se dice que hay una alta precisión, mientras que si los valores obtenidos están muy dispersos, se dice que hay una baja precisión.</p>
<p>Un ejemplo de precisión sería si se midiera la longitud de una mesa varias veces y se obtuvieran resultados cercanos entre sí, aunque no necesariamente cercanos al valor verdadero. En este caso, se puede decir que la medida es precisa, aunque no necesariamente exacta.</p>
<br>
<center><h2>INEXACTITUD E IMPRECISIÓN</h2></center>
<br>
<p><strong>Inexactitud:</strong> se refiere a la desviación sistemática del valor verdadero, también conocida como sesgo. Esto significa que, en una serie de mediciones, el valor obtenido siempre se desvía en una dirección determinada del valor verdadero.</p>
<p>Por ejemplo, si se midiera la longitud de una mesa varias veces, pero se utilizara una cinta métrica que estuviera un poco estirada, todos los valores obtenidos estarían por encima del valor verdadero, lo que indicaría una inexactitud sistemática.</p>
<p><strong>Imprecisión (incertidumbre):</strong> se refiere a la magnitud en la dispersión de los datos. En otras palabras, se refiere a la variabilidad aleatoria de los valores obtenidos.</p>
<p>Un ejemplo de imprecisión sería si se midiera la longitud de una mesa varias veces, pero se utilizara una cinta métrica que estuviera desgastada y no pudiera proporcionar valores precisos. En este caso, los valores obtenidos estarían dispersos al azar, lo que indicaría una alta imprecisión.</p>
"""

texto_pagina2 ="""
    <center><h2>DEFINICIONES DE ERROR</h2></center>
    <br>
    <p>
      Los errores son desviaciones entre el resultado obtenido y el resultado exacto esperado en cálculos matemáticos. Estas desviaciones se generan debido a aproximaciones que se realizan para representar cantidades y operaciones matemáticas exactas. Estos errores pueden clasificarse en diferentes categorías según su origen, como errores de redondeo, errores de truncamiento, errores de propagación y errores de modelado, entre otros. La comprensión y la gestión adecuada de los errores son fundamentales en la mayoría de las áreas de la ciencia y la ingeniería, ya que los errores pueden afectar significativamente la precisión y la confiabilidad de los resultados.
    </p>
    <br>
    <h2>Errores de truncamiento y errores de redondeo</h2>
    <p>
      Los errores de truncamiento resultan del empleo de aproximaciones como un procedimiento matemático exacto. Los errores de redondeo se producen cuando se usan números que tienen un límite de cifras significativas para representar un valor exacto. Para ambos, el valor verdadero es igual al valor aproximado más el error. El valor exacto del error (Et) se calcula restando el valor verdadero del valor aproximado.
    </p>
    <p>
      Cuando los órdenes de magnitud del valor verdadero y del valor aproximado son diferentes, se pueden utilizar dos fórmulas para calcular el error relativo: el error relativo fraccional verdadero (que se expresa como una fracción) y el error relativo porcentual (que se expresa como un porcentaje). En el caso del error relativo porcentual, se utiliza la siguiente fórmula:
    </p>
    <br>
    <center><p>Et = ((Valor verdadero – Valor aproximado) / Valor verdadero) * 100%</p></center>
    <br>
    <p>
      Por ejemplo, si se tiene que medir la longitud de un puente y la de un remache, y se obtiene 9.999 cm y 9 cm, respectivamente, y los valores verdaderos son 10.000 cm y 10 cm, se puede calcular el error verdadero y el error relativo porcentual en cada caso. Para el puente, el error verdadero es 0.001 cm y el error relativo porcentual es 0.01%. Para el remache, el error verdadero es 1 cm y el error relativo porcentual es 10%.
    </p>
    <h2>Normalización del error y métodos iterativos para disminuir el error</h2>
    <br>
    <p>Cuando no se cuenta con el valor verdadero, se puede normalizar el error utilizando la mejor estimación posible del valor verdadero. El error aproximado a un valor normalizado (Ea) se calcula dividiendo el error aproximado entre el valor aproximado y multiplicando por 100%:</p>
    <br>
    <center><p>Ea = (Error aproximado / Valor aproximado) * 100%</p></center>
    <br>
<p>Para disminuir el error, se pueden utilizar métodos iterativos que refinen la aproximación sucesivamente, acercándose cada vez más al valor verdadero. Estos métodos implican realizar cálculos repetidos utilizando la aproximación actual para obtener una nueva aproximación más precisa. Algunos ejemplos de métodos iterativos son el método de Newton-Raphson, el método de punto fijo y el método de bisección. Estos métodos permiten reducir el error a medida que se realizan más iteraciones.</p>

"""

texto_pagina3 ="""
<center><h1>Errores de Redondeo (Errores de computadora)</h1></center>
<br>
  <p>La computadora utiliza una representación en base 2, lo que significa que no puede representar algunos números en base 10 de manera exacta. Esta discrepancia debido a la omisión de cifras significativas se conoce como error de redondeo. Estos errores están relacionados con la forma en que los números se almacenan en la memoria de la computadora. La unidad básica de representación es la palabra, que es una cadena de dígitos binarios o bits. Por lo general, los números se guardan en una o más palabras.</p>
  <h2>Sistema numérico:</h2>
  <br>
  <p>Un sistema numérico es una convención utilizada para representar cantidades. En el sistema decimal (base 10), se utilizan los dígitos del 0 al 9. Para representar cantidades grandes, los dígitos se combinan y su posición o valor de posición especifica su magnitud.</p>
  <p>Por ejemplo: (8x10^4) + (6x10^3) + (4x10^2) + (0x10^1) + (9x10^0) = 86409</p>
  <p>En el caso de las computadoras, estas tienen 2 dedos. {0,1}. Base 2</p>
  <p>Por ejemplo: (1x2^5) + (0x2^4) + (1x2^3) + (1x2^2) + (0x2^1) + (1x2^0) = 45</p>
  <br>
  <center><img src="imagenes/binario.png" width="300" height="300" alt="Imagen binario"></center>
  <br>
  <h2>Solución de sistemas pequeños de ecuaciones con Eliminación de Gauss simple:</h2>
  <br>
  <p>Este método está diseñado para resolver un sistema general de n ecuaciones:</p>
  <br>
  <center><p>a11x1 + a12x2 + a13x3 + … + a1nxn = b1</p>
  <p>a21x1 + a22x2 + a23x3 + … + a2nxn = b2</p>
  <p>an1x1 + an2x2 + an3x3 + … + annxn = bn</p>

  <h3>Sustitución hacia atrás:</h3>
  <p>X3 = C3/a33</p>
  <p>X2 = (C2 – a23x3) / a22</p>
  <p>X1 = (C1 – a12x2 – a13x3) / a11</p></center>
  """

class Pagina_1(QMainWindow):
    def __init__(self):
        super(Pagina_1, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml(texto_pagina1)
        text_edit.setFixedHeight(800)
        # Crear botón "Volver"
        button_volver = QPushButton("Volver")


        # Configurar objeto de diseño horizontal para centrar la imagen
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(Ventana())
        h_layout.addStretch()

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

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Ventana con imagen")

        # Cargar imagen "E_P.jpg" y escalarla
        pixmap = QPixmap("imagenes/E_P.jpg")
        pixmap.scaledToHeight(500)

        # Crear QLabel para mostrar la imagen
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)

        # Configurar objeto de diseño horizontal para centrar la imagen
        h_layout = QVBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(image_label)
        h_layout.addStretch()

        # Configurar diseño vertical para el contenido de la ventana
        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        # Añadir espacio flexible en el layout para que se expanda y se ajuste al tamaño de la ventana
        layout.addStretch()

        # Establecer el widget principal de la ventana
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


class Pagina_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina2)
        text_edit.setReadOnly(True)
        text_edit.setFixedHeight(850)
        # Crear botón "Volver"
        button_volver = QPushButton("Volver")


        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        layout.addWidget(Calculardor_porcentaje_error())

        # Añadir espacio flexible en el layout para que se expanda y se ajuste al tamaño de la ventana
        layout.addStretch()

        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)
        scroll_area.setWidgetResizable(True)  # Hacer que el contenido del scroll sea redimensionable
        self.setCentralWidget(scroll_area)

class Calculardor_porcentaje_error(QMainWindow):
    def __init__(self):
        super(Calculardor_porcentaje_error, self).__init__()
        self.interface()

    def interface(self):
        # Crear el layout principal
        layout = QVBoxLayout()

        # Layout horizontal para la etiqueta y campo de texto del valor verdadero
        verdadero_layout = QHBoxLayout()
        verdadero_label = QLabel("Valor Verdadero:")
        self.verdadero_text = QLineEdit()
        verdadero_layout.addWidget(verdadero_label)
        verdadero_layout.addWidget(self.verdadero_text)

        # Layout horizontal para la etiqueta y campo de texto del valor obtenido
        obtenido_layout = QHBoxLayout()
        obtenido_label = QLabel("Valor Obtenido:")
        self.obtenido_text = QLineEdit()
        obtenido_layout.addWidget(obtenido_label)
        obtenido_layout.addWidget(self.obtenido_text)

        # Botón para calcular el resultado
        self.calcular_button = QPushButton("Calcular")
        self.calcular_button.clicked.connect(self.calcular_porcentaje)

        # Etiqueta para mostrar el resultado
        self.resultado_label = QTextEdit()
        self.resultado_label.setFixedHeight(200)
        # Agregar los layouts y elementos al layout principal
        layout.addLayout(verdadero_layout)
        layout.addLayout(obtenido_layout)
        layout.addWidget(self.calcular_button)
        layout.addWidget(self.resultado_label)

        # Crear un widget y establecer el layout principal
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget como el contenido central de la ventana principal
        self.setCentralWidget(widget)

    def calcular_porcentaje(self):

        try:
            valor_verdadero = float(self.verdadero_text.text())
            valor_obtenido = float(self.obtenido_text.text())

            resultado = abs((valor_obtenido - valor_verdadero) / valor_verdadero * 100)

            self.resultado_label.setHtml(f"<center>El margen de error es de: {round(resultado,3)}%</center><br>")
            self.resultado_label.append(f"(({self.verdadero_text.text()} - {self.obtenido_text.text()}) / {self.verdadero_text.text()}) *100%")

        except:
            self.resultado_label.setText(f"Digite los datos.")

class Pagina_3(QMainWindow):
    def __init__(self):
        super(Pagina_3, self).__init__()
        self.interface()

    def interface(self):
        # Establecer tamaño de ventana
        self.setGeometry(0, 0, 500, 500)

        # Crear QTabWidget
        self.tab_widget = QTabWidget()

        # Crear páginas como widgets
        self.page1 = Pagina3_1()
        self.page2 = Binario_Decimal()
        self.page3 = Eliminacion_Gauss()

        # Agregar páginas al QTabWidget
        self.tab_widget.addTab(self.page1, 'Informe')
        self.tab_widget.addTab(self.page2, 'Conversión')
        self.tab_widget.addTab(self.page3, 'Graficar funciones lineales')

        # Crear botones para cambiar de página

        # Crear diseño vertical
        layout = QVBoxLayout(self)
        layout.addWidget(self.tab_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_to_page1(self):
        self.tab_widget.setCurrentWidget(self.page1)

    def change_to_page2(self):
        self.tab_widget.setCurrentWidget(self.page2)

    def change_to_page3(self):
        self.tab_widget.setCurrentWidget(self.page3)

class Pagina3_1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina3)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

class Binario_Decimal(QMainWindow):
    def __init__(self):
        super(Binario_Decimal, self).__init__()
        self.interface()

    def interface(self):
        # Establecer tamaño de ventana
        self.setGeometry(0, 0, 500, 500)

        # Texto
        label_binario_decimal = QLabel("Binario a Decimal")
        label_decimal_binario = QLabel("Decimal a Binario")

        # Layouts verticales
        layout_v_1 = QVBoxLayout()
        layout_v_1.addWidget(label_binario_decimal)
        layout_v_1.addWidget(Calculardor_binario_d())

        layout_v_2 = QVBoxLayout()
        layout_v_2.addWidget(label_decimal_binario)
        layout_v_2.addWidget(Calculardor_decimal_b())

        # Layout horizontal
        layout_H = QHBoxLayout()
        layout_H.addLayout(layout_v_1)
        layout_H.addLayout(layout_v_2)

        # Establecer el layout principal de la ventana
        central_widget = QWidget()
        central_widget.setLayout(layout_H)
        self.setCentralWidget(central_widget)


class Eliminacion_Gauss(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):

        self.setGeometry(0,0,400,400)
        self.setWindowTitle("Errores de redondeo")

        self.valor1_input = QLineEdit(self)
        self.valor1_input.setText("3")
        x1_label = QLabel(self)
        x1_label.setText("x1")
        x1_label.setFont(QFont("Arial", 10))
        self.valor2_input = QLineEdit(self)
        self.valor2_input.setText("1")
        x2_label = QLabel(self)
        x2_label.setText("x2 = ")
        x2_label.setFont(QFont("Arial", 10))
        self.valor3_input = QLineEdit(self)
        self.valor3_input.setText("10")

        self.valor4_input = QLineEdit(self)
        self.valor4_input.setText("1")
        x1_label_2 = QLabel(self)
        x1_label_2.setText("x1")
        x1_label_2.setFont(QFont("Arial", 10))
        self.valor5_input = QLineEdit(self)
        self.valor5_input.setText("-3")
        x2_label_2 = QLabel(self)
        x2_label_2.setText("x2 = ")
        x2_label_2.setFont(QFont("Arial", 10))
        self.valor6_input = QLineEdit(self)
        self.valor6_input.setText("4")

        self.pantalla = QTextEdit()
        self.pantalla.setReadOnly(True)
        self.pantalla.setText("0")
        self.pantalla.setFont(QFont("Arial",20))

        self.boton_calcular = QPushButton("Calcular")
        self.boton_calcular.clicked.connect(self.graficar)

        primer_horizontal_layout = QHBoxLayout()
        primer_horizontal_layout.addWidget(self.valor1_input)
        primer_horizontal_layout.addWidget(x1_label)
        primer_horizontal_layout.addWidget(self.valor2_input)
        primer_horizontal_layout.addWidget(x2_label)
        primer_horizontal_layout.addWidget(self.valor3_input)

        segundo_horizontal_layout = QHBoxLayout()
        segundo_horizontal_layout.addWidget(self.valor4_input)
        segundo_horizontal_layout.addWidget(x1_label_2)
        segundo_horizontal_layout.addWidget(self.valor5_input)
        segundo_horizontal_layout.addWidget(x2_label_2)
        segundo_horizontal_layout.addWidget(self.valor6_input)

        self.grafico()

        main_form = QFormLayout()
        main_form.addRow(primer_horizontal_layout)
        main_form.addRow(segundo_horizontal_layout)
        main_form.addRow(self.pantalla)
        main_form.addRow(self.boton_calcular)
        main_form.addRow(self.canvas)

        self.setLayout(main_form)

    def grafico(self):
        # para graficar conforme se pida requerimientos

        # Crear el canvas de la figura
        self.canvas = FigureCanvas(plt.figure())

        # Valores del eje X que toma el gráfico.
        x = range(-10, 15)

        # Graficar ambas funciones.
        plt.plot(x, [0 for i in x])

        # Establecer el color de los ejes.
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        # Limitar los valores de los ejes.
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        plt.title('Función Lineal')
        plt.grid()

    def graficar(self):
        # Obtener los valores de los QLineEdit y convertirlos a números
        valor1 = self.valor1_input.text()
        valor2 = self.valor2_input.text()
        valor3 = self.valor3_input.text()
        valor4 = self.valor4_input.text()
        valor5 = self.valor5_input.text()
        valor6 = self.valor6_input.text()

        try:
            valor1 = float(valor1)
            valor2 = float(valor2)
            valor3 = float(valor3)
            valor4 = float(valor4)
            valor5 = float(valor5)
            valor6 = float(valor6)

            if valor2 == 0:
                self.pantalla.setPlainText("El segundo parámetro no puede ser 0")
                return
        except ValueError:
            self.pantalla.setPlainText("Solo se admiten números")
            return

        # Limpiar la figura antes de graficar la nueva función
        plt.clf()

        # Valores del eje X que toma el gráfico.
        x = range(-10, 15)

        def f1(x):
            return -(valor1 / valor2) * x + (valor3 / valor2)
        def f2(x):
            return -(valor4 / valor5) * x + (valor6 / valor5)


        # Configurar la cuadrícula
        plt.xticks(range(-10, 15, 5))
        plt.yticks(range(-10, 15, 5))
        plt.grid(True)

        # Graficar ambas funciones.
        plt.plot(x, [f1(i) for i in x])
        plt.plot(x, [f2(i) for i in x])

        # Establecer el color de los ejes.
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        # Limitar los valores de los ejes.
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        plt.title('Función Lineal')

        # Redibujar la gráfica
        self.canvas.draw()

        # Mostrar el resultado en el QTextEdit pantalla
        resultado = f'<center> <span style="color: blue; font-weight: bold; font-size: 18px;"> y = {round(-(valor1 / valor2), 3)}X + {round(valor3 / valor2, 3)}</span> &nbsp;&nbsp;&nbsp; <span style="color: orange; font-weight: bold; font-size: 18px;">y = {round(-(valor4 / valor5), 3)}X + {round(valor6 / valor5, 3)}</span>'
        self.pantalla.setHtml(resultado)


class Calculardor_decimal_b(QWidget):
    def __init__(self):
        super().__init__()

        # Crear etiquetas y campos de entrada/salida
        self.label1 = QLabel("Número decimal:")
        self.number_input = QLineEdit()
        self.label2 = QLabel("Número binario:")
        self.number_output = QLineEdit()

        # Crear botón de conversión
        self.convert_button = QPushButton("Convertir")
        self.convert_button.clicked.connect(self.dec_to_bin)

        # Crear diseño horizontal para etiquetas y campos de entrada
        layout1 = QHBoxLayout()
        layout1.addWidget(self.label1)
        layout1.addWidget(self.number_input)

        # Crear diseño horizontal para etiquetas y campos de salida
        layout2 = QHBoxLayout()
        layout2.addWidget(self.label2)
        layout2.addWidget(self.number_output)

        # Crear diseño vertical para contener
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addWidget(self.convert_button)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        main_layout.addWidget(self.text_edit)

        # Establecer el diseño principal del widget
        self.setLayout(main_layout)
        self.setStyleSheet(style)

    def dec_to_bin(self):
        # Convertir el número decimal a binario y mostrarlo en el campo de salida
        try:
            dec_number = int(self.number_input.text())
            bin_number = bin(dec_number)[2:]
            self.number_output.setText(bin_number)
            self.text_edit.setText("")
            """muestra división"""
            tabulador = 0
            while True:
                residuo = dec_number % 2
                self.text_edit.append("{}{}|2".format("\t" * tabulador, dec_number))
                self.text_edit.append("{}{} --".format("\t" * tabulador, residuo))
                tabulador += 1
                dec_number = int(dec_number / 2)
                if dec_number == 1 or dec_number == 0:
                    self.text_edit.append("{}{}".format("\t" * tabulador, dec_number))
                    break
        except ValueError:
            self.number_output.setText("Error: número inválido")



class Calculardor_binario_d(QWidget):
    def __init__(self):
        super().__init__()

        # Crear etiquetas y campos de entrada/salida
        self.label1 = QLabel("Número binario:")
        self.number_input = QLineEdit()
        self.label2 = QLabel("Número decimal:")
        self.number_output = QLineEdit()

        # Crear botón de conversión
        self.convert_button = QPushButton("Convertir")
        self.convert_button.clicked.connect(self.bin_to_dec)

        # Crear diseño horizontal para etiquetas y campos de entrada
        layout1 = QHBoxLayout()
        layout1.addWidget(self.label1)
        layout1.addWidget(self.number_input)

        # Crear diseño horizontal para etiquetas y campos de salida
        layout2 = QHBoxLayout()
        layout2.addWidget(self.label2)
        layout2.addWidget(self.number_output)

        # Crear diseño vertical para contener
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addWidget(self.convert_button)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        main_layout.addWidget(self.text_edit)

        # Establecer el diseño principal del widget y la hoja de estilo
        self.setLayout(main_layout)
        self.setStyleSheet(style)

    def bin_to_dec(self):
        # Convertir el número binario a decimal y mostrarlo en el campo de salida
        try:
            self.text_edit.clear()
            def binario_a_decimal(binario):
                # Convertir el número binario a una cadena de dígitos individuales
                digitos = list(binario)
                # Invertir la lista de dígitos para facilitar los cálculos
                digitos.reverse()
                # Inicializar el valor decimal y el exponente
                decimal = 0
                exponente = 0

                # Realizar los cálculos para cada dígito
                for digito in digitos:
                    # Calcular el valor decimal del dígito actual
                    valor = int(digito) * (2 ** exponente)

                    # Agregar el valor al decimal total
                    decimal += valor
                    # Mostrar la operación actual en pantalla
                    self.text_edit.append(f"{digito} * 2^{exponente} = {valor}")

                    # Incrementar el exponente
                    exponente += 1
                # Devolver el valor decimal calculado
                return decimal

            digitos = self.number_input.text()
            if any(char.isdigit() and char != '0' and char != '1' for char in digitos):
                self.number_output.setText("Error: número inválido")

            else:
                # Pedir al usuario que ingrese un número binario
                binario = self.number_input.text()

                # Convertir el número binario a decimal
                decimal = binario_a_decimal(binario)
                self.text_edit.append(f"\nEl número binario {binario} es igual a {decimal} en decimal.")
                self.number_output.setText(str(decimal))

        except ValueError:
            self.number_output.setText("Error: número inválido")
