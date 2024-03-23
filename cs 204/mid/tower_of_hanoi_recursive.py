def tower_of_hanoi_recursive(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
        return
    tower_of_hanoi_recursive(n - 1, source, auxiliary, target)
    print(f"Move disc {n} from {source} to {target}")
    tower_of_hanoi_recursive(n - 1, auxiliary, target, source)

# Example usage:
tower_of_hanoi_recursive(3, 'A', 'C', 'B')
