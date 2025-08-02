import tkinter as tk
import os
import subprocess

# -- THEME/STYLE CONSTANTS --
BLACK = "#18141c"
WHITE = "#ffffff"
RED = "#e50914"
BTN_BG = "#fff"
BTN_FG = "#e50914"
BTN_HOVER_BG = "#e50914"
BTN_HOVER_FG = "#fff"
ERROR_COLOR = "#ff3647"
DIM = "#aaa"
BTN_FONT = ("Arial", 18, "bold")
LABEL_FONT = ("Arial", 36, "bold")
SUB_FONT = ("Arial", 16, "italic")

def on_btn_enter(e):
    e.widget["bg"] = BTN_HOVER_BG
    e.widget["fg"] = BTN_HOVER_FG
    e.widget.config(font=("Arial", 19, "bold"), bd=3, relief="solid")

def on_btn_leave(e):
    e.widget["bg"] = BTN_BG
    e.widget["fg"] = BTN_FG
    e.widget.config(font=BTN_FONT, bd=1, relief="ridge")

def launch_solver():
    _launch_script("cube.py")

def launch_2x2():
    _launch_script("2x2SolverGUI.py")

def _launch_script(script):
    if not os.path.exists(script):
        error_label.config(text=f"Error: '{script}' not found!")
        return
    try:
        cmd = ['python', script] if os.name == 'nt' else ['python3', script]
        subprocess.Popen(cmd)
        error_label.config(text="")
    except Exception as e:
        error_label.config(text=f"Error launching {script}: {e}")

root = tk.Tk()
win_width, win_height = 980, 760
root.geometry(f"{win_width}x{win_height}")

# Center window on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (win_width // 2)
y = (screen_height // 2) - (win_height // 2)
root.geometry(f"{win_width}x{win_height}+{x}+{y}")

root.title("Hackathon Cube Launcher")
root.configure(bg=BLACK)
root.resizable(True, True)

# ---------- SCROLLABLE MAIN CONTENT ----------
container = tk.Frame(root, bg=BLACK)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container, bg=BLACK, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

content_frame = tk.Frame(canvas, bg=BLACK)

# Use anchor="center" for true centering
content_frame_id = canvas.create_window(
    (0, 0), window=content_frame, anchor="center"
)

def on_frame_configure(event):
    # Update scrollregion to fit the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_resize(event):
    # Always center the content frame in the canvas
    canvas.coords(content_frame_id, event.width//2, event.height//2)

content_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_resize)

# ---------- HEADER ----------
header = tk.Frame(content_frame, bg=BLACK)
header.pack(pady=(36, 0), padx=0, fill="x")

badge = tk.Label(
    header,
    text=" COLLINS AEROSPACE • AEROHACK 2025 ",
    font=("Arial", 13, "bold"),
    bg=RED, fg=WHITE,
    padx=16, pady=6, relief="solid", bd=2
)
badge.pack(pady=(0, 16))

tk.Label(header, text="🧩", font=("Arial", 65), bg=BLACK, fg=RED).pack(pady=(0, 3))

main_title = tk.Label(
    header,
    text=" REAL-TIME RUBIX CUBE SOLVER SUITE",
    font=LABEL_FONT, bg=BLACK, fg=WHITE
)
main_title.pack(pady=(0, 2))

subtitle = tk.Label(
    header,
    text="Fastest solutions for 3×3 & 2×2 cubes",
    font=SUB_FONT, bg=BLACK, fg=DIM
)
subtitle.pack(pady=(0, 24))

# ------------ THREE CARDS IN A ROW -------------
cards_content = [
    (
        "⚡ Real-time Rubik's Cube solutions\nwith optimized algorithms!",
        RED  # Red accent
    ),
    (
        "🔴 2×2 Cube: Uses Bidirectional BFS for shortest solutions.\n"
        "Time Complexity: O(b^d/2), Space Complexity: O(b^d/2) ",
        "GREEN"  # Dark accent 
    ),
    (
        "🔵 3×3 Cube: Employs CFOP (Cross, F2L, OLL, PLL) for pro, humanlike solves.\n"
        "Time Complexity: O(1), Space Complexity: O(1)",
        "#1a36eb"  # Blue accent
    )
]


cards_frame = tk.Frame(content_frame, bg=BLACK)
cards_frame.pack(pady=(2, 20), fill="x", expand=True)

for i, (text, border_color) in enumerate(cards_content):
    card = tk.Frame(
        cards_frame,
        bg=WHITE,
        highlightbackground=border_color,
        highlightthickness=4,
        bd=0,
        padx=18,
        pady=14,
        relief="ridge"
    )
    label = tk.Label(
        card,
        text=text,
        font=("Arial", 13, "bold" ),
        fg=BLACK,
        bg=WHITE,
        wraplength=255,
        justify="left",
        anchor="w"
    )
    label.pack(fill="both", expand=True)
    card.grid(row=0, column=i, padx=22, pady=8, sticky="nsew")
    cards_frame.grid_columnconfigure(i, weight=1)

# ------ Unique Feature Card -----
unique_card = tk.Frame(
    content_frame,
    bg=WHITE,
    highlightbackground=RED,
    highlightthickness=2,
    bd=0,
    padx=18,
    pady=12,
    relief="ridge"
)
unique_label = tk.Label(
    unique_card,
    text="✨ Unique: 2x2 Solver: Optimal and pedagogical,bidirectional BFS is both theoretically optimal and fast enough to solve all possible scrambles instantly, showing every intermediate state.\n""3x3 solver:CFOP-based solvers are unique in that they mimic human solves, making them perfect for learning and visualizing the solution path step-by-step,something not typically provided by shortest-move solvers\n",
    font=("Arial", 13, "italic"),
    fg=RED,
    bg=WHITE,
    wraplength=800,
    justify="center"
)
unique_label.pack(fill="both", expand=True)
unique_card.pack(pady=(4, 18), padx=26, fill="x")

# ----------- BUTTONS (Centered) --------------
buttons_frame = tk.Frame(content_frame, bg=BLACK)
buttons_frame.pack(padx=35, pady=(0,25), fill="x")

btn3 = tk.Button(
    buttons_frame, text="🚀 LAUNCH 3×3 CUBE SOLVER",
    font=BTN_FONT,
    bg=BTN_BG, fg=BTN_FG, borderwidth=1, width=30,
    relief="ridge", cursor="hand2",
    activebackground=BTN_HOVER_BG, activeforeground=BTN_HOVER_FG,
    command=launch_solver
)
btn3.pack(pady=(8,6), ipady=7)
btn3.bind("<Enter>", on_btn_enter)
btn3.bind("<Leave>", on_btn_leave)

btn2 = tk.Button(
    buttons_frame, text="🟥 LAUNCH 2×2 CUBE SOLVER",
    font=BTN_FONT,
    bg=BTN_BG, fg=BTN_FG, borderwidth=1, width=30,
    relief="ridge", cursor="hand2",
    activebackground=BTN_HOVER_BG, activeforeground=BTN_HOVER_FG,
    command=launch_2x2
)
btn2.pack(pady=(0,6), ipady=7)
btn2.bind("<Enter>", on_btn_enter)
btn2.bind("<Leave>", on_btn_leave)

error_label = tk.Label(
    content_frame, text="",
    font=("Arial", 12, "italic"),
    bg=BLACK, fg=ERROR_COLOR
)
error_label.pack(pady=(10, 22))

# ----------- FOOTER -----------
footer = tk.Label(
    content_frame,
    text=" • Collins AeroHack 2025 • ",
    font=("Arial",12, "italic"), bg=WHITE, fg=RED
)
footer.pack(side="bottom", pady=13)

# --- Enable mousewheel scroll for the canvas frame
def _on_mousewheel(event):
    delta = int(-1*(event.delta/120))
    canvas.yview_scroll(delta, "units")

def _on_linux_scroll_up(event):
    canvas.yview_scroll(-1, "units")

def _on_linux_scroll_down(event):
    canvas.yview_scroll(1, "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows/macOS
canvas.bind_all("<Button-4>", _on_linux_scroll_up)    # Linux scroll up
canvas.bind_all("<Button-5>", _on_linux_scroll_down)  # Linux scroll down

root.mainloop()
