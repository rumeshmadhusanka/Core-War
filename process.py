from cyclic_stack import CyclicStack


class Process:
    def __init__(self):
        self.registers = [0 for _ in range(16)]
        self.stack = CyclicStack(16)
        self.PC = 0
        self.Z = 0
