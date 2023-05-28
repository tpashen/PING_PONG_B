#Sidorenko - 1
from pygame import*
'''Необходимые классы'''

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
        #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(widt, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Fedaev - 2

#Zhiharev - 3

#3ralenno - 4



