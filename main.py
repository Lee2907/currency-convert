# importing the required modules
import tkinter
import requests
# creating a window

response = requests.get('https://api.exchangerate-api.com', auth=('user', 'pass'))
data = response.json()
print(data)

root = tkinter.Tk()
root.title("Currency Converter")   # naming the recently created window
root.geometry("720x500")   #  setting the size of the window
root.config(bg="antique white")   # setting the background color for the window

l1 = tkinter.LabelFrame(root, text="Pesos To US$", padx=20, pady=20)
l1.grid(row=2, column=0)

e1 = tkinter.Entry(l1, state="disable")
e1. grid(row=4, column=0)

# setting the state for Pesos
def cel_active():
    e2.configure(state='disable')
    e1.configure(state="normal")


btn_active = tkinter.Button(root, text="Activate - ARS To US$", command=cel_active)
btn_active.grid(row=6, column=0)

l2 = tkinter.LabelFrame(root, text="ZAR To US$", padx=20, pady=20)
l2.grid(row=2, column=5)

e2 = tkinter.Entry(l2, state="disable")
e2.grid(row=4, column=5)


# setting the state for Rands
def far_active():
    e1.configure(state="disable")
    e2.configure(state="normal")


btn_active1 =tkinter.Button(root, text="Activate - ZAR To US$", command=far_active)
btn_active1.grid(row=6, column=5)


# defining function that will exit/ close the window/ program
def close():
    root.destroy()


exit_btn = tkinter.Button(text="Exit Program", command=close)
exit_btn.grid(row=9, column=6)


# defining function for converting Pesos to Dollars
def convert_C():
    if e1["state"] == "normal" and e1.get() != "":
        peso = int(e1.get())
        dollar = peso * 0.082
        result_entry.insert(0, str(dollar))


# defining function for converting Rands to Dollars
def convert_f():
    if e2["state"] == "normal" and e2.get() != "":
        rand = int(e2.get())
        dollar = rand * 0.074
        result_entry.insert(0, dollar)


result_btn = tkinter.Button(root, text="Convert A-$", command=convert_C)
result_btn.grid(row=7, column=2)


# creating the action button for converting Rands to Dollars and calling the convert_f()
result_btn2 = tkinter.Button(root, text="Convert R-$", command=convert_f)
result_btn2.grid(row=7, column=4)


# creating the result_entry or output entry
result_entry = tkinter.Entry(root, bg="#f37683")
result_entry.grid(row=8, column=2)

# defining function that will delete the figure in the Entry box/ input box
def clear():
    e1.delete(0)
    e2.delete(0)
    result_entry.delete(0)


# creating the Clear button and calling the clear()
clear_btn = tkinter.Button(root, text="Clear", command=clear)
clear_btn.grid(row=8, column=6)


# starting the app
root.mainloop()



