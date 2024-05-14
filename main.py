import pygame
from dialog import DialogBox

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Визуальная новелла")

# Загрузка фона
background = pygame.image.load("background2.png").convert()

# Создание диалогового окна
dialog_box = DialogBox("dialog_box.png")

# Загрузка диалога из файла
dialog_box.load_dialog("dialog.txt")

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # При нажатии на кнопку мыши переходим к следующей строке диалога
            dialog_box.next_line()

    # Очистка экрана
    screen.blit(background, (0, 0))

    # Отображение диалогового окна
    dialog_box.update()
    dialog_box.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()