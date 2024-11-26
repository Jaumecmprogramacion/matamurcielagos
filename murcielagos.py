import turtle
import random
import math

# Configuración inicial
ventana = turtle.Screen()
ventana.setup(800, 600)
ventana.bgcolor("navy")
ventana.title("Caza Murciélagos y Esquiva Calaveras")
ventana.tracer(0)

# Crear forma de murciélago
def crear_forma_murcielago():
    forma = turtle.Turtle()
    forma.hideturtle()
    forma.penup()
    forma.color("dark gray")
    forma.begin_poly()
    forma.goto(0, 0)
    forma.goto(10, 5)
    forma.goto(15, 10)
    forma.goto(20, 5)
    forma.goto(25, 0)
    forma.goto(20, -5)
    forma.goto(10, -10)
    forma.goto(0, -5)
    forma.goto(-10, -10)
    forma.goto(-20, -5)
    forma.goto(-25, 0)
    forma.goto(-20, 5)
    forma.goto(-15, 10)
    forma.goto(-10, 5)
    forma.goto(0, 0)
    forma.end_poly()
    return forma.get_poly()

forma_murcielago = crear_forma_murcielago()
ventana.register_shape("murcielago", forma_murcielago)

# Crear forma de calavera
def crear_forma_calavera():
    forma = turtle.Turtle()
    forma.hideturtle()
    forma.penup()
    forma.color("white")
    forma.begin_poly()
    forma.circle(10)
    forma.goto(-5, -10)
    forma.goto(5, -10)
    forma.goto(0, -5)
    forma.goto(-5, -10)
    forma.end_poly()
    return forma.get_poly()

forma_calavera = crear_forma_calavera()
ventana.register_shape("calavera", forma_calavera)

class Murcielago(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("murcielago")
        self.color("dark gray")
        self.shapesize(0.8, 0.8)
        self.setheading(random.randint(0, 360))
        self.goto(random.randint(-380, 380), random.randint(-280, 280))
        self.velocidad = random.uniform(2, 4)
        self.tiempo_aleteo = random.uniform(0, 2 * math.pi)
    
    def mover(self):
        if random.random() < 0.05:
            self.left(random.randint(-30, 30))
        
        self.forward(self.velocidad)
        
        self.tiempo_aleteo += 0.3
        factor_aleteo = math.sin(self.tiempo_aleteo) * 0.2 + 1
        self.shapesize(0.8 * factor_aleteo, 0.8)
        
        x, y = self.pos()
        if x < -390 or x > 390:
            self.setheading(180 - self.heading())
        if y < -290 or y > 290:
            self.setheading(-self.heading())

class Calavera(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("calavera")
        self.color("white")
        self.shapesize(1.2, 1.2)
        self.setheading(random.randint(0, 360))
        self.goto(random.randint(-380, 380), random.randint(-280, 280))
        self.velocidad = random.uniform(1, 3)
    
    def mover(self):
        if random.random() < 0.03:
            self.left(random.randint(-20, 20))
        
        self.forward(self.velocidad)
        
        x, y = self.pos()
        if x < -390 or x > 390:
            self.setheading(180 - self.heading())
        if y < -290 or y > 290:
            self.setheading(-self.heading())

# Crear murciélagos y calaveras
murcielagos = [Murcielago() for _ in range(15)]
calaveras = [Calavera() for _ in range(5)]

# Configurar marcador
marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.goto(0, 260)
marcador.color("white")

puntos = 0

def actualizar_marcador():
    marcador.clear()
    marcador.write(f"Puntos: {puntos}   Tiempo: {tiempo_restante}", align="center", font=("Arial", 16, "normal"))

# Configurar temporizador
temporizador = turtle.Turtle()
temporizador.hideturtle()
temporizador.penup()
temporizador.goto(0, -260)
temporizador.color("white")

tiempo_inicial = 60
tiempo_restante = tiempo_inicial

def actualizar_temporizador():
    global tiempo_restante
    tiempo_restante = max(0, tiempo_restante - 1)
    actualizar_marcador()
    if tiempo_restante > 0:
        ventana.ontimer(actualizar_temporizador, 1000)
    else:
        temporizador.clear()
        temporizador.write("¡Tiempo terminado!", align="center", font=("Arial", 24, "normal"))

# Función para manejar clics
def clic(x, y):
    global puntos
    for murcielago in murcielagos:
        if murcielago.distance(x, y) < 15:
            puntos += 1
            actualizar_marcador()
            murcielago.goto(random.randint(-380, 380), random.randint(-280, 280))
            return
    for calavera in calaveras:
        if calavera.distance(x, y) < 18:
            puntos -= 10
            actualizar_marcador()
            calavera.goto(random.randint(-380, 380), random.randint(-280, 280))
            return

# Registrar función de clic
ventana.onclick(clic)

# Función principal de animación
def animar():
    for murcielago in murcielagos:
        murcielago.mover()
    for calavera in calaveras:
        calavera.mover()
    ventana.update()
    if tiempo_restante > 0:
        ventana.ontimer(animar, 50)

# Iniciar juego
actualizar_marcador()
actualizar_temporizador()
animar()

ventana.mainloop()
