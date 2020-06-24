from extract import to_signed, extract


class InvalidOperation(Exception):
    pass


# import to_signed, extract
class AbstractOperand:
    def __init__(self, value):
        self.value = value

    def read(self, memory, process):
        raise InvalidOperation

    def write(self, memory, process, value):
        raise InvalidOperation

    @staticmethod
    def create(opmode, opvalue):
        if opmode == 0:
            # immediate
            return ImmediateOperand(opvalue)
        elif opmode == 1:
            # relative
            return RelativeOperand(opvalue)
        elif opmode == 2:
            # computed
            return ComputedOperand(opvalue)
        elif opmode == 3:
            # register
            return RegisterOperand(opvalue)


class ImmediateOperand(AbstractOperand):
    def __init__(self, value):
        super().__init__(value)

    def read(self, memory, process):
        a = to_signed(self.value, 12)
        b = to_signed(a, 32)
        return b

    def write(self, memory, process, value):
        return super().write(memory, process, value)


class RegisterOperand(AbstractOperand):
    def __init__(self, value):
        super().__init__(value)

    def read(self, memory, process):
        return self.value & 15

    def write(self, memory, process, value):
        process.registers[self.value & 15] = value


class RelativeOperand(AbstractOperand):
    def __init__(self, value):
        super().__init__(value)

    def read(self, memory, process):
        return memory[to_signed(self.value, 12) + process.PC]

    def write(self, memory, process, value):
        memory[to_signed(self.value, 12) + process.PC] = value


class ComputedOperand(AbstractOperand):
    def __init__(self, value):
        super().__init__(value)

    def read(self, memory, process):
        self.l_val = to_signed(self.value + process.PC, 12)
        return memory[self.l_val]

    def write(self, memory, process, value):
        extract(self.l_val, 0, 12)
