import arcade
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Tractor en movimiento")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.centro_x = 400
        self.centro_y = 300
        self.angulo = 0
        self.radio = 200
        self.tractor_x = 0
        self.tractor_y = 0
    
    def on_draw(self):
        self.clear()

        self.angulo += math.pi/100
        self.tractor_x = self.centro_x + math.cos(self.angulo) * self.radio
        self.tractor_y = self.centro_y + math.sin(self.angulo) * self.radio

        dibujar_tractor(self.tractor_x, self.tractor_y, 0.5 )
        
        
        # Poner aquí el código del dibujo
        # Cambiar la posición y/o tamaño del dibujo para crear animación

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
