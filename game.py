
import pygame
import random
import string

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Practica de Teclado")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Fuente y tamaño de texto
fuente = pygame.font.Font(None, 74)

# Inicializar variables
letra = random.choice(string.ascii_uppercase)  # Letra aleatoria
x = random.randint(50, ANCHO - 50)  # Posición inicial en X
y = 0  # Posición inicial en Y
velocidad = 5  # Velocidad de caída
puntaje = 0

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.unicode.upper() == letra:  # Verificar la tecla presionada
                puntaje += 1
                letra = random.choice(string.ascii_uppercase)
                x = random.randint(50, ANCHO - 50)
                y = 0

    # Actualizar la posición de la letra
    y += velocidad
    if y > ALTO:  # Si la letra llega al fondo
        letra = random.choice(string.ascii_uppercase)
        x = random.randint(50, ANCHO - 50)
        y = 0

    # Dibujar en la pantalla
    ventana.fill(NEGRO)
    texto = fuente.render(letra, True, BLANCO)
    ventana.blit(texto, (x, y))

    # Mostrar puntaje
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, ROJO)
    ventana.blit(texto_puntaje, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limitar a 30 FPS

pygame.quit()









