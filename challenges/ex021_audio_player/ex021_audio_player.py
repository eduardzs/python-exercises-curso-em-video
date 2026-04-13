import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("challenges/021_playing_mp3/lo-fi.mp3")
pygame.mixer.music.play()

input("Pressione ENTER para sair...")
