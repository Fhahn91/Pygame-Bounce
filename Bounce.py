##
#   Program that imports the Pygame module to have an image of a dog and cat
#   bounce around the frame.
#
 
# Importing Pygame Module
import pygame
 
# Intilizing Pygame modules
pygame.init()
 
# Defining the colors.
red = (255, 0, 0)
black = (0, 0, 0)
blue = (51, 51, 255)
keylime = (204, 255, 102)

#Defining the screen size, setting the display, and naming display.
output_display = [1000, 600]
screen = pygame.display.set_mode(output_display)
pygame.display.set_caption("Cat Chase")
 
# Setting variables that will bounce and importing images into them ; Converts image
# pixels to include alpha channels.
Cat = pygame.image.load('C:\\Python\\Images\\GypGyp.png').convert_alpha()
Dog = pygame.image.load('C:\\Python\\Images\\PupPup.png').convert_alpha()
Bckgrnd = pygame.image.load('C:\\Python\\Images\\dvdsnvle_ste_prk.jpg').convert_alpha()
 
# Defining event
Bounce = False
 
# Setting clock variable
clock = pygame.time.Clock()
 
# Defining positions
red_pos_x = 0
red_pos_y = 0
key_pos_x = 90
key_pos_y = 30
cat_pos_x = 20
cat_pos_y = 20
dog_pos_x = 186
dog_pos_y = 186
 
# Defining speed and direction
spd_dir_x = 15
spd_dir_y = 10
spd_dir1_x = 15
spd_dir1_y = 10
spd_dir2_x = 20
spd_dir2_y = 15
spd_dir3_x = 23
spd_dir3_y = 12
 
# Intializing event with while loop.
while Bounce == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bounce = True
 
    # Creating displaying and setting background to black.
    screen.blit(Bckgrnd, [0,0])
 
    # Drawing the images on the screen and setting their position.
    screen.blit(Cat, (cat_pos_x, cat_pos_y))
    screen.blit(Dog, (dog_pos_x, dog_pos_y))
    pygame.draw.circle(screen, keylime, (key_pos_x, key_pos_y), 20, 0)
    pygame.draw.circle(screen, red, (red_pos_x, red_pos_y), 20, 0)
 
    # Using the addition assignment operator to update positions.
    cat_pos_x += spd_dir_x
    cat_pos_y += spd_dir_y
    dog_pos_x += spd_dir1_x
    dog_pos_y += spd_dir1_y
    key_pos_x += spd_dir2_x
    key_pos_y += spd_dir2_y
    red_pos_x += spd_dir3_x
    red_pos_y += spd_dir3_y
    
 
    # Using 'if' loop and 'or' operator to invert the speed and
    # direction of the images when they reach the display boundries.
    if cat_pos_y > 500 or cat_pos_y < 0:
        spd_dir_y = spd_dir_y * -1
    if cat_pos_x > 900 or cat_pos_x < 20:
        spd_dir_x = spd_dir_x * -1
 
    if dog_pos_y > 500 or dog_pos_y < 0:
        spd_dir1_y = spd_dir1_y * -1
    if dog_pos_x > 900 or dog_pos_x < 20:
        spd_dir1_x = spd_dir1_x * -1

    if key_pos_y > 500 or key_pos_y < 0:
        spd_dir2_y = spd_dir2_y * -1
    if key_pos_x > 900 or key_pos_x < 20:
        spd_dir2_x = spd_dir2_x * -1

    if red_pos_y > 500 or red_pos_y < 0:
        spd_dir3_y = spd_dir3_y * -1
    if red_pos_x > 900 or red_pos_x < 20:
        spd_dir3_x = spd_dir3_x * -1
    # Using clock to set frames per second.
    clock.tick(60)
 
    # Updating the cotents of the entire display.
    pygame.display.flip()
 
# Unintializing display module.
pygame.quit()
