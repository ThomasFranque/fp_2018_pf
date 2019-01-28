import pygame, sys

class menu():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("Sprites/ui/menu.png").convert_alpha()

    def quit_game(self):
        pygame.quit()
        sys.exit()
        
    def wait_key_press(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Pressing ESC quits.
                        self.quit_game()
                    return

    def start_screen(self):
        self.screen.blit(self.image,(0,0))
        pygame.display.update()
        self.wait_key_press()
