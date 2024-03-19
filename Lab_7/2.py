# 2. Create music player with keyboard controller. You have to be able to press keyboard:
# play, stop, next and previous as some keys.
# Player has to react to the given command appropriately.
# control the music player using the spacebar to play or pause,
# and "n" and "p" keys to go to the next or previous track

import pygame
import os
pygame.init()
pygame.display.set_caption("Music")
screen = pygame.display.set_mode((400, 400))
music_dir = r"C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_7"
music_files = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]
pygame.mixer.init()

def play_next_track():
    global current_track_index
    if current_track_index < len(music_files) - 1:
        current_track_index += 1
        pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
        pygame.mixer.music.play()

def play_previous_track():
    global current_track_index
    if current_track_index > 0:
        current_track_index -= 1
        pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
        pygame.mixer.music.play()

def stop_playing():
    pygame.mixer.music.stop()

def start_playing():
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track_index]))
    pygame.mixer.music.play()

current_track_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_playing()
                else:
                    start_playing()
            elif event.key == pygame.K_n:
                play_next_track()
            elif event.key == pygame.K_p:
                play_previous_track()

pygame.quit()