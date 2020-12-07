print('Soal 1')
def hashtag(string):
    lower = x.lower()
    y = len(x.replace(' ',''))
    listing = lower.split()
    list3= []
    list2 = []
    if y > 140 :
        print(False)
    elif y == 0 :
        print(False)
    else :
        for i in range (len(listing)):
            list2 += listing[i]
            final = (listing[i].capitalize())
            list3.append(final)
        print('#'+''.join(list3))


x = str(input('Masukkan Kalimat : '))
hashtag(str(x))

print()
print('Soal 2')
def create_phone_numbers(number):
    if len(hp) < 10 :
        print('Nomor HP Minimal 10 Angka')
    else :
        print (str('('+ hp[0:3] +') '+ hp[3:6] + '-' + hp[6:] ))
    
hp = str(input('Masukkan No HP : '))
create_phone_numbers(hp)


print()
print('Soal 3')
angka = [5,3,2,8,1,4]
def sort_odd_even(num):
    odd =[]
    even = []
    for i in num :
        if i % 2 == 0 :
            even.append(i)
        elif i == 0 :
            even.append(i)
        else:
            odd.append(i)
    y = sorted(odd)[0:2]+sorted(even,reverse=True)[0:2]+sorted(odd)[-1:]+sorted(even,reverse=True)[-1:]
    return y
print(sort_odd_even(angka))

print()
print('Soal 4')
def hollowtriangle(n):
    if n == 1 :
        print('#')
        return False
    atas = ['-' * (n-1)+'#'+'-'*(n-1)]
    bawah = ('#'*((2*n)) + '#')
    mid = []
    for i in range (n-2 , 0, -1):
        mid.append(('-'*i)+'#'+('-'*((2*n)-(2*i)-3))+'#'+('-'*i))
    
    print(atas[0])

    for i in mid:
        print(i)

    print(bawah[0:-2])

baris = int(input('Masukkan Jumlah Baris : '))
hollowtriangle(baris)
