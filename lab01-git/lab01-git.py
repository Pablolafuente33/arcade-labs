import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Hola mundo", 350, 300, arcade.color.WHITE)
arcade.draw_circle_filled(400, 200, 50, arcade.color.BLUE)
arcade.finish_render()

arcade.run()
