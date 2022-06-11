
def duplicate_count(text):
    n = 0
    textSorted = sorted(text.upper())
    
    for i in range(len(textSorted)):
        if textSorted[ i] != textSorted[ i - 1 ] and i+1 < len(textSorted):
            if textSorted[ i ] == textSorted[ i + 1 ]:
                n+= 1
    return n
print(duplicate_count("Indivisibilities"))