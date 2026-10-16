from tkinter import *
from datetime import date
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")

# Safe icon configuration
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "calculator age.icon.jpg")
    icon_img = Image.open(icon_path)
    root.icon_image = ImageTk.PhotoImage(icon_img)
    root.iconphoto(False, root.icon_image)
except Exception as e:
    print("Icon load error:", e)

# Safe image loading using Pillow for the GUI banner/logo
try:
    image_path = os.path.join(script_dir, "calculator age.icon.jpg")
    img = Image.open(image_path)
    # Optional: Resize image if it's too big for the top banner (e.g., 100x100)
    img = img.resize((100, 100))
    root.logo_img = ImageTk.PhotoImage(img)
    myimage = Label(image=root.logo_img)
    myimage.pack(padx=15, pady=15)
except Exception as e:
    print("Banner image load error:", e)

# Global variable to hold result label so it updates instead of overlapping
result_label = None

def calculateAge():
    global result_label
    try:
        today = date.today()
        birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        
        # If label already exists, just update it, otherwise create a new one
        if result_label:
            result_label.destroy()
            
        result_label = Label(root, text=f"{namevalue.get()}, your age is {age} years", font=('Arial', 14, 'bold'))
        result_label.place(x=300, y=500)
    except Exception as e:
        if result_label:
            result_label.destroy()
        result_label = Label(root, text="Please enter valid date details!", font=('Arial', 12, 'bold'), fg="red")
        result_label.place(x=300, y=500)

Label(text="Name", font=('Arial', 12)).place(x=200, y=250)
Label(text="Year", font=('Arial', 12)).place(x=200, y=300)
Label(text="Month", font=('Arial', 12)).place(x=200, y=350)
Label(text="Day", font=('Arial', 12)).place(x=200, y=400)

namevalue = StringVar()
yearvalue = StringVar()
monthvalue = StringVar()
dayvalue = StringVar()

nameEntry = Entry(root, textvariable=namevalue, width=30, bd=3, font=('Arial', 12))
nameEntry.place(x=300, y=250)

yearEntry = Entry(root, textvariable=yearvalue, width=30, bd=3, font=('Arial', 12))
yearEntry.place(x=300, y=300)

monthEntry = Entry(root, textvariable=monthvalue, width=30, bd=3, font=('Arial', 12))
monthEntry.place(x=300, y=350)

dayEntry = Entry(root, textvariable=dayvalue, width=30, bd=3, font=('Arial', 12))
dayEntry.place(x=300, y=400)

Button(root, text="Calculate Age", font=('Arial', 10, 'bold'), bg="black", fg="white", width=15, height=2, command=calculateAge).place(x=300, y=450)

root.mainloop()