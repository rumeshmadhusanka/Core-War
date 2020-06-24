def extract(w, m, n):
    # print(bin(w))
    msk1 = 2 ** (m + n) - 1
    first = w & msk1
    ans = first >> m
    # print(bin(ans))
    return ans


def to_signed(w, n):
    if (w & (1 << (n - 1))) != 0:
        w = w - (1 << n)
    return w


def of_signed(i, n):
    mask = 2 ** n - 1
    flipped = mask & i
    return flipped + 1


def idecode(w):
    # (opcode, (modeA, operandA),     (modeB, operandB))
    opcode = extract(w, 0, 4)

    mode_a = extract(w, 4, 32)
    mode_a = extract(mode_a, 0, 2)

    mode_b = extract(w, 6, 32)
    mode_b = extract(mode_b, 0, 2)

    operand_a = extract(w, 8, 32)
    operand_a = extract(operand_a, 0, 12)

    operand_b = extract(w, 20, 32)
    operand_b = extract(operand_b, 0, 12)
    return opcode, (mode_a, operand_a), (mode_b, operand_b)


def resolve_writes(base, xs):

    base_list = list(bin(base)[2:].zfill(32))
    xs_list = []

    for i in xs:
        xs_list.append(list(bin(i)[2:].zfill(32)))
    p = len(base_list)
    for bit_idx in range(p):
        zero = 0
        one = 0
        for lst in xs_list:
            b = int(lst[bit_idx])
            if b == 0:
                zero += 1
            else:
                one += 1
        if zero > one:
            base_list[bit_idx] = '0'
        elif one > zero:
            base_list[bit_idx] = '1'
    ret = ""
    for i in base_list:
        ret += i
    return int(ret, 2)


if __name__ == "__main__":
    pass
    # print(to_signed(298704996, 29))  #-238165916
    # print(to_signed(12, 8))  # 12
    # print(to_signed(298704996, 29))
    # print(idecode(2746317214))  # (14, (1, 377), (2, 2619))

    # print(extract(2746317213, 0, 2))
    # print(extract(2410529190, 22, 3))
    pq = (resolve_writes(4249970407, [3974524835, 2748778025, 2955633093, 2392080954, 943239975, 2940395824, 1392783744, 3620021414]))  # 3208930211

    # print("my res", bin(pq)[2:].zfill(32))
    # print("base  ", bin(107420370)[2:].zfill(32))
    # print("xs1   ", bin(3184935164)[2:].zfill(32))
    # print("xs2   ", bin(1181241944)[2:].zfill(32))
    # print("xs3   ", bin(1051802513)[2:].zfill(32))
    # print("result", bin(1055937240)[2:].zfill(32))
    print(pq)

    print(list(bin(4249970407)[2:].zfill(32)))
