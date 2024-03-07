from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    print("Password generator have been clicked")
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list += random.choice(symbols)

    for _ in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, f"{password}")
    pyperclip.copy(f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    a = website_entry.get()
    b = username_entry.get()
    c = password_entry.get()
    if not len(a) or not len(b) or not len(c):
        messagebox.showerror("Error:", "One of the boxes are empty/ Try again!")
    else:
        response = messagebox.askyesno("Important", f"Please check if the details are correct, "
                                                    f"yes/no\n Website: {a}\n Username: {b}\n Password: {c}")
        if response:
            with open("data", "a") as file:
                file.write(f"{a} | {b} | {c}\n")
                website_entry.delete(0, "end")
                username_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()
        else:
            print("Try Again!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# Applying password image
image = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
image.create_image(100, 100, image=password_image)
image.grid(column=1, row=0)

# Applying labels to the password generator
# Website text
website_label = Label(text="Website: ")
website_label.grid(column=0, row=2)
# Website entry - allows to type
website_entry = Entry(width=62)
website_entry.insert(0, "www.example.com")
website_entry.focus()
website_entry.grid(column=1, row=2, sticky="w", columnspan=2)
# Email/username text
username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=3)
# Email/username entry - allows to type
username_entry = Entry(width=62)
username_entry.insert(0, "example@gmail.com")
username_entry.grid(column=1, row=3, sticky="w", columnspan=2)
# Password text
password_label = Label(text="Password: ")
password_label.grid(column=0, row=4)
# Password entry - allows to type
password_entry = Entry(width=42)
password_entry.grid(column=1, row=4, sticky="w", columnspan=2)
# Generate password button
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=4)
# Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=5, columnspan=1)

window.mainloop()
