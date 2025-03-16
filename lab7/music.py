import pygame

pygame.init()


songs = ["song1.mp3", "song2.mp3", "song3.mp3", "song4.mp3"]  
current_song = 0
pygame.mixer.init()
pygame.mixer.music.load(songs[current_song])


screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

running = True

def play_song(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

while running:
    screen.fill((255, 255, 255))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  
                current_song = (current_song + 1) % len(songs)
                play_song(current_song)
            elif event.key == pygame.K_p:  
                current_song = (current_song - 1) % len(songs)
                play_song(current_song)

    pygame.display.flip()

pygame.quit()

