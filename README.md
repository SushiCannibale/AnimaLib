# Pygame `AnimaLib`

The `AnimaLib` is a library for animating `Sprites` of the [PyGame](https://www.pygame.org/) library.

---

## Installation

Simply run 

> pip install anima-lib

to download and install the library from [PyPI](https://pypi.org/project/anima-lib/).

---

### How it works

- #### The loop
The core of the animation stands in the `frames` parameter of the `AnimatedSprite`.

In fact, the program will check if the duration associated to the current frame has been reached.
If so, the current frame will be set to the next one, and the duration will be reset, waiting for the next duration to be reached, and so on.

- #### The stop statement
The programm will look for the `do_kill` parameter **before changing the frame**.

If the `last_frame` is reached (The last image of the list if not specified), the animation will stop
and the sprite will be removed from its groups.



---

## How to use
### Classes
- #### Class `AnimatedSprite`
The class `AnimatedSprite` is a subclass of the [pygame.sprite.Sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) class
that takes two mandatory parameters :

| Argument | Description                                      |
| --- |--------------------------------------------------|
| `frames` | A list of tuples of the form `(image, duration)` |
| `*groups` | A list of groups to add the sprite to. |

And a bunch of optional parameters :

| Optional argument | Description                                                                             |
| --- |-----------------------------------------------------------------------------------------|
| `start_frame` | The index of the first frame that will be displayed                                     |
| `first_frame` | The index of the first frame on which the animation will loop [^1]                      |
| `last_frame` | The index of the last frame on which the animation will loop [^1]                       |
| `lock_at` | The index of the frame on which the animation will stop at                              |
| `do_kill` | A boolean that indicates whether the sprite will be removed from its groups or not [^2] |
| `delay_before_kill` | The delay before the sprite is removed from its groups [^2]                             |


[^1]: Considering the animation <ins>**will**</ins> loop.

[^2]: To be efficient, the `lock_at` parameter <ins>**has to be set**</ins>.

---

### Functions:
- `update()`

If the sprite is added to a group, it will automatically be updated.
Although, you can manuallly call `update()` to update the sprite each frame.

- `draw(surface:pygame.Surface, pos:iterable)`

If the sprite is added to a group, then it will automatically be drawn.
Although, you can call `draw(surface, pos)` to draw the sprite on a surface.
