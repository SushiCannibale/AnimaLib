# Pygame `AnimaLib`

La bibliothèque `AnimaLib` est une bibliothèque d'animation des `Sprites` de [PyGame](https://www.pygame.org/).

([GitHub](https://github.com/SushiCannibale/AnimaLib))

---

## Installation

Tapez 
`pip install animalib` 
pour télécharger et installer la bibliothèque depuis [PyPI](https://pypi.org/project/animalib/).

---

### Comment ça marche ?

Le coeur de l'animation réside dans le paramètre `frames` de l'`AnimatedSprite`.

Concrètement, le programme va vérifier si la durée associée à la frame actuelle a été atteinte.
Si c'est le cas, la frame actuelle sera remplacée par la suivante, et la durée sera remise à zéro, 
attendant que la durée suivante soit atteinte, et ainsi de suite.

---

## Utilisation
### Classes
- #### Classe `AnimatedSprite`
La classe `AnimatedSprite` est une sous-classe de la classe [pygame.sprite.Sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite)
mais possède deux nouveaux paramètres obligatoires :

| Argument  | Description                                        |
|-----------|----------------------------------------------------|
| `frames`  | Une liste de tuples de la forme : `(image, durée)` |
| `*groups` | Une liste de groups auxquels le sprite sera ajouté |

Ainsi que quelques paramètres optionnels :

| Argument optionnel  | Description                                                                              |
|---------------------|------------------------------------------------------------------------------------------|
| `start_frame`       | L'indice de la première frame qui sera dessinée (au tout début de l'animation)           |
| `first_frame`       | L'indice de la première frame sur laquelle l'animation va boucler [^1]                   |
| `last_frame`        | L'indice de la dernière frame sur laquelle l'animation va boucler [^1]                   |
| `lock_at`           | L'indice de la frame à laquelle l'animation va se bloquer                                |
| `do_kill`           | Un booléen indiquant si le sprite doit être retiré de ses groupes ou non [^2]            |
| `delay_before_kill` | Un entier reprsentatn le délai avant que le sprite soit retiré de ses groupes  [^2] [^3] |


[^1]: En partant du principe que l'animation **va** boucler.

[^2]: Pour fonctionner, le paramètre `lock_at` **doit être défini**.

[^3]: Pour fonctionner, le paramètre `do_kill` doit valoir `True`.

---

### Fonctions:
- `update()`

Si le sprite est ajouté à un groupe, il sera automatiquement mis à jour.
Mais si ce n'est pas le cas, vous pouvez appeler manuellement `update()` pour mettre à jour le sprite à chaque frame.

- `draw(surface:pygame.Surface, pos:iterable)`

Si le sprite est ajouté à un groupe, il sera automatiquement dessiné.
Mais si ce n'est pas le cas, vous pouvez appeler manuellement `draw(surface, pos)` pour dessiner le sprite sur une surface donnée.

Veuillez noter que la position `pos` est optionnelle. Si elle n'est pas renseignée, la postion du rect du sprite sera utilisé.

---

## Exemples

- #### Impératif (en utilisant un groupe)

```python
import pygame
from animalib import animalib
pygame.init()

run = True

screen = pygame.display.set_mode((500, 500))
group = pygame.sprite.Group()

frames = []
# [(image_0, durée_0), (image_1, durée_1), ...]

r, g, b = 255, 255, 255
for i in range(0, 10):
    surf = pygame.Surface((400, 400))
    surf.fill((r, g, b))
    # Vous pouvez aussi charger une image depuis un fichier plutôt que de créer une surface
    # du moment que le type résultant est une `pygame.Surface`.
    
    frames.append((surf, 500))
    # la durée est en millisecondes
    
    r -= 25
    g -= 25
    b -= 25

sprite = animalib.AnimatedSprite(frames, group)

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            break
    screen.fill((0, 0, 0))
    
    group.update()
    group.draw(screen)
    
    pygame.display.flip()
pygame.quit()
```

- #### En P.O.O (sans utiliser de groupe, et en utilisant le `lock_at`)

```python
import pygame
from animalib import animalib

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 500))
        self.run = False
        frames = self.load_frames()
        self.sprite = animalib.AnimatedSprite(frames, lock_at=5)

    def load_frames(self):
        frames = []
        r, g, b = 255, 255, 255
        for i in range(0, 10):
            surf = pygame.Surface((400, 400))
            surf.fill((r, g, b))
            # Vous pouvez aussi charger une image depuis un fichier plutôt que de créer une surface
            # du moment que le type résultant est une `pygame.Surface`.
    
            
            frames.append((surf, 500))
            # la durée est en millisecondes
            
            r -= 25
            g -= 25
            b -= 25
        return frames
        
        
    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False
                
    def loop(self):
        self.run = True
        while self.run:
            self.events()
            self.screen.fill((0, 0, 0))
            
            self.sprite.update()
            self.sprite.draw(self.screen, (0, 0))
            
            pygame.display.flip()
        pygame.quit()

game = Game()
game.loop()
```

Dans ces exemples, l'image du sprite change toutes les 500 millisecondes,
et sa couleur passe du blanc au gris. Cependant, dans le premier, l'animation boucle,
et le groupe gère le dessin lui-même.

Mais dans le second exemple, le sprite se bloque à la 5ème frame,
et le dessin est géré manuellement.
