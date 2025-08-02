# real-time-rubix-solvers-
Rubik’s Cube Solver Suite is an interactive Python-based application suite featuring optimal solvers and modern GUIs for both 2×2 and 3×3 Rubik's Cubes. Powered by advanced algorithms: bidirectional BFS for 2×2 (guaranteeing optimal solutions) and CFOP for 3×3 (mirroring  real-time techniques), 
This project is a comprehensive Rubik’s Cube solving suite comprising two main parts:

**2×2 Cube Solver:** An optimal solver using a bidirectional breadth-first search (BFS) algorithm to find the shortest solutions instantly. Features stepwise move visualization with a clean GUI.
**3×3 Cube Solver:** A solver implementing the popular CFOP speedcubing method (Cross, F2L, OLL, PLL). It mimics human solving steps with full GUI support, scramble generation, move execution, and solution walk-through.
The suite is designed for educational use, demonstrations, and learning Rubik’s Cube solving in a visually intuitive way.

**Features**
**2×2 Cube Solver**
Optimal Bidirectional BFS: Finds shortest move sequences for any scramble.

Stepwise Solution: Progress through solutions one move at a time.

Visual Cube Net: Shows all six faces updating per move.

Reset & Rescramble: Reset to original scramble or generate new shuffles.

Clean GUI: Built with Tkinter for responsive interaction.

**3×3 Cube Solver**
CFOP Method Implementation:
Cross: Bottom-layer cross solving.
F2L: First two layers solved by pairing edges and corners.
OLL: Last layer orientation using recognized patterns.
PLL: Last layer piece permutation into solved positions.

Interactive Move Input: Enter and execute custom moves.
Scramble Generator: Random or user-defined scrambles.
Stepwise & Instant Solve: Solve the entire cube or step through stages.
3D-Style Visualization: Canvas-rendered cube with toggleable transparency.
Cube Rotation Controls: Rotate cube view for better perspective.

**Installation**
Ensure you have Python 3.x installed on your system.
Setup steps:
Clone or download this repository.
Optionally, create and activate a virtual environment for dependency management.
Tkinter is required and usually pre-installed with Python.
Launcher
Launches a themed window offering choice between the 2×2 and 3×3 solvers.

**2×2 Solver**
Upon launch, the cube is scrambled and solution computed instantly.
Use the "Next Step to Solution" button to advance moves.
"Reset Cube" restores scramble state.
Cube net displays all six faces with color-coded stickers.

**3×3 Solver**
Enter moves manually to manipulate cube state.
Press "Scramble" for random scramble or input a custom scramble.
"Solve Cube" instantly solves from the current state.
Step through solving phases: Cross, F2L, OLL, PLL.
Visualize solution progress with updated colors on a 3D-like canvas.
Rotate cube view using dedicated buttons.
Copy scrambles or solutions to clipboard easily.

**Code Structure**
text
/ (Root)
├── 2x2SolverGUI.py    # 2x2 solver GUI and logic integration
├── cube.py            # 3x3 solver logic and GUI with CFOP implementation
├── possible_moves.py  # Defines face-twist transformations for 2x2 cube states
├── solver.py          # BFS solver backend for 2x2 cube (bidirectional search)
├── launcher.py        # Launch menu GUI to start 2x2 or 3x3 solvers
└── README.md          # This file

**Algorithms Summary**
**2×2 Solver**
Uses bidirectional BFS exploring from both scrambled and solved states.
Moves are defined as face twists with precise sticker permutation mappings.
Efficient queue and dictionary-based search ensures optimal shortest-path solution.
**3×3 Solver (CFOP Method)**
Cross: Build the bottom cross with edge alignment.
F2L: Inserts corner-edge pairs into their slots.
OLL: Orients last layer pieces using pattern matching ("fish," "Sune," etc.).
PLL: Permutes last layer pieces using known algorithms (H perm, Z perm, U perm).
Moves are simplified to reduce redundancy.
Cube represented as 3D arrays with colors — rendered visually with Tkinter Canvas.

**Acknowledgments**
Inspired by standard Rubik’s Cube solving algorithms and speedcubing CFOP techniques.
Thanks to the open-source community for algorithm references and GUI design ideas.
This project was developed for Collins Aerospace AeroHack 2025.

