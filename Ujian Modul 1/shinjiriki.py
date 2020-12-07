# Soal nomor 1
def hashtag(string):
    y = [i.capitalize() for i in string.split()]
    x = '#'+''.join(y)
    if len(y) == 0:
        print(False)
    elif len(x) > 140 :
        print(False) 
    else:
        print(x)
# user = input()
# hashtag(user)
hashtag(" Hello there how are you doing")
hashtag("  Hello    World   ")
hashtag("")

# Soal nomor 2
def create_phone_number(number):
    if len(number) > 10:
        return print('Number exceeds di length of 10')
    for i in number:
        if i > 9 or i < 0:
            return print('Number should be between 0 and 9')
    number = [str(i) for i in number]
    number = ''.join(number)
    x = '('+ number[:3] + ') '
    y = number[3:6]+'-'
    z = number[6:]
    print(x+y+z)    
# user = [int(i) for i in input()]
# create_phone_number(user)
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Soal nomor 3
def sort_odd_even(num):
    dup = num.copy()
    odd = [i for i in num if i%2 == 1]
    odd.sort()
    even = [i for i in num if i%2 == 0]
    even.sort(reverse=True)
    dupodd = [dup.index(i) for i in odd]
    dupodd.sort()
    dupeven = [dup.index(i) for i in even]
    dupeven.sort()
    counter = 0
    for i in dupodd:
        dup[i] = odd[counter]
        counter += 1
    counter = 0
    for i in dupeven:
        dup[i] = even[counter]
        counter += 1
    print(dup)
# user = [int(i) for i in input().split()]
# sort_odd_even(user)
sort_odd_even([5, 3, 2, 8, 1, 4])

# Soal nomor 4
def hollowtriangle(a):
    if a == 1:
        return print('#')
    hasil = ''
    banyakbintang = 1
    banyakisi = 0
    for i in range(a-1, 0, -1):
        listbintang = ['#' for i in range(banyakbintang)]
        for j in range(1, banyakisi*2):
            listbintang[j] = '_'
        spasi = '_'*i
        hasil = spasi+''.join(listbintang)+spasi
        print(hasil)
        banyakbintang += 2
        banyakisi += 1
    print('#'*(len(hasil)))
# user = int(input())
# hollowtriangle(user)
hollowtriangle(1)
hollowtriangle(2)
hollowtriangle(3)
hollowtriangle(4)
hollowtriangle(5)
hollowtriangle(6)
