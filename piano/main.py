# Piano Tiles

# Author : Prajjwal Pathak (pyguru)
# Date : Thursday, 30 November, 2021

import os
import json
import random
import pygame
import pandas as pd
from threading import Thread
from datetime import datetime
from demo_database import Database

from .objects import Tile, Square, Text, Button, Counter

class Piano():
	def __init__(self):
		pygame.init()
		SCREEN = WIDTH, HEIGHT = 800, 812
		TILE_WIDTH = WIDTH // 4
		TILE_HEIGHT = 260

		self.username = Database.get_current_user()
		self.game = "Piano Tiles"
		self.score_list = []

		info = pygame.display.Info()
		width = info.current_w
		height = info.current_h

		if width >= height:
			win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
		else:
			win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

		clock = pygame.time.Clock()
		FPS = 30

		# COLORS *********************************************************************

		WHITE = (255, 255, 255)
		GRAY = (75, 75, 75)
		BLUE = (30, 144, 255)

		# IMAGES *********************************************************************

		bg_img = pygame.image.load('piano/Assets/bg.png')
		bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

		piano_img = pygame.image.load('piano/Assets/piano.png')
		piano_img = pygame.transform.scale(piano_img, (212, 212))

		title_img = pygame.image.load('piano/Assets/title.png')
		title_img = pygame.transform.scale(title_img, (200, 50))

		start_img = pygame.image.load('piano/Assets/start.png')
		start_img = pygame.transform.scale(start_img, (120, 40))
		start_rect = start_img.get_rect(center=(WIDTH//2, HEIGHT-80))

		overlay = pygame.image.load('piano/Assets/red overlay.png')
		overlay = pygame.transform.scale(overlay, (WIDTH, HEIGHT))

		# MUSIC **********************************************************************

		buzzer_fx = pygame.mixer.Sound('piano/Sounds/piano-buzzer.mp3')

		pygame.mixer.music.load('piano/Sounds/piano-bgmusic.mp3')
		pygame.mixer.music.set_volume(0.8)
		pygame.mixer.music.play(loops=-1)

		# FONTS **********************************************************************

		score_font = pygame.font.Font('piano/Fonts/Futura condensed.ttf', 32)
		title_font = pygame.font.Font('piano/Fonts/Alternity-8w7J.ttf', 30)
		gameover_font = pygame.font.Font('piano/Fonts/Alternity-8w7J.ttf', 40)

		title_img = title_font.render('Piano Tiles', True, WHITE)

		# BUTTONS ********************************************************************

		close_img = pygame.image.load('piano/Assets/closeBtn.png')
		replay_img = pygame.image.load('piano/Assets/replay.png')
		sound_off_img = pygame.image.load("piano/Assets/soundOffBtn.png")
		sound_on_img = pygame.image.load("piano/Assets/soundOnBtn.png")

		close_btn = Button(close_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 120)
		replay_btn = Button(replay_img, (36,36), WIDTH // 2  - 18, HEIGHT//2 + 115)
		sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120)

		# GROUPS & OBJECTS ***********************************************************

		tile_group = pygame.sprite.Group()
		square_group = pygame.sprite.Group()
		text_group = pygame.sprite.Group()

		time_counter = Counter(win, gameover_font)

		# FUNCTIONS ******************************************************************

		def get_speed(score):
			return 150 + 5 

		def play_notes(notePath):
			pygame.mixer.Sound(notePath).play()

		# NOTES **********************************************************************

		with open('piano/notes.json') as file:
			notes_dict = json.load(file)

		# VARIABLES ******************************************************************

		score = 0
		high_score = 0
		speed = 0
		save_status = True
		self.start_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

		clicked = False
		pos = None

		home_page = True
		game_page = False
		game_over = False
		sound_on = True

		count = 0
		overlay_index = 0

		running = True
		while running:
			pos = None

			count += 1
			if count % 100 == 0:
					square = Square(win)
					square_group.add(square)
					counter = 0

			win.blit(bg_img, (0,0))
			square_group.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE or \
						event.key == pygame.K_q:
						running = False

				if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
					pos = event.pos

				if (event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w)) and not game_over:
					left = True
				
				if (event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w)) and not game_over:
					left = False

			if home_page:
				win.blit(piano_img, (WIDTH//8, HEIGHT//8))
				win.blit(start_img, start_rect)
				win.blit(title_img, (WIDTH // 2 - title_img.get_width() / 2 + 10, 300))

				if pos and start_rect.collidepoint(pos) or (event.type == pygame.KEYDOWN and 
				(event.key == pygame.K_UP or event.key == pygame.K_DOWN or\
	 			 event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_w)):
					home_page = False
					game_page = True

					x = random.randint(0, 3)
					t = Tile(x * TILE_WIDTH, -TILE_HEIGHT, win)
					tile_group.add(t)

					pos = None
					left = False

					notes_list = notes_dict['2']
					note_count = 0
					pygame.mixer.set_num_channels(len(notes_list))

			if game_page:
				time_counter.update()
				if time_counter.count <= 0:
					for tile in tile_group:
						tile.update(speed)

						if left:
							if tile.alive:
								tile.alive = False
								score += 1
								if score >= high_score:
									high_score = score
								
								note = notes_list[note_count].strip()
								th = Thread(target=play_notes, args=(f'piano/Sounds/{note}.ogg', ))
								th.start()
								th.join()
								note_count = (note_count + 1) % len(notes_list)

								tpos = tile.rect.centerx - 10, tile.rect.y
								text = Text('+1', score_font, tpos, win)
								text_group.add(text)

						if pos:
							if tile.rect.collidepoint(pos):
								if tile.alive:
									left = False
									tile.alive = False
									score += 1
									if score >= high_score:
										high_score = score
									
									note = notes_list[note_count].strip()
									th = Thread(target=play_notes, args=(f'piano/Sounds/{note}.ogg', ))
									th.start()
									th.join()
									note_count = (note_count + 1) % len(notes_list)

									tpos = tile.rect.centerx - 10, tile.rect.y
									text = Text('+1', score_font, tpos, win)
									text_group.add(text)

								pos = None

						if tile.rect.bottom >= HEIGHT and tile.alive:
							if not game_over:
								tile.color = (255, 0, 0)
								buzzer_fx.play()
								game_over = True

					if pos:
						buzzer_fx.play()
						game_over = True

					if len(tile_group) > 0:
						t = tile_group.sprites()[-1]
						if t.rect.top + speed >= 0:
							x = random.randint(0, 3)
							y = -TILE_HEIGHT - (0 - t.rect.top)
							t = Tile(x * TILE_WIDTH, y, win)
							tile_group.add(t)

					text_group.update(speed)
					img1 = score_font.render(f'Score : {score}', True, WHITE)
					win.blit(img1, (70 - img1.get_width() / 2, 10))
					img2 = score_font.render(f'High : {high_score}', True, WHITE)
					win.blit(img2, (200 - img2.get_width() / 2, 10))
					for i in range(4):
						pygame.draw.line(win, WHITE, (TILE_WIDTH * i, 0), (TILE_WIDTH*i, HEIGHT), 1)

					speed = int(get_speed(score) * (FPS / 1000))


					if game_over:
						speed = 0						

						if save_status:
							save_status = False
							self.score_analysis(score)

						if overlay_index > 20:
							win.blit(overlay, (0,0))

							img1 = gameover_font.render('Game over', True, WHITE)
							img2 = score_font.render(f'Score : {score}', True, WHITE)
							win.blit(img1, (WIDTH // 2 - img1.get_width() / 2, 180))
							win.blit(img2, (WIDTH // 2 - img2.get_width() / 2, 250))

							if close_btn.draw(win):
								running = False

							if replay_btn.draw(win) or (event.type == pygame.KEYDOWN and 
							(event.key == pygame.K_UP or event.key == pygame.K_DOWN or\
							 event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_w)):
								index = random.randint(1, len(notes_dict))
								notes_list = notes_dict[str(index)]
								note_count = 0
								pygame.mixer.set_num_channels(len(notes_list))

								text_group.empty()
								tile_group.empty()
								score = 0
								speed = 0
								overlay_index = 0
								game_over = False
								save_status = True
								self.start_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

								time_counter = Counter(win, gameover_font)

								x = random.randint(0, 3)
								t = Tile(x * TILE_WIDTH, -TILE_HEIGHT, win)
								tile_group.add(t)

							if sound_btn.draw(win):
								sound_on = not sound_on
						
								if sound_on:
									sound_btn.update_image(sound_on_img)
									pygame.mixer.music.play(loops=-1)
								else:
									sound_btn.update_image(sound_off_img)
									pygame.mixer.music.stop()
						else:
							overlay_index += 1
							if overlay_index % 3 == 0:
								win.blit(overlay, (0,0))

			pygame.draw.rect(win, BLUE, (0,0, WIDTH, HEIGHT), 2)
			clock.tick(FPS)
			pygame.display.update()

	# Function To Analyze Result Score
	def score_analysis(self, score):
		finish_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
		self.accuracy = self.analysis(score)
		# self.data.update_ranking(self.username, self.game, int(score))
		data = {
            "เกม": self.game, 
            "คะแนน": str(score), 
            "เวลาเริ่มต้น": self.start_time, 
            "เวลาสิ้นสุด": finish_time, 
            "ความแม่นยำ": self.accuracy,
            "หมายเหตุ": pd.NA
        }
		self.score_list.append(data)
		# task = Thread(target=Database.update_score, args=(self.game, self.username, str(score), self.start_time, finish_time, self.accuracy,))
		# task.start()
		# Database.update_score(self.game, self.username, str(score), self.start_time, finish_time, self.accuracy)
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

if __name__ == '__main__':
	piano = Piano()