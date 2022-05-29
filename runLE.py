
def run_length_encoding(str):
    n = 1
    index = 0
    runLE = []
    if str == '':
        return []
    while True:  
        if index == len(str) - 1:
            runLE.append([n,str[index]])
            break
    
        if str[index] == str[index + 1]:
            n = n + 1
        else:         
            runLE.append([n,str[index]])
            n = 1
            if index + 1 == len(str) - 1:
                runLE.append([1,str[index + 1]])
                break
        index += 1
    return runLE

print(run_length_encoding(''))
print(run_length_encoding('2'))
print(run_length_encoding('ab'))
print(run_length_encoding('aa'))
print(run_length_encoding("abc"))
print(run_length_encoding("aab"))
print(run_length_encoding("hello world!"))

    