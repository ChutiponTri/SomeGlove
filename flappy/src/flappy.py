from datetime import datetime
from ctypes import windll
import asyncio
import sys
import pandas as pd
import pygame
from pygame.locals import K_ESCAPE, K_SPACE, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT
from threading import Thread
from demo_database import Database

from .entities import (
    Background,
    Floor,
    GameOver,
    Pipes,
    Player,
    PlayerMode,
    Score,
    WelcomeMessage,
)
from .utils import GameConfig, Images, Sounds, Window

class Flappy:
    def __init__(self):
        # Initialize Game 
        pygame.init()
        pygame.display.set_caption("Flappy Bird")

        windll.user32.SetProcessDPIAware()

        # physical_width, physical_height = pygame.display.list_modes()[0]
        physical_width, physical_height = 1920, 1080

        window = Window(physical_width, physical_height)
        screen = pygame.display.set_mode((window.width, window.height))
        images = Images()
        icon = pygame.image.load("icons/flappy.jpg")
        pygame.display.set_icon(icon)

        # Initialize Database
        self.username = Database.get_current_user()
        self.game = "FlappyBird"
        self.score_list = []

        # Initialize Game Config
        self.config = GameConfig(
            screen=screen,
            clock=pygame.time.Clock(),
            fps=30,
            window=window,
            images=images,
            sounds=Sounds(),
        )

    # Async Function Main Loop
    async def start(self):
        while True:
            self.background = Background(self.config)
            self.floor = Floor(self.config)
            self.player = Player(self.config)
            self.welcome_message = WelcomeMessage(self.config)
            self.game_over_message = GameOver(self.config)
            self.pipes = Pipes(self.config)
            self.score = Score(self.config)
            await self.splash()
            await self.play()
            await self.game_over()
    
    # Async Function Game Start
    async def splash(self):
        """Shows welcome splash screen animation of flappy bird"""

        self.player.set_mode(PlayerMode.SHM)

        while True:
            for event in pygame.event.get():
                self.check_quit_event(event)
                if self.is_tap_event(event):
                    self.start_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    return

            self.background.tick()
            self.floor.tick()
            self.player.tick()
            self.welcome_message.tick()

            pygame.display.update()
            await asyncio.sleep(0)
            self.config.tick()

    # Function To Check If Quit Was Toggle
    def check_quit_event(self, event):
        if event.type == QUIT or (
            event.type == KEYDOWN and event.key == K_ESCAPE
            ):
            # task = Thread(target=Database.update_score, args=(self.score_list,))
            # task.start()
            pygame.quit()
            sys.exit()
            
    # Function To Check If Keyboard Was Pressed
    def is_tap_event(self, event):
        m_left, _, _ = pygame.mouse.get_pressed()
        space_or_up = event.type == KEYDOWN and (
            event.key == K_SPACE or event.key == K_UP or event.key == K_RIGHT or 
            event.key == K_LEFT or event.key == pygame.K_w or event.key == pygame.K_s or
            event.key == K_DOWN
        )
        screen_tap = event.type == pygame.FINGERDOWN
        return m_left or space_or_up or screen_tap

    # Async Function To Play The Game
    async def play(self):
        self.score.reset()
        self.player.set_mode(PlayerMode.NORMAL)

        while True:
            if self.player.collided(self.pipes, self.floor):
                return

            for i, pipe in enumerate(self.pipes.upper):
                if self.player.crossed(pipe):
                    self.score.add()

            for event in pygame.event.get():
                self.check_quit_event(event)
                if self.is_tap_event(event):
                    self.player.flap()

            self.background.tick()
            self.floor.tick()
            self.pipes.tick()
            self.score.tick()
            self.player.tick()

            pygame.display.update()
            await asyncio.sleep(0)
            self.config.tick()

    # Async Function Game Over
    async def game_over(self):
        """crashes the player down and shows gameover image"""

        self.player.set_mode(PlayerMode.CRASH)
        self.pipes.stop()
        self.floor.stop()
        self.score_analysis()

        while True:
            for event in pygame.event.get():
                self.check_quit_event(event)
                if self.is_tap_event(event):
                    if self.player.y + self.player.h >= self.floor.y - 1:
                        return

            self.background.tick()
            self.floor.tick()
            self.pipes.tick()
            self.score.tick()
            self.player.tick()
            self.game_over_message.tick()

            self.config.tick()
            pygame.display.update()
            await asyncio.sleep(0)

    # Function To Analyze Result Score
    def score_analysis(self):
        finish_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        score = self.score.score
        self.accuracy = self.analysis(score)
        data = {
            "เกม": self.game, 
            "คะแนน": str(score), 
            "เวลาเริ่มต้น": self.start_time, 
            "เวลาสิ้นสุด": finish_time, 
            "ความแม่นยำ": self.accuracy,
            "หมายเหตุ": pd.NA
        }
        self.score_list.append(data)
        task = Thread(target=Database.insert_score, args=(self.username, self.game, score, self.start_time, finish_time, self.accuracy, "None"))
        task.start()
        print(score)
    
    # Function To Get Accuracy
    def analysis(self, score):
        if score <= 10:
            return "พอใช้"
        elif 10 < score <= 20:
            return "ดี"
        elif 20 < score <= 30:
            return "ดีมาก"
        elif 30 < score <= 40:
            return "ดีเยี่ยม"
        elif score <= 0:
            return "ปรับปรุง" 
        else:
            return "ยอดเยี่ยม"
        