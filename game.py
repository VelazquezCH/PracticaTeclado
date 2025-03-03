import pygame
import random
import string

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Practica de Teclado - Niveles con Letras")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Fuente
fuente = pygame.font.Font(None, 74)

# Variables
letra_personalizadas = ["A", "E", "I", "O", "U"] # Define el rango personalizado de letras (ejemplo: solo vocales)
letra_actual = random.choice(string.ascii_uppercase)  # Seleccionar letra aleatoria
nivel = 1
velocidad = 5
puntaje = 0
x, y = random.randint(50, ANCHO - 50), 0

# Variables para efectos visuales
mensaje = ""
color_mensaje = BLANCO
contador_efecto = 0  # Controla cuánto tiempo se muestra el mensaje



# Función para mostrar el menú de selección de nivel
def menu_seleccion_nivel():
    seleccionando = True
    nivel_seleccionado = 1

    while seleccionando:
        ventana.fill(NEGRO)

        # Título del menú
        titulo = fuente.render("Selecciona el Nivel", True, BLANCO)
        ventana.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))

        # Dibujar botones de niveles
        for i in range(1, 6):  # Niveles del 1 al 5
            color = AZUL if nivel_seleccionado == i else BLANCO
            texto_nivel = pygame.font.Font(None, 40).render(f"Nivel {i}", True, color)
            ventana.blit(texto_nivel, (ANCHO // 2 - texto_nivel.get_width() // 2, 150 + i * 60))

        # Actualizar pantalla
        pygame.display.flip()

        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                # Cambiar selección con flechas
                if evento.key == pygame.K_UP and nivel_seleccionado > 1:
                    nivel_seleccionado -= 1
                if evento.key == pygame.K_DOWN and nivel_seleccionado < 5:
                    nivel_seleccionado += 1
                # Confirmar selección con Enter
                if evento.key == pygame.K_RETURN:
                    seleccionando = False

    return nivel_seleccionado

# Seleccionar nivel antes de iniciar el juego
nivel = menu_seleccion_nivel()

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            # Verificar si el usuario tecleó correctamente
            if evento.unicode.upper() == letra_actual: # Letra correcta
                #letra_actual = random.choice(string.ascii_uppercase)
                letra_actual = random.choice(letra_personalizadas)
                x, y = random.randint(50, ANCHO - 50), 0
                puntaje += 1
                mensaje = "Bien hecho!"
                color_mensaje = (0,255,0) # Verde
                contador_efecto = 30 # muestra el mensaje por 30 frames
            else: # Letra incorrecta
                mensaje ="¡Fallaste!"
                color_mensaje = (255, 0, 0) # Rojo
                contador_efecto = 30 # Mostrar el mensaje por 30 frames

    # Actualizar posición
    y += velocidad * nivel
    if y > ALTO:  # Si la letra llega al fondo
        letra_actual = random.choice(string.ascii_uppercase)
        x, y = random.randint(50, ANCHO - 50), 0

    # Dibujar en la pantalla
    ventana.fill(NEGRO)
    texto = fuente.render(letra_actual, True, BLANCO)
    ventana.blit(texto, (x, y))

    # Dibujar el Puntaje
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, ROJO)
    ventana.blit(texto_puntaje, (10, 10))

    #Mostrar el mensaje de efecto visual
    if contador_efecto > 0 :
        texto_mensaje = fuente.render(mensaje, True, color_mensaje)
        ventana.blit(texto_mensaje, (ANCHO //2 - texto_mensaje.get_width() // 2, ALTO // 2))
        contador_efecto -= 1 # Reducir la duración del efecto


    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()






# import pygame
# import random
# import string

# # Inicializar pygame
# pygame.init()

# # Configuración de la ventana
# ANCHO, ALTO = 800, 600
# ventana = pygame.display.set_mode((ANCHO, ALTO))
# pygame.display.set_caption("Practica de Teclado")

# # Colores
# BLANCO = (255, 255, 255)
# NEGRO = (0, 0, 0)
# ROJO = (255, 0, 0)

# # Fuente y tamaño de texto
# fuente = pygame.font.Font(None, 74)

# # Inicializar variables
# letra = random.choice(string.ascii_uppercase)  # Letra aleatoria
# x = random.randint(50, ANCHO - 50)  # Posición inicial en X
# y = 0  # Posición inicial en Y
# velocidad = 5  # Velocidad de caída
# puntaje = 0

# # Bucle principal
# ejecutando = True
# while ejecutando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             ejecutando = False
#         if evento.type == pygame.KEYDOWN:
#             if evento.unicode.upper() == letra:  # Verificar la tecla presionada
#                 puntaje += 1
#                 letra = random.choice(string.ascii_uppercase)
#                 x = random.randint(50, ANCHO - 50)
#                 y = 0

#     # Actualizar la posición de la letra
#     y += velocidad
#     if y > ALTO:  # Si la letra llega al fondo
#         letra = random.choice(string.ascii_uppercase)
#         x = random.randint(50, ANCHO - 50)
#         y = 0

#     # Dibujar en la pantalla
#     ventana.fill(NEGRO)
#     texto = fuente.render(letra, True, BLANCO)
#     ventana.blit(texto, (x, y))

#     # Mostrar puntaje
#     texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, ROJO)
#     ventana.blit(texto_puntaje, (10, 10))

#     pygame.display.flip()
#     pygame.time.Clock().tick(30)  # Limitar a 30 FPS

# pygame.quit()









