import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip


def extract_audio():
    video_path = filedialog.askopenfilename()
    if video_path:
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                  filetypes=[("MP3 files", "*.mp3")])
        if audio_path:
            try:
                video = VideoFileClip(video_path)
                audio = video.audio
                if audio:
                    audio.write_audiofile(audio_path)
                    label_result.config(text=f"Аудіо збережено: {audio_path}")
                else:
                    messagebox.showerror("Помилка", "Не вдалося вилучити аудіо.")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))


# Створення вікна
root = tk.Tk()
root.title("Вилучення аудіо з відео")

# Створення кнопок і міток
label_instruction = tk.Label(root, text="Виберіть відеофайл та збережіть аудіо")
label_instruction.pack()

button_extract = tk.Button(root, text="Вилучити аудіо", command=extract_audio)
button_extract.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Запуск GUI
root.mainloop()
