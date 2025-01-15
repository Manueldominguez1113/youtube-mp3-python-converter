import os
from pathlib import Path
from pytubefix import YouTube
import tkinter as tk


def conversion(url, label):
    try:
        # setting up the url string
        yt = YouTube(url.get())
        # extracting the audio only
        video = yt.streams.filter(only_audio=True).first()
        # save location
        destination = str(Path.home()) + "/Downloads/"
        # download file
        outfile = video.download(output_path=destination)

        # renaming the fle to the video+mp3
        base, ext = os.path.splitext(outfile)
        new_file=base+".mp3"
        os.rename(outfile, new_file)

        label.config(text=f"{new_file} has been converted to mp3 and saved!")

    except Exception as e:
        label.config(text=e)


def check_url(url, label):
    pass
    if label.cget("text") != "":
        label.config(text="")

    if url.get()== "":
        label.config(text="No url entered!!")
    # elif "eee" in url.get():
    #     label.config(text="skksdsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
    elif "you" not in url.get():
        label.config(text="must be a youtube or you.tube url")
    else:
        label.config(text="downloading.. please wait")
        conversion(url, label)


class App:
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("YouTube Converter")
        self.root.geometry("600x200")
        self.build_gui()
        self.root.resizable(False, False)
        self.root.mainloop()

    def exit(self):
        self.root.destroy()

    def build_gui(self):
        main_container = tk.Frame(self.root)
        main_container.grid(sticky="nsew", padx=10, pady=10)

        title = tk.Label(main_container, text="Hello! Welcome to DZ's personal Youtube-to-MP3 downloader")
        title.grid(row=0, column=2, sticky="ew")

        main_container.grid_columnconfigure((0,20), weight=2)
        self.root.grid_columnconfigure((0,20), weight=2)

        input_label = tk.Label(main_container, text="Enter full YouTube URL :")
        input_label.grid(row=3, column=1, sticky="e")

        url = tk.StringVar()
        inputt = tk.Entry(main_container, textvariable=url)
        inputt.focus()
        inputt.grid(row=3, column=2)

        url_button = tk.Button(main_container, text="Convert", command=lambda: check_url(url, output_label))
        url_button.grid(row=3, column=3, sticky="E",ipadx=20, ipady=10)

        instructions_label = tk.Label(main_container, text="Tips: Press Enter to run, press Esc to quit")
        instructions_label.grid(row=4, column=2)

        exit_button = tk.Button(main_container, text="Exit", command=self.exit)
        exit_button.grid(row=5, column=2, ipadx=20, ipady=5)

        output_label = tk.Label(main_container, text="",wraplength=300)
        output_label.grid(row=9, column=2, sticky="SEW")

        self.root.bind("<Return>", lambda event: check_url(url,output_label))
        self.root.bind("<Escape>", lambda event : self.exit())


if __name__ == '__main__':
    App()
