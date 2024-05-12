import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import os
import pygame  # Import pygame for playing sound
from datetime import datetime  # Import datetime to print the current time

def show_popup():
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the sound in a loop
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play(-1)  # Play the sound in an infinite loop

    # Select a random image from the list
    images = ['sleep1.jpeg', 'sleep2.jpeg', 'sleep3.jpeg', 'sleep4.jpeg', 'sleep5.jpeg', 'sleep6.jpeg']
    selected_image = random.choice(images)
    image_path = os.path.join('images', selected_image)
    
    # Create the root window
    root = tk.Tk()
    root.title("Reminder")

    # Print the time the popup was displayed
    display_time = datetime.now()
    print(f"Popup displayed at: {display_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Function to stop music and close the window
    def on_close():
        pygame.mixer.music.stop()  # Stop the music
        pygame.mixer.quit()  # Quit the mixer
        root.destroy()  # Close the window

        # Print the time the popup was closed
        close_time = datetime.now()
        print(f"Popup closed at: {close_time.strftime('%Y-%m-%d %H:%M:%S')}")

    root.protocol("WM_DELETE_WINDOW", on_close)  # Call on_close when the window is closed

    # Open the image
    img = Image.open(image_path)
    img = img.resize((300, 200), Image.Resampling.LANCZOS)  # Resize image using LANCZOS
    photo = ImageTk.PhotoImage(img)

    # Create a label for image and text
    label = tk.Label(root, text="go see harshul", compound=tk.TOP)
    label.pack(pady=20)

    # Create an image label
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  # Keep a reference!
    image_label.pack(padx=20, pady=10)

    # Run the window
    root.mainloop()

# Loop to show the popup every 2 hours
while True:
    show_popup()
    time.sleep(7200)  # Sleep for 2 hours (7200 seconds)
