import pygame

class DialogBox:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 720)
        self.text = ""
        self.name = ""
        self.font_name = pygame.font.Font(None, 48)
        self.font_text = pygame.font.Font(None, 42)
        self.typing_speed = 30
        self.typing_timer = 0
        self.typing_index = 0
        self.dialog_lines = []
        self.current_line = 0

    def update(self):
        if self.typing_index < len(self.text):
            self.typing_timer += pygame.time.get_ticks()
            if self.typing_timer >= self.typing_speed:
                self.typing_timer = 0
                self.typing_index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        name_surface = self.font_name.render(self.name, True, (255, 255, 255))
        name_rect = name_surface.get_rect()
        name_rect.bottomleft = self.rect.topleft
        name_rect.x += 10
        name_rect.y += 40
        screen.blit(name_surface, name_rect)
        text_surface = self.font_text.render(self.text[:self.typing_index], True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = name_rect.bottomleft
        text_rect.x += 10
        text_rect.y += 15
        screen.blit(text_surface, text_rect)

    def set_text(self, text, name=""):
        self.text = text
        self.name = name
        self.typing_index = 0
        self.typing_timer = 0

    def load_dialog(self, dialog_file):
        characters = {}
        with open(dialog_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    character, text = line.split('"', 1)
                    character = character.strip()
                    text = text.strip('"')
                    if character not in characters:
                        characters[character] = []
                    characters[character].append(text)

        for character, lines in characters.items():
            for line in lines:
                self.dialog_lines.append((character, line))

    def next_line(self):
        if self.current_line < len(self.dialog_lines):
            self.name, self.text = self.dialog_lines[self.current_line]
            self.typing_index = 0
            self.typing_timer = 0
            self.current_line += 1
        if self.text == "quit":
            pygame.quit()