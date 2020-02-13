from tkinter import *

root = Tk()
root.title('PropertyGran')
root.geometry('1200x800+100+100')

# создаем главное меню
main_menu = Menu(root)
root.config(menu=main_menu)

# в главное меню добавляем его первый пункт "Файл"
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Файл', menu=file_menu)
# в пункт меню "файл" добавряем его содержимое
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Выход')

# фрейм с полями для поиска информации
search_info_frame = Frame(root, width=800, height=400)
search_info_frame.place(anchor='nw', x=10, y=10)

# input_string_id = Entry(width=40)
# input_string_id.place(anchor='nw', x=100, y=10)


class InputString:
    def __init__(self, wind, width, anchor, x, y):
        self.input_string_id = Entry(wind, width=width)
        self.input_string_id.place(anchor=anchor, x=x, y=y)

    def label(self, wind, text, anchor, xl, yl):
        self.label = Label(wind, text=text)
        self.label.place(anchor=anchor, x=xl, y=yl)


input_string_id = InputString(search_info_frame, 40, 'nw', 100, 10).label(search_info_frame, 'text', 'nw', 40, 10)
input_string_rm = InputString(search_info_frame, 40, 'nw', 100, 50).label(search_info_frame, 'text2', 'nw', 40, 50)
input_string_p = InputString(search_info_frame, 40, 'nw', 100, 90).label(search_info_frame, 'text2', 'nw', 40, 90)

# input_label_id = InputString.label(search_info_frame, 'text', 'nw', 100, 20)



root.mainloop()