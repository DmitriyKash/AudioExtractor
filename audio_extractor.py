import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from moviepy.editor import VideoFileClip
import threading


def update_progress_bar(progress, value):
    progress['value'] = value
    root.update_idletasks()


def extract_audio():
    video_path = filedialog.askopenfilename()
    if video_path:
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                  filetypes=[("MP3 files", "*.mp3")])
        if audio_path:
            try:
                video = VideoFileClip(video_path)

                # Оновлення прогрес-бару
                update_progress_bar(progress, 25)

                audio = video.audio
                if audio:
                    # Ще одне оновлення прогрес-бару
                    update_progress_bar(progress, 50)

                    audio.write_audiofile(audio_path)

                    # Фінальне оновлення прогрес-бару
                    update_progress_bar(progress, 100)

                    label_result.config(text=f"Аудіо збережено: {audio_path}")
                else:
                    messagebox.showerror("Помилка", "Не вдалося вилучити аудіо.")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))


def start_extract_audio():
    threading.Thread(target=extract_audio).start()


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

button_extract = tk.Button(frame_bottom, text="Вилучити аудіо", command=start_extract_audio)
button_extract.pack(side=tk.LEFT, padx=10)

label_result = tk.Label(root, text="")
label_result.pack()

button_extract.config(bg="lightgreen", fg="black")
label_instruction.config(bg="lightblue", fg="darkblue")
label_result.config(bg="lightblue", fg="darkblue")

# Запуск GUI
root.mainloop()
