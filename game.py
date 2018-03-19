# Jack Good (jg8dp)
# This is a little project I made just for fun
# it is a simple game based on user input
# it has sound and colorful images and backgrounds
# I encourage you to run it, it can be pretty fun :)


import pygame
import gamebox
import random

""" The main idea of this game is to have a player dodge objects falling from above. I plan on having the user input be
 pressing the right and left keys to move the player horizontally.
 """
camera = gamebox.Camera(800, 600)
character = gamebox.from_image(50, 200, "http://www.freeiconspng.com/uploads/rocket-ship-png-6.png")
background = gamebox.from_image(camera.x,camera.y,"https://i.ytimg.com/vi/fOl6TUPTcO8/maxresdefault.jpg")
# Create a list of walls
enemies = []
health = [
    gamebox.from_color(750,15,'red',50,25),
    gamebox.from_color(695,15,'red',50,25),
    gamebox.from_color(640,15,'red',50,25),
]
health_text = gamebox.from_text(700, 45, "Health", 'Arial', 25, 'white', italic=True)
start_screen = [
    gamebox.from_text(400,250, "Asteroid Dodge!", "Arial", 25, 'white'),
    gamebox.from_text(400,300, "By Jack Good", "Arial", 25, 'white'),
    gamebox.from_text(400,350, "Use the right and left arrow keys to dodge the asteriods. You have 3 lives.", "Arial", 25, 'white'),
    gamebox.from_text(400,400, "Press enter to begin", "Arial", 25, 'white', bold = True),
    ]
music = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/3/3c/Beat_electronic.ogg")
counter = 0
screen_motion = 0
seconds = 0
enemy_index = 0
num = 0
divider = 60
game_on = False
end_game = False
def tick(keys):
    global game_on
    global counter
    global screen_motion
    global seconds
    global health
    global enemy_index
    global enemies
    global end_game
    global num
    global divider

    if end_game == False:
        camera.clear('cyan')
        camera.draw(background)
        if game_on == False:
            camera.draw(background)
            for text in start_screen:
                camera.draw(text)
        if pygame.K_RETURN in keys:
            game_on = True



        if game_on == True:
            camera.clear('cyan')
            if pygame.K_RIGHT in keys:
                character.x += 15
            if pygame.K_LEFT in keys:
                character.x -= 15

            character.yspeed = -6
            character.y = 500 - screen_motion
            background.yspeed = -6
            background.y = 300 - screen_motion

            camera.draw(background)
            camera.draw(character)
            camera.y -= 6
            if character.x > 790:
                character.x = 785
            if character.x < 10:
                character.x = 15

            counter += 1
            if counter % divider == 0:
                new_enemies = gamebox.from_image(random.randint(0, 800), camera.y - 300, 'https://opengameart.org/sites/default/files/styles/thumbnail/public/1346943991.png ')
                # new_enemies2 = gamebox.from_image(random.randint(200,600), camera.y -300, 'http://img12.laughinggif.com/pic/HTTP29yaWcxNS5kZXZpYW50YXJ0Lm5ldC84YWQ4L2YvMjAxNS8yNDEvNy9kL2ZpcmViYWxsX2dpZl9ieV90YXRtaW9uZS1kOTdscWJ1LmdpZgloglog.gif')
                enemies.append(new_enemies)
                enemy_index += 1
                # wall list continues to grow
            if counter % 0.5 == 0:
                screen_motion += 6
            if counter == 1:

                music.play()
            for health_bar in health:
                health_bar.y = 15 -screen_motion
                camera.draw(health_bar)

            for enemy in enemies:
                # if character.touches(enemy):
                #     character.move_to_stop_overlapping(enemy)
                camera.draw(enemy)
                if character.touches(enemy,-95,0):
                    music1 = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/5/56/Aplausos.ogg")
                    music1.play()
                    enemy_index1 = enemies.index(enemy)
                    enemies.pop(enemy_index1)
                    health.pop()
                    num += 1

            if counter % 30 == 0:
                seconds +=1
            if seconds % 5 == 0 and counter%30 ==0:
                print(seconds,divider)
                divider = divider/2
            show_score = gamebox.from_text(120, 15, "Time elapsed: " +str(seconds)+ " seconds", 'Arial', 25, 'white',)
            show_score.y = 15 - screen_motion
            camera.draw(show_score)
            health_text.y = 45 - screen_motion
            camera.draw(health_text)
            if num == 3:
                end_game = True
        camera.display()

    else:
        camera.clear('black')
        camera.draw(background)
        end_screen = [
            gamebox.from_text(400, 295-screen_motion, "Good Game. Well Played.", "Arial", 50, 'white'),
            gamebox.from_text(400, 355-screen_motion, "You Lasted " + str(seconds) + " seconds", "Arial", 50, 'white')
        ]
        for text in end_screen:
            camera.draw(text)
        music.stop()



        camera.display()

ticks_per_second = 30


gamebox.timer_loop(ticks_per_second, tick)