import sys

def can_pass_brick(A, B, C, D, E):
    brick_min1, brick_min2 = sorted([A, B, C])[:2]
    hole_min, hole_max = sorted([D, E])
    return "YES" if brick_min1 <= hole_min and brick_min2 <= hole_max else "NO"

def main():
    data = list(map(int, sys.stdin.read().split()))
    A, B, C, D, E = data[0], data[1], data[2], data[3], data[4]
    print(can_pass_brick(A, B, C, D, E))

if __name__ == "__main__":
    main()