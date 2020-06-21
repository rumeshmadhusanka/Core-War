def extract(w, m, n):
    print(bin(w))
    msk1 = 2 ** (m + n) - 1
    first = w & msk1
    ans = first >> m
    return ans
    # print(bin(first))
    # print(bin(first>>(m)))


def to_signed(w, n):
    mask = 2 ** n - 1
    return (~w) & mask


def of_signed(i, n):
    mask = 2 ** n - 1
    flipped = mask & i
    return flipped + 1


def idecode(w):
    # (opcode, (modeA, operandA),     (modeB, operandB))
    opcode = extract(w, 4, 4)
    mode_a = extract(w, 6, 2)
    mode_b = extract(w, 8, 2)
    operand_a = extract(w, 20, 12)
    operand_b = extract(w, 32, 12)
    return opcode, (mode_a, operand_a), (mode_b, operand_b)


def resolve_writes(base, xs):
    for i in xs:
        base = base ^ i
    return base


if __name__ == "__main__":
    pass
    print(to_signed(2746317213, 32))
    print(idecode(2746317213))
    # print(extract(2746317213, 0, 2))
    # print(extract(2410529190, 22, 3))
