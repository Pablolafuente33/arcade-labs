"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

def dibujar_tractor(x : int, y : int, escala: int):
    # Draw the engine
    ## TOMAMOS DE REFERENCIA x = 600 , y = 120 que es el donde se encuntra el motor del tractor primero
    arcade.draw_rect_filled(arcade.XYWH(x, y, 140 * escala, 70 * escala), arcade.color.GRAY)
    arcade.draw_rect_filled(arcade.XYWH(x - (10 * escala), y - (15 * escala), 90 * escala, 40 * escala), arcade.color.BLACK)

    # Draw the smoke stack
    arcade.draw_rect_filled(arcade.XYWH(x - (20 * escala), y + 55 * escala, 10*escala, 40*escala), arcade.color.BLACK)

    # Back wheel
    arcade.draw_circle_filled(x- (110 * escala), y - (10 * escala), 50*escala, arcade.color.BLACK)
    arcade.draw_circle_filled(x- (110 * escala), y - (10 * escala), 45*escala, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x- (110 * escala), y - (10 * escala), 35*escala, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x- (110 * escala), y - (10 * escala), 10*escala, arcade.color.RED)

    # Front wheel
    arcade.draw_circle_filled(x + (50 * escala), (y - 30 * escala), 30*escala, arcade.color.BLACK)
    arcade.draw_circle_filled(x + (50 * escala),(y - 30 * escala), 25*escala, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x + (50 * escala), (y - 30 * escala), 18*escala, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x + (50 * escala), (y - 30 * escala), 5*escala, arcade.color.RED)

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Get ready to draw

# Draw the grass
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BITTER_LIME)

# --- Draw the barn ---

# Barn cement base
arcade.draw_lrbt_rectangle_filled(30, 350, 170, 210, arcade.color.BISQUE)

# Bottom half
arcade.draw_lrbt_rectangle_filled(30, 350, 210, 350, arcade.color.BROWN)

# Left-bottom window
arcade.draw_rect_filled(arcade.XYWH(70, 260, 30, 40), arcade.color.BONE)
arcade.draw_rect_filled(arcade.XYWH(70, 260, 20, 30), arcade.color.BLACK)

# Right-bottom window
arcade.draw_rect_filled(arcade.XYWH(310, 260, 30, 40), arcade.color.BONE)
arcade.draw_rect_filled(arcade.XYWH(310, 260, 20, 30), arcade.color.BLACK)

# Barn door
arcade.draw_rect_filled(arcade.XYWH(190, 230, 100, 100), arcade.color.BLACK_BEAN)

# Rail above the door
arcade.draw_rect_filled(arcade.XYWH(190, 280, 180, 5), arcade.color.BONE)

# Draw second level of barn
arcade.draw_polygon_filled([[20, 350],
                            [100, 470],
                            [280, 470],
                            [360, 340]],
                            arcade.color.BROWN)

# Draw loft of barn
arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

# Left-top window
arcade.draw_rect_filled(arcade.XYWH(130, 440, 30, 40), arcade.color.BONE)
arcade.draw_rect_filled(arcade.XYWH(130, 440, 20, 30), arcade.color.BLACK)

# Right-top window
arcade.draw_rect_filled(arcade.XYWH(250, 440, 30, 40), arcade.color.BONE)
arcade.draw_rect_filled(arcade.XYWH(250, 440, 20, 30), arcade.color.BLACK)

# Draw 2nd level door
arcade.draw_rect_outline(arcade.XYWH(190, 310, 30, 60), arcade.color.BONE, 5)

# --- Draw the tractor ---
x = 30
y = 60
for i in range(1,6): # Empezamos en 1 para que no haya escala 0
    escala =  i / 5
    dibujar_tractor(x, y, escala)
    ancho_tractor_actual = 340 * escala
    x += ancho_tractor_actual + 10
   
# --- Finish drawing ---

# Keep the window up until someone closes it.
arcade.finish_render()
arcade.run()