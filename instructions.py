from low_level import *
from operands import InvalidOperation


class AbstractInstruction:
    def __init__(self, operandA, operandB):
        self.operandA = operandA
        self.operandB = operandB

    def exec(self, memory, process):
        raise NotImplementedError

    @staticmethod
    def create(opcode, operandA, operandB):
        if opcode == 0:
            return FORK(operandA, operandB)
        elif opcode == 1:
            return MOV(operandA, operandB)
        elif opcode == 2:
            return NOT(operandA, operandB)
        elif opcode == 3:
            return AND(operandA, operandB)
        elif opcode == 4:
            return OR(operandA, operandB)
        elif opcode == 5:
            return LS(operandA, operandB)
        elif opcode == 6:
            return AS(operandA, operandB)
        elif opcode == 7:
            return ADD(operandA, operandB)
        elif opcode == 8:
            return SUB(operandA, operandB)
        elif opcode == 9:
            return CMP(operandA, operandB)
        elif opcode == 10:
            return LT(operandA, operandB)
        elif opcode == 11:
            return POP(operandA, operandB)
        elif opcode == 12:
            return PUSH(operandA, operandB)
        elif opcode == 13:
            return JMP(operandA, operandB)
        elif opcode == 14:
            return BZ(operandA, operandB)
        elif opcode == 15:
            return DIE(operandA, operandB)
        else:
            raise InvalidOperation


class FORK(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        process.Z = 0
        process.PC += 1
        process.PC %= 4096


class MOV(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        # print(self.operandA,self.operandB)
        self.operandB.write(memory, process, self.operandA.read(memory, process))
        process.PC += 1
        process.PC %= 4096
        return []


class NOT(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = self.operandA.read(memory, process)
        res = eval_NOT(res)
        self.operandB.write(memory, process, res)
        if res == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class AND(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = eval_AND(self.operandA.read(memory, process), self.operandB.read(memory, process))
        self.operandB.write(memory, process, res)
        if res == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class OR(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = eval_OR(self.operandA.read(memory, process), self.operandB.read(memory, process))
        self.operandB.write(memory, process, res)
        if res == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class LS(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        a = to_signed(self.operandA.read(memory, process), 32)
        b = eval_LS(a, self.operandB.read(memory, process))
        self.operandB.write(memory, process, b)
        if b == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class AS(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        a = to_signed(self.operandA.read(memory, process), 32)
        b = eval_AS(a, self.operandB.read(memory, process))
        self.operandB.write(memory, process, b)
        if b == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class ADD(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = eval_ADD(self.operandA.read(memory, process), self.operandB.read(memory, process))
        self.operandB.write(memory, process, res)
        if res == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class SUB(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = eval_SUB(self.operandA.read(memory, process), self.operandB.read(memory, process))
        self.operandB.write(memory, process, res)
        if res == 0:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class CMP(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = eval_CMP(self.operandA.read(memory, process), self.operandB.read(memory, process))
        if res:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class LT(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = eval_LT(to_signed(self.operandA.read(memory, process)), to_signed(self.operandB.read(memory, process)))
        if res:
            process.Z = 1
        else:
            process.Z = 0
        process.PC += 1
        process.PC %= 4096
        return []


class POP(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        res = process.stack.pop()
        self.operandA.write(memory, process, res)
        process.PC += 1
        process.PC %= 4096
        return []


class PUSH(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        process.stack.push(self.operandA.read(memory, process))
        process.PC += 1
        process.PC %= 4096
        return []


class JMP(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        a = to_signed(self.operandA.read(memory, process), 32)
        process.PC += a
        process.PC %= 4096
        return []


class BZ(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        a = to_signed(self.operandA.read(memory, process), 32)
        if process.Z:
            process.PC += a
            process.PC %= 4096
        else:
            process.PC += 1
            process.PC %= 4096
        return []


class DIE(AbstractInstruction):
    def __init__(self, operandA, operandB):
        super().__init__(operandA, operandB)

    def exec(self, memory, process):
        raise InvalidOperation


if __name__ == '__main__':
    AbstractInstruction.create(1, 5435, 5345).exec("cedc", "crece")
