import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#my label
my_label = tkinter.Label(text="My first label", font=("Arial", 24, 'bold' ))
my_label.pack()

#button

# def button_get_click():
#     my_label.config(text="Button get clicked", font=("Arial", 24, 'bold'))
#     my_label.pack()


# button = tkinter.Button(text="click me", command=button_get_click)
# button.pack()

#entry
def button_get_click():
    new_text = input.get()
    my_label.config(text=new_text, font=("Arial", 24, 'bold'))
    my_label.pack()


button = tkinter.Button(text="click me", command=button_get_click)
button.pack()

input = tkinter.Entry()
input.pack()



window.mainloop()