import random
import pygame
import pygame.display

pygame.init()
SCREEN=WIDTH,HEIGHT=288,512
info=pygame.display.Info()
width=info.current_w
height=info.current_h
if width>=height:
    win=pygame.display.set_mode(SCREEN,pygame.NOFRAME)
else:
    win=pygame.display.set_mode(SCREEN,pygame.N0FRAME|pygame.SCALED|pygame.FULLSCREEN)
clock=pygame.time.Clock()
FPS=60
WHITE=(255,255,255)
BLUE=(30,144,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,20)

plane_img = pygame.image.load('Assets/plane.png')
logo_img = pygame.image.load('Assets/logo.png')
fighter_img = pygame.image.load('Assets/fighter.png')
clouds_img = pygame.image.load('Assets/clouds.png')
clouds_img = pygame.transform.scale(clouds_img, (WIDTH, 350))

home_img=pygame.image.load("Assets/Buttons/homeBtn.png")
replay_img=pygame.image.load("Assets/Buttons/Reply.png")
sound_off_img=pygame.image.load("Assets/Buttons/soundOffBtn.png")
sound_on_img=pygame.image.load("Assets/Buttons/soundOnBtn.png")

home_btn=Button(home_img,(24,24),WIDTH//4-18,HEIGHT//2+120)
replay_btn=Button(replay_img,(36,36),WIDTH//2-18,HEIGHT//2+115)
sound_btn=Button(sound_on_img,,(24,24),WIDTH-WIDTH//4-18,HEIGHT//2+120)
game_over_font="Fonts/ghostclan.tff"
tap_to_play_font="BubblegumSans-regular.tff"
score_font="Fonts/DalelandUnicalBold821A.tff"
final_font="Fonts/DroneflyRegular_K78LA.tff"

game_over_msg=Message(WIDTH//2,230,30,'Game Over',game_over_font,WHITE,win)
score_msg=Message(WIDTH-50,28,30,'0',final_font,RED,win)
final_score_msg=Messgae(WIDTH//2,280,30,'0',final_font,RED,win)
tap_to_play_msg=tap_to_play=BlinkingText(WIDTH//2,HEIGHT-60,25,"Tap To Play",tap_to_play_font,WHITE,win)

player_bullet_fx = pygame.mixer.Sound('Sounds/gunshot.wav')
click_fx = pygame.mixer.Sound('Sounds/click.mp3')
collision_fx = pygame.mixer.Sound('Sounds/mini_exp.mp3')
blast_fx = pygame.mixer.Sound('Sounds/blast.wav')
fuel_fx = pygame.mixer.Sound('Sounds/fuel.wav')

pygame.mixer.music.load('Sounds/Defrini - Spookie.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)