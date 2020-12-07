                    # Soal 1
def Hashtag(string):
    if len(string) > 140:
        return False
    elif string == '':
        return False
    else:
        string = string.split()
        string.insert(0, '#')
    return ''.join(string)

kalimat = input('Masukkan sebuah kalimat = ').title()
print(Hashtag(kalimat))
                    # Soal 2
def konterhp(x):
    a =[]
    b =[]
    c =[]
    if len(x) >= 10 :
        for i in range (0,3):
            a.append(x[i])
        for i in range (3,6):
            b.append(x[i])
        for i in range (6,len(x)):
            c.append(x[i])
    else :
        print (False)
    a = "".join(a)
    b ="".join(b)
    c = "".join(c)
    print(f'({a}) {b}-{c}')

x = input("Nomor Telpon = ")
konterhp(x)
                    # Soal 3
def gg(numbers):
    ganjil = []
    genap = []
    for i in numbers:
        if i % 2 == 0:
            genap.append(i)
        else:
            ganjil.append(i)
    return (sorted(ganjil)+sorted(genap, reverse=True))  #ganjil ascending, genap kena reverse

data = list(map(int,input('masukan urutan angka = ').split()))
print(gg(data))
                # Soal 4
def pusing(n):
    if n == 1:
        print('#')
        return (False)
    
    pucuk = ['_'*(n-1)+'#'+'_'*(n-1)]
    dasar = ['##'*(n-1)+'#']
    tengah = []
    for i in range(n-2,0,-1):
        tengah.append(('_'*i)+'#'+('_'*((2*n)-(2*i)-3))+'#'+('_'*i))
    print(pucuk[0])

    for i in tengah:
        print(i)
    
    print(dasar[0])

baris = int(input('Masukkan jumlah baris: '))
pusing(baris)
