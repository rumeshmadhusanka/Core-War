class CyclicStack:
    def __init__(self, size):
        self.size = size
        self.top_index = 1
        self.stack = [[0] for _ in range(size)]

    def __len__(self):
        return self.size

    def get_current_index(self):
        return self.top_index % self.size

    def pop(self):
        self.top_index -= 1
        index = self.get_current_index()
        content = self.stack[index][0]
        # self.stack[index] = [0]
        print("Pop idx:", index, "  Pop content: ", content)
        return content

    def push(self, n):
        index = self.get_current_index()
        print("push to: ", index, "    value: ", n)
        self.stack[index] = [n]
        self.top_index += 1





if __name__ == "__main__":
    pass
