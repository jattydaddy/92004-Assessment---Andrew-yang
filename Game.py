'''
Yuan has unfortunately lost his beloved girlfriend Trista, 
he must go find her.
Yuan leaves a nasty stink trail behind him that reveals whoever's caught in it.
Use A, D and SPACE to run around and locate people.
But be careful, the person you find could also be Cody, and Yuan doesn't want him to be his girlfriend.

(Full permissions to make this game and use these images were granted by the Yuan Dong himself)
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
textbox_colour = (230, 162, 173)

# Fonts
font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 100)

# Text locations
default_text_y = 230
text_spacing = 50 # Vertical text offset


# Define text displayed in center of screen
def message(y, text):
    text = font.render(text, True, white)
    text_pos = text.get_rect(center = (screen_width // 2, y))
    screen.blit(text, (text_pos))


def get_username(): # Function to get username

    # Text input stuff
    inputted_text = ""
    input_active = True
    banned_names = ["yuan", "yuan dong", "yu an", "dong", "yuans dongy", "dongy", "yuans", "yuandong"]
    max_name_length = 12 # Longest name allowed
    max_input_length = 45 # Max amount of characters allowed to be typed in the text box

    # Input box
    input_box_start_size = 150 # Width input box starts at
    input_box_spacing = 20 # Space between input box and text inside
    
    # Define message for when input is denied
    def denied_input(text):
        screen.fill(black)
        text = font.render(text, True, white)
        text_pos = text.get_rect(center = (screen_width // 2, screen_height // 2))
        screen.blit(text, (text_pos))
        pygame.display.flip()
        time.sleep(2)

    # Loop to get name of user
    while input_active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows game to be closed
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN: # If pygame event is keydown
                if event.key == pygame.K_RETURN: # If return is pressed, check for conditions
                    if len(inputted_text) > max_name_length: # Show message if length of user input is longer than 12
                        denied_input("Too long, keep it under 12")

                    elif len(inputted_text) <= 0: # Show message if length of user input is same or shorter than 0 somehow
                        denied_input("You need a name")

                    elif inputted_text.lower() in banned_names: # Show message if name is in banned_names list
                        denied_input("Nah you cant play")
                        
                    else:
                        return inputted_text # Return inputted text

                    inputted_text = "" # Reset inputted text after pressing enter

                elif event.key == pygame.K_BACKSPACE: # Lets user delete letters
                    inputted_text = inputted_text[:-1]
                elif len(inputted_text) < max_input_length: # Add typed characters into the variable as long as it's not too long
                    inputted_text += event.unicode

            screen.fill(hoshino_pink)

            # Get text width and height
            text_width, text_height = font.size(inputted_text)
            text_width = max(input_box_start_size, text_width) # Make textbox start at a certain width
            input_box_width = text_width + input_box_spacing
            input_box_height = text_height + input_box_spacing
        
            # Input box location
            textbox_x = (screen_width - input_box_width) // 2 # Centers textbox
            textbox_y = default_text_y + text_spacing * 3 - 25

            # Draw input box
            pygame.draw.rect(screen, textbox_colour, (textbox_x, textbox_y, input_box_width, input_box_height))

        

        # Blit text
        message(default_text_y, "Welcome to Yuans Love Life")
        message(default_text_y + text_spacing, "Please enter your name to begin")
        message(default_text_y + text_spacing * 2, "V")

        # Show what the user has typed
        message(default_text_y + text_spacing * 3, inputted_text)

        pygame.display.flip() # Update display
        clock.tick(60) # Set fps

def intro(username): # Function to show intro messages
    # Load background image
    background = pygame.image.load("love_background.png")
    background = pygame.transform.scale(background, (screen_width, screen_height))

    message_number = 0

    intro_running = True
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
            message(default_text_y, f"Alright hi {username},")
            message(default_text_y + text_spacing, "Yuan has lost his girlfriend Trista")
            message(default_text_y + text_spacing * 2, "You gotta go find her")
            message(default_text_y + text_spacing * 4, "(Use arrow keys to navigate intro)")

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

            message(default_text_y, "Move with A and D.")
            message(default_text_y + text_spacing, "Jump with spacebar")
            message(default_text_y + text_spacing * 2, "(You can jump infinitely)")
        
        elif message_number == 5:
            intro_running = False

        pygame.display.flip() # Update display
        clock.tick(60) # Set fps

# Names of difficulties
difficulty_names = ["Easy", "Medium", "Hard"]
def difficulty_select():
    # Button stuff
    button_width = 200
    button_height = 100

    # Load background image
    buttons_background = pygame.image.load("yuanbackground.jpg")
    buttons_background = pygame.transform.scale(buttons_background, (screen_width, screen_height))

    button_y_pos = [180, 330, 480]

    # Button colour
    transparent_white = (255, 255, 255, 100)

    button_loop = True
    # Loop for buttons
    while button_loop:

        # Blit background image
        screen.blit(buttons_background, (0, 0))

        # Draw text
        text = big_font.render("Choose the difficulty", True, white)
        text_pos = text.get_rect(center = (screen_width // 2, screen_width // 10))
        screen.blit(text, (text_pos))


        for i in range(len(difficulty_names)): # For number of things in the list
            text = difficulty_names[i] # Assign the string to text
            button_y = button_y_pos[i] # Assign y position from button_y_pos list to button_y
            button_x = (screen_width - button_width) // 2 # Center button to screen
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height) # Make the button dimensions button_rect

            if button_rect.collidepoint(pygame.mouse.get_pos()): # If mouse position is over the button
                button_colour = white
            else:
                button_colour = transparent_white

            # Draw boxes for buttons
            button_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA) # Make new surface that allows opacity
            button_surface.fill(button_colour) # Fills the buttons in
            screen.blit(button_surface, (button_x, button_y)) # Blits the buttons onto the surface

            text = font.render(difficulty_names[i], True, black) # Render text on button
            text_pos = text.get_rect(center = (button_x + button_width // 2, button_y + button_height // 2)) # Set text location to be in middle of button box
            screen.blit(text, (text_pos)) # Blit text at that position


        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows game to be closed
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # When mouse clicks
                mouse_pos = pygame.mouse.get_pos() # Get position of mouse
                for i in range(len(difficulty_names)):
                    button_y = button_y_pos[i]
                    button_x = (screen_width - button_width) // 2
                    button_rect = pygame.Rect(button_x, button_y, button_width, button_height) 

                    if button_rect.collidepoint(mouse_pos): # If the position of the mouse collides with the button rect
                        if difficulty_names[i] == difficulty_names[0]:
                            return difficulty_names[i]
                        elif difficulty_names[i] == difficulty_names[1]:
                            return difficulty_names[i]
                        elif difficulty_names[i] == difficulty_names[2]:
                            return difficulty_names[i]

        pygame.display.flip()
        clock.tick(60)

# 2 Names used in the game
people_list = ["Cody", "Trista"]
def game(difficulty): # Function for the actual game
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
    trail_length = 13

    # Timer stuff
    if difficulty == difficulty_names[0]:
        timer_duration = 600
    elif difficulty == difficulty_names[1]:
        timer_duration = 400
    elif difficulty == difficulty_names[2]:
        timer_duration = 300

    # Random text and random text locations
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
        if len(trail) > trail_length: # Remove oldest position in list if length is longer than set number
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
        clock.tick(60) # Set fps

    return selected_person

def buttons(selected_person): # Function to show buttons
    # Button stuff
    button_width = 300
    button_height = 150
    button_y = 250
    button_x_pos = [110, 480]
    button_options = [people_list[0], people_list[1]]

    # Load background image
    buttons_background = pygame.image.load("yuanbackground.jpg")
    buttons_background = pygame.transform.scale(buttons_background, (screen_width, screen_height))

    # Button colour
    transparent_white = (255, 255, 255, 100)

    # Define ending message
    def end_message(text, text2):
        screen.fill(black)
        text = big_font.render(text, True, white)
        text_pos = text.get_rect(center = (screen_width // 2, screen_height // 2 - text_spacing))
        screen.blit(text, (text_pos))

        text2 = big_font.render(text2, True, white)
        text2_pos = text2.get_rect(center = (screen_width // 2, screen_height // 2 + text_spacing))
        screen.blit(text2, (text2_pos))

        pygame.display.flip()
        time.sleep(2)
        


    button_loop = True
    # Loop for buttons
    while button_loop:

        # Blit background image
        screen.blit(buttons_background, (0, 0))


        for i in range(len(button_options)): # For number of things in the list
            text = button_options[i] # Assign the string to text
            button_x = button_x_pos[i] # Go through list of x coords
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

            if button_rect.collidepoint(pygame.mouse.get_pos()): # If mouse position is over the button
                button_colour = white
            else:
                button_colour = transparent_white

            # Draw boxes for buttons
            button_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA) # Make new surface that allows opacity
            button_surface.fill(button_colour) # Fills the buttons in
            screen.blit(button_surface, (button_x, button_y)) # Blits the buttons onto the surface

            text = big_font.render(people_list[i], True, black) # Render text on button
            text_pos = text.get_rect(center = (button_x + button_width // 2, button_y + button_height // 2)) # Set text location to be in middle of button box
            screen.blit(text, (text_pos)) # Blit text at that position


        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allows game to be closed
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # When mouse clicks
                mouse_pos = pygame.mouse.get_pos() # Get position of mouse
                for i in range(len(button_options)): # For number of names in list
                    button_x = button_x_pos[i]
                    button_rect = pygame.Rect(button_x, button_y, button_width, button_height) 

                    if button_rect.collidepoint(mouse_pos): # If the position of the mouse collides with the button rect
                        if button_options[i] == selected_person:
                            end_message("you win", "yuan dong is proud")
                            button_loop = False


                        elif button_options[i] == selected_person:
                            end_message("you win", "yuan dong is proud")
                            button_loop = False

                        else:
                            end_message("you lose, yuan dong", "is disappointed")                       
                            button_loop = False
                            
        pygame.display.flip()
        clock.tick(60)

def replay(): # Function for replay screen
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
        text_pos = text.get_rect(center = (screen_width // 2, screen_height // 2))
        screen.blit(text, (text_pos))

        pygame.display.flip()
        clock.tick(60)


username = get_username()
intro(username)

while True:
    selected_difficulty = difficulty_select()
    selected_person = game(selected_difficulty)
    buttons(selected_person)

    replay()