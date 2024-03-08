from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- Search GENERATOR ------------------------------- #

def search_info():
    website = website_entry.get()
    try:
        with open("data.json") as read_file:
            data = json.load(read_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="This account doesn't exist")
    else:
        if website in data:
            messagebox.showinfo(title="Your account info", message=f"Your email: {data[website]['email']}"
                                                                   f"\nYour Password: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message="This account doesn't exist")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    print("Password generator have been clicked")
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwd_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    passwd_letters_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    passwd_letters_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    new_pass = passwd_letters + passwd_letters_symbols + passwd_letters_numbers

    random.shuffle(new_pass)
    password = "".join(new_pass)
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
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
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
