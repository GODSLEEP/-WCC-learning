import tkinter as tk
import time

class TowerOfHanoiGUI:
    def __init__(self, master, num_discs, speed):
        # Initialize the GUI window
        self.master = master
        self.num_discs = num_discs
        self.speed = speed

        # Create a Tkinter canvas
        self.canvas = tk.Canvas(master, width=600, height=600)  # Set canvas dimensions
        self.canvas.pack()

        # Initialize the layout of discs on three pegs
        self.peg_a = [i for i in range(num_discs, 0, -1)]  # Discs on Peg A
        self.peg_b = []  # Discs on Peg B
        self.peg_c = []  # Discs on Peg C

        # Draw the initial state of pegs
        self.draw_pegs()

        # Move discs to solve the Tower of Hanoi problem
        self.move_discs(num_discs, 'A', 'C', 'B')

    def draw_pegs(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Define parameters for pegs and discs
        peg_width = 10
        peg_height = 200
        disc_height = 20

        # Draw Peg A
        self.canvas.create_rectangle(100 - peg_width / 2, 600, 100 + peg_width / 2, 600 - peg_height, fill='brown')
        for i, disc in enumerate(self.peg_a):
            disc_width = disc * 20
            self.canvas.create_rectangle(100 - disc_width / 2, 600 - peg_height - (i + 1) * disc_height,
                                         100 + disc_width / 2, 600 - peg_height - i * disc_height, fill='blue')

        # Draw Peg B
        self.canvas.create_rectangle(300 - peg_width / 2, 600, 300 + peg_width / 2, 600 - peg_height, fill='brown')
        for i, disc in enumerate(self.peg_b):
            disc_width = disc * 20
            self.canvas.create_rectangle(300 - disc_width / 2, 600 - peg_height - (i + 1) * disc_height,
                                         300 + disc_width / 2, 600 - peg_height - i * disc_height, fill='blue')

        # Draw Peg C
        self.canvas.create_rectangle(500 - peg_width / 2, 600, 500 + peg_width / 2, 600 - peg_height, fill='brown')
        for i, disc in enumerate(self.peg_c):
            disc_width = disc * 20
            self.canvas.create_rectangle(500 - disc_width / 2, 600 - peg_height - (i + 1) * disc_height,
                                         500 + disc_width / 2, 600 - peg_height - i * disc_height, fill='blue')

        # Update the canvas
        self.master.update()
        time.sleep(self.speed)

    def move_discs(self, n, source, target, auxiliary):
        if n > 0:
            # Recursively call the steps to move discs
            self.move_discs(n - 1, source, auxiliary, target)

            # Move a disc and update the state of pegs
            disc = getattr(self, f'peg_{source.lower()}').pop()
            getattr(self, f'peg_{target.lower()}').append(disc)
            self.draw_pegs()

            # Recursively call the steps to move discs
            self.move_discs(n - 1, auxiliary, target, source)

def run_gui(num_discs, speed):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Tower of Hanoi GUI")

    # Create an instance of TowerOfHanoiGUI and run the GUI
    gui = TowerOfHanoiGUI(root, num_discs, speed)

    root.mainloop()

# Example usage:
run_gui(num_discs=3, speed=2)
