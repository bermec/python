
def count(string, letter):
    x = 0
    for i in string:
        if i == letter:
            x += 1
    return x

ans = count('"The letter "+letter+" appears " +str(x)+" times in the string: "+string', 't')
print  ans

def reverse_string(fruit):
    index = len(fruit)
    while index > 0:
        letter =fruit[index -1]
        print letter
        index -= 1

strng = raw_input('Enter a fruit..:  ')
ans = reverse_string(strng)

