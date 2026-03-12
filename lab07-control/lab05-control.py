import arcade
import math
# --- Constants ---

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
MOVEMENT_SPEED = 3
DEAD_ZONE = 0.02

def draw_background():
    """Draws a beach scene background using arcade shapes."""
 
    # --- Sky ---
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGTH * 0.4, SCREEN_HEIGTH,
                                      arcade.color.LIGHT_BLUE)
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGTH * 0.33, SCREEN_HEIGTH * 0.4,
                                      arcade.color.PALE_BLUE)
 
    # --- Sun ---
    sun_x = SCREEN_WIDTH * 0.85
    sun_y = SCREEN_HEIGTH * 0.78
    arcade.draw_circle_filled(sun_x, sun_y, 55, arcade.color.YELLOW)
    arcade.draw_circle_filled(sun_x, sun_y, 45, arcade.color.ORANGE)
    arcade.draw_circle_filled(sun_x, sun_y, 35, arcade.color.YELLOW)
 
    # Sun rays
    for i in range(12):
        angle = i * 30
        x_end = sun_x + math.cos(math.radians(angle)) * 75
        y_end = sun_y + math.sin(math.radians(angle)) * 75
        arcade.draw_line(sun_x, sun_y, x_end, y_end, arcade.color.YELLOW, 2)
 
    # --- Sea ---
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGTH * 0.27, SCREEN_HEIGTH * 0.43,
                                      arcade.color.OCEAN_BOAT_BLUE)
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGTH * 0.27, SCREEN_HEIGTH * 0.35,
                                      arcade.color.SEA_BLUE)
 
    # Waves
    arcade.draw_ellipse_outline(SCREEN_WIDTH * 0.13, SCREEN_HEIGTH * 0.39, 140, 15, arcade.color.WHITE, 2)
    arcade.draw_ellipse_outline(SCREEN_WIDTH * 0.38, SCREEN_HEIGTH * 0.36, 160, 15, arcade.color.WHITE, 2)
    arcade.draw_ellipse_outline(SCREEN_WIDTH * 0.63, SCREEN_HEIGTH * 0.38, 130, 12, arcade.color.WHITE, 2)
    arcade.draw_ellipse_outline(SCREEN_WIDTH * 0.25, SCREEN_HEIGTH * 0.33, 120, 10, arcade.color.WHITE, 2)
    arcade.draw_ellipse_outline(SCREEN_WIDTH * 0.75, SCREEN_HEIGTH * 0.32, 150, 10, arcade.color.WHITE, 2)
 
    # --- Sand ---
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGTH * 0.30,
                                      arcade.color.SANDY_BROWN)
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGTH * 0.15,
                                      (210, 180, 100))
 
    # Sand texture dots
    for x in range(20, SCREEN_WIDTH, 45):
        for y in range(10, int(SCREEN_HEIGTH * 0.28), 35):
            arcade.draw_circle_filled(x, y, 3, (190, 160, 80))
 
    # --- Palm tree (left side) ---
    trunk_base_x = SCREEN_WIDTH * 0.10
    trunk_base_y = SCREEN_HEIGTH * 0.10
    trunk_top_x  = SCREEN_WIDTH * 0.14
    trunk_top_y  = SCREEN_HEIGTH * 0.50
 
    arcade.draw_line(trunk_base_x, trunk_base_y,
                     trunk_top_x,  trunk_top_y,
                     arcade.color.BROWN, 8)
 
    # Leaves
    arcade.draw_ellipse_filled(trunk_top_x, trunk_top_y, 110, 22, arcade.color.DARK_GREEN, tilt_angle=30)
    arcade.draw_ellipse_filled(trunk_top_x, trunk_top_y, 110, 22, arcade.color.DARK_GREEN, tilt_angle=-30)
    arcade.draw_ellipse_filled(trunk_top_x, trunk_top_y,  95, 20, arcade.color.DARK_GREEN, tilt_angle=80)
    arcade.draw_ellipse_filled(trunk_top_x, trunk_top_y,  95, 20, arcade.color.DARK_GREEN, tilt_angle=-80)
    arcade.draw_ellipse_filled(trunk_top_x, trunk_top_y,  85, 20, arcade.color.DARK_GREEN, tilt_angle=0)
 
 
    # --- Beach umbrella (right side) ---
    pole_x      = SCREEN_WIDTH * 0.72
    pole_bottom = SCREEN_HEIGTH * 0.13
    pole_top    = SCREEN_HEIGTH * 0.38
 
    arcade.draw_line(pole_x, pole_bottom, pole_x, pole_top, arcade.color.WHITE, 4)
 
    arcade.draw_triangle_filled(pole_x - 80, pole_top,
                                 pole_x + 80, pole_top,
                                 pole_x,      pole_top + 55,
                                 arcade.color.RED)
    arcade.draw_triangle_filled(pole_x - 80, pole_top,
                                 pole_x,       pole_top,
                                 pole_x - 40,  pole_top + 28,
                                 arcade.color.WHITE)
    arcade.draw_triangle_filled(pole_x,      pole_top,
                                 pole_x + 80, pole_top,
                                 pole_x + 40, pole_top + 28,
                                 arcade.color.WHITE)
 
 
class Ball:
    def __init__(self, x, y,dx,dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def on_update(self):
        #Movemos la pelota 
        self.x += self.dx
        self.y += self.dy
        
        # Para elllo vemos que si se sale de la pantalla rebote.
        if self.x < self.radius:
            self.x = self.radius
        if self.x > SCREEN_WIDTH - self.radius:
            self.x = SCREEN_WIDTH - self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > SCREEN_HEIGTH - self.radius:
            self.y = SCREEN_HEIGTH - self.radius


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer 
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGTH, "Lab05 - Control")

        # HAcemos que nuestro ratón desaparezca cuando estemos en la ventana
        self.set_mouse_visible(False)
        
        #Creamos nuestra pelota.
        self.ball = Ball(50,50,0,0,15, arcade.color.AUBURN)

        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

        

    def on_draw(self):
        self.clear()

        draw_background()

        self.ball.draw()
    
    def on_update(self, delta_time):

        # Update the position according to the game controller
        if self.joystick:
        # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.dx = 0
            else:
                self.ball.dx = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.dy = 0
            else:
                self.ball.dy = -self.joystick.y * MOVEMENT_SPEED

        self.ball.on_update()

    ### Con el ratón
    def on_mouse_motion(self,x,y,dx,dy):
        """ 'Llamado para actualizar nuestro objeto unas 60 veces por segundo (60 Hz)'"""
            
        self.ball.x = x
        self.ball.y = y
    
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ 'Called when the user presses a mouse button.' """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)
    
    ### Con el teclado
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.dx = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.dx = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.dy = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.dy = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0
    
    ### Con joystick
    

def main():
    window = MyGame()
    arcade.run()


main()