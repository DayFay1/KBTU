import pygame.mixer
import keyboard

# Initialize Pygame mixer
pygame.mixer.init()

# Load a list of songs
songs = ['pacman_death.wav', 'pacman_extrapac.wav', 'pacman_intermission.wav']

# Initialize the index of the current song
current_song = 0

# Load the first song in the list
pygame.mixer.music.load(songs[current_song])

# Define the keyboard controls
keyboard.add_hotkey('ctrl+shift+p', pygame.mixer.music.play)
keyboard.add_hotkey('ctrl+shift+s', pygame.mixer.music.stop)
keyboard.add_hotkey('ctrl+shift+n', lambda: next_song(songs))
keyboard.add_hotkey('ctrl+shift+b', lambda: prev_song(songs))

# Define the function to play the next song
def next_song(songs):
    global current_song
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

# Define the function to play the previous song
def prev_song(songs):
    global current_song
    current_song = (current_song - 1) % len(songs)
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

# Start the event loop
keyboard.wait()
