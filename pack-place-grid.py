import tkinter

window = tkinter.Tk()

window.title("pack-place-grid")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="My first label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)


# Button
def button_get_click():
    my_label.config(text="Button get clicked", font=("Arial", 24, 'bold'))
    my_label.grid(column=0, row=0)


my_button = tkinter.Button(text="Click me", command=button_get_click)
my_button.grid(column=1, row=1)

my_button_2 = tkinter.Button(text="my_button_2", command=button_get_click)
my_button_2.grid(column=2, row=0)

# Entry
input = tkinter.Entry()

print(input.get())
input.grid(column=3, row=3)

window.mainloop()
