def tower_of_hanoi_iterative(n: int, src: str, aux: str, dst: str):
    """
    Solve the Tower of Hanoi problem using a stack data structure.

    n: Number of discs
    src: Source peg name
    aux: Auxiliary peg name
    dst: Destination peg name
    """
    moves = []  # List to store the sequence of moves
    stack = []  # Stack to simulate recursion

    # Push the initial parameters onto the stack
    stack.append((n, src, aux, dst))

    while stack:
        # Pop the top parameters from the stack
        n, src, aux, dst = stack.pop()

        if n == 1:
            # Base case: If there is only one disc, move it from the source peg to the destination peg
            moves.append(f"Move disc from {src} to {dst}")
        else:
            # Move the top n-1 discs from the source peg to the auxiliary peg, using the destination peg as auxiliary
            stack.append((n - 1, src, dst, aux))
            # Move the nth disc from the source peg to the destination peg
            stack.append((1, src, aux, dst))
            # Move the n-1 discs from the auxiliary peg to the destination peg, using the source peg as auxiliary
            stack.append((n - 1, aux, src, dst))
    
    return moves

# Test function
print(tower_of_hanoi_iterative(3, "A", "B", "C"))
