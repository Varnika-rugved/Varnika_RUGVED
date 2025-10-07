def triple_and(x, y, z):
    result = x and y and z
    return result


print(triple_and(True, True, True))
print(triple_and(True, False, True))
print(triple_and(False, False, False))
