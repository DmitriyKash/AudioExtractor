from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import threading


def update_progress_bar(progress, value, root):
    progress['value'] = value
    root.update_idletasks()


def extract_audio(progress, label_result, root):
    video_path = filedialog.askopenfilename()
    if video_path:
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                  filetypes=[("MP3 files", "*.mp3")])
        if audio_path:
            try:
                video = VideoFileClip(video_path)

                # Оновлення прогрес-бару
                update_progress_bar(progress, 25, root)

                audio = video.audio
                if audio:
                    # Ще одне оновлення прогрес-бару
                    update_progress_bar(progress, 50, root)

                    audio.write_audiofile(audio_path)

                    # Фінальне оновлення прогрес-бару
                    update_progress_bar(progress, 100, root)

                    label_result.config(text=f"Аудіо збережено: {audio_path}")
                else:
                    messagebox.showerror("Помилка", "Не вдалося вилучити аудіо.")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))


def start_extract_audio(progress, label_result, root):
    threading.Thread(target=extract_audio, args=(progress, label_result, root)).start()
