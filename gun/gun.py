from tkinter import *
from random import choice, randint

#я взял для удобства квадратный экран
screen_width = 400
screen_height = 400
timer_delay = 100


class Ball:
    initial_number=10
    minimal_radius=15
    maximal_radius=40
    available_colors=['green', 'blue', 'red', 'magenta', '#CCCCAA']

    def __init__(self):
        """создаю шарик в случайном положении
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor=choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1,
                                            fill=fillcolor, outline=fillcolor)

        self._Vx = randint(-2,+2)
        self._Vy = randint(-2,+2)


    def fly(self):
        """
        шарики летают
        :return:
        """
        self._x += self._Vx
        self._y += self._Vy
        #отталкивается от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width-2*self._R-1
            self._Vx = -self._Vx
        #отталкивается от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2* self._R >= screen_height:
            self._y = screen_height-2*self._R-1
            self._Vy = -self._Vy

        canvas.coords(self._avatar, self._x, self._y,
                      self._x + 2*self._R, self._y+2*self._R)


class Gun:
    def __init__(self):
        """расположение пушки в начале
        :return:
        """
        self._x = 0
        self._y = screen_height-1
        self._lx = 30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly)


    def shoot(self):
        """
        стрельба
        :return: возвращает объект снаряда
        """
        shell = Ball()
        shell._x = self._x + self._lx
        shell._y = self._y + self._ly
        shell._Vx = self._lx/10
        shell._Vy = self._ly/10
        shell._R = 5
        shell.fly()
        return shell


    def gun_move(self):
        """
        движение пушки за мышью и смещение шарика
        :return:
        """
        self._kx = self._x+self._lx
        self._ky = self._y+self._ly
        if self._kx > move_x:
            self._kx = move_x
        elif self._ky < move_y:
            self._ky = move_y
        elif move_x>self._kx and move_y<screen_width-move_x:
            self._kx = move_x
        elif move_y<self._ky and move_x>screen_height-move_y:
            self._ky = move_y
        canvas.coords(self._avatar, self._x, self._y,
                      self._kx, self._ky)



def init_game():
    """
    создаем объекты-шарики и объект пушку
    :return:
    """
    global balls, gun, shells_on_fly
    balls = [Ball() for i in range(Ball.initial_number)]
    shells_on_fly = []
    gun = Gun()



def init_main_window():
    """
    Иниципализцаия окна
    """
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    canvas = Canvas(root, width=screen_width, height=screen_height, bg="white")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)
    canvas.bind('<Button-1>', click_event_handler)
    canvas.bind('<Motion>', move_event_handler)


def timer_event():
    """Создание таймера - все периодические рассчеты, которые я хочу, делаются здесь
    """
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()
    canvas.after(timer_delay, timer_event)


def click_event_handler(event):
    """считывание клика и выстред
    """
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)


def move_event_handler(event):
    """считывание движения мыши и поворот пушки
    """
    global move_x, move_y
    move_x = event.x
    move_y = event.y
    gun.gun_move()

    #FIXME

if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()
    print ('закрыто')