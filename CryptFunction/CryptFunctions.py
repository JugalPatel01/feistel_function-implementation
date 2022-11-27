def add(a, b):
    ans = bin(int(a, 2) + int(b, 2))
    return ans[2:]


def sub(a, b):
    ans = bin(int(a, 2) - int(b, 2))
    return ans[2:]


def multiply(a, b):
    ans = bin(int(a, 2) * int(b, 2))
    return ans[2:]


def xor_num(a, b):
    temp = ""
    for i in range(len(a)):
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"
    return temp


def complement(a):
    ans = bin(~int(a, 2))
    return ans[1:]


def lshift_str(a, pos: int):
    ans = bin(int(a, 2) << pos)
    return ans[2:]


def rshift_str(a, pos: int):
    ans = bin(int(a, 2) >> pos)
    return ans[2:]


def com_xor_num(a, b):
    ac = complement(a)
    bc = complement(b)
    ans = bin(int(ac, 2) ^ int(bc, 2))
    return ans[2:]


def and_num(a, b):
    ans = bin(int(a, 2) & int(b, 2))
    return ans[2:]


def com_and_num(a, b):
    ac = complement(a)
    bc = complement(b)
    ans = bin(int(ac, 2) & int(bc, 2))
    return ans[2:]


def or_num(a, b):
    ans = bin(int(a, 2) | int(b, 2))
    return ans[2:]


def com_or_num(a, b):
    ac = complement(a)
    bc = complement(b)
    ans = bin(int(ac, 2) | int(bc, 2))
    return ans[2:]


def comjfun(a, b):
    ac = complement(a)
    bc = complement(b)
    ac = lshift_str(ac, 5)
    bc = rshift_str(bc, 5)
    bc = lshift_str(bc, 5)
    ac = com_and_num(ac, bc)
    bc = com_or_num(ac, bc)
    ans = bin(int(ac, 2) ^ int(bc, 2))
    return ans[2:]
