
# REVERSE NUMBER
def reverse_number(number):
    sign = -1 if number < 0 else 1
    reverse_number = 0
    while abs(number) > 0:
        reverse_number += (abs(number) % 10) * pow(10,(len(str(abs(number)))-1))
        number = int(str(abs(number))[0:-1]) if len(str(abs(number))) > 1 else 0

    return reverse_number * sign if (reverse_number*sign).bit_length() <= 32 else 0



# LETTER COMBINATIONS

from functools import reduce

phone_dial = {1:[],2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z'],0:['+']}



def letter_combinations(digits):
    lists = [phone_dial[int(x)] for x in digits]
    possible_combinations = []
    possibilities = reduce(lambda x, y: x*y, [len(x) for x in lists]) if lists else 0

    for i in range(possibilities):
        possible_combinations.append('')
    

    index = 1
    for list_index in range(len(lists)):
        index = index*len(lists[list_index])

        letter_index = 0
        for pos in range(possibilities):
            possible_combinations[pos]+=lists[list_index][letter_index]
            
            if (pos+1)%(possibilities/index) == 0:
                if letter_index < len(lists[list_index])-1:
                    letter_index += 1
                else:
                    letter_index = 0

    
    return possible_combinations





# JUSTIFYING WORDS

def justify_text(words,max_width):
    justify_list = []
    list_words = words.replace(' ',' _ ').split(' ')

    line_width = 0
    line = ''
    
    for index,word in enumerate(list_words):
        if line_width + len(word) <= max_width:
            line += word
            line_width += len(word)
        elif index == len(list_words) - 1:
            justify_list.append(line)
            justify_list.append(word)
        else:
            justify_list.append(line)
            line = word
            line_width = len(word)
        

    
    final_justification =[]
    for l in justify_list[:-1]:
        l = l[1:] if l[0] == '_' else l
        l = l[:-1] if l[-1] == '_' else l
        coun = l.count('_')
        spaces = []
        if coun != 0:
            for i in range(coun): spaces.append('')
            for i in range(max_width - (len(l) - coun)): spaces[i%coun] += '_' 
        final_string = ''
        for index,el in enumerate(l.split('_')):
            if index <= (len(spaces) - 1):
                final_string += el + spaces[index]
            else:
                final_string += el
        
        final_string = line if not final_string else final_string
            
        final_justification.append(final_string)

    final_justification.append(justify_list[-1])


    print(*final_justification,sep='\n')
        







