#Soal 1
def hastag (data):
    x = str(data).split()
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_alph = list(alph)
    temp = []
    for i in x :
        if i[0] in list_alph : 
            temp.append(i)
        else :
            temp.append(i[0].upper()+i[1::])
    if len(data) >140:
        print (False)
    elif len(data) == 0 :
        print (False)
    else :
        print(str('#')+ ''.join(temp))
    

hastag('Hello there how are you doing')
hastag('   Hello    World')
hastag('')


####################################################################
print ('LANJUT SOAL BARU')
####################################################################


#Soal 2


def create_phone_number(x) :
    if max(x) > 9 :
        print ('Masukkan angka dari 0 - 9')
    else :
        awal = []
        tengah = []
        akhir = []
        for i in x[0:3]:
            awal.append(i)
        for j in x[3:6]:
            tengah.append(j)
        for k in x[6::]:
            akhir.append(k)

        temp_awal = ''
        temp_tengah = ''
        temp_akhir = ''
        for a in awal :
            temp_awal += str(a)
        for b in tengah :
            temp_tengah += str(b)
        for c in akhir :
            temp_akhir += str(c)

        print (f'({temp_awal}) {temp_tengah}-{temp_akhir}')


create_phone_number(([1,2,3,4,5,6,7,8,9,0]))


####################################################################
print ('LANJUT SOAL BARU')
####################################################################


#Soal 3

def sort_odd_even(data):
    if len(data) == 0 :
        print ('Data Kosong')
    else :
        for i in range(len(data)):
            if data[i]%2 != 0:
                for j in range(len(data)):
                    if data[i] < data[j] and data[j] %2 != 0:
                        data [i],data[j] = data[j],data[i]
                    else :
                        pass
            else :
                for j in range(len(data)):
                    if data[i] > data[j] and data[j] % 2 == 0:
                        data [i],data[j] = data[j],data[i]
                    else :
                        pass
        print (data)
                    
    
sort_odd_even([5,3,2,8,1,4]) #[1,3,8,4,5,2]


####################################################################
print ('LANJUT SOAL BARU')
####################################################################


#Soal 4

def hollowTriangle(data):
    space = data - 1
    temp = (space * '_') + '#' + (space * '_')
    penutup = ((data*2)-1) * '#'
    if data == 1 :
        print (temp)
    elif data == 2 :
        print(temp)
        print(penutup)
    else :
        for i in range (1,data-1):
            temp += '\n'
            space -= 1
            temp += (space * '_') + '#' + (((2*i)-1) * '_') + '#' + (space * '_')
        print(temp)
        print(penutup)

jumlah_baris = int(input('Masukkan Jumlah Baris : '))
hollowTriangle(jumlah_baris)
