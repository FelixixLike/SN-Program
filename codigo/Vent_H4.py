import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QTabWidget, QComboBox,QLineEdit, QStackedWidget, QScrollArea, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QTextEdit, QFormLayout
from  PyQt6.QtGui import QFont,  QPixmap, QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from Style import style

texto_pagina1 ="""
<center><h1>Raíces de ecuaciones: qué son y cómo encontrarlas</h1></center>
<br>
<h2>Introducción</h2>
<p>Las ecuaciones son expresiones matemáticas que relacionan una o más variables y establecen una igualdad. Una ecuación se resuelve encontrando el valor o valores de la variable que la hacen verdadera. Estos valores se conocen como las raíces de la ecuación y son de gran importancia en muchos campos de la ciencia y la ingeniería.</p>
<br>
<h2>¿Qué son las raíces de una ecuación?</h2>
<p>Las raíces de una ecuación son los valores de la variable que hacen que la ecuación sea verdadera. En otras palabras, son los valores de la variable que satisfacen la ecuación. Por ejemplo, en la ecuación x^2 - 4 = 0, las raíces son x = 2 y x = -2, ya que son los valores de la variable que hacen que la ecuación sea verdadera.</p>
<h2>Tipos de raíces</h2>
<p>Existen diferentes tipos de raíces dependiendo de la naturaleza de la ecuación. A continuación, se describen los más comunes:</p>
<h3>Raíces reales</h3>
<p>Las raíces reales son aquellas que corresponden a valores reales de la variable. Por ejemplo, las raíces de la ecuación x^2 - 4 = 0 son x = 2 y x = -2, que son valores reales.</p>
<h3>Raíces complejas</h3>
<p>Las raíces complejas son aquellas que corresponden a valores complejos de la variable. Una ecuación con coeficientes reales puede tener raíces complejas si no tiene raíces reales. Por ejemplo, la ecuación x^2 + 1 = 0 no tiene raíces reales, pero tiene dos raíces complejas: x = i y x = -i, donde i es la unidad imaginaria.</p>
<h3>Raíces múltiples</h3>
<p>Las raíces múltiples son aquellas que corresponden a un mismo valor de la variable. Por ejemplo, la ecuación (x - 1)^2 = 0 tiene una raíz doble en x = 1, ya que la ecuación se puede expresar como (x - 1)(x - 1) = 0.</p>
<h2>Cómo encontrar las raíces de una ecuación</h2>
<p>Existen diferentes métodos para encontrar las raíces de una ecuación, dependiendo de la complejidad de la misma. Algunos de los métodos más comunes son:</p>
<ul>
  <li>Método de factorización</li>
  <li>Método de la fórmula general para ecuaciones de segundo grado</li>
  <li>Método de bisección para ecuaciones no lineales</li>
  <li>Método de Newton-Raphson para ecuaciones no lineales</li>
</ul> 
<p>Cada método tiene sus ventajas y desventajas y es importante elegir el método adecuado para la ecuación en cuestión.</p>
"""

texto_pagina2_1 = """
<h2>Métodos Gráficos</h2>
<p>Un método simple para obtener una aproximación a la raíz de la ecuación f(x) = 0 consiste en graficar la función y observar dónde cruza el eje x. Este punto, que representa el valor de x para el cual f(x) = 0, ofrece una aproximación inicial de la raíz.</p>
<h3>Ejemplo:</h3>
<p>Busquemos la raíz (en este caso tenemos 2) de la ecuación f(x) = 2x<sup>2</sup> - 5x, para ello le daremos parámetros a x de -1 a 3 con un paso de 1. Obtenemos los siguientes datos:</p>
<center>
<table>
	<thead>
		<tr>
			<th>x</th>
			<th>|</th>
			<th>y</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>-1</td>
			<th>|</th>
			<td>7</td>
		</tr>
		<tr>
			<td>0</td>
			<th>|</th>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<th>|</th>
			<td>-3</td>
		</tr>
		<tr>
			<td>2</td>
			<th>|</th>
			<td>-2</td>
		</tr>
		<tr>
			<td>3</td>
			<th>|</th>
			<td>3</td>
		</tr>
	</tbody>
</table>
</center>
<p>Mirando la tabla, podemos observar que en el intervalo entre 2 y 3 tenemos un cambio de signo, por lo que en medio de estos dos valores podemos encontrar la segunda raíz.</p>
<p>Sin necesidad de ver la tabla, en el gráfico se pueden observar los puntos en x que hacen que la función sea igual a 0. El problema radica en que no siempre el valor es un número sencillo, y en ocasiones puede tener muchas cifras decimales, lo que complica el análisis y la exactitud.</p>
"""

texto_pagina2_2 = """

<center><h1>Método de bisección para encontrar raíces de una función</h1></center>
<br>
<p>El método de bisección es un método numérico para encontrar la raíz de una función continua en un intervalo cerrado. Este es uno de los métodos cerrados más simples y robustos para encontrar la raíz de una función.</p>
<br>
<h3>EL MÉTODO DE BISECCIÓN PASO A PASO</h3>
<p><strong>Paso 1:</strong> Elija valores iniciales inferiores XL, y superiores Xu, que encierren la raíz, de forma tal que la función cambie de signo en el intervalo. Esto se verifica comprobando:</p>
<p style="margin-left: 30px;">f(XL) * f(Xu) &lt; 0</p>
<p><strong>Paso 2:</strong> Una aproximación de la raíz Xr se determina mediante:</p>
<p style="margin-left: 30px;">Xr = (XL + Xu) / 2</p>
<p><strong>Paso 3:</strong> Realice las siguientes evaluaciones para determinar en qué subintervalo está la raíz.</p>
<p style="margin-left: 30px;"><strong>a)</strong> Si f(XL)*f(Xr) &lt; 0 ; entonces la raíz se encuentra en el subintervalo inferior o izquierdo. Por lo tanto, haga Xu = Xr y vuelva al paso 2.</p>
<p style="margin-left: 30px;"><strong>b)</strong> Si f(Xl)*f(Xr) &gt; 0 ; entonces la raíz se encuentra dentro del subintervalo superior o derecho. Por lo tanto, haga XL = Xr y vuelva al paso 2.</p>
<p style="margin-left: 30px;"><strong>c)</strong> Si f(XL)*f(Xr) = 0, la raíz es igual a Xr; termina el cálculo.</p>
<br>
<br>
<h3>Ventajas y desventajas del método de bisección</h3>
<p><strong>Ventajas:</strong></p>
<ul>
  <li>El método de bisección siempre converge a una solución, a menos que la función no sea continua en el intervalo dado.</li>
  <li>El método es muy fácil de implementar.</li>
  <li>El método es muy robusto y no requiere conocimiento previo sobre la función o su comportamiento.</li>
</ul>
<p><strong>Desventajas:</strong></p>
<ul>
  <li>El método de bisección puede ser muy lento para encontrar la raíz, ya que se requieren varias iteraciones para alcanzar la precisión deseada.</li>
  <li>Si el intervalo inicial no es elegido adecuadamente, el método de bisección puede converger muy lentamente o puede no converger en absoluto.</li>
  <li>El método de bisección no proporciona información adicional sobre la función o su comportamiento, solo proporciona la raíz.</li>
</ul>
<h2>CONCLUSIÓN</h2>
<p>El método de bisección es un método numérico simple y robusto para encontrar la raíz de una función en un intervalo cerrado. Aunque es un método lento, es muy fácil de implementar y no requiere conocimiento previo sobre la función o su comportamiento. Sin embargo, se debe tener cuidado al elegir el intervalo inicial y es importante tener en cuenta que el método solo proporciona la raíz y no información adicional sobre la función o su comportamiento.</p>
"""

texto_pagina2_3 = """
<center><h1>La fórmula cuadrática y método de bisección</h1></center>
<br>
<p>La fórmula cuadrática se utiliza para encontrar las raíces de una ecuación cuadrática en la forma de ax^2 + bx + c = 0. La fórmula es la siguiente:</p>
<p>x = (-b ± sqrt(b^2 - 4ac)) / (2a)</p>
<p>Para la ecuación cuadrática -0.5x^2 + 2.5x + 4.5 = 0, tenemos los siguientes coeficientes:</p>
<p>a = -0.5</p>
<p>b = 2.5</p>
<p>c = 4.5</p>
<p>Sustituyendo estos valores en la fórmula cuadrática, obtenemos:</p>
<p>X1 = (-2.5 + sqrt(2.5^2 - 4(-0.5)(4.5))) / (2(-0.5))</p>
<p>X2 = (-2.5 - sqrt(2.5^2 - 4(-0.5)(4.5))) / (2(-0.5))</p>
<br>
<h2>Calculando los valores:</h2>
<p>
X1 ≈ 6.40512<br>
X2 ≈ -1.40512
</p>
<p>
Por lo tanto, los puntos que cortan la ecuación -0.5x^2 + 2.5x + 4.5 = 0 en 0 son X1 ≈ 6.40512 y X2 ≈ -1.40512. Siendo estos puntos la raíz de la ecuación.
</p>
<br>
<h2>Método Bisección:</h2>
<p>
Con tres iteraciones determinar el valor de la raíz más grande de la ecuación, empleando Xl = 5 y Xu = 10.
</p>
<center><h3>Iteración 1</h3>
<p>
<strong>Paso 1:</strong> XL = 5 ; Xu = 10<br>
f(XL) * f(Xu) = 4.5 * -20.5 = -92.25
</p>
<p>
<strong>Paso 2:</strong><br>
Xr = (10 + 5) / 2  = 7.5 ; f(Xr) = -4.875
</p>
<p>
<strong>Paso 3:</strong><br>
f(XL) * f(Xu) = 4.5 * -4.875 = -21.93  ; &lt; 0<br>
Xu = Xr = 7.5<br>
EPV = (6.40512 – 7.5) / 6.40512 * 100 = 17%
</p>
<h3>Iteración 2</h3>
<p>
<strong>Paso 2:</strong> XL = 5 ; Xu = 7.5<br>
Xr = (5 + 7.5) / 2 = 6.25; f(Xr) = 0.59375
</p>
<p>
<strong>Paso 3:</strong><br>
f(XL) * f(Xr) = 4.5 * 0.59375 = 2.6  ; &gt; 0<br>
XL = Xr = 6.25<br>
EPV = (6.40512 – 6.25) / 6.40512 * 100 = 2.42%<br>
EPA = (6.25 – 7.5) / 6.25 * 100 = 20%
</p>
<h3>Iteración 3</h3>
<p>
<strong>Paso 2:</strong> XL = 6.25 ; Xu = 7.5<br>
Xr = 6.875 ; f(Xr) = -1.9453125
</p>
<p>
<strong>Paso 3:</strong><br>
f(XL) * f(Xu) = -1.945 * -4.875 = 6.875 ; &gt; 0<br>
Xu = 6.875<br>
EPV = (6.40512 – 6.875) / 6.40512 * 100 = 7.3%<br>
EPA = (6.875 – 6.25) / 6.875 * 100 = 9%
</p></center>"""

texto_pagina3 = """
<center><h1>Método de Newton-Raphson</h1></center>
<br>
  <p>
    El método de Newton-Raphson es un método abierto para encontrar las raíces de una ecuación. Este método utiliza la idea de la aproximación lineal para iterativamente acercarse a la raíz de la ecuación.
  </p>
  <p>
    El proceso iterativo del método de Newton-Raphson se puede describir de la siguiente manera:
  </p>
  <ol>
    <li>Dado un punto inicial x₀ cercano a la raíz que queremos encontrar.</li>
    <li>Calcular el valor de la función en ese punto, f(x₀), y su derivada, f'(x₀).</li>
    <li>Utilizando la fórmula de la recta tangente, encontrar la intersección de la recta tangente con el eje x. Este punto de intersección será la siguiente aproximación de la raíz y se calcula mediante la siguiente fórmula: x₁ = x₀ - (f(x₀) / f'(x₀)).</li>
    <li>Repetir los pasos 2 y 3 usando x₁ como la nueva aproximación de la raíz.</li>
    <li>Continuar iterando hasta que la diferencia entre dos aproximaciones sucesivas sea suficientemente pequeña o hasta que se alcance un número máximo de iteraciones.</li>
  </ol>
  <p>
    El método de Newton-Raphson es altamente efectivo cuando se parte de un punto inicial lo suficientemente cerca de la raíz buscada y cuando la función es lo suficientemente suave.
  </p>
  <br>
  <h3>Ejemplo: Encontrando una raíz de una ecuación cúbica</h3>
  <p>
    Queremos encontrar una raíz de la ecuación cúbica x³ - 5x² + 4x - 2 = 0. Vamos a utilizar el método de Newton-Raphson para encontrar una aproximación de la raíz.
  </p>
  <ol>
    <li>Dado un punto inicial x₀ cercano a la raíz que queremos encontrar. Supongamos que x₀ = 2.</li>
    <li>Calculamos el valor de la función en ese punto, f(x₀), y su derivada, f'(x₀).</li>
    <ul>
      <li>f(x₀) = x₀³ - 5x₀² + 4x₀ - 2 = 2³ - 5(2)² + 4(2) - 2 = 8 - 20 + 8 - 2 = -6</li>
      <li>f'(x₀) = 3x₀² - 10x₀ + 4 = 3(2)² - 10(2) + 4 = 12 - 20 + 4 = -4</li>
    </ul>
    <li>Utilizamos la fórmula de Newton-Raphson para obtener la siguiente aproximación de la raíz:</li>
  <pre>
     x₁ = x₀ - (f(x₀) / f'(x₀)) = 2 - (-6 / -4) = 2 - 1.5 = 0.5
  </pre>
  <li>Repetimos los pasos 2 y 3 usando x₁ como la nueva aproximación de la raíz.</li>
  <li>Iteración 2:
    <ul>
      <li>Calculamos f(x₁) = x₁³ - 5x₁² + 4x₁ - 2 = 0.5³ - 5(0.5)² + 4(0.5) - 2 = 0.125 - 1.25 + 2 - 2 = -0.375</li>
      <li>Calculamos f'(x₁) = 3x₁² - 10x₁ + 4 = 3(0.5)² - 10(0.5) + 4 = 0.75 - 5 + 4 = -0.25</li>
      <li>Aplicamos la fórmula de Newton-Raphson: x₂ = x₁ - (f(x₁) / f'(x₁)) = 0.5 - (-0.375 / -0.25) = 0.5 + 1.5 = 2</li>
    </ul>
  </li>
  <li>Continuamos iterando hasta obtener la precisión deseada o hasta alcanzar un número máximo de iteraciones.</li>
</ol>
<p>El valor de x se acercará cada vez más a la raíz de la ecuación cúbica a medida que se realicen más iteraciones. Vale la pena señalar que en este ejemplo hemos encontrado una de las raíces posibles de la ecuación cúbica, pero existen otras dos raíces que podrían requerir puntos iniciales diferentes o iteraciones adicionales.</p>"""
class Pagina_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina1)

        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)

        # Crear widget central para la página 2
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class Pagina_2(QMainWindow):
    def __init__(self):
        super(Pagina_2, self).__init__()
        self.interface()

    def interface(self):
        # Establecer tamaño de ventana
        self.setGeometry(0, 0, 500, 500)

        # Crear QTabWidget
        self.tab_widget = QTabWidget()

        # Crear páginas como widgets
        self.page1 = pagina2_1()
        self.page2 = pagina2_2()
        self.page3 = pagina2_3()

        # Agregar páginas al QTabWidget
        self.tab_widget.addTab(self.page1, 'Grafica')
        self.tab_widget.addTab(self.page2, 'Metodo Bisección')
        self.tab_widget.addTab(self.page3, 'Ejemplo')

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

class pagina2_1(QMainWindow):
    def __init__(self):
        super(pagina2_1, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Cargar imagen y escalarla
        pixmap = QPixmap("imagenes/raiz-grafico.png")
        pixmap = pixmap.scaledToWidth(1400)

        # Crear QLabel para mostrar la imagen
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)

        # Crear widget de edición de texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina2_1)
        text_edit.setFixedHeight(500)
        text_edit.setReadOnly(True)  # hacer el texto no editable

        # Crear botón "Volver"
        button_volver = QPushButton("Volver")


        # Configurar objeto de diseño horizontal para centrar la imagen
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(image_label)
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


class pagina2_2(QMainWindow):
    def __init__(self):
        super(pagina2_2, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina2_2)
        text_edit.setReadOnly(True)
        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)

        # Crear widget central para la página 2
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

class pagina2_3(QMainWindow):
    def __init__(self):
        super(pagina2_3, self).__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear widget principal QScrollArea
        scroll_area = QScrollArea(self)

        # Crear contenido de la página 2 (por ejemplo, un widget o diseño)
        content_widget = QWidget()

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setHtml(texto_pagina2_3)
        text_edit.setReadOnly(True)
        text_edit.setFixedHeight(1500)


        # Configurar objeto de diseño horizontal para centrar la imagen
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(Biseccion())
        h_layout.addStretch()
        h_layout.addWidget(Grafico_Biseccion())

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

class Biseccion(QMainWindow):

    def __init__(self):
        super(Biseccion, self).__init__()
        self.interface()

    def interface(self):
        # Crear el botón y conectarlo a la función calcular_raiz
        btn_calcula = QPushButton('Calcular raíz', self)
        btn_calcula.clicked.connect(self.biseccion)

        # label de la ecuación
        ecuacion = QTextEdit()
        ecuacion.setHtml("<center><h3>-0.5x^2+2.5x+4.5</h3></center>")
        ecuacion.setReadOnly(True)
        ecuacion.setFixedHeight(50)

        # Crear el QLabel para la etiqueta 'Raiz a buscar'
        raiz_label = QLabel("Raiz a comparar: ")

        # Crear el QComboBox con las opciones 'a' y 'b'
        self.raiz = QComboBox(self)
        self.raiz.addItem('-1.40512')
        self.raiz.addItem('6.40512')

        # Crear el QHBoxLayout y agregar la etiqueta y el combo box
        layoutH_raiz = QHBoxLayout()
        layoutH_raiz.addWidget(raiz_label)
        layoutH_raiz.addWidget(self.raiz)

        label_xl = QLabel("Xl: ")
        self.xl = QLineEdit()
        label_xu = QLabel("Xu: ")
        self.xu = QLineEdit()
        error_label = QLabel("Porcentaje de error")
        self.error_input = QLineEdit()
        self.error_input.setText("0.05")
        # Formulario
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_xl)
        form_layout.addWidget(self.xl)
        form_layout.addWidget(label_xu)
        form_layout.addWidget(self.xu)
        layout_error = QHBoxLayout()
        layout_error.addWidget(error_label)
        layout_error.addWidget(self.error_input)

        layoutV_1 = QVBoxLayout()
        layoutV_1.addLayout(form_layout)
        layoutV_1.addLayout(layout_error)


        # Crear el QTextEdit para ingresar los números
        self.txt_operacion = QTextEdit(self)
        self.txt_operacion.setFixedWidth(800)
        self.txt_operacion.setFixedHeight(200)
        self.txt_operacion.setReadOnly(True)

        # Crear el QVBoxLayout y agregar el layout horizontal, el QTextEdit y el botón
        layoutV_general = QVBoxLayout()
        layoutV_general.addWidget(ecuacion)
        layoutV_general.addLayout(layoutH_raiz)
        layoutV_general.addLayout(layoutV_1)
        layoutV_general.addWidget(self.txt_operacion)
        layoutV_general.addWidget(btn_calcula)

        # Crear el widget central y establecer el layout
        widget = QWidget(self)
        widget.setLayout(layoutV_general)

        # Establecer el widget central de la ventana
        self.setCentralWidget(widget)

    def biseccion(self):

        raiz = float(self.raiz.currentText())

        def primera(x):
            return (-0.5 * (x ** 2)) + (2.5 * x) + 4.5

        try:
            self.txt_operacion.setText("")
            xl = float(self.xl.text())
            xu = float(self.xu.text())
            error = float(self.error_input.text())
            if primera(xl) * primera(xu) < 0:
                iterar = 1
                error_verdadero = 100
                while error_verdadero > error:
                    xr = (xl + xu) / 2
                    fxr = primera(xr)
                    resultado = primera(xl) * fxr
                    error_verdadero = round(abs(((raiz - xr) / raiz) * 100), 3)
                    self.txt_operacion.insertHtml(f"<center>{iterar}) {round(xr, 5)}; f(x) = {round(resultado, 5)}; Error: {error_verdadero}%<center><br>")
                    iterar += 1
                    if resultado < 0:
                        xu = xr
                    elif resultado > 0:
                        xl = xr
                    else:
                        break
                    if error_verdadero <= error:
                        break
            else:
                self.txt_operacion.setText("No se encuentra raiz.")

        except:
            self.txt_operacion.setText(f"Datos incoherentes")

class Grafico_Biseccion(QWidget):
    def __init__(self):
        super(Grafico_Biseccion, self).__init__()
        self.interface()

    def interface(self):
        self.grafico()
        main_form = QFormLayout(self)
        main_form.addRow(self.canvas)

    def grafico(self):
        def f1(x):
            return (-0.5 * (x ** 2)) + (2.5 * x) + 4.5

        # para graficar conforme se pida requerimientos

        # Crear el canvas de la figura
        self.canvas = FigureCanvas(plt.figure())

        # Valores del eje X que toma el gráfico.
        x = range(-10, 15)

        # Graficar funcion.
        plt.plot(x, [f1(i) for i in x])

        # Establecer el color de los ejes.
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        # Limitar los valores de los ejes.
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        plt.title('Función -0.5x^2+2.5x+4.5')
        plt.grid()


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
        self.page1 = pagina3_1()

        # Agregar páginas al QTabWidget
        self.tab_widget.addTab(self.page1, 'Metodo de Newton-Raphson')

        # Crear botones para cambiar de página

        # Crear diseño vertical
        layout = QVBoxLayout(self)
        layout.addWidget(self.tab_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_to_page1(self):
        self.tab_widget.setCurrentWidget(self.page1)

class pagina3_1(QMainWindow):
    def __init__(self):
        super(pagina3_1, self).__init__()
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


if __name__ == '__main__':
    app = QApplication([])
    ventana = Pagina_2()
    ventana.show()
    app.exec()