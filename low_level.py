from extract import to_signed


def eval_ADD(w1, w2):
    mask = 2 ** 32 - 1
    return (w1 + w2) & mask


def eval_SUB(w1, w2):
    mask = 2 ** 32 - 1
    return (w1 + (~w2) + 1) & mask


def eval_NOT(w):
    mask = 2 ** 32 - 1
    return mask ^ w


def eval_AND(w1, w2):
    return w1 & w2


def eval_OR(w1, w2):
    return w1 | w2


def eval_LS(a, w):
    i = to_signed(a, 32)
    if i >= 0:
        return w >> i
    else:
        j = abs(i)
        return w << j


def eval_AS(a, w):
    w = to_signed(w,32)
    i = a
    if i >= 0:
        return to_signed(w >> i, 32)
    else:
        j = abs(i)
        return to_signed(w << j, 32)


def eval_CMP(w1, w2):
    res = w1 ^ w2
    if not res:
        return True
    else:
        return False


def eval_LT(w1, w2):
    w1_signed = to_signed(w1, 32)
    w2_signed = to_signed(w2, 32)
    return w1_signed < w2_signed


if __name__ == "__main__":
    # a,b =(107420370, 3184935164)
    # print(bin(a))
    # print(bin(b))
    # c = eval_SUB(a,b)
    # exp = 1217452502
    # print(bin(exp))
    # print(c)
    # print(bin(c))

    # print(eval_LT(2746317214, 478163328)) # True
    print(bin(4294967278))
    print(bin(107420370))
    print(eval_LS(4294967278, 107420370))  # 1799880704
    print(eval_AS(4294967278, 107420370))  # 1799880704
