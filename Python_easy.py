import sys
import os
from tkinter import *
from PIL import Image, ImageTk

# Определяем функцию для получения пути к ресурсам
def resource_path(relative_path):
    """ Получает абсолютный путь к ресурсу, работает как в режиме разработки, так и в режиме сборки. """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Создаем главное окно
root = Tk()
root.geometry("550x537")
root.resizable(False, False)
root["bg"] = "gray14"
root.title("Python - легко!")

# Устанавливаем путь к изображению
background_image_path = resource_path("fg.png")  # Используем относительный путь

# Проверяем, существует ли файл изображения
if os.path.exists(background_image_path):
    img = Image.open(background_image_path)
    bg = ImageTk.PhotoImage(img)
    
    # Устанавливаем изображение в качестве фона
    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    print(f"Файл изображения не найден: {background_image_path}")
    # Можно установить цвет фона, если изображение не найдено
    root["bg"] = "gray15"

# Создаем страницы

pages = [

    {"title": "Введение", "text": "Python - это высокоуровневый язык программирования, который используется для разработки различных типов программ, таких как веб-приложения, игры, научные приложения и т.д. Для вывода текста, используют функцию print()",

     "task": "Задача: Напишите программу, которая выводит 'Hello, Python!'"},

    {"title": "Условные операторы", "text": "Условные операторы if используются для принятия решений в зависимости от определенных условий. Они позволяют программе выполнять различные действия в зависимости от истинности или ложности условия. Чтобы присвоить число с оператору обычно пишут '=='",

     "task": "Задача: Напишите условие, которое выводит 'Условие истинно', если переменная x равна 10."},

    {"title": "Модули и функции", "text": "Модули в Python - это файлы, содержащие код, который можно использовать в других программах. Функции - это блоки кода, которые выполняют определенную задачу, пр.: +,-,/ и т.п ",

     "task": "Задача: Напишите функцию, которая принимает два числа и возвращает их сумму."},

    {"title": "Структуры данных", "text": "Структуры данных в Python позволяют организовывать и хранить данные. Основные структуры данных включают списки (list), также есть особые операторы для списков такие как sum, которые выводят сумму из всего списка",

     "task": "Задача: Создайте список из 5 чисел и выведите их сумму."},

    {"title": "Циклы", "text": "Циклы в Python позволяют выполнять блок кода несколько раз. Основные типы циклов - это 'for' и 'while'.",

     "task": "Задача: Напишите цикл, который выводит все четные числа от 1 до 20."},

    {"title": "Обработка исключений", "text": "Обработка исключений позволяет управлять ошибками, которые могут возникнуть во время выполнения программы. Используйте 'try' и 'except' для обработки исключений.",

     "task": "Задача: Напишите код, который запрашивает у пользователя число и обрабатывает возможное деление на ноль."},

    {"title": "Работа с файлами", "text": "Python позволяет работать с файлами, открывать их, читать и записывать данные. Используйте 'open()', 'read()', 'write()' для работы с файлами.",

     "task": "Задача: Напишите код, который открывает файл 'output.txt' и записывает в него строку 'Hello, File!'."},

    {"title": "Списки и их методы", 

     "text": "Списки в Python - это изменяемые последовательности, которые могут содержать элементы различных типов. Списки поддерживают множество методов, таких как `append()`, `remove()`, `sort()`, и другие.",

     "task": "Задача: Создайте список из 5 фруктов и отсортируйте его в алфавитном порядке."},

    {"title": "Классы и объекты", 

     "text": "Классы в Python позволяют создавать собственные типы данных. Объекты - это экземпляры классов. Классы могут содержать методы и атрибуты.",

     "task": "Задача: Напишите класс `Car`, который имеет атрибуты `brand` и `model`, и метод `display_info()`, который выводит информацию о машине."},


    {"title": "Работа с библиотеками", 

     "text": "Python имеет множество встроенных и сторонних библиотек, которые расширяют его функциональность. Для использования библиотеки необходимо ее импортировать с помощью ключевого слова `import`.",

     "task": "Задача: Импортируйте библиотеку `math` и используйте ее для вычисления квадратного корня из числа 16."},


    {"title": "Результаты", "text": "Поздравляем с прохождением базы изучения Python! Теперь вы знаете основу для дальнейшего изучения"}

]


# Создаем метки и кнопки

current_page = 0


title_label = Label(root, text=pages[current_page]["title"], font='Times 30', fg='#fff200', bg="gray15")

title_label.pack(pady=20)


text_label = Label(root, text=pages[current_page]["text"], font='Times 12', fg='white', bg="gray15", wraplength=500, justify=LEFT)

text_label.pack(pady=20)


# Условие для отображения задания

task_label = Label(root, text=pages[current_page]["task"], font='Times 12', fg='white', bg="gray15", wraplength=500, justify=LEFT)

task_label.pack(pady=20)


answer_field = Entry(root, width=40, font='Times 14')

answer_field.pack(pady=10)


result_label = Label(root, text="", font='Times 14', fg="gray12")

result_label.pack(pady=10)


def check_answer():
    answer = answer_field.get().strip()  # Убираем лишние пробелы

    if current_page == 0 and answer == "print('Hello, Python!')":
        result_label.config(text="Верно!", fg="green")
    elif current_page == 1 and answer == "if x == 10:":
        result_label.config(text="Верно!", fg="green")
    elif current_page == 2 and answer == "a + b":
        result_label.config(text="Верно!", fg="green")
    elif current_page == 3 and answer == "sum([1, 2, 3, 4, 5])":
        result_label.config(text="Верно!", fg="green")
    elif current_page == 4 and answer == "for i in range(1, 21):\n    if i % 2 == 0:\n        print(i)":
        result_label.config(text="Верно!", fg="green")
    elif current_page == 5 and answer.startswith("try:") and "except ZeroDivisionError:" in answer:
        result_label.config(text="Верно!", fg="green")
    elif current_page == 6 and answer.startswith("with open('output.txt', 'w') as f:") and "f.write('Hello, File!')" in answer:
        result_label.config(text="Верно!", fg="green")
    elif current_page == 7 and answer.startswith("fruits = [") and answer.endswith("]") and "sorted(fruits)" in answer:
        result_label.config(text="Верно!", fg="green")
    elif current_page == 8 and answer.startswith("class Car:") and "def display_info(self):" in answer:
        result_label.config(text="Верно!", fg="green")
    elif current_page == 9 and answer.startswith("import math") and "math.sqrt(16)" in answer:
        result_label.config(text="Верно!", fg="green")
    else:
        result_label.config(text="Неверно!", fg="red")

def next_page():
    global current_page
    if current_page < len(pages) - 1:
        current_page += 1
        title_label.config(text=pages[current_page]["title"])
        text_label.config(text=pages[current_page]["text"])
        
        if current_page < len(pages) - 1:  # Условие для отображения задания
            task_label.config(text=pages[current_page]["task"])
        else:  # На последней странице убираем текст задания
            task_label.config(text="")
        
        answer_field.delete(0, END)
        result_label.config(text="")
        
        # Обновляем видимость кнопок
        check_button.pack(pady=10)
        next_button.pack(pady=10)
        
        if current_page == len(pages) - 1:
            answer_field.pack_forget()  # Скрыть поле для ответов
            check_button.pack_forget()  # Скрыть кнопку проверки
            next_button.pack_forget()  # Скрыть кнопку следующей страницы
            exit_button.pack(pady=10)  # Показать кнопку выхода
        else:
            answer_field.pack(pady=10)  # Показать поле для ответов на остальных страницах

def exit_program():
    root.quit()  # Закрыть приложение

# Кнопка для проверки ответа
check_button = Button(root, text="Проверить ответ", command=check_answer, font='Times 14')
check_button.pack(pady=10)

# Кнопка для перехода к следующей странице
next_button = Button(root, text="Следующий", command=next_page, font='Times 14')
next_button.pack(pady=10)

# Кнопка выхода из программы
exit_button = Button(root, text="Выход", command=exit_program, font='Times 14')
exit_button.pack_forget()  # Скрыть кнопку выхода изначально

# Запускаем главный цикл приложения
root.mainloop()

