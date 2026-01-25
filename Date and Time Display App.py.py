import tkinter as tk
from datetime import datetime

def update_time():
    now = datetime.now()
    hour = now.hour

    # Auto Day/Night Theme
    if 6 <= hour < 18:
        # 🌞 Day Theme
        bg_color = "white"
        date_color = "black"
        time_color = "blue"
        theme_text = "DAY MODE"
    else:
        # 🌙 Night Theme
        bg_color = "black"
        date_color = "cyan"
        time_color = "lime"
        theme_text = "NIGHT MODE"

    window.configure(bg=bg_color)
    date_label.config(
        text=now.strftime('%A, %d %B %Y'),
        fg=date_color,
        bg=bg_color
    )
    time_label.config(
        text=now.strftime('%I:%M:%S %p'),
        fg=time_color,
        bg=bg_color
    )
    mode_label.config(
        text=theme_text,
        fg=date_color,
        bg=bg_color
    )

    window.after(1000, update_time)  # update every second

# Window
window = tk.Tk()
window.title("Smart Digital Clock")
window.geometry("450x250")

# Mode Label
mode_label = tk.Label(
    window,
    font=("Arial", 12, "bold")
)
mode_label.pack(pady=10)

# Date Label
date_label = tk.Label(
    window,
    font=("Arial", 16)
)
date_label.pack(pady=10)

# Time Label
time_label = tk.Label(
    window,
    font=("Digital-7", 30, "bold")
)
time_label.pack(pady=10)

update_time()
window.mainloop()
