import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Hello, world", 350, 300, arcade.color.WHITE)
arcade.draw_circle_filled(400, 200, 50, arcade.color.BLUE)
arcade.draw_rect_filled(arcade.XYWH(55, 55, 100, 100), arcade.color.BLACK_BEAN)
arcade.finish_render()

arcade.run()