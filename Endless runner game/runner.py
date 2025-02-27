
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True

background_img = pygame.image.load('Screenshot 2024-10-15 014855.png').convert()
obstacles_img = pygame.image.load('snail1.png').convert()
obstacle_rect = obstacles_img.get_rect(bottomright=(600, 300))

game_over = test_font.render('Game Over Press space to Restart', False, (150, 150, 150))
game_over_rect = game_over.get_rect(center=(400, 200))

player_img = pygame.image.load('player_stand.png').convert_alpha()
player_rect = player_img.get_rect(midbottom=(80, 300))  

score = 0
player_gravity = 0
obstacle_passed = False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_rect.left = 800
                score = 0  
                obstacle_passed = False

    if game_active:        
        screen.blit(background_img, (0, -300))
        screen.blit(obstacles_img, obstacle_rect)
        
        score_text = test_font.render(f'Score: {score}', True, 'black')
        screen.blit(score_text, (50, 50))
        
        obstacle_rect.x -= 5
        if obstacle_rect.right <= 0:
            obstacle_rect.left = 800
            obstacle_passed = False  

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_img, player_rect)

        if obstacle_rect.right < player_rect.left and not obstacle_passed:
            score += 1
            obstacle_passed = True  

        if obstacle_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('red')
        screen.blit(game_over, game_over_rect)
        
    pygame.display.update()
    clock.tick(60)
