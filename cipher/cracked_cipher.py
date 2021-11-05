import base64
import string

powers = {0: 97, 1: 1, 32: 2, 49: 3, 54: 4, 21: 5, 16: 6, 26: 7, 79: 8, 73: 9, 90: 10, 31: 11, 27: 12, 74: 13, 56: 14, 59: 15, 6: 16, 68: 17, 8: 18, 77: 19, 67: 20, 13: 21, 22: 22, 5: 23, 88: 24, 53: 25, 40: 26, 85: 27, 46: 28, 14: 29, 45: 30, 86: 31, 95: 32, 64: 33, 42: 34, 61: 35, 62: 36, 15: 37, 39: 38, 37: 39, 10: 40, 80: 41, 28: 42, 93: 43, 25: 44, 78: 45, 63: 46, 50: 47, 3: 48, 94: 49, 47: 50, 34: 51, 19: 52, 72: 53, 4: 54, 69: 55, 17: 56, 87: 57, 60: 58, 58: 59, 82: 60, 35: 61, 36: 62, 55: 63, 33: 64, 2: 65, 11: 66, 52: 67, 83: 68, 51: 69, 12: 70, 57: 
71, 44: 72, 9: 73, 92: 74, 75: 75, 84: 76, 30: 77, 20: 78, 89: 79, 29: 80, 91: 81, 38: 82, 41: 83, 23: 84, 70: 85, 66: 86, 7: 87, 24: 88, 18: 89, 71: 90, 81: 91, 76: 92, 43: 93, 48: 94, 65: 95, 96: 96}



def most_frequent(List):
    return max(set(List), key = List.count)



def find_x_indexes(encoded_list):
    # where x is (letter_index*c+b)
    new_list = []
    prev = 0
    for y in encoded_list:
        if prev > powers[y]:
            x = 97 - (prev-powers[y])
        else:
            x = powers[y] - prev

        new_list.append(x)
        prev = y
    
    return new_list


def find_b_c(letter,index,b,c):
    find = False
    if (string.printable.index(letter)*c + b) % 97 == index:
        find = True
    return find


def decode(b,c,res_lists):
    guess_string = ''
    if find_b_c(' ',51,b,c):
        for index_res in res_lists:
        # print((string.printable.index('n')*c+b)%97)
            for letter in string.printable[0:97]:
                if (string.printable.index(letter)*c+b)%97 == index_res:
                    guess_string += str(letter)
                

    if len(guess_string) == len(res_lists):
        # print(len(guess_string), len(res_lists))
        return guess_string




coded_string='Ky9gL1YBSlsfJhZLJkJDXU8vAQhDIlkKW04qPglSFglGJlU+BjoTDCkwFldXW04sBzgaHhAuRBYGCEMNMFJDMwRJPkpETTI0EBItBj9EH1wtTRJUJ0BUUV9ADSExIgQnYFBbHA4IXwIVLEQTNEEmQkMXOUwvATNTDxg+QBoeMiRDJ0BDWVUlHSEaHlg0MTFdT0JEEDQ/Sw4EEwY/KkE6TS5bRik8PgBdJkU1EQZZHFYKD2AGCFdQXF0eOFojEwwYPhdcRB0AWwJIAzstYCUdBUgoKg0jQgo3HQRXF1ECK01WAShRSwRXGh5NA0g1DzdJRk9AWhkcNWAdHltNQ1kvAVdQXBoeQgMQDQg9YCwLBB5ZXSxMTS4AXT5KLjc0SjUaIhURUx9cEhsZVBRfXikXMCAoTUBbTktWSwQTOjshJz1gMjYwUSk3ECEaHk0jFEU3SQxFGh4MUgs6NjlPQFpaGSkXPD4GXjhaPgYhQi9WHApOXwAKSC5bHyYvLEEEBgcYLFldXl9eSR9ZXTRBUEZcJ1k9PDQQGzIrNgAiEVIgKT0KPDhbMkcYCDpLVh0FPEE0EFNCNEUFUVglBFcjKVQUOSI/RAY6S1YdHSxBRxYrUVgqKFEMEywjMkYJOClUFkdEEzE1FSwHHFlNA0MjSw0wNgA9O1o+ESorICswRTkfXQ0hSAhdJSwHWAojVwshLVgcNQJSQFtORxwWCTEjQiAyNjtaFzkARBYqNBA+T0Q4UVUVKAgXOR87WhdETUMXXClVEjNTHgkZYC8sEVdQOTMbHQVICyQWKjoORgY/HQUvQTEXPQ8LO1pdT1MOVlgxCxVcQQwlGFA6NjBFBTweW0ZeTl9aLi0NITwGBVtOLAUDMCAOVzUaPzIQIlAqIUJSI0JCFDg9O1oLOksUNTwPBllVVktMXwEACTobDSMUFA=='
decoded = base64.b64decode(coded_string)
# print(decoded.decode("utf-8"))
# print(decoded)
decoded_s = []
for el in decoded:
    decoded_s.append(el)
# print(max(decoded_s))

indexes_x = find_x_indexes(decoded_s)
print(decode(79,74,indexes_x))







# write as string 
code_string = ''
for el in decoded_s:
    code_string += string.printable[el]
# print(code_string)






