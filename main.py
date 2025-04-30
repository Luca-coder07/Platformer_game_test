import wasabi2d as wsb2d

scene = wsb2d.Scene(width=750, height=300, title="Platformer-Spider", background='#55b0ed', pixel_art=True)

earth = scene.layers[0].add_rect(
	width=750,
	height=50,
	fill=True,
	color='#995a0e',
	pos=(scene.width / 2, scene.height - 25),
)

grass = scene.layers[0].add_rect(
	width=750,
	height=10,
	fill=True,
	color='#6c802d',
	pos=(scene.width / 2, scene.height - 45)
)

player = scene.layers[2].add_rect(
	width=50,
	height=50,
	fill=True,
	color='#ff051e',
	pos=(50, scene.height - 70)
)

@wsb2d.event
def update(dt, keyboard):
	vt = 20 * dt
	if keyboard.right:
		player.pos = (player.pos[0] + vt, player.pos[1])
		print(player.pos[0])
	elif keyboard.left:
		player.pos = (player.pos[0] - vt, player.pos[1])	
		print(player.pos[0])

wsb2d.run()
