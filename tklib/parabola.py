import tkinter

default_color = "green"


def _parabola(page, size):
    for x in range(-size, size):
        _plot(page, x, x * x / size)


def _plot(page, x, y):
    global default_color  # use global variable
    page.create_line(x, -y, x+1, -y+1, fill=default_color)


def _circle(page, radius, x, y, color="red"):
    page.create_oval(x + radius, -y + radius, x - radius, -y - radius, outline=color, width=2)


def _draw_axes(page):
    page.update()
    x_origin = page.winfo_width() // 2
    y_origin = page.winfo_height() // 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, -y_origin, 0, y_origin, fill="black")
    print(locals())


def main_parabola():
    mainWindow = tkinter.Tk()
    mainWindow.title("Parabola Demo")
    mainWindow.geometry('640x480')
    canvas = tkinter.Canvas(mainWindow, {"width": 640, "height": 480})
    canvas.grid({"row": 0, "column": 0})
    _draw_axes(canvas)
    _parabola(canvas, 320)
    _parabola(canvas, 100)
    _circle(canvas, 10, 100, 100)
    _circle(canvas, 50, -100, -100, color="black")
    mainWindow.mainloop()


if __name__ == "__main__":
    main_parabola()


