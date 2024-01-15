# X_L

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

    <h1 style="text-align:center;">Diferenciación Numérica</h1>
    <br>
  <p>La diferenciación numérica es una técnica utilizada para aproximar las derivadas de una función cuando no es posible obtener una expresión analítica para dichas derivadas. En el contexto de los sistemas de ecuaciones no lineales, la diferenciación numérica se aplica para aproximar las derivadas parciales de las ecuaciones que componen el sistema.</p>

<p>La diferenciación numérica se basa en la idea de que la derivada de una función puede aproximarse mediante una diferencia finita entre dos puntos cercanos. En el caso de sistemas de ecuaciones no lineales, se utilizan métodos de diferencias finitas para aproximar las derivadas parciales de las ecuaciones.</p>

<p>Existen varios métodos de diferenciación numérica que se pueden aplicar en sistemas de ecuaciones no lineales. Algunos de los métodos más comunes son:</p>

<ul>
  <li>Diferencias finitas hacia adelante: Este método aproxima la derivada de una función utilizando la diferencia entre los valores de la función en dos puntos cercanos. Para aproximar las derivadas parciales de un sistema de ecuaciones, se aplica este método a cada ecuación del sistema.</li>
  <li>Diferencias finitas hacia atrás: Similar al método de diferencias finitas hacia adelante, pero utiliza los valores de la función en dos puntos cercanos pero anteriores para aproximar la derivada.</li>
  <li>Diferencias finitas centradas: Este método utiliza los valores de la función en dos puntos cercanos, uno anterior y otro posterior al punto en el que se desea aproximar la derivada. Proporciona una mayor precisión en comparación con los métodos de diferencias finitas hacia adelante o hacia atrás.</li>
</ul><h2>Fórmulas</h2>
    <br>
    <center><img src="imagenes/diferenciacion_numerica.png"  height="300"></center>
    <br>
    <p>Es importante tener en cuenta que la diferenciación numérica introduce errores de aproximación, por lo que la precisión de los resultados obtenidos dependerá de la elección adecuada del tamaño de paso y del método de diferenciación utilizado. Además, es posible que se requieran varios iteraciones para obtener una solución convergente.</p>
    <hr>
    <h2>Ejemplo Práctico</h2>
    <div class="example">
        <p>Consideremos la función f(x) = x^2 + 2x + 1.</p>
        <p>Para calcular la derivada de f(x) en x = 2 usando diferencias hacia adelante con h = 0.1:</p>
        <pre>
            var h = 0.1;
            var x = 2;
            var derivative = (Math.pow(x + h, 2) + 2*(x + h) + 1 - (Math.pow(x, 2) + 2*x + 1)) / h;
            console.log("f'(2) =", derivative);
        </pre>
        <p>El resultado obtenido sería f'(2) ≈ 6.4.</p>
    </div>"""

# X_L
texto_pagina2 = """
<h1 style="text-align:center;">Integración Numérica</h1>
<br>

<p>La integración numérica para sistemas de ecuaciones no lineales es una técnica utilizada para aproximar las soluciones de sistemas de ecuaciones que no pueden resolverse de forma analítica. Estos sistemas pueden contener ecuaciones no lineales, lo que significa que no se pueden resolver directamente mediante métodos algebraicos.</p>
<br>
 <h1>Regla del trapecio</h1>
 <br>
 <center><img src="imagenes/integracion_numerica.png"></center>
<br>
  <p>La regla del trapecio es un método de integración numérica que se utiliza para aproximar el valor de una integral definida. Este método se basa en aproximar el área bajo la curva de una función mediante la suma de áreas de trapecios.</p>
  <p>La regla del trapecio se puede aplicar de forma general para una función f(x) en un intervalo [a, b] de la siguiente manera:</p>
  <p>∫[a, b] f(x) dx ≈ h/2 * [f(a) + 2f(x1) + 2f(x2) + ... + 2f(xn-1) + f(b)]</p>
  <p>Donde h es el tamaño del intervalo (h = (b - a)/n) y n es el número de subintervalos utilizados para aproximar la integral. Los valores x1, x2, ..., xn-1 son los puntos dentro de cada subintervalo.</p>
  
  <h2>Ejemplo:</h2>
  <p>Supongamos que queremos aproximar la integral definida de la función f(x) = x^2 en el intervalo [0, 2] utilizando la regla del trapecio con n = 4 subintervalos.</p>
  <p>Paso 1: Calcular el tamaño del intervalo (h):</p>
  <p>h = (b - a) / n = (2 - 0) / 4 = 0.5</p>
  <p>Paso 2: Calcular los puntos dentro de cada subintervalo:</p>
  <p>x0 = 0</p>
  <p>x1 = 0.5</p>
  <p>x2 = 1</p>
  <p>x3 = 1.5</p>
  <p>x4 = 2</p>
  <p>Paso 3: Calcular los valores de la función en los puntos de los subintervalos:</p>
  <p>f(x0) = f(0) = 0^2 = 0</p>
  <p>f(x1) = f(0.5) = (0.5)^2 = 0.25</p>
  <p>f(x2) = f(1) = 1^2 = 1</p>
  <p>f(x3) = f(1.5) = (1.5)^2 = 2.25</p>
  <p>f(x4) = f(2) = 2^2 = 4</p>
  <p>Paso 4: Aplicar la fórmula de la regla del trapecio:</p>
  <p>∫[0, 2] x^2 dx ≈ h/2 * [f(0) + 2f(0.5) + 2f(1) + 2f(1.5) + f(2)]</p>
  <p>≈ 0.5/2 * [0 + 2(0.25) + 2(1) + 2(2.25) + 4]</p>
  <p>≈ 0.25 * [0 + 0.5 + 2 + 4.5 + 4]</p>
  <p>≈ 0.25 * 11.5</p>
  <p>≈ 2.875</p>
  <p>Por lo tanto, utilizando la regla del trapecio con n = 4 subintervalos, la aproximación de la integral definida de f(x) = x^2 en el intervalo [0, 2] es 2.875.</p>
  <p>Es importante destacar que cuanto mayor sea el número de subintervalos utilizados (n), más precisa será la aproximación de la integral. La regla del trapecio es un método sencillo pero puede no ser tan preciso como otros métodos de integración numérica, especialmente cuando se integran funciones con curvas complicadas.</p>


"""


texto_pagina3 = """
<h1 style="text-align:center;">Método de Euler para Resolver Ecuaciones Diferenciales</h1>
<br>
<p>El método de Euler es un método numérico utilizado para resolver ecuaciones diferenciales ordinarias (EDOs). Es un método de primer orden que se basa en la aproximación de la derivada de una función mediante una diferencia finita. Aunque es un método simple, puede proporcionar una solución aproximada útil para ecuaciones diferenciales en sistemas de ecuaciones no lineales.</p>

<h2>Fórmula del Método de Euler</h2>
<p>La fórmula del método de Euler para resolver una EDO de primer orden es la siguiente:</p>

<pre>
y<sub>n+1</sub> = y<sub>n</sub> + h * f(x<sub>n</sub>, y<sub>n</sub>)
</pre>

<p>Donde:</p>
<ul>
  <li><code>y<sub>n</sub></code> es el valor aproximado de la función en el punto <code>x<sub>n</sub></code>.</li>
  <li><code>h</code> es el tamaño del paso, es decir, la distancia entre los puntos <code>x<sub>n</sub></code> y <code>x<sub>n+1</sub></code>.</li>
  <li><code>f(x<sub>n</sub>, y<sub>n</sub>)</code> es la función que define la EDO en términos de la variable independiente <code>x</code> y la función desconocida <code>y(x)</code>.</li>
</ul>

<h2>Ejemplo Práctico</h2>
<p>Supongamos que queremos resolver la siguiente EDO de primer orden:</p>

<pre>
dy/dx = x^2 + y
y(0) = 1
</pre>

<p>Usaremos el método de Euler con un tamaño de paso <code>h = 0.1</code> para aproximar la solución en el intervalo <code>[0, 1]</code>.</p>

<ol>
  <li>Inicializar los valores:</li>
  <pre>
  <li>x<sub>0</sub> = 0</li>
  <li>y<sub>0</sub> = 1</li>
  </pre>
  <li>Calcular <code>y<sub>n+1</sub></code> en cada paso utilizando la fórmula del método de Euler:</li>
  <pre>
  <li>x<sub>1</sub> = x<sub>0</sub> + h = 0 + 0.1 = 0.1</li>
  <li>y<sub>1</sub> = y<sub>0</sub> + h * (x<sub>0</sub>^2 + y<sub>0</sub>) = 1 + 0.1 * (0^2 + 1) = 1.1</li>

  <li>x<sub>2</sub> = x<sub>1</sub> + h = 0.1 + 0.1 = 0.2</li>
  <li>y<sub>2</sub> = y<sub>1</sub> + h * (x<sub>1</sub>^2 + y<sub>1</sub>) = 1.1 + 0.1 * (0.1^2 + 1.1) = 1.221</li>
  
  ...
</ol>

<p>Continúa este proceso hasta alcanzar el punto final deseado.</p>

<p>En este caso, los valores aproximados de <code>y</code> en cada paso se obtienen utilizando la fórmula del método de Euler. Siguiendo el proceso descrito, puedes calcular los valores aproximados de <code>y</code> para los puntos <code>x</code> correspondientes.</p>

<p>Recuerda que el método de Euler es un método de primer orden y puede tener errores acumulativos significativos a medida que se aleja del punto inicial. En sistemas de ecuaciones no lineales, pueden requerirse métodos numéricos más avanzados y precisos para obtener soluciones más precisas.</p>

"""

class Pagina_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
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
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml(texto_pagina2)

        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)

        # Crear widget central para la página 2
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

class Pagina_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setGeometry(0, 0, 500, 500)

        # Crear texto
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml(texto_pagina3)

        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)

        # Crear widget central para la página 2
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

# X_L