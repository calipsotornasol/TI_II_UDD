def safe_divide(a, b):
    try:
        return a / b
    except:
        return 1E100


#print(safe_divide(1, 2))
print(safe_divide(2, 0))
