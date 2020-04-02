import sys, pygame 
import random 
import pandas as pd
from ship import *
from asteroid import *
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w * 0.5), int(screen_info.current_h * 0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

# read and store game data
df = pd.read_csv('game_info.csv')

# Setup Game Variables
Asteroids = pygame.sprite.Group()
NumLevels = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
AsteroidCount = LevelData['AsteroidCount']
Player = Ship((LevelData['PlayerX'], LevelData['PlayerY']))


def init():
    global AsteroidCount, Asteroids, LevelData

def main():
    global Level
    while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player.speed[0] = 10
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = -10
                if event.key == pygame.K_UP:
                    Player.speed[1] = -10
                if event.key == pygame.K_DOWN:
                    Player.speed[1] = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    Player.speed[0] = 0
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = 0
                if event.key == pygame.K_UP:
                    Player.speed[1] = 0
                if event.key == pygame.K_DOWN:
                    Player.speed[1] = 0

        screen.fill(color)
        Player.update()
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()