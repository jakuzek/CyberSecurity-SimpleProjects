from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x250")
root.title("Encryption and Decryption")
root.configure(bg='bisque2')

def encrypt_decrypt_image():
    choose_file = filedialog.askopenfile(mode="r", filetypes=[("jpg file", "*.jpg")])

    if choose_file:
        file_name = choose_file.name
        key = input_key.get(1.0, END)

        with open(file_name, "rb") as file:
            binary_image = file.read()

        binary_image = bytearray(binary_image)

        for index, value in enumerate(binary_image):
            binary_image[index] = value^int(key)
        
        with open(file_name, "wb") as file:
            file.write(binary_image)
        
    
        input_key.destroy()
        text.destroy()
        button1.destroy()

        done = Label(root, text="DONE!", bg="bisque2", font=('Times', 24))
        done.place(x=100, y=90)

        root.update()
    

input_key = Text(root, height=1 , width=20)
input_key.place(x=75, y=80)

text = Label(root, text="Please enter number in range 1-255", bg="bisque2", font=("Times", 9))
text.place(x=73, y=55)

button1 = Button(root, text="encrypt / decrypt", bg='PeachPuff2', command=encrypt_decrypt_image)
button1.place(x=105 ,y= 140)

root.mainloop()
