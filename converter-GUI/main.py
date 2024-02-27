from tkinter import *

window = Tk()
window.title("Miles to KM program")
window.config(padx=100, pady=100)


def convert():
    print("converting")
    miles_to_km = 1.60934
    miles = input.get()
    conversion = miles_to_km * int(miles)
    results.config(text=int(conversion))


my_label = Label(text="is equal to", font=("Arial", 8, "bold"))
my_label.grid(column=0, row=1)
#
input = Entry(width=10)
input.get()
input.grid(column=1, row=0)

results = Label(text="0", font=("Arial", 8, "bold"))
results.grid(column=1, row=1)


my_button = Button(text="Calculate", command=convert)
my_button.grid(column=1, row=2)

my_label = Label(text="(Miles)", font=("Arial", 8, "bold"))
my_label.grid(column=2, row=0)

my_label = Label(text="(Km)", font=("Arial", 8, "bold"))
my_label.grid(column=2, row=1)










window.mainloop()
