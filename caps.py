import tkinter as tk
import threading
import pyautogui
import sys

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
            if not self.running:
                break

    def start_toggling(self):
        interval = self.interval_entry.get()
        if not interval.isdigit():
            tk.messagebox.showerror("Error", "Interval must be a positive integer.")
            return

        interval = int(interval)
        if interval <= 0:
            tk.messagebox.showerror("Error", "Interval must be a positive integer.")
            return

        self.running = True
        self.toggling_thread = threading.Thread(target=self.toggle_caps_lock, args=(interval,))
        self.toggling_thread.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_toggling(self):
        self.running = False
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CapsLockTogglerGUI(root)
    root.mainloop()


"""import tkinter as tk
import threading
import pyautogui
import sys

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
            if not self.running:
                break

    def start_toggling(self):
        interval = self.interval_entry.get()
        if not interval.isdigit():
            tk.messagebox.showerror("Error", "Interval must be a positive integer.")
            return

        interval = int(interval)
        if interval <= 0:
            tk.messagebox.showerror("Error", "Interval must be a positive integer.")
            return

        self.running = True
        self.toggling_thread = threading.Thread(target=self.toggle_caps_lock, args=(interval,))
        self.toggling_thread.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Check if the toggling thread has terminated every 100 milliseconds
        self.check_thread()

    def stop_toggling(self):
        self.running = False

    def check_thread(self):
        if self.toggling_thread is not None and self.toggling_thread.is_alive():
            self.root.after(100, self.check_thread)
        else:
            self.root.destroy()
            sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CapsLockTogglerGUI(root)
    root.mainloop()

"""