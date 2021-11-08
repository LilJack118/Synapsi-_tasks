
import string
import random
import base64
import json

l = 'V1xLFh8TKyQuEUs='

list_s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96] 

# for el in range(97):
#     list_s.append(el)

# print(list_s)
# random.shuffle(list_s)
# print(list_s)

def encoder(letter_index_list):
    encrypted_list = []

    input_rotator_1 = [64, 57, 30, 80, 89, 52, 6, 96, 34, 28, 71, 19, 60, 35, 16, 9, 88, 79, 7, 78, 51, 40, 87, 55, 14, 22, 95, 17, 68, 84, 92, 75, 49, 23, 11, 61, 21, 32, 41, 2, 3, 50, 93, 74, 69, 39, 56, 8, 4, 90, 10, 31, 67, 70, 46, 36, 91, 86, 5, 24, 77, 85, 76, 59, 0, 62, 47, 18, 37, 83, 44, 72, 25, 43, 73, 13, 81, 66, 58, 42, 65, 53, 1, 12, 15, 48, 38, 63, 26, 29, 45, 54, 82, 27, 33, 94, 20] 
    output_rotator_1 = [80, 28, 61, 30, 46, 96, 57, 62, 67, 55, 20, 33, 15, 90, 29, 25, 36, 51, 44, 12, 9, 0, 69, 43, 63, 93, 70, 50, 83, 32, 45, 92, 22, 66, 73, 84, 54, 48, 87, 60, 41, 68, 23, 74, 16, 14, 81, 8, 31, 53, 49, 7, 85, 76, 10, 3, 40, 26, 47, 35, 65, 77, 79, 17, 4, 27, 75, 34, 42, 6, 21, 13, 94, 11, 88, 2, 52, 72, 82, 58, 38, 18, 24, 89, 86, 1, 91, 95, 39, 5, 56, 71, 59, 37, 78, 19, 64] 

    input_rotator_2 = [76, 88, 30, 63, 17, 56, 92, 31, 96, 47, 19, 12, 66, 77, 53, 21, 48, 62, 33, 7, 43, 75, 36, 9, 70, 38, 69, 28, 89, 59, 45, 80, 85, 81, 67, 18, 55, 60, 34, 82, 3, 44, 27, 52, 86, 32, 25, 65, 91, 58, 68, 29, 74, 50, 51, 22, 54, 61, 49, 40, 39, 83, 1, 46, 24, 71, 84, 57, 5, 78, 15, 64, 93, 94, 73, 87, 11, 35, 79, 23, 16, 72, 8, 14, 0, 37, 26, 4, 13, 20, 41, 6, 42, 10, 2, 95, 90]
    output_rotator_2 = [33, 37, 53, 77, 23, 41, 61, 39, 6, 28, 72, 35, 95, 50, 14, 22, 17, 80, 62, 63, 86, 40, 32, 1, 8, 12, 56, 92, 94, 69, 51, 44, 90, 36, 74, 65, 84, 73, 91, 89, 67, 71, 2, 75, 93, 68, 30, 79, 70, 81, 87, 83, 9, 59, 58, 34, 16, 26, 88, 24, 82, 45, 60, 29, 57, 3, 20, 55, 0, 48, 5, 38, 66, 42, 85, 47, 13, 78, 27, 49, 15, 54, 21, 4, 19, 31, 18, 52, 7, 25, 10, 46, 43, 96, 76, 64, 11]

    reflector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96] 

    for letter_index in letter_index_list:
        output_1 = output_rotator_1.index(input_rotator_1[letter_index])

        input_rotator_1.append(input_rotator_1.pop(0))

        output_2 = output_rotator_2.index(input_rotator_2[output_1])

        encrypted_list.append(reflector[output_2])

   
    return encrypted_list


print(encoder([61,12,14,61,61]))



def decryptor(letter_index_list):

    reflector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96] 

    input_rotator_1 = [64, 57, 30, 80, 89, 52, 6, 96, 34, 28, 71, 19, 60, 35, 16, 9, 88, 79, 7, 78, 51, 40, 87, 55, 14, 22, 95, 17, 68, 84, 92, 75, 49, 23, 11, 61, 21, 32, 41, 2, 3, 50, 93, 74, 69, 39, 56, 8, 4, 90, 10, 31, 67, 70, 46, 36, 91, 86, 5, 24, 77, 85, 76, 59, 0, 62, 47, 18, 37, 83, 44, 72, 25, 43, 73, 13, 81, 66, 58, 42, 65, 53, 1, 12, 15, 48, 38, 63, 26, 29, 45, 54, 82, 27, 33, 94, 20] 
    output_rotator_1 = [80, 28, 61, 30, 46, 96, 57, 62, 67, 55, 20, 33, 15, 90, 29, 25, 36, 51, 44, 12, 9, 0, 69, 43, 63, 93, 70, 50, 83, 32, 45, 92, 22, 66, 73, 84, 54, 48, 87, 60, 41, 68, 23, 74, 16, 14, 81, 8, 31, 53, 49, 7, 85, 76, 10, 3, 40, 26, 47, 35, 65, 77, 79, 17, 4, 27, 75, 34, 42, 6, 21, 13, 94, 11, 88, 2, 52, 72, 82, 58, 38, 18, 24, 89, 86, 1, 91, 95, 39, 5, 56, 71, 59, 37, 78, 19, 64] 

    input_rotator_2 = [76, 88, 30, 63, 17, 56, 92, 31, 96, 47, 19, 12, 66, 77, 53, 21, 48, 62, 33, 7, 43, 75, 36, 9, 70, 38, 69, 28, 89, 59, 45, 80, 85, 81, 67, 18, 55, 60, 34, 82, 3, 44, 27, 52, 86, 32, 25, 65, 91, 58, 68, 29, 74, 50, 51, 22, 54, 61, 49, 40, 39, 83, 1, 46, 24, 71, 84, 57, 5, 78, 15, 64, 93, 94, 73, 87, 11, 35, 79, 23, 16, 72, 8, 14, 0, 37, 26, 4, 13, 20, 41, 6, 42, 10, 2, 95, 90]
    output_rotator_2 = [33, 37, 53, 77, 23, 41, 61, 39, 6, 28, 72, 35, 95, 50, 14, 22, 17, 80, 62, 63, 86, 40, 32, 1, 8, 12, 56, 92, 94, 69, 51, 44, 90, 36, 74, 65, 84, 73, 91, 89, 67, 71, 2, 75, 93, 68, 30, 79, 70, 81, 87, 83, 9, 59, 58, 34, 16, 26, 88, 24, 82, 45, 60, 29, 57, 3, 20, 55, 0, 48, 5, 38, 66, 42, 85, 47, 13, 78, 27, 49, 15, 54, 21, 4, 19, 31, 18, 52, 7, 25, 10, 46, 43, 96, 76, 64, 11]

    shifted_letter_list = []
    for el in letter_index_list:
        shifted_letter_list.insert(0,el)
        input_rotator_1.append(input_rotator_1.pop(0))

    decrypted_list = []
    for letter_index in shifted_letter_list:

        output_2 = reflector.index(letter_index)
        
        input_rotator_1.insert(0,input_rotator_1.pop(96))
        output_1 = input_rotator_2.index(output_rotator_2[output_2])

        letter = input_rotator_1.index(output_rotator_1[output_1])
        decrypted_list.insert(0,letter)

    return decrypted_list


print(decryptor([34, 21, 37,43]))


encoded_list = encoder([61,12,14,61,61])
json_encoded_list = json.dumps(encoded_list)
json_encoded = str.encode(json_encoded_list)
encoded = base64.b64encode(json_encoded)
print(encoded)