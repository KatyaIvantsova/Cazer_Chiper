import tkinter as tk
from tkinter import messagebox
import random
import string

def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def encrypt():
    text = entry_text.get()
    shift = int(entry_key.get())
    encrypted_text = caesar(text, shift)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, encrypted_text)

def decrypt():
    text = entry_text.get()
    shift = int(entry_key.get())
    decrypted_text = caesar(text, -shift)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decrypted_text)

def generate_key():
    key = random.randint(1, 25)
    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)

def brute_force():
    text = entry_text.get()
    possible_decryptions = []
    for shift in range(1, 26):
        decrypted_text = caesar(text, -shift)
        possible_decryptions.append(decrypted_text)

    result = "\n".join(possible_decryptions)
    messagebox.showinfo("Возможное описание", result)

root = tk.Tk()
root.title("Шифр Цезаря")

label_text = tk.Label(root, text="Введите текст:")
label_text.pack()

entry_text = tk.Entry(root, width=60)
entry_text.pack()

label_key = tk.Label(root, text="Введите ключ (1-25):")
label_key.pack()

entry_key = tk.Entry(root, width=5)
entry_key.pack()

button_encrypt = tk.Button(root, text="Шифрование", command=encrypt)
button_encrypt.pack()

button_decrypt = tk.Button(root, text="Расшифровка", command=decrypt)
button_decrypt.pack()

button_generate_key = tk.Button(root, text="Генерация ключа", command=generate_key)
button_generate_key.pack()

button_brute_force = tk.Button(root, text="Взлом шифра", command=brute_force)
button_brute_force.pack()

label_result = tk.Label(root, text="Результат:")
label_result.pack()

entry_result = tk.Entry(root, width=60)
entry_result.pack()

root.mainloop()
