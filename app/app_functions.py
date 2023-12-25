from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import threading


def update_progress_bar(progress, value, root):
    """
    Updates the progress bar with a new value.
    Parameters:
        progress (tkinter.ttk.Progressbar): The progress bar widget.
        value (int): The new value for the progress bar.
        root (tkinter.Tk): The root window.
    Returns:
        None
    """
    progress['value'] = value
    root.update_idletasks()


def extract_audio(progress, label_result, root):
    """
    Extracts audio from a video file and saves it as an MP3 file.

    Args:
        progress (int): The progress of the extraction process.
        label_result (Label): The label to display the result of the extraction.
        root (Tk): The root window of the application.

    Returns:
        None
    """
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
    """
    Start the extraction of audio in a separate thread.

    :param progress: A progress bar to track the extraction progress.
    :param label_result: A label to display the result of the extraction.
    :param root: The root directory where the extraction should take place.
    """
    threading.Thread(target=extract_audio, args=(progress, label_result, root)).start()
