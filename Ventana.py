class Ventana:
    __titulo = ""
    __valor_x_superior = 0
    __valor_y_superior = 0
    __valor_x_inferior = 0
    __valor_y_inferior = 0

    def __init__(self, titulo, valor_x_superior=0, valor_y_superior=0, valor_x_inferior=500, valor_y_inferior=500):
        self.__titulo = titulo
        self.__valor_x_superior = valor_x_superior
        self.__valor_y_superior = valor_y_superior
        self.__valor_x_inferior = valor_x_inferior
        self.__valor_y_inferior = valor_y_inferior

    def mostar(self):
        return print(f"""Nombre {self.__titulo}
Valores Superior Izquierda(x,y): {self.__valor_x_superior, self.__valor_y_superior}
Valores Infrerior Derecha(x,y): {self.__valor_x_inferior, self.__valor_y_inferior}""")

    def gettitulo(self):
        return str(self.__titulo)

    def alto(self):
        return self.__valor_x_inferior - self.__valor_x_superior

    def ancho(self):
        return self.__valor_y_inferior - self.__valor_y_superior

    def moverderecha(self, i):
        self.__valor_x_inferior = self.__valor_x_inferior + i
        self.__valor_x_superior = self.__valor_x_superior + i

    def moverizquierda(self, i):
        self.__valor_x_inferior = self.__valor_x_inferior - i
        self.__valor_x_superior = self.__valor_x_superior - i

    def bajar(self, i):
        self.__valor_y_superior = self.__valor_y_superior - i
        self.__valor_y_inferior = self.__valor_y_inferior - i
