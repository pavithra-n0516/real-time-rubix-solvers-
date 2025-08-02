import tkinter as tk
import solver

def Info2x2GUIy(rt, on_start=None):
    rt.geometry("600x410")
    rt.configure(bg="#FFFFFF")
    rt.resizable(True, True)
    rt.grid_rowconfigure(0, weight=1)
    rt.grid_columnconfigure(0, weight=1)

    frame = tk.Frame(rt, bg="#FFFFFF")
    frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=2)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Heading
    heading = tk.Label(
        frame,
        text="2x2 Cube Solver Instructions",
        font=("Arial", 30, "bold"),
        fg="#C20000",
        bg="#FFFFFF",
        anchor="center",
        pady=16
    )
    heading.grid(row=0, column=0, sticky="ew")

    # Instructions
    instructions = (
        "Welcome to the 2x2 Cube Solver!\n\n"
        "Features:\n"
        "• Step through the optimal solution move-by-move, or solve instantly.\n"
        "• View move sequence and the cube state for each step.\n"
        "• Reset to your starting scramble or make a new one anytime.\n"
        
    )
    InfoLabel = tk.Label(
        frame,
        text=instructions,
        justify="center",
        anchor="center",
        font=("Arial", 15),
        bg="#FFFFFF",
        fg="#101010",
        wraplength=520,
        pady=12
    )
    InfoLabel.grid(row=1, column=0, sticky="n", pady=(0, 10))

    # Start button
    def handle_start():
        rt.destroy()
        if on_start:
            on_start()  

    # X button just closes info page, never launches solver
    def on_close():
        rt.destroy()

    rt.protocol("WM_DELETE_WINDOW", on_close)

    InfoQuitButton = tk.Button(
        frame,
        text="Start Cubing",
        fg="#FFFFFF",
        bg="#C20000",
        font=("Arial", 16, "bold"),
        activebackground="#A60000",
        activeforeground="#FFFFFF",
        command=handle_start,
        width=18,
        height=2
    )
    InfoQuitButton.grid(row=2, column=0, pady=(12, 12), sticky="n")


class CubeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2x2 Cube BFS Solver")
        self.state('zoomed')
        self.resizable(True, True)

        # Load the backend cube/shuffle/solution logic
        self.solve = solver.Solver()
        self.shuffled = self.solve.shuffled
        self.solve.find_solution()
        self.route = self.solve.route
        if self.route and self.route[0] == ''.join(self.shuffled):
            self.route.pop(0)
        self.totalMoves = len(self.route)
        self.count = 0
        self.colors = {'w': 'white', 'b': 'blue', 'o': 'orange', 'g': 'green', 'r': 'red', 'y': 'yellow'}
        self.points = {i: self.colors[self.shuffled[i][0]] for i in range(24)}

        self._build_gui()
        self._update_cube()
        self.bind('<Configure>', lambda e: self._update_cube())

    def _build_gui(self):
        
        self.heading = tk.Label(self, text="2x2 Cube Solver", font=("Arial", 36, "bold"), fg="#C20000", bg="#FFFFFF")
        self.heading.pack(side="top", pady=(22, 5))
        self.top_frame = tk.Frame(self, bg="#FFFFFF")
        self.top_frame.pack(side="top", fill="x", pady=12)
        self.move_label = tk.Label(self.top_frame, text=f"Moves Left: {self.totalMoves - self.count}", font=("Arial", 16, "bold"), fg="#C20000", bg="#FFFFFF")
        self.move_label.pack(side=tk.RIGHT, padx=10)
        button_style = {"bg":"#C20000", "fg":"#FFFFFF", "font":("Arial", 13, "bold"), "activebackground":"#A60000", "activeforeground":"#FFFFFF", "bd":0, "relief":"ridge"}
        self.next_btn = tk.Button(self.top_frame, text="Next Step to Solution", command=self.next_step, **button_style)
        self.next_btn.pack(side=tk.LEFT, padx=7)
        self.reset_btn = tk.Button(self.top_frame, text="Reset Cube", command=self.reset_cube, **button_style)
        self.reset_btn.pack(side=tk.LEFT, padx=7)

        # ==== Cube net (ALL 6 faces) ====
        self.cube_area = tk.Frame(self, bg="#FFFFFF")
        self.cube_area.pack(expand=1, fill="both")

        self.face_order = [
            # row, col, face label, sticker indices
            (0, 1, 'U', [4,5,6,7]),
            (1, 0, 'L', [16,17,18,19]),
            (1, 1, 'F', [0,1,2,3]),
            (1, 2, 'R', [8,9,10,11]),
            (1, 3, 'B', [12,13,14,15]),
            (2, 1, 'D', [20,21,22,23])
        ]
        self.face_labels = {}
        for row, col, face, indices in self.face_order:
            frame = tk.LabelFrame(self.cube_area, text=face, bg="#FFFFFF", font=("Arial", 13, "bold"), labelanchor='n')
            frame.grid(row=row, column=col, padx=10, pady=10, ipadx=2, ipady=2)
            squares = []
            for i in range(2):
                for j in range(2):
                    idx = indices[i*2+j]
                    lbl = tk.Label(frame, width=6, height=3, bd=2, relief="ridge")
                    lbl.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                    squares.append((lbl, idx))
            self.face_labels[face] = squares
      
        for i in range(3): self.cube_area.rowconfigure(i, weight=1)
        for i in range(4): self.cube_area.columnconfigure(i, weight=1)

    def _update_cube(self):
        for face, squares in self.face_labels.items():
            for lbl, idx in squares:
                lbl.config(bg=self.points[idx])
        moves_left = self.totalMoves - self.count
        self.move_label['text'] = f"Moves Left: {moves_left}"
        if moves_left == 0:
            self.next_btn.config(state="disabled")
        else:
            self.next_btn.config(state="normal")

    def reset_cube(self):
        self.shuffled = self.solve.shuffled
        self.points = {i: self.colors[self.shuffled[i][0]] for i in range(24)}
        self.count = 0
        self._update_cube()

    def next_step(self):
        if self.count < self.totalMoves:
            move = self._conversion(self.route[self.count])
            for i in range(24):
                self.points[i] = self.colors[move[i][0]]
            self.count += 1
            self._update_cube()

    def _conversion(self, current):
        assert len(current) == 72
        return [current[i:i+3] for i in range(0, 72, 3)]

# ----------- Launcher usage -----------
if __name__ == "__main__":
    def launch_solver_gui():
        CubeGUI().mainloop() 
    root = tk.Tk()
    root.title("2x2 Cube Info")
    Info2x2GUIy(root, on_start=launch_solver_gui)
    root.mainloop()
