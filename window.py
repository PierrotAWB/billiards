import pyglet
import pymunk 
from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1280, 720, "Pymunk Test", resizable=False)
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0,-1000

# DYNAMIC, affected by gravity and other forces (e.g., ball, player, enemies etc.)
# KINEMATIC, not affected by gravity or other forces, but can be moved (e.g., platforms, doors)
# STATIC, not affected by gravity or other forces, and cannot be moved (e.g., ground, building)

poly = pymunk.Poly.create_box(None, size=(150, 150))
moment = pymunk.moment_for_poly(1, poly.get_vertices())
print(moment)

body = pymunk.Body(1, moment, pymunk.Body.DYNAMIC)
body.position = 640,600

space.add(body, poly)

@window.event
def on_draw():
	window.clear()
	space.debug_draw(options)

def update(dt):
	space.step(dt)

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1.0/60)
	pyglet.app.run()