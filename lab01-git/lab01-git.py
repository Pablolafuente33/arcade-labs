import arcade

WIDTH = 800
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Hello!!", 350, 300, arcade.color.WHITE)
arcade.draw_circle_filled(400, 200, 50, arcade.color.BLUE)
arcade.draw_rect_filled(arcade.LBWH(0, 0, 100, 100), arcade.color.BLACK_BEAN) # LBWH pone la esquina inferior izquierda en el punto que le indicas
arcade.finish_render()

arcade.run()
