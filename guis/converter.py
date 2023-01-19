from tkinter import *

def calculate():
    print("I got clicked")
    miles = int(input.get())
    km = miles * 1.6
    label1.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

label1 = Label(text="is equal to", font=("Arial", 24, "bold"))
label1.grid(column=0, row=1)

label1 = Label(text="0", font=("Arial", 24, "bold"))
label1.grid(column=1, row=1)

# Label
label2 = Label(text="Km", font=("Arial", 24, "bold"))
label2.grid(column=2, row=1)

# Label
label3 = Label(text="Miles", font=("Arial", 24, "bold"))
label3.grid(column=2, row=0)


window.mainloop()