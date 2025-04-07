def add_binary(a, b):
    max_len = max(len(a), len(b))
    a = [0]*(max_len - len(a)) + a
    b = [0]*(max_len - len(b)) + b
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        s = a[i] + b[i] + carry
        result.append(s % 2)
        carry = s // 2
    if carry:
        result.append(carry)
    return result[::-1]

def multiply_binary(a_str, b_str):
    a = [int(bit) for bit in a_str]
    b = [int(bit) for bit in b_str]
    result = [0]
    for i in range(len(b) - 1, -1, -1):
        if b[i] == 1:
            partial = a + [0] * (len(b) - 1 - i)
            result = add_binary(result, partial)
    return ''.join(map(str, result))

# Przykład użycia:
a = input("Podaj pierwszą liczbę binarną: ")
b = input("Podaj drugą liczbę binarną: ")
print("Wynik mnożenia:", multiply_binary(a, b))
