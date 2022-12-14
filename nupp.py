class Nupp():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image=image
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text= self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image=self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos, self.y_pos))
    #nupu klass mis võtab parameetriteks 2 värvi, fonti,teksti, ja asukoha
    #kui me nupule png pilti ei anna siis tekst üksi töötab ka nupuna
        
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    #värskendab nupu graafilist olekut
        
    def checkinput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    #see funktsioon on hiire asukoha kontrollimiseks, väljastab True vaid siis kui hiir on nupu peal
    #kasutame seda, et muuta hiire peale ajades nupu/teksti värvi
    
    def changecolor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
    #muudab nupu värvi olenevalt hiire asukohast(kui on nelinurgas, siis värv on hovering_color