#начинаю учить pygame, поэтому сегодня напишу одну из программ
import pygame

pygame.init()

display_width = 800
display_height = 600



car_width = 252
car_height = 311

black = (0, 0, 0)
#чёрный цвет в формате RGB
white = (255, 255, 255)
#белый цвет в формате RGB
red = (255, 0, 0)
#красный цвет в формате RGB

gameDisplay = pygame.display.set_mode((display_width, display_height))
#размер нашего окна 
pygame.display.set_caption('A bit Racey')
#устанавливает название окна
clock = pygame.time.Clock()
#время рендеринга

carImg = pygame.image.load('RaceCar.png')
#функция для импортирования изображения в наш
#модуль, он обязательно должен находиться в текущем каталоге!!! В скобочках название
#импортируемого изображения ОБЯЗАТЕЛЬНО в формате .png!!!

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    gameDisplay.update

    time.sleep(2)

    game_loop()


def car(x, y):
    gameDisplay.blit(carImg, (x, y))
#def car(x, y) создана чтобы мы отобразили изображение на координатах в скобках (x, y)
#gameDisplay.blit(carImg, (x, y)) отображает нашу картинку (в данном случае carImg) на
#определенных координатах  (в данном случае (x, y)




def gaming_process():
    x = (display_width * 0.2)#display_width это ширина вызванного окна
    y = (display_height * 0.2)#display_height это высота вызванного окна

    #переменные display_width и display_height умножаются на числа типа float для того, чтобы
    #место расположения нашей машинки не соприкасалось с границами и её элементы
    #не выходили за пределы раскрытого окна


    x_change = 0
    y_change = 0
    gamExit = True
    #переменная, использующаяся в цикле
    while gamExit:
        for event in pygame.event.get():
            #pygame.event.get() является перехватчиком действий (список)
            if event.type == pygame.QUIT:
                #event.type это тип выполненного действия
                #pygame.QUIT это функция, означающая выход из модуля pygame программы
                #event.type == pygame.QUIT означает "если действие в программе = выход из неё,
                #то необходимо выполнить следующее условие":
                gamExit = False
            
            if event.type == pygame.KEYDOWN:
                #если у нас происходит событие, связанное с нажатием кнопки на клавиатуре, то:
                if event.key == pygame.K_LEFT:
                    #если была нажата стрелочка влево
                    x_change = -5
                    #то переменная, отвечающая за положение нашей картинки после каждого цикла
                    #равняется -5, что двигает наше изображение на координатной плоскости
                    #на 5 позиций влево
                if event.key == pygame.K_RIGHT:
                    #если была нажата стрелочка вправо
                    x_change = 5
                    #то переменная, отвечающая за положение нашей картинки после каждого цикла
                    #равняется 5, что двигает наше изображение на координатной плоскости
                    #на 5 позиций вправо

                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            #!ОЧЕНЬ ВАЖНО ЗАВОДИТЬ УСЛОВИЕ ВЫШЕ, ЕСЛИ ВЫ ХОТИТЕ, ЧТОБЫ ОБЪЕКТ ДВИГАЛСЯ
            #СТРОГО ПОСЛЕ НАЖАТИЕ КНОПКИ ВПРАВО, ВЛЕВО, ВВЕРХ ИЛИ ВНИЗ.
            #ЕСЛИ ЖЕ ТАКОГО УСЛОВИЯ У ВАС НЕ БУДЕТ, ТО, НАПРИМЕР, ПОСЛЕ ОДНОГО
            #НАЖАТИЯ КНОПКИ ВЛЕВО, КАКУЮ БЫ ВЫ КНОПКУ НА КЛАВИАТУРЕ ПОСЛЕ НЕ
            #НАЖИМАЛИ, БУДЕТ ВЫПОЛНЯТСЯ КОМАНДА, ПРОПИСАННАЯ ДЛЯ ЛЕВОЙ КНОПКИ!!!

            x += x_change
            y += y_change

        gameDisplay.fill(black)
                #функцию gameDisplay.fill() мы используем для того, чтобы создать задний фон
                #то, что у нас в скобочках - это цвет заднего фона, который мы задали раньше
                
        car(x, y)
                #вызываем функцию car(x, y) во время выполнения цикла выше

        if x>display_width-car_width  or x<0 or y>display_height-car_height or y<0:
            print('Boom!')
            gamExit = False 
        pygame.display.update()
            #выполнять обновление окна модуля
        clock.tick(60)
            #установленное время обновления окна - 60
gaming_process()
pygame.quit()
#выход из модуля pygame
quit()
#выход из самого модуля



