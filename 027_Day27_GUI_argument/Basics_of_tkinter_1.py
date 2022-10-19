import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label

# * pack is used to show the text we use on tkinter label
# * to change the side of the label we can give side="left" inside pack, check doc for more (https://docs.python.org/3/library/tkinter.html#the-packer)
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.pack()


window.mainloop()
