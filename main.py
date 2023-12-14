import pygame
import schedule
from game import Game
from button import Button

width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))

game = Game(screen)
pygame.init()
pygame.display.set_caption("Five Nights at Freddy's Simulator")

background_color = (0, 0, 0)

screen.fill(background_color)

def get_objects_under_cursor(cursor_pos) -> list:
    return [id for id in game.objects.keys() if game.objects[id].rect.collidepoint(cursor_pos)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_buttons = [id for id in get_objects_under_cursor(pos) if isinstance(game.objects[id], Button)]
            for button_id in clicked_buttons:
                game.objects[button_id].on_click(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3:
                print("List of gameobjects:")
                for id in game.objects.keys():
                    print(f"{id}: {game.objects[id]}")
            elif event.key == pygame.K_DELETE:
                print("Deleting the gameobjects under your cursor")
                mouse_pos = pygame.mouse.get_pos()
                for id in get_objects_under_cursor(mouse_pos):
                    print(f"Deleted {id}: {game.objects[id]}")
                    del game.objects[id]

    screen.fill(background_color)

    schedule.run_pending()

    for layer in sorted(game.display.layers):
        for id in game.display.layers[layer]:
            game.objects[id].draw(screen)
    
    pygame.display.update()


