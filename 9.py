with open('two_cities_ascii.txt','r') as file:
    f = file.read()

binary_converted = ' '.join(format(ord(i), 'b') for i in f)

print(binary_converted)

binary_converted = ''.join(format(ord(i), 'b') for i in f)
 
digit_string = str(binary_converted)
digit_map = map(int, digit_string)
My_List = list(digit_map)

target = 0
def longest_seq(My_List, target):
    cnt, max_val = 0, 0  
    for e in My_List:
        cnt = cnt + 1 if e == target else 0  
        max_val = max(cnt, max_val)  
    return max_val
 
 
print(longest_seq(My_List, target))
print("Zeros")

target = 1
print('And')
print(longest_seq(My_List, target))
print("Ones")
