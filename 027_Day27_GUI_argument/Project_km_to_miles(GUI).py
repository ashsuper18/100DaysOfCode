import tkinter as ttk

window = ttk.Tk()
window.title("Km to miles converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=40)

# entry
write = ttk.Label(text="Enter Here 👉")
write.grid(row=0, column=0)

km_entry = ttk.Entry(width=10)
km_entry.grid(row=0, column=1)

km_label = ttk.Label(text="Km")
km_label.grid(row=0, column=3)

equal = ttk.Label(text="is equal to")
equal.grid(row=1, column=0)

miles_label = ttk.Label(text="Miles")
miles_label.grid(row=1, column=2)

# ******* Funitonality********
output_label = ttk.Label()
output_label.grid(row=1, column=1)


def calulate_miles():
    km_value = km_entry.get()
    miles_value = float(km_value) / 1.609
    output_label.config(text=round(miles_value, 3))


button = ttk.Button(text="Calulate", command=calulate_miles, width=10)
button.grid(row=2, column=1)
# ************ ## *************


window.mainloop()
