import turtle
import math

# Configurar la ventana de dibujo
window = turtle.Screen()
window.bgcolor("sky blue")

# Crear un objeto Turtle para dibujar
girasol = turtle.Turtle()
girasol.shape("circle")
girasol.color("yellow")
girasol.speed(2)  # Velocidad máxima

# Función para dibujar un pétalo
def dibujar_petalo():
    for _ in range(2):
        girasol.circle(50, 60)
        girasol.left(120)

# Función para dibujar el girasol completo
def dibujar_girasol():
    for _ in range(6):
        dibujar_petalo()
        girasol.left(60)
    girasol.right(90)
    girasol.forward(200)

# Mover el girasol al centro
girasol.penup()
girasol.goto(0, -200)
girasol.pendown()

# Dibujar el girasol
dibujar_girasol()

# Ocultar el objeto Turtle
girasol.hideturtle()

# Cerrar la ventana al hacer clic en ella
window.exitonclick()
