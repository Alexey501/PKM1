import tkinter as tk
from tkinter import ttk
import psutil
import time


class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor")

        # Створення віджетів
        self.cpu_label = ttk.Label(root, text="CPU Usage:")
        self.cpu_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.memory_label = ttk.Label(root, text="Memory Usage:")
        self.memory_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.disk_label = ttk.Label(root, text="Disk Usage:")
        self.disk_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.network_label = ttk.Label(root, text="Network Traffic:")
        self.network_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Оновлення інтерфейсу
        self.update_data()

    def update_data(self):
        # Отримання інформації про систему
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent

        # Отримання інформації про мережевий трафік
        network_traffic = psutil.net_io_counters()
        sent = network_traffic.bytes_sent
        received = network_traffic.bytes_recv

        # Оновлення віджетів
        self.cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        self.memory_label.config(text=f"Memory Usage: {memory_percent}%")
        self.disk_label.config(text=f"Disk Usage: {disk_percent}%")
        self.network_label.config(text=f"Network Traffic: Sent - {sent} bytes, Received - {received} bytes")

        # Періодичне оновлення інтерфейсу
        self.root.after(1000, self.update_data)


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()
