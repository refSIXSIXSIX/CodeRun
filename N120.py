def main():
    def insert(root, value):
        if root is None:
            return {"value": value, "left": None, "right": None}
        if value < root["value"]:
            root["left"] = insert(root["left"], value)
        elif value > root["value"]:
            root["right"] = insert(root["right"], value)
        return root

    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root["left"]), height(root["right"]))

    numbers = list(map(int, input().split()))
    root = None
    for num in numbers:
        if num == 0:
            break
        root = insert(root, num)

    print(height(root))

if __name__ == "__main__":
    main()