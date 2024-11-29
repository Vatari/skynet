from ursina import *

app = Ursina()

# Player setup
player = FirstPersonController()
player.cursor.visible = True  # Show the mouse cursor for testing

# Create the world
ground = Entity(model='plane', scale=(100, 1, 100), texture='grass', texture_scale=(10, 10))
walls = [
    Entity(model='cube', color=color.gray, scale=(5, 10, 1), position=(5, 0, 5)),
    Entity(model='cube', color=color.gray, scale=(5, 10, 1), position=(-5, 0, -5))
]

# Add a gun
gun = Entity(
    model='cube',
    color=color.black,
    scale=(0.2, 0.1, 1),
    position=(0.5, -0.2, 1.5),
    parent=camera.ui
)

# Bullets list
bullets = []

# Shoot function
def input(key):
    if key == 'left mouse down':  # Shoot bullets when clicking the mouse
        bullet = Entity(
            model='sphere',
            color=color.red,
            scale=0.2,
            position=gun.world_position + Vec3(0, 0, 1),
            collider='box'
        )
        bullets.append(bullet)

# Update function
def update():
    for bullet in bullets:
        bullet.position += Vec3(0, 0, 10 * time.dt)
        if bullet.z > 50:  # Remove bullets that move too far
            bullets.remove(bullet)
            destroy(bullet)

app.run()
