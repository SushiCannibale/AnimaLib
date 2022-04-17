import pygame as pg
from src.animalib.animalib import AnimatedSprite
pg.init()

group = pg.sprite.Group()

anim_frames = []
for i in range(0, 8):
    img = pg.image.load(f"example_imgs/example_{i}.png")
    img = pg.transform.scale(img, (100, 100))
    anim_frames.append((img, 500))

example_sprite = AnimatedSprite(anim_frames, group)

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Example - AnimaLib")

clock = pg.time.Clock()

run = True

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
            break
    screen.fill((12, 12, 12))

    example_sprite.update()
    group.draw(screen)

    pg.display.update()
    clock.tick(60)

pg.quit()