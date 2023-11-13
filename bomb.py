#want to be able to make sure its only plantable in certain spot

class Bomb():
    def __init__(self,pos):
        # attributes  image, rect
        self.image = pygame.image.load('assets/images/{insertimagehere}')
        self.image = pygame.transform.scale_by(self.image, 0.05)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.boom_time = 25

print('po')