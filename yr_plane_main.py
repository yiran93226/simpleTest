# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:42:23 2022

@author: HUAWEI
"""

import sys
import pygame
import yr_plane_sprite as sp


class PlaneGame(object):
    
    def __init__(self):
        print("Initialization")
        
        self.screen = pygame.display.set_mode(sp.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        
        pygame.time.set_timer(sp.CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(sp.HERO_FIRE_EVENT, 500)
        
    def __create_sprites(self):
        bg1 = sp.Backgroud()
        bg2 = sp.Backgroud(True)        
        self.back_group = pygame.sprite.Group(bg1, bg2)
        
        self.enemy_group = pygame.sprite.Group()
        
        self.hero = sp.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    
    def start_game(self):
        print("Start game...")
            
        
        while True:
            self.clock.tick(sp.FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    
    def __event_handler(self):
        for event in pygame.event.get():
        
            # quit the game
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()  
            elif event.type == sp.CREATE_ENEMY_EVENT:
                # print("Enemy is coming...")
                enemy = sp.Enemy()
                
                self.enemy_group.add(enemy)
            elif event.type == sp.HERO_FIRE_EVENT:
                self.hero.fire()
                
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("right")
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 3
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -3
            else:
                self.hero.speed = 0
    
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            self.__game_over()
    
    def __update_sprites(self):
        
        self.back_group.update()
        self.back_group.draw(self.screen)
        
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
    
    @staticmethod
    def __game_over():
        print("Game over!")
        pygame.quit()
        sys.exit()
    
        
if __name__ == '__main__':
    
    game = PlaneGame()
    game.start_game()

