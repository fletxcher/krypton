
import tkinter as tk
from tkinter import ttk
from tkinter import *
from Crypto.Cipher import AES
from secrets import token_bytes

# create the application gui 
root = tk.Tk()
root.title('Krypton')
root.geometry ('500x200')
root.resizable = (False, False)
root.configure(bg = 'black')

window_width = 500
window_height = 200

# message input 
label = ttk.Label(root, text = 'Message:', background= 'black', foreground = 'white')
label.place(x = window_width - 490, y = window_height - 180)
text = StringVar()
message = ttk.Entry(root, width = 78, textvariable = text)
message.place(x = window_width - 490, y = window_height - 160)

# translation output 
label = ttk.Label(root, text = 'Translation:', background= 'black', foreground = 'white')
label.place(x = window_width - 490, y = window_height - 130)
translate = ttk.Entry(root, width = 78)
translate.place(x = window_width - 490, y = window_height - 110)

# AES encryption algorithm
key = token_bytes(16)

def encrypt(message):
    global nonce, ciphertext, tag 
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('ascii'))
    return nonce, ciphertext, tag 

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except ValueError:
        print("key incorrect or message corrupted")
        return False

def fetch_data():
    global memo
    memo = message.get()

# encrypt message button
encryption_button = tk.Button(root, text = 'Encrypt Message', command = lambda: [fetch_data(), translate.insert(0, encrypt(memo)[1])], background = 'black', foreground = 'white')
encryption_button.place (x = window_width - 490, y = window_height - 40)

# decrypt message button
encryption_button = tk.Button(root, text = 'Decrypt Message', command = lambda: [fetch_data(), translate.insert(0, decrypt(nonce, ciphertext, tag))], background = 'black', foreground = 'white')
encryption_button.place (x = window_width - 110, y = window_height - 40)

# run the application
root.mainloop()


