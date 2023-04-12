import pygame, time, random
import gameobjects

pygame.init()

# Initialize the game
bg_img = pygame.image.load('background.jpg')
bg_rect = (175,0,1000,666)

screen = pygame.display.set_mode((1350,666))
screen_rect = screen.get_rect()




no_of_diamonds = 10
diamond_group = pygame.sprite.Group() #this initializes a group for the daimonds
for i in range(no_of_diamonds):
   diamond_group.add(gameobjects.Diamond(screen_rect)) #creating objects of type daimond and adding it to the group 

no_of_spaceships = 1
spaceship_group = pygame.sprite.Group()
for i in range(no_of_spaceships):
   spaceship_group.add(gameobjects.Spaceship(screen_rect))

black = (0,0,0)

#drawing the left rectangle
l_rect_w = 175
l_rect_l = 666
#left_rect = pygame.Rect(0,0,l_rect_w,l_rect_l)
#pygame.draw.rect(screen,blue,left_rect)

left_rectangle = pygame.Rect(0,0,l_rect_w,l_rect_l)


left_rect = gameobjects.Rectangle(0,0,l_rect_w,l_rect_l)


#drawing the right rectangle
r_rect_w = 175
r_rect_l = 666

right_rectangle = pygame.Rect(1175,0,175,666)
right_rect = gameobjects.Rectangle(screen_rect.width-175,0,r_rect_w,r_rect_l)

#pygame.draw.rect(screen,blue,right_rect)

#making boundries for the collsion detection
top_bound = pygame.Rect(175,0,1000,1)
bottom_bound = pygame.Rect(175,664,1000,1)
left_bound = pygame.Rect(175,0,1,666)
right_bound = pygame.Rect(1175,0,1,666)

#making the groups for taken and saved
taken_group = pygame.sprite.Group()
saved_group = pygame.sprite.Group()

#diamond1 = gameobjects.Diamond(left_rectangle)
#taken_group.add(diamond1)

diamond_image = pygame.image.load("diamond.png")

font = pygame.font.Font('CoffeeHealing.ttf', 36)
taken = font.render("Taken: {}".format(int(len(taken_group))),True, (223,50,31))
saved = font.render("Saved: {}".format(int(len(saved_group))),True, (223,50,31))

def render():
    screen.blit(bg_img,bg_rect)

    #pygame.draw.rect(screen,blue,left_rect)
    left_rect.draw_rect(screen,black)
    right_rect.draw_rect(screen,black)

    diamond_group.update() #this will update the status of the group 
    diamond_group.draw(screen) #the group will now draw the daimonds on the screen
    

    spaceship_group.update()
    spaceship_group.draw(screen)

    taken_group.draw(screen)
    saved_group.draw(screen)
    screen.blit(taken, (10, 10))
    screen.blit(saved, (1175,10))

    pygame.display.flip()



render() #initialize the screen 
running = True
# gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in diamond_group.sprites():
                if sprite.rect.collidepoint(event.pos):
                    diamond_group.remove(sprite)
                    diamond_group.update()
                    diamond_group.draw(screen)
                    sprite = gameobjects.NewDiamonds(right_rectangle)
                    saved_group.add(sprite)
                    saved = font.render("Saved: {}".format(int(len(saved_group))),True, (223,50,31))
                    print("saved ",saved_group)
    #game logic
    collided_dict = pygame.sprite.groupcollide(diamond_group,spaceship_group,True,False) 
    for diamond in collided_dict.keys():
        diamond = gameobjects.NewDiamonds(left_rectangle)
        taken_group.add(diamond)
        print("taken ",taken_group)
        left_rect.draw_diamond_left(diamond_image)
        taken = font.render("Taken: {}".format(int(len(taken_group))),True, (223,50,31))
    #checks for collision between two different groups 
    #(group1,group2,dokill1,dokill2), so since I want the daimond to disapear i will put true for dokill1
    #render
    render()
    time.sleep(0.05)

pygame.quit()