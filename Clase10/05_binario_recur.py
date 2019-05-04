def recursive_bin(n):
    if n == 0:
        return ''
    else:
        return recursive_bin(n//2) + str(n%2)


print(recursive_bin(28))
