#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import json


def file_read():
    with open('database.json', encoding='utf8') as file:
        data = json.load(file)

    return data


def main():
    data = file_read()

    root = tk.Tk()
    root.geometry('500x70')
    entry = tk.Entry(root)
    entry.pack(fill=tk.BOTH, expand=True)

    def save_input():
        input_data = entry.get()
        entry.delete(0, tk.END)
        try:
            messagebox.showinfo('Ответ', data[input_data])
        except KeyError:
            messagebox.showinfo('Ответ', 'Миша, все хуйня, давай по новой')

    def paste_text():
        text = root.clipboard_get()
        entry.insert(tk.INSERT, text)

    paste_button = tk.Button(root, text="Вставить", command=paste_text)
    paste_button.pack(fill=tk.X)

    button = tk.Button(root, text="OK", command=save_input)
    button.pack(fill=tk.X)

    entry.bind("<<Paste>>", paste_text)
    root.bind('<Return>', lambda event: save_input())
    root.mainloop()


if __name__ == "__main__":
    main()
