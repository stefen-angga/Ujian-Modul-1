# soal 1
def hashtag(text):
    if (text == '') or (len(text)) > 140:
        return False
    else:
        kosong = []
        text = text.split()
        for i in text:
            kosong.append(i.capitalize())
        kosong.insert(0, '#')
        kosong.insert(len(text),'') 
    return (''.join(kosong))

user = str(input('Masukkan Sebuah Kalimat : '))
print(hashtag(user))

# soal 2
def create_phone_number(a):
    bag1 = []
    bag2 = []
    bag3 = []
    bag1.extend(a[:3])
    bag2.extend(a[3:6])
    bag3.extend(a[6:])
    print('('+''.join(bag1)+')'+' '+''.join(bag2)+'-'+''.join(bag3))
    

nomor = input('masukkan nomor : ').split() # pada saat input setiap angka harus dipisah dengan spasi
create_phone_number(nomor) 

# soal 3
def sort_ganjil_genap(a):
    b = sorted(a)
    a = b
    ganjil = []
    genap = []
    for i in a:
        if i%2 == 0:
            genap.append(i)
        else:
            ganjil.append(i)
    genap.reverse()
    ganjil.insert(2, genap[0])
    ganjil.insert(3, genap[1])
    ganjil.insert(5, genap[2])
    print(ganjil)
 
x = [5,3,2,8,1,4]
sort_ganjil_genap(x)

# soal 4
def segitigabolong(n):
    if n == 1:
        print('#')
        return False
    
    atas = ['_'*(n-1)+ '#'+ '_'*(n-1)]
    bawah = ['#'*(n)+ '#'*(n-1)]
    tengah = []
    for i in range (n-2, 0, -1):
        tengah.append('_'*i + '#' + ('_'*((2*n)-(2*i)-3)) + '#' + ('_'*i))
    
    print(atas[0])
    
    for i in tengah:
        print(i)
    
    print(bawah[0])

baris = int(input('masukkan jumlah baris : '))
segitigabolong(baris)
