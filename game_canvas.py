import tkinter
from random import choice, randint

ball_initial_number=10
ball_minimal_radius=15
ball_maximal_radius=40
ball_available_colors=['green', 'blue', 'red', 'magenta', '#CCCCAA']


def click_ball(event):
    """Обработчик событий для холста
    По клику нужно удалять тот объект, на который указывает мышка
    """
    obj=canvas.find_closest(event.x, event.y)
    x1,y1,x2,y2 = canvas.coords(obj)

    if x1<=event.x<=x2 and y1<=event.y<=y2:
        canvas.delete(obj)
        create_random_ball()


def move_all_balls(event):
    """передвигает шарик на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(obj,dx,dy)


def create_random_ball():
    """
    Создает шарик случайного цвета
    :return:
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())


def random_color():
    """
    :return: Случайный цвет из некоторого набора
    """
    return choice(ball_available_colors)


def init_ball_catch_game():
    """
    создает необходимое для игры количество шариков, по которым можно будет кликать
       """
    for i in range(ball_initial_number):
        create_random_ball()


def init_main_window():
    """
    Иниципализцаия окна
    """
    global root, canvas
    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__=="__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print ('закрыто')