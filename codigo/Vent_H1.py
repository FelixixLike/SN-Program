from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QMainWindow, \
    QStackedWidget, QGridLayout, QTextEdit, QScrollArea, QLabel, QLineEdit, QFormLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import operator
import math
import sys
from PyQt6.QtGui import QIcon
from Style import style
import math

texto_pagina = """
<center><h2>MODELADO MATEMÁTICO SIMPLE</h2></center>
<br>
<p>Es una formulación o una ecuación que expresa las características esenciales de un sistema físico o de un proceso en términos matemáticos.</p>
<p><strong>Variable dependiente = f(variables independientes, parámetros, funciones de fuerza)</strong></p>
<p>En física: F = m.a => a = F/m<br>
Donde F => Función fuerza<br>
m => Parámetro</p>
<p><strong>Características típicas de modelos matemáticos en física:</strong></p>
<ul>
<li>Matematiza</li>
<li>Idealiza</li>
<li>Reproduce Resultados</li>
</ul>
<p>La situación general de caída libre:</p>
<p>Solución analítica: (dv/dt = mg - cv/m = g - c/m .v) donde para resolver esta ecuación, se utilizan condiciones de frontera v = 0 en t = 0.<br>
V(t) = gm/c .(1-e^(c/m)t)<br>
Donde<br>
V(t) => Variable dependiente<br>
t => Variable independiente<br>
c, m => Parámetros<br>
g => Función de fuerza</p>
<p>Solución Numérica: dv/dt = ∆v/∆t = V(ti+1) - V(ti) / ti+1 - ti. Aproximación en diferencia finita dividida de la derivada en el tiempo ti, el resultado es aproximado porque ∆t es finito. Sustituyendo daría lo siguiente:<br>
V(ti+1) = V(ti) + [g - c/m . V(ti)] (ti+1 - ti)</p>
<br>
<p><strong>Ejemplo:</strong> Calcular la velocidad de un paracaidista antes de que se abra el paracaídas. m = 68.1 kg, coeficiente de fricción = 12.5 kg/s. Lo resolveremos con los dos métodos para comparar los resultados:</p>
<br>
<center><table>
    <thead>
        <tr>
            <th>    MÉTODO ANALÍTICO</th>
            <th></th>
            <th></th>
            <th></th>
            <th>    MÉTODO NUMÉRICO</th>
            <th></th>
            <th></th>
            <th></th>
        </tr>
        <tr>
            <th>t(s)</th>
            <th>V(m/s)</th>
            <th></th>
            <th></th>
            <th>t(s)</th>
            <th>V(m/s)</th>
            <th></th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
            <td>0.0</td>
            <td></td>
            <td></td>
            <td>0</td>
            <td>0.0</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>2</td>
            <td>16.4</td>
            <td></td>
            <td></td>
            <td>2</td>
            <td>19.6</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>4</td>
            <td>27.77</td>
            <td></td>
            <td></td>
            <td>4</td>
            <td>32.0</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>6</td>
            <td>35.64</td>
            <td></td>
            <td></td>
            <td>6</td>
            <td>39.85</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>8</td>
            <td>41.10</td>
            <td></td>
            <td></td>
            <td>8</td>
            <td>44.82</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>10</td>
            <td>44.87</td>
            <td></td>
            <td></td>
            <td>10</td>
            <td>47.97</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>12</td>
            <td>47.49</td>
            <td></td>
            <td></td>
            <td>12</td>
            <td>49.96</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>100</td>
            <td>53.39</td>
            <td></td>
            <td></td>
            <td>100</td>
            <td>53.39</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table> </center>"""



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

        # Crear texto con título en negrita
        text_edit = QTextEdit()
        text_edit.setFixedHeight(1100)
        text_edit.setReadOnly(True)
        text_edit.setHtml(texto_pagina)


        # Crear botón "Volver"
        button_volver = QPushButton("Volver")

        # Configurar diseño horizontal para las imágenes
        images_layout = QHBoxLayout()

        # Metodos en vertical
        label_s_a = QLabel("Solución Analítica caída libre")
        label_s_m_n = QLabel("Solución método Numérico")
        layout_v_1 = QVBoxLayout()
        layout_v_1.addWidget(label_s_a)
        layout_v_1.addWidget(solucion_analitica())
        layout_v_2 = QVBoxLayout()
        layout_v_2.addWidget(label_s_m_n)
        layout_v_2.addWidget(solucion_m_numerico())


        # Metodos en horizontal
        layout_h = QHBoxLayout()
        layout_h.addLayout(layout_v_1)
        layout_h.addLayout(layout_v_2)

        # Configurar diseño vertical para el contenido de la página 2
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        layout.addLayout(layout_h)

        # Añadir espacio flexible en el layout para que se expanda y se ajuste al tamaño de la ventana
        layout.addStretch()

        content_widget.setLayout(layout)
        scroll_area.setWidget(content_widget)
        scroll_area.setWidgetResizable(True)  # Hacer que el contenido del scroll sea redimensionable
        self.setCentralWidget(scroll_area)

class solucion_analitica(QWidget):
    def __init__(self):
        super().__init__()
        self.interfece()

    def interfece(self):

        # Crear inputs
        self.masa_input = QLineEdit(self)
        self.gravedad_input = QLineEdit(self)
        self.coeficiente_input = QLineEdit(self)
        self.pasos_input = QLineEdit(self)
        self.masa_input.setText("61.8")
        self.gravedad_input.setText("9.8")
        self.coeficiente_input.setText("12.5")
        self.pasos_input.setText("2")

        # Texto
        formula = QLabel("(g*masa)/c_resistencia)* (1 - (e^-(c_resistencia/masa)) * tiempo")

        # Pantalla
        self.pantalla = QTextEdit()
        self.pantalla.setFixedHeight(350)
        self.pantalla.setReadOnly(True)

        # Boton
        self.boton = QPushButton("Operar")
        self.boton.clicked.connect(self.calcular)

        # Formulario
        form_layout_1 = QFormLayout()
        form_layout_1.addRow(QLabel("Masa:"), self.masa_input)
        form_layout_1.addRow(QLabel("Gravedad:"), self.gravedad_input)
        form_layout_2 = QFormLayout()
        form_layout_2.addRow(QLabel("Coeficiente f:"), self.coeficiente_input)
        form_layout_2.addRow(QLabel("Pasos:"), self.pasos_input)

        # Layout horizontal
        form_h_layout = QHBoxLayout()
        form_h_layout.addLayout(form_layout_1)
        form_h_layout.addLayout(form_layout_2)

        # Layout vertical
        form_v_layout = QVBoxLayout()
        form_v_layout.setContentsMargins(20, 20, 20, 20)  # Margen de 20 pixeles en los 4 lados
        form_v_layout.addLayout(form_h_layout)
        form_v_layout.addWidget(formula)
        form_v_layout.addWidget(self.boton)
        form_v_layout.addWidget(self.pantalla)

        self.setLayout(form_v_layout)

    def calcular(self):

        def sa_caida_libre(masa, c_resistencia, tiempo, g):
            """Desarrollas función de sistema analitico caida libre"""
            operacion = ((g * masa) / c_resistencia) * (1 - (math.e ** -(c_resistencia / masa * tiempo)))
            return operacion

        try:
            coeficiente = float(self.coeficiente_input.text())
            salto = float(self.pasos_input.text())
            masa = float(self.masa_input.text())
            g = float(self.gravedad_input.text())

            self.pantalla.setHtml("")
            self.pantalla.insertHtml("""<center>
                                    <h2>METODO ANALITICO</h2>
                                    <h3>t(s) | V(m/s)</h3> 
                                    <h3>----    ------</h3>
                                    </center>\n
                            """)
            resultado = 0
            contar = 0
            if salto > 0.05:
                while contar < 101:
                    resultado = sa_caida_libre(masa, coeficiente, contar, g)
                    self.pantalla.insertHtml(f"<center><br>{round(contar, 2)} &nbsp;&nbsp; | &nbsp;&nbsp; {round(resultado, 3)}m/s"
)
                    contar += salto
            else:
                self.pantalla.setPlainText(f"Los pasos deben ser mayor a 0.05")

        except:
            self.pantalla.setPlainText(f"Debes rellenar todos los espacios con números")


class solucion_m_numerico(QWidget):
    def __init__(self):
        super().__init__()
        self.interfece()

    def interfece(self):
        # Establecer color de la ventana

        # Crear inputs
        self.masa_input = QLineEdit(self)
        self.gravedad_input = QLineEdit(self)
        self.coeficiente_input = QLineEdit(self)
        self.pasos_input = QLineEdit(self)

        self.masa_input.setText("61.8")
        self.gravedad_input.setText("9.8")
        self.coeficiente_input.setText("12.5")
        self.pasos_input.setText("2")

        # Texto
        formula = QLabel("velocidad + (g - (c_resistencia/ masa) * velocidad}) * (tiempo + salto - tiempo)")

        # Pantalla
        self.pantalla = QTextEdit()
        self.pantalla.setHtml("")
        self.pantalla.setReadOnly(True)

        # Boton
        self.boton = QPushButton("Operar")
        self.boton.clicked.connect(self.calcular)

        # Formulario
        form_layout_1 = QFormLayout()
        form_layout_1.addRow(QLabel("Masa:"), self.masa_input)
        form_layout_1.addRow(QLabel("Gravedad:"), self.gravedad_input)
        form_layout_2 = QFormLayout()
        form_layout_2.addRow(QLabel("Coeficiente f:"), self.coeficiente_input)
        form_layout_2.addRow(QLabel("Pasos:"), self.pasos_input)

        # Layout horizontal
        form_h_layout = QHBoxLayout()
        form_h_layout.addLayout(form_layout_1)
        form_h_layout.addLayout(form_layout_2)

        # Layout vertical
        form_v_layout = QVBoxLayout()
        form_v_layout.setContentsMargins(20, 20, 20, 20)  # Margen de 20 pixeles en los 4 lados
        form_v_layout.addLayout(form_h_layout)
        form_v_layout.addWidget(formula)
        form_v_layout.addWidget(self.boton)
        form_v_layout.addWidget(self.pantalla)

        self.setLayout(form_v_layout)

    def calcular(self):

        def a_caida_libre_metodo_e(velocidad, masa, c_resistencia, tiempo, salto, g):
            """Desarrolla el metodo de eules retorna resultado"""
            iteracion = tiempo + 1
            if iteracion == 1:
                return 0
            """print(velocidad + (g - (c_resistencia/ masa) * velocidad}) * (tiempo + salto - tiempo))"""
            velocidad = (velocidad) + (g - (c_resistencia / masa) * velocidad) * (tiempo + salto - tiempo)
            return velocidad

        try:
            coeficiente = float(self.coeficiente_input.text())
            salto = float(self.pasos_input.text())
            masa = float(self.masa_input.text())
            g = float(self.gravedad_input.text())
            print(salto)
            self.pantalla.setHtml("")
            self.pantalla.insertHtml("""<center>
                                    <h2>METODO NUMÉRICO EULER</h2>
                                    <h3>t(s) | V(m/s)</h3> 
                                    <h3>----    ------</h3>
                                    </center>\n
                            """)
            resultado = 0
            contar = 0
            if salto > 0.5:

                while contar < 101:
                    resultado = a_caida_libre_metodo_e(resultado, masa, coeficiente, contar, salto, g)
                    self.pantalla.insertHtml(f"<center><br>{round(contar, 2)} &nbsp;&nbsp; | &nbsp;&nbsp; {round(resultado, 3)}m/s"
)
                    contar += salto
            else:
                self.pantalla.setPlainText(f"Los pasos deben ser mayor a 0.5")

        except:
            self.pantalla.setPlainText(f"Debes rellenar todos los espacios con números")


