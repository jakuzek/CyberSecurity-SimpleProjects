from tkinter import *
import string

alphabet = "".join(string.ascii_lowercase)


# ------------- Window ---------------
root = Tk()
root.geometry("300x450")
root.title("Caesar Cipher - Encryption")
root.configure(bg="light grey")


# ------ Encryption Function ---------
def encryption():
    encrypted_text = ""
    key = input_key.get(1.0, END)
    text = input_text.get(1.0, END)

    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = alphabet.find(letter)
            if index == -1:
                encrypted_text += letter
            else:
                new_index = index + int(key)
                if new_index >= len(alphabet):
                    new_index -= len(alphabet)

                encrypted_text += alphabet[new_index]

    results(encrypted_text)


# ------ Decryption Function ---------
def decryption():
    encrypted_text = ""
    key = input_key.get(1.0, END)
    text = input_text.get(1.0, END)

    for letter in text:
        letter = letter.lower()
        if not letter == " ":
            index = alphabet.find(letter)
            if index == -1:
                encrypted_text += letter
            else:
                new_index = index - int(key)
                if new_index < 0:
                    new_index += len(alphabet)

                encrypted_text += alphabet[new_index]

    results(encrypted_text)


# ------------- Results --------------
def results(encrypted_text):
    CipherText = Label(root, text="--- Results ---", bg="light grey", font=("Times", 10))
    CipherText.place(x=115, y=300)

    CipherText_Results = Text(root, height=7, width=37)
    CipherText_Results.place(y=330)
    CipherText_Results.tag_configure("tag_name", justify='center')
    CipherText_Results.insert("1.0", encrypted_text)
    CipherText_Results.tag_add("tag_name", "1.0", "end")

    root.update()


# ---------------- Key ---------------
text_key = Label(root, text="Enter the key (1 through 26)", bg="light grey", font=("Times", 9))
text_key.place(x=80, y=30)

input_key = Text(root, height=1, width=20)
input_key.place(x=70, y=60)


# --------------- Text ---------------
text_to_encrypt = Label(root, text="Enter the text to encrypt", bg="light grey", font=("Times", 9))
text_to_encrypt.place(x=90, y=100)

input_text = Text(root, height=6, width=20)
input_text.place(x=70, y=130)


# -------------- Button --------------
button_encryption = Button(root, text="ENCRYPT", bg='grey', command=encryption)
button_encryption.place(x=80, y= 250)

button_decryption = Button(root, text="DECRYPT", bg='grey', command=decryption)
button_decryption.place(x=160, y= 250)

root.mainloop()