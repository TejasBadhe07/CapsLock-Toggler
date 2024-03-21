import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui

class CapsLockTogglerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caps Lock Toggler")

        self.interval_label = tk.Label(root, text="Interval (seconds):")
        self.interval_label.grid(row=0, column=0, padx=5, pady=5)

        self.interval_entry = tk.Entry(root)
        self.interval_entry.grid(row=0, column=1, padx=5, pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.start_toggling)
        self.start_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_toggling, state=tk.DISABLED)
        self.stop_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.toggling_thread = None
        self.running = False

    def toggle_caps_lock(self, interval):
        while self.running:
            pyautogui.press('capslock')
            self.root.after(interval * 1000)

    def start_toggling(self):
        interval = self.interval_entry.get()
        if not interval.isdigit():
            messagebox.showerror("Error", "Interval must be a positive integer.")
            return

        interval = int(interval)
        if interval <= 0:
            messagebox.showerror("Error", "Interval must be a positive integer.")
            return

        self.running = True
        self.toggling_thread = threading.Thread(target=self.toggle_caps_lock, args=(interval,))
        self.toggling_thread.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_toggling(self):
        self.running = False
        self.toggling_thread.join()

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CapsLockTogglerGUI(root)
    root.mainloop()
