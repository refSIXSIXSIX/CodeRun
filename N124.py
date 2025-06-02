def main():
    def insert(root, value):
        if root is None:
            return {"value": value, "left": None, "right": None}
        if value < root["value"]:
            root["left"] = insert(root["left"], value)
        elif value > root["value"]:
            root["right"] = insert(root["right"], value)
        return root

    def find_leaves(root, leaves):
        if root is None:
            return
        if root["left"] is None and root["right"] is None:
            leaves.append(root["value"])
        find_leaves(root["left"], leaves)
        find_leaves(root["right"], leaves)

    numbers = list(map(int, input().split()))
    root = None
    for num in numbers:
        if num == 0:
            break
        root = insert(root, num)

    leaves = []
    find_leaves(root, leaves)
    leaves.sort()
    print(' '.join(map(str, leaves)))

if __name__ == "__main__":
    main()