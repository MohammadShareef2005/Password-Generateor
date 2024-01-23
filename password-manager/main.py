from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def onclick_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for n in range(nr_letters)]

    password_number = [random.choice(numbers) for m in range(nr_symbols)]

    password_symbol = [random.choice(symbols) for o in range(nr_numbers)]

    password_list = password_symbol + password_number + password_letter

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)


def onclick_add():

    if len(entry_1.get()) == 0 or len(entry_3.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f'{entry_1.get()}', message=f"These are the details entered: \nEmail:{entry_2.get()}"
                                                                         f"\n Password: {entry_3.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{entry_1.get()} | {entry_2.get()} | {entry_3.get()}"+"\n")
                entry_1.delete(0, END)
                entry_3.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=2)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

entry_1 = Entry(width=50)
entry_1.grid(column=1, row=1, columnspan=2)
entry_1.focus()

entry_2 = Entry(width=50)
entry_2.grid(column=1, row=2, columnspan=2)
entry_2.insert(0, "mohammadshareef@gamil.com")

entry_3 = Entry(width=32)
entry_3.grid(column=1, row=3)

add = Button(text="Add", width=43, highlightthickness=0, command=onclick_add)
add.grid(column=1, row=4, columnspan=2)

generate_pass = Button(text="Generate Password", highlightthickness=0, command=onclick_generate)
generate_pass.grid(column=2, row=3)

window.mainloop()
