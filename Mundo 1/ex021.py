
#--- Exercício 021 ---#

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#--- Alternativa que funcionou no meu PC ;) ---#

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()
