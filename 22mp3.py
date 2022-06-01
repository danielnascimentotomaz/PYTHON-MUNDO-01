"""
22)Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""

import pygame


pygame.mixer.init()

pygame.mixer.music.load('22mp3.mp3')
pygame.mixer.music.play()

input('\033[33mINSÔNIA\033[m')