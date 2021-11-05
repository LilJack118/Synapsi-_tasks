import string
import base64
# You're on the right track!
# encode=lambda a,b,c:(d:=0)or[(d:=pow(string.printable.index(e)*c+b+d,101,97))for e in a]
# If your stuck you can ask for a hint at recruitment@synapsi.xyz

def list_to_string(e_list):
    final_string = ''
    for e in e_list:
        final_string += string.printable[e]
    return final_string



encode=lambda a,b,c:(d:=0)or[(d:=pow(string.printable.index(e)*c+b+d,101,97))for e in a]


# pow(x,y,z) = (x**y)%z

powers = {0: 97, 1: 1, 32: 2, 49: 3, 54: 4, 21: 5, 16: 6, 26: 7, 79: 8, 73: 9, 90: 10, 31: 11, 27: 12, 74: 13, 56: 14, 59: 15, 6: 16, 68: 17, 8: 18, 77: 19, 67: 20, 13: 21, 22: 22, 5: 23, 88: 24, 53: 25, 40: 26, 85: 27, 46: 28, 14: 29, 45: 30, 86: 31, 95: 32, 64: 33, 42: 34, 61: 35, 62: 36, 15: 37, 39: 38, 37: 39, 10: 40, 80: 41, 28: 42, 93: 43, 25: 44, 78: 45, 63: 46, 50: 47, 3: 48, 94: 49, 47: 50, 34: 51, 19: 52, 72: 53, 4: 54, 69: 55, 17: 56, 87: 57, 60: 58, 58: 59, 82: 60, 35: 61, 36: 62, 55: 63, 33: 64, 2: 65, 11: 66, 52: 67, 83: 68, 51: 69, 12: 70, 57: 
71, 44: 72, 9: 73, 92: 74, 75: 75, 84: 76, 30: 77, 20: 78, 89: 79, 29: 80, 91: 81, 38: 82, 41: 83, 23: 84, 70: 85, 66: 86, 7: 87, 24: 88, 18: 89, 71: 90, 81: 91, 76: 92, 43: 93, 48: 94, 65: 95, 96: 96}


# print(encode('hi',1,2))
indexes = [51, 16, 20, 39, 43, 35, 24, 46, 40, 16, 4, 17, 56, 37, 9, 51, 53, 33, 4, 23, 48,
38, 1, 15, 40, 36, 29, 43, 44, 39, 5, 55, 47, 37, 48, 27, 54, 16, 57, 46, 55, 32, 12, 17, 50,
35, 32, 47, 55, 52, 52, 5, 36, 17, 16, 37, 37, 35, 48, 57, 42, 41, 8, 38, 39, 34, 16]

indexes_2 = [51, 16, 20, 39, 43, 35, 24, 46, 40, 16, 4, 17, 56]

indexes_x = [93, 7, 49, 51, 81, 12, 12, 7, 17, 51, 81]



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

# print(find_x_indexes(encoded_hi))



# full_cipher_x = find_x_indexes([string.printable.index(x) for x in cipher])
# print(len(set(full_cipher_x)))


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
            

#  b = 79 , c = 74
word = decode(79,74,indexes_x)
print(word)

words = set()
for b in range(100):
    for c in range(100):
        word = decode(b,c,indexes_x)
        try:
            if (' ' in word): 
                print(word, b, c)
                words.add(word)
        except:
            pass
        
print(set(words))




