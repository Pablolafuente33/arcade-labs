import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Hello, world", 350, 300, arcade.color.WHITE)
arcade.draw_circle_filled(400, 300, 50, arcade.color.BLUE)
arcade.draw_rectangle_filled(200, 150, 100, 50, arcade.color.RED)
arcade.finish_render()

arcade.run()