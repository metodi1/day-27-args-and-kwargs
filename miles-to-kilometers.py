import tkinter

window = tkinter.Tk()
window.title("Miles to kilometers converter")
window.minsize(width=500, height=300)


def calculate():
    miles = float(input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}", font=("Arial", 24, 'bold'))


# input
input = tkinter.Entry()
input.grid(column=1, row=0)

# miles_label
miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

# is_equal_label
is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(column=0, row=1)

# result_label
result_label = tkinter.Label(text="0", font=("Arial", 12, "bold"))
result_label.grid(column=1, row=1)

# km_label
km_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# button calculate

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
