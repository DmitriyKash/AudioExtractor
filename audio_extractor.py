import tkinter as tk
from tkinter import ttk

from app.app_functions import start_extract_audio

# Створення вікна
root = tk.Tk()
root.title("Вилучення аудіо з відео")

# Зміна кольору фону
root.config(bg="lightblue")

# Створення фреймів
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

# Створення міток, кнопок та індикатора прогресу
label_instruction = tk.Label(frame_top, text="Виберіть відеофайл та збережіть аудіо", font=("Helvetica", 10))
label_instruction.pack()

progress = ttk.Progressbar(frame_bottom, orient="horizontal", length=200, mode="determinate")
progress.pack(side=tk.LEFT)

button_extract = tk.Button(frame_bottom, text="Вилучити аудіо",
                           command=lambda: start_extract_audio(progress, label_result, root))
button_extract.pack(side=tk.LEFT, padx=10)

label_result = tk.Label(root, text="")
label_result.pack()

button_extract.config(bg="lightgreen", fg="black")
label_instruction.config(bg="lightblue", fg="darkblue")
label_result.config(bg="lightblue", fg="darkblue")

# Запуск GUI
root.mainloop()
