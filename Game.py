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
pygame.display.set_caption("yuans a bum")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)

# Fonts
font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 100)

# Text input stuff
inputted_text = ""
input_active = True


# Loop to get name of user
while input_active:

    for event in pygame.event.get():
        # Allows game to be closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN: # If pygame event is keydown
            if event.key == pygame.K_RETURN: # If return is pressed, check for conditions
                if len(inputted_text) > 12: # Show message if length of user input is longer than 12
                    screen.fill(black)
                    text = font.render("Too long, keep it under 12", True, white)
                    screen.blit(text, (150, 230))
                    pygame.display.flip()
                    time.sleep(2)
                elif len(inputted_text) <= 0: # Show message if length of user input is same or shorter than 0 somehow
                    screen.fill(black)
                    text = font.render("You need a name", True, white)
                    screen.blit(text, (150, 230))
                    pygame.display.flip()
                    time.sleep(2)
                else:
                    input_active = False

            elif event.key == pygame.K_BACKSPACE: # Lets user delete letters
                inputted_text = inputted_text[:-1]
            else:
                inputted_text += event.unicode # Add typed characters into the variable

    screen.fill(black)

    # Blit text
    text = font.render("Please enter your name here", True, white)
    screen.blit(text, (150, 230))

    text = font.render(inputted_text, True, white)
    screen.blit(text, (150, 280))

    pygame.display.flip() # Update display
    clock.tick(60) # Set fps



intro_running = True
start_time = pygame.time.get_ticks() # Get tick at time of loop start

while intro_running:

    for event in pygame.event.get():
        # Allows game to be closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


    time_elapsed = pygame.time.get_ticks() # Get surrent running time
    running_time = time_elapsed - start_time # Make running_time the time the loop has been running

    screen.fill(black)

    if running_time > 200 and running_time < 4000:
        text = font.render(f"Alright hi {inputted_text},", True, white)
        screen.blit(text, (130, 230))
        text = font.render("Yuan has lost his girlfriend Trista", True, white)
        screen.blit(text, (130, 280))
        text = font.render("You gotta go find her", True, white)
        screen.blit(text, (130, 330))

    elif running_time > 4000 and running_time < 8000:
        text = font.render("But the only issue is that", True, white)
        screen.blit(text, (130, 230))
        text = font.render("the person you find might be Cody,", True, white)
        screen.blit(text, (130, 280))
        text = font.render("and Yuan really doesn't want to", True, white)
        screen.blit(text, (130, 330))
        text = font.render("date Cody", True, white)
        screen.blit(text, (130, 380))

    elif running_time > 8000 and running_time < 12000:
        text = font.render("Yuan so stinky he leaves a", True, white)
        screen.blit(text, (130, 230))
        text = font.render("trail of gross slob behind him.", True, white)
        screen.blit(text, (130, 280))
        text = font.render("It reveals anyone caught in it,", True, white)
        screen.blit(text, (130, 330))
        text = font.render("use it to find his girlfriend", True, white)
        screen.blit(text, (130, 380))


    elif running_time > 12000 and running_time < 16000:
        text = font.render("After the search timer ends, you", True, white)
        screen.blit(text, (130, 230))
        text = font.render("will be presented with an option", True, white)
        screen.blit(text, (130, 280))
        text = font.render("between Trista or Cody, pick the", True, white)
        screen.blit(text, (130, 330))
        text = font.render("person you saw while searching", True, white)
        screen.blit(text, (130, 380))

    if running_time > 16000 and running_time < 18000:
        text = font.render("(Move with A, D and Spacebar btw)", True, white)
        screen.blit(text, (130, 230))
    
    if running_time > 18000:
        intro_running = False

    pygame.display.flip() # Update display
    clock.tick(60) # Set fps


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
    duration_of_jump = 10
    jump_time = 0
    jump_strength = 35
    gravity = 10

    # Player Trail
    trail = []

    # Timer stuff
    timer_duration = 300

    # Random text and random text locations
    people_list = ["Cody", "Trista"]
    text_x = random.randint(50, 850)
    text_y = random.randint(30, 670)
    selected_person = random.choice(people_list)

    while timer_duration > 0:

        for event in pygame.event.get():
            # Allows game to be closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            # Looks for space bar press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump_time = duration_of_jump
        
        # Side to side movement
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if key_pressed[pygame.K_d] and player_x < screen_width - player_width:
            player_x += player_speed

        # Jump if jump_time is greater than 0
        if jump_time > 0:
            player_y -= jump_strength
            jump_time -= 1
        if player_y < 0:
            jump_time = 0
        
        # Gravity
        if player_y < screen_height - player_height:
            player_y += gravity

        screen.fill(black)

        # Trail
        trail.append((player_x, player_y)) # Store player positions in list
        if len(trail) > 13: # Remove oldest position in list if length is longer than set number
            trail.pop(0)
        # Draw trail
        for position in trail: # For every position stored in trail
            pygame.draw.rect(screen, green, (*position, player_width, player_height))

            # Blit hidden text onto screen
        text = font.render(selected_person, True, black)
        screen.blit(text, (text_x, text_y))

        # Blit player image onto screen
        screen.blit(player_image, (player_x, player_y))

        # Timer
        timer_duration -= 1
        text = font.render(f"{round(timer_duration / 60, 2)}", True, white) # Display timer in seconds rounded to 2 decimal places
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

    def end_message(x, y, text):
        screen.fill(black)
        text = big_font.render(text, True, white)
        screen.blit(text, (x, y))
        pygame.display.flip()
        time.sleep(3)

    button_loop = True
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
            # Allows game to be closed
            if event.type == pygame.QUIT:
                sys.exit(0)
            
            # Detect mouse click on buttons
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos_x >= button_x and mouse_pos_x <= button_x + button_width and mouse_pos_y >= button_y and mouse_pos_y <= button_y + button_height:
                if selected_person == people_list[0]: # Show win message if correct button is clicked
                    end_message(180, 300, "Wow gj you win")
                    button_loop = False
                else: # Show lose message if wrong button is clicked
                    end_message(200, 300, "Wow you suck")
                    button_loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos_x >= button2_x and mouse_pos_x <= button2_x + button_width and mouse_pos_y >= button2_y and mouse_pos_y <= button2_y + button_height:
                if selected_person == people_list[1]:
                    end_message(180, 300, "Wow gj you win")
                    button_loop = False
                else:
                    end_message(200, 300, "Wow you suck")
                    button_loop = False

        pygame.display.flip()

        clock.tick(60)

    restart_loop = True
    while restart_loop:
        for event in pygame.event.get():
            # Allows game to be closed
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                restart_loop = False
        
        screen.fill(black)

        text = big_font.render("Click to play again", True, white)
        screen.blit(text, (150, 300))

        pygame.display.flip()
        clock.tick(60)