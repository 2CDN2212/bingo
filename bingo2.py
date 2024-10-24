import tkinter as tk
import random


n = []
yet = list(range(1, 76)) 


def draw_number():
    if yet:
        number = random.choice(yet)
        yet.remove(number)
        n.append(number) 
        label.config(text=f"出た数：{number}")
        history_label.config(text=f"既に出た数：{', '.join(map(str, n))}")
    else:
        label.config(text="全ての数が出ました")
        draw_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Bingo")


label = tk.Label(root, text="Let's bingo!", font=("Arial", 24))
label.pack(pady=20)

history_label = tk.Label(root, text="ビンゴを始める", font=("Arial", 14))
history_label.pack(pady=20)

draw_button = tk.Button(root, text="抽選", command=draw_number, font=("Arial", 18))
draw_button.pack(pady=20)


root.mainloop()
