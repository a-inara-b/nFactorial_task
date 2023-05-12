import pygame, random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = (width, height) = (850, 640)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rock paper scissors")

clock = pygame.time.Clock()
FPS = 60

rock_image = pygame.image.load("images/rock.png")
paper_image = pygame.image.load("images/paper.png")
scissors_image = pygame.image.load("images/scissors.png")

rock_image = pygame.transform.scale(rock_image, (30, 30))
paper_image = pygame.transform.scale(paper_image, (30, 30))
scissors_image = pygame.transform.scale(scissors_image, (30, 30))

font = pygame.font.SysFont("Comic Sans MS", 25)
font1 = pygame.font.SysFont("Verdana", 50)
scissors_text = font.render("Scissors:", True, BLACK)
rocks_text = font.render("Rocks:", True, BLACK)
paper_text = font.render("Paper:", True, BLACK)

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy, type):
        super().__init__()
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.type = type
        self.image = None
        self.set_image()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # self.rect_center = (self.x, self.y)

    def draw(self):
        self.set_image()
        screen.blit(self.image, self.rect)

    def set_image(self):
        if self.type == "rock":
            self.image = rock_image
        if self.type == "paper":
            self.image = paper_image
        if self.type == "scissors":
            self.image = scissors_image

    def move(self):
        self.rect.move_ip(self.speedx, self.speedy)
        self.x += self.speedx
        self.y += self.speedy
        # self.rect_center = (self.x, self.y)

        if self.rect.bottom > 600:
            if self.speedy > 0:
                self.speedy *= -1
        if self.rect.top < 50:
            if self.speedy < 0:
                self.speedy *= -1
        if self.rect.right > 820:
            self.speedx *= -1
        if self.rect.left < 30:
            self.speedx *= -1

        self.draw()
 
def init_objects():
    objects = []
    for i in range(10):
        objects.append(Object(random.randint(30, 790), random.randint(45, 570), random.uniform(0.8, 2) * random.choice([-1, 1]), random.uniform(0.8, 2) * random.choice([-1, 1]), "rock"))
        objects.append(Object(random.randint(30, 790), random.randint(45, 570), random.uniform(0.8, 2) * random.choice([-1, 1]), random.uniform(0.8, 2) * random.choice([-1, 1]), "paper"))
        objects.append(Object(random.randint(30, 790), random.randint(45, 570), random.uniform(0.8, 2) * random.choice([-1, 1]), random.uniform(0.8, 2) * random.choice([-1, 1]), "scissors"))
    return objects

objects = init_objects()

rocks = pygame.sprite.Group() 
papers = pygame.sprite.Group() 
scissorss = pygame.sprite.Group() 
for i in objects:
    if i.type == "rock":
        rocks.add(i)
    elif i.type == "paper":
        papers.add(i)
    elif i.type == "scissors":
        scissorss.add(i)

def check_for_win():
    if len(scissorss) == 30:
        won_text = font1.render("Scissors won!", True, BLACK)
        screen.blit(won_text, (250, 280))
        # pygame.display.flip()
    elif len(papers) == 30:
        won_text = font1.render("Paper won!", True, BLACK)
        screen.blit(won_text, (270, 280))
        # pygame.display.flip()
    elif len(rocks) == 30:
        won_text = font1.render("Rocks won!", True, BLACK)
        screen.blit(won_text, (270, 280))
        # pygame.display.flip()

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    scissors_cnt_text = font.render(str(len(scissorss)), True, BLACK)
    rocks_cnt_text = font.render(str(len(rocks)), True, BLACK)
    paper_cnt_text = font.render(str(len(papers)), True, BLACK)
    won_text = font1.render("Paper won!", True, BLACK)

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (30, 50), (820, 50), 1)
    pygame.draw.line(screen, BLACK, (30, 600), (820, 600), 1)
    pygame.draw.line(screen, BLACK, (30, 50), (30, 600), 1)
    pygame.draw.line(screen, BLACK, (820, 50), (820, 600), 1)
    screen.blit(scissors_text, (30, 10))
    screen.blit(scissors_cnt_text, (150, 10))
    screen.blit(rocks_text, (350, 10))
    screen.blit(rocks_cnt_text, (440, 10))
    screen.blit(paper_text, (705, 10))
    screen.blit(paper_cnt_text, (795, 10))
    for i in objects:
        # screen.blit()
        i.draw()
        i.move()

    for rock in rocks:
        if pygame.sprite.spritecollideany(rock, papers):
            rock.type = "paper"
            papers.add(rock)
            rocks.remove(rock)
    for paper in papers:
        if pygame.sprite.spritecollideany(paper, scissorss):
            paper.type = "scissors"
            scissorss.add(paper)
            papers.remove(paper)
    for scissors in scissorss:
        if pygame.sprite.spritecollideany(scissors, rocks):
            scissors.type = "rock"
            rocks.add(scissors)
            scissorss.remove(scissors)

    check_for_win()
    pygame.display.update()
    clock.tick(FPS)
print(len(rocks))
print(len(papers))
print(len(scissorss))
pygame.quit()