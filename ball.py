import tkinter
#активация модуля


def button1_command():
    print('button1 pressed')


def print_hello(event):
    me = event.widget
    if me == button1:
        print(1)
    elif me==button2:
        print(2)
    else:
        ValueError()

def init_main_window():
    """
    инициализация главного окна
    :return:
    """
    global root, button1, label, button1, button2, text, scale
    root = tkinter.Tk()

    #создаем кнопку
    button1 = tkinter.Button(root, text="Button1", command=button1_command())
    # упаковываем кнопку, иначе ее не будет видно
    button1.bind("<Button>",print_hello)
    button1.pack()

    button2 = tkinter.Button(root, text="Button2")
    # упаковываем кнопку, иначе ее не будет видно
    button2.bind("<Button>",print_hello)
    button2.pack()

    variable = tkinter.IntVar()
    label = tkinter.Label(root, text="Какой-то текст")
    scale = tkinter.Scale(root)
    text = tkinter.Entry(root)

    for obj in button1, button2, label, scale, text:
        obj.pack()

if __name__ == "__main__":
    init_main_window()

     #запуск пустого окна
    root.mainloop()

