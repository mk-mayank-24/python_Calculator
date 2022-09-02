from tkinter import *
calc = Tk()
calc.title('Simple Calculator')

s = Entry(calc, borderwidth=5, width=27, font=21)
s.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

a = Entry(calc, borderwidth=5, width=7, font=21)
a.grid(row=0, column=3, columnspan=1, padx=10, pady=10)

e = Entry(calc, borderwidth=5, width=38, font=21)
e.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

global current
global k
k = 0

def button_click(num):
    global current
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear_button():
    e.delete(0, END)

def add_button():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Addition'
    s.insert(0, int(first_num))
    a.insert(0, "+")
    f_num = int(first_num)
    e.delete(0, END)

def subtract_button():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Subtraction'
    s.insert(0, int(first_num))
    a.insert(0, "-")
    f_num = int(first_num)
    e.delete(0, END)

def multiply_button():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Multiply'
    s.insert(0, int(first_num))
    a.insert(0, "x")
    f_num = int(first_num)
    e.delete(0, END)

def divide_button():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Divide'
    s.insert(0, int(first_num))
    a.insert(0, "/")
    f_num = int(first_num)
    e.delete(0, END)

def equal_button():
    second_num = e.get()
    e.delete(0, END)

    if operation == 'Addition':
        e.insert(0, f_num + int(second_num))

    elif operation == 'Subtraction':
        e.insert(0, f_num - int(second_num))

    elif operation == 'Multiply':
        e.insert(0, f_num * int(second_num))
    
    elif operation == 'Divide':
        e.insert(0, f_num / int(second_num))


b1 = Button(calc, text='1', padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(calc, text='2', padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(calc, text='3', padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(calc, text='4', padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(calc, text='5', padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(calc, text='6', padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(calc, text='7', padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(calc, text='8', padx=40, pady=20, command=lambda: button_click(8))
b9 = Button(calc, text='9', padx=40, pady=20, command=lambda: button_click(9))
b0 = Button(calc, text='0', padx=40, pady=20, command=lambda: button_click(0))
b_clear = Button(calc, text='Clear', padx=30, pady=20, command=lambda: clear_button())
b_add = Button(calc, text='+', padx=20, pady=20, command=add_button)
b_subtract = Button(calc, text='-', padx=20, pady=20, command=subtract_button)
b_multiply = Button(calc, text='*', padx=20, pady=20, command=multiply_button)
b_divide = Button(calc, text='/', padx=20, pady=20, command=divide_button)
b_equal = Button(calc, text='=', padx=40, pady=20, command=equal_button)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=1)
b_add.grid(row=2, column=3)
b_subtract.grid(row=3, column=3)
b_multiply.grid(row=4, column=3)
b_divide.grid(row=5, column=3)
b_clear.grid(row=5, column=0)
b_equal.grid(row=5, column=2)


calc.mainloop()