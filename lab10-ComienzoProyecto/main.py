"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade
import random

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "JuegoNuevo"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5

GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class GameView(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable = True) 
                # con resizable hacemos que pueda ponerse la pantalla completa
                # con fullscreen hacemos que se habra en pantalla completa

        #Variable to hold our texture for our player
        self.player_texture = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # SpriteList for our player
        self.player_list = None

            # SpriteList for our boxes and ground
            # Putting our ground and box Sprites in the same SpriteList
            # will make it easier to perform collision detection against
            # them later on. Setting the spatial hash to True will make
            # collision detection much faster if the objects in this
            # SpriteList do not move.
        self.wall_list = None

        self.camera = None

        self.coin_list = None

        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        self.gui_camera = None
        self.score = 0

        self.score_text = None

        self.scene = None
        
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.player_texture = arcade.load_texture(":resources:images/animated_characters/male_person/malePerson_idle.png") 
        
        #Ponemos el dibujo de un jugador
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64 #Donde se situa nuestro sprite en el eje x
        self.player_sprite.center_y = 128 #Donde se situa nuestro sprite en el eje y

        self.scene.add_sprite("Player", self.player_sprite)   

        self.wall_list = arcade.SpriteList(use_spatial_hash=True) # use_spatial_hash para que se detecten las colisiones

        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", scale=TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        #Creamos el motoor de física
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls =self.wall_list, gravity_constant = GRAVITY
        )

        self.camera = arcade.Camera2D()
        #DEfinimos una lista de sprites de monedas

        self.coin_list = arcade.SpriteList(use_spatial_hash= True)
        for pos in range(128, 1250, 256):
            coin = arcade.Sprite(
                ":resources:images/items/coinGold.png", scale=TILE_SCALING)
            coin.center_x = pos
            coin.center_y = 96
            self.coin_list.append(coin)

        self.background_color = arcade.color.ANTIQUE_BRASS

        self.gui_camera = arcade.Camera2D()
        self.score = 0

        self.score_text = arcade.Text(f'Score: {self.score}', x = 0, y = 5)

        self.scene = arcade.Scene()

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        #Activate our cam before drawing
        self.camera.use()

        # Code to draw other things will go here
        self.player_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()

        self.gui_camera.use()
        self.score_text.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.ESCAPE:
            self.setup()

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and Game Logic"""
        self.physics_engine.update()

        #See if we hit a coin
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )

        for coin in coin_hit_list:
            #Borramos la moneda
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 75
            self.score_text.text = f'Score: {self.score}'

        self.camera.position = self.player_sprite.position



def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()