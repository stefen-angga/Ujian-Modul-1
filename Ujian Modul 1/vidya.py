#soal #no #1
#buat def 
#menambahkan tanda # di awal kalimat
#merubah list menjadi str
#memasukan rumus capitalize
#loop

def Hashtag(string):
    z="#"
    for i in string.split():
        z += i.capitalize()

    if len(string) >= 140:
        print(False)
    elif z == '#':
        print(False)
    else:
        print(z)

string = str(input("Input text: "))
Hashtag(string)

#soal #no #2
#buat fungsi def
#ubah int menjadi list
#buat fungsi loop
#output nya adalah no telepon dengan tanda kurung dan strip

def create_phone_num(n):
    phone = [] 
    print(phone)
    print(type(phone))
    for i in n:
        phone.append(i)
    if len(phone) >= 10:
        print("Wrong number")
    elif phone != 0 and phone != 9:
        print("Memiliki angka 0 dan 9")
    else:
        print("This is the phone number: ", ''.join(phone)) 

n=input('Enter Phone Number: ')
print(n)
print(type(n))
create_phone_num(n)

#soal #no #3 
#buat fungsi sort
#pastikan 0 adalah even number

num = str(input("Enter Number: "))

convertStr = num.split(",")
for i in range(0, len(convertStr)): 
    convertStr[i] = int(convertStr[i])

even = sorted([i for i in convertStr if i%2 == 0])
odd = sorted([i for i in convertStr if i%2])

even.reverse()
allnum = odd + even
print(type(allnum))
print(allnum)

print('odd numbers ascending: ', allnum.choice(odd), '(Odds number in the index 0,1, and 2)') 
print('even numbers ascending: ', allnum[even], '(Even number in the index 3,4, and 5)')

#soal #no #4
#buat input
#pastikan baris awal hanya terdiri dari 1 baris (index 0)
#buat fungsi loop utk bikin hollow triangle dulu
#sisanya print underscore

rows = int(input("Masukkan Jumlah Baris: "))
rows = rows - 1
for i in range(0,rows+1):
    for j in range(1, 2*rows+2):
        if i == rows or i + j == rows + 1 or j - i == rows + 1: 
            print("#", end="")
        else:
            print("_", end="")
    print()
