'''
Yuan has unfortunately lost his beloved girlfriend Trista, 
he must go find her.
Yuan leaves a nasty stink trail behind him that reveals whoever's caught in it.
Use A, D and SPACE to run around and locate people.
But be careful, the person you find could also be Cody, and Yuan doesn't want him to be his girlfriend.
'''
# Import libraries
import pygame
import sys
import time
import random

pygame.init()

clock = pygame.time.Clock()

# Set up the screen
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Yuan's Love Story")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
hoshino_pink = (255, 182, 193)

# Fonts
font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 100)







# Text locations
default_text_x = 130
default_text_y = 230
text_spacing = 50

# Text input stuff
inputted_text = ""
input_active = True
banned_names = ["yuan", "yuan dong", "yu an", "dong", "yuans dongy", "dongy"]

# Define message for when input is denied
def denied_input(y, text):
    screen.fill(black)
    text = font.render(text, True, white)
    text_pos = text.get_rect(center = (screen_width / 2, y))
    screen.blit(text, (text_pos))
    pygame.display.flip()
    time.sleep(3)

# Define text displayed in center of screen
def message(y, text):
    text = font.render(text, True, white)
    text_pos = text.get_rect(center = (screen_width / 2, y))
    screen.blit(text, (text_pos))

# Loop to get name of user
while input_active:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Allows game to be closed
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN: # If pygame event is keydown
            if event.key == pygame.K_RETURN: # If return is pressed, check for conditions
                if len(inputted_text) > 12: # Show message if length of user input is longer than 12
                    denied_input(default_text_y, "Too long, keep it under 12")

                elif len(inputted_text) <= 0: # Show message if length of user input is same or shorter than 0 somehow
                    denied_input(default_text_y, "You need a name")

                elif inputted_text.lower() in banned_names: # Show message if name is in banned_names list
                    denied_input(default_text_y, "Nah you cant play")

                else:
                    input_active = False # End loop

            elif event.key == pygame.K_BACKSPACE: # Lets user delete letters
                inputted_text = inputted_text[:-1]
            else:
                inputted_text += event.unicode # Add typed characters into the variable

    screen.fill(black)
    

    # Blit text
    message(default_text_y, "Welcome to Yuans Love Life")
    message(default_text_y + text_spacing, "Please enter your name to begin")
    message(default_text_y + text_spacing * 2, "V")

    # Show what the user has typed
    message(default_text_y + text_spacing * 3, inputted_text)

    pygame.display.flip() # Update display
    clock.tick(60) # Set fps








# Load background image
background = pygame.image.load("love_background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

message_number = 0

intro_running = True
start_time = pygame.time.get_ticks() # Get tick at time of loop start
# Loop for the intro messages
while intro_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Allows game to be closed
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                message_number += 1
            elif event.key == pygame.K_LEFT:
                message_number -= 1


    screen.blit(background, (0, 0))

    if message_number == 0:
        message(default_text_y, f"Alright hi {inputted_text},")
        message(default_text_y + text_spacing, "Yuan has lost his girlfriend Trista")
        message(default_text_y + text_spacing * 2, f"You gotta go find her")

    elif message_number == 1:

        message(default_text_y, "But the only issue is that")
        message(default_text_y + text_spacing, "the person you find might be Cody,")
        message(default_text_y + text_spacing * 2, "and Yuan really doesn't want to")
        message(default_text_y + text_spacing * 3, "date Cody")

    elif message_number == 2:

        message(default_text_y, "Yuan so stinky he leaves a")
        message(default_text_y + text_spacing, "trail of gross slob behind him.")
        message(default_text_y + text_spacing * 2, "It reveals anyone caught in it,")
        message(default_text_y + text_spacing * 3, "so use it to find his girlfriend")



    elif message_number == 3:

        message(default_text_y, "After the search timer ends, you")
        message(default_text_y + text_spacing, "will be presented with an option")
        message(default_text_y + text_spacing * 2, "between Trista or Cody, pick the")
        message(default_text_y + text_spacing * 3, "person you saw while searching")


    elif message_number == 4:

        message(default_text_y, "(Move with A, D and Spacebar btw)")


    
    elif message_number == 5:
        intro_running = False

    pygame.display.flip() # Update display
    clock.tick(60) # Set fps










# Loop that covers whole game part to allow for replaying
while True:

    # Player stuffs like width and position
    player_x = 100
    player_y = 400
    player_width = 90
    player_height = 90

    # Importing an image for the player
    player_image = pygame.image.load("yuansdongy.jpg")
    player_image = pygame.transform.scale(player_image, (player_width, player_height))

    # Player movement
    player_speed = 10

    jump_gravity = 1.8
    jump_height = 25
    jump_strength = 0
    falling_max_velocity = 30


    # Player Trail
    trail = []

    # Timer stuff
    timer_duration = 600

    # Random text and random text locations
    people_list = ["Cody", "Trista"] # List containing 2 names
    text_x = random.randint(20, 820)
    text_y = random.randint(30, 670)
    selected_person = random.choice(people_list)


    # Loop for player movement and game mechanics
    while timer_duration > 0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows game to be closed
                pygame.quit()
                sys.exit()

            # Looks for space bar press for jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump_strength = jump_height
        
        # Side to side movement
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if key_pressed[pygame.K_d] and player_x < screen_width - player_width:
            player_x += player_speed

        # Code for jump
        player_y -= jump_strength # Move player up
        if jump_strength > -falling_max_velocity: # Limits falling speed
            jump_strength -= jump_gravity

        # Prevents player from landing under the screen
        if player_y > screen_height - player_height:
            player_y = screen_height - player_height
            jump_strength = 0

        # Prevents player from going above the screen
        elif player_y < 0:
            player_y = 0
            jump_strength = 0

        # Fill screen with background colour
        screen.fill(hoshino_pink)

        # Trail
        trail.append((player_x, player_y)) # Store player positions in list
        if len(trail) > 13: # Remove oldest position in list if length is longer than set number
            trail.pop(0)
        # Draw trail
        for position in trail: # For every position stored in trail
            pygame.draw.rect(screen, green, (*position, player_width, player_height))

        # Blit hidden text onto screen
        text = font.render(selected_person, True, hoshino_pink)
        screen.blit(text, (text_x, text_y))

        # Blit player image onto screen
        screen.blit(player_image, (player_x, player_y))

        # Timer
        timer_duration -= 1
        text = font.render(f"{round(timer_duration / 60, 2)}", True, black) # Display timer in seconds rounded to 2 decimal places
        screen.blit(text, (20, 20))

        # Update the screen
        pygame.display.flip()

        # Set fps
        clock.tick(60)








    # Button stuff
    button_width = 300
    button_height = 150

    # First button location
    button_x = 110
    button_y = 250

    # Second button location
    button2_x = 480
    button2_y = 250

    # Define ending message
    def end_message(text):
        screen.fill(black)
        text = big_font.render(text, True, white)
        text_pos = text.get_rect(center = (screen_width / 2, screen_height / 2))
        screen.blit(text, (text_pos))
        pygame.display.flip()
        time.sleep(3)


    button_loop = True
    # Loop for buttons
    while button_loop:

        screen.fill(black)

        # Draw boxes for buttons
        pygame.draw.rect(screen, white, (button_x, button_y, button_width, button_height))
        pygame.draw.rect(screen, white, (button2_x, button2_y, button_width, button_height))

        # Blit text onto the buttons
        text = big_font.render(f"{people_list[0]}", True, black)
        screen.blit(text, (button_x + 60, button_y + 40))
        text = big_font.render(f"{people_list[1]}", True, black)
        screen.blit(text, (button2_x + 55, button2_y + 40))

        # Constantly check position of mouse
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows game to be closed
                pygame.quit()
                sys.exit()
            
            # Detect mouse click on buttons
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos_x >= button_x and mouse_pos_x <= button_x + button_width and mouse_pos_y >= button_y and mouse_pos_y <= button_y + button_height:
                if selected_person == people_list[0]: # Show win message if correct button is clicked
                    end_message("Wow gj you win")
                    button_loop = False
                else: # Show lose message if wrong button is clicked
                    end_message("Wow you suck")
                    button_loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos_x >= button2_x and mouse_pos_x <= button2_x + button_width and mouse_pos_y >= button2_y and mouse_pos_y <= button2_y + button_height:
                if selected_person == people_list[1]:
                    end_message("Wow gj you win")
                    button_loop = False
                else:
                    end_message("Wow you suck")
                    button_loop = False

        pygame.display.flip()

        clock.tick(60)








    restart_loop = True
    # Loop for restart button
    while restart_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows game to be closed
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                restart_loop = False
        
        screen.fill(black)

        text = big_font.render("Click to play again", True, white)
        text_pos = text.get_rect(center = (screen_width / 2, screen_height / 2))
        screen.blit(text, (text_pos))

        pygame.display.flip()
        clock.tick(60)