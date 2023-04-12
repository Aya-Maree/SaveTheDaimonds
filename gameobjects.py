import pygame,random


top_bound = pygame.Rect(175,0,1000,1)
bottom_bound = pygame.Rect(175,665,1000,1)
left_bound = pygame.Rect(175,0,1,666)
right_bound = pygame.Rect(1175,0,1,666)
bg_rect = (175,0,1000,666)


class GameObject(pygame.sprite.Sprite): #this is the parent class, it holds any similarities between any game objects
    def __init__(self,x,y,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path) #this loads the image
        self.rect = self.image.get_rect()   #this gets the rect of the image
        self.rect.center = (x,y) #this centers the center of the rect
        #picking a random x and a random y direction for the objects to move in
        self.rand_xd = random.choice([-1,1]) 
        self.rand_yd = random.choice([-1,1])

    def update(self): #to update, we need to specify how we wany to update (self so it updates itself)
       self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed) 
      # if self.rect.x < 125 or self.rect.x > 1125
       #move method takes the x and y displacements 
       #defing the speed in the Diamond and Spaceship classes will help us make them move faster


class Rectangle():
    def __init__(self,left,top,width,height):
        self.rect = pygame.Rect(left,top,width,height)
        self.image = pygame.Surface((width, height))
    def draw_rect(self,screen,color):
        pygame.draw.rect(screen,color,self.rect)
    def draw_diamond_left(self, diamond_image):
        x = random.randint(0,20)
        y = random.randint(0,600)
        self.image.blit(diamond_image,(x,y))

class NewDiamonds(GameObject):
    def __init__(self,rect):
        
        rand_x = random.randint(rect.left+70,rect.right-70)
        rand_y = random.randint(rect.top+70, rect.bottom-70)
        super().__init__(rand_x,rand_y,"diamond.png" )


class Diamond(GameObject):
    def __init__(self,rect):
        rand_x = random.randint(rect.left+250,rect.width-250) 
        rand_y = random.randint(rect.top+250, rect.height-250)
        super().__init__(rand_x,rand_y,"diamond.png" )
        self.speed = 5 #moves 5 pixels at a time
    def update(self):
        super().update()
        if self.rect.colliderect(left_bound) or self.rect.colliderect(right_bound):
            self.rand_xd = self.rand_xd*(-1)
        if self.rect.colliderect(top_bound) or self.rect.colliderect(bottom_bound):
            self.rand_yd = self.rand_yd*(-1)




class Spaceship(GameObject):
    def __init__(self, screen_rect):
        super().__init__(screen_rect.centerx, screen_rect.centery, 'spaceship.png')
        self.speed = 2 #moves 2 pixels at a time
    def update(self):
        super().update()
        if self.rect.colliderect(left_bound) or self.rect.colliderect(right_bound):
            self.rand_xd = self.rand_xd*(-1)
        if self.rect.colliderect(top_bound) or self.rect.colliderect(bottom_bound):
            self.rand_yd = self.rand_yd*(-1)
            

