import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import os
import pygame
from datetime import datetime
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import threading

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Log file to store the display and close times
log_file = "popup_log.txt"

def write_to_log(message):
    """ Helper function to write messages to the log file """
    with open(log_file, "a") as file:
        file.write(message + "\n")

def show_popup():
    pygame.mixer.init()
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play(-1)

    images = ['sleep1.jpeg', 'sleep2.jpeg', 'sleep3.jpeg', 'sleep4.jpeg', 'sleep5.jpeg', 'sleep6.jpeg']
    selected_image = random.choice(images)
    image_path = os.path.join('images', selected_image)
    
    root = tk.Tk()
    root.title("Reminder")

    display_time = datetime.now()
    display_message = f"Popup displayed at: {display_time.strftime('%Y-%m-%d %H:%M:%S')}"
    print(display_message)
    write_to_log(display_message)

    def on_close():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        root.destroy()

        close_time = datetime.now()
        close_message = f"Popup closed at: {close_time.strftime('%Y-%m-%d %H:%M:%S')}"
        print(close_message)
        write_to_log(close_message)

    root.protocol("WM_DELETE_WINDOW", on_close)

    img = Image.open(image_path)
    img = img.resize((300, 200), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, text="go see harshul", compound=tk.TOP)
    label.pack(pady=20)

    image_label = tk.Label(root, image=photo)
    image_label.image = photo
    image_label.pack(padx=20, pady=10)

    root.mainloop()

@app.route('/')
def index():
    """ Serve the log file as a web page """
    with open(log_file, "r") as file:
        log_content = file.readlines()
    return render_template('index.html', log_content=log_content)

def run_app():
    # Run Flask app without reloader
    app.run(debug=True, use_reloader=False, port=5000)

def run_popup_loop():
    while True:
        show_popup()
        #time.sleep(7200)
        time.sleep(10)

if __name__ == "__main__":
    # Clear the log file at the start
    open(log_file, 'w').close()

    # Start the Flask app in a separate thread
    threading.Thread(target=run_app).start()

    # Start the popup loop
    run_popup_loop()
