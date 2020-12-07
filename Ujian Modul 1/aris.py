#Soal No.1
def hashtag(word=input("Input String: ")):
    #VALIDATION
    arrWord = word.split()
    temp =[]
    if len(arrWord) == 0:
        return False

    #CONVERT TO HASH
    for i in arrWord:
        temp.append(i.lower().title())
    result = "#"+"".join(temp)
    
    #2nd VALIDATION
    if len(result) > 140:
        return False
    else:
        return result

print(hashtag())
##########################################################################
#Soal No. 2
def create_phone_number(numbers):
    # VALIDATION
    temp = []
    if len(numbers) != 10:
        return "List must be 10 elements" 
    for i in numbers:
        if i > 9 or i < 0:
            return "List must contain element between 0 and 9"
        else:
            temp.append(str(i))

    #CONVERT TO PHONE NUMBER
    front = "".join(temp[0:3])
    middle = "".join(temp[3:6])
    behind = "".join(temp[6:])
    return "("+front+") "+middle+"-"+behind

a = [1,2,3,4,5,6,7,8,9,0]
print(create_phone_number(a))
##########################################################################
#Soal No.3
def sort_odd_even(numbers):
    #Init List
    odd = []
    even =[]
    checker = []
    result = []
    #Split Odd and Evens
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
            checker.append(True)
        else:
            odd.append(i)
            checker.append(False)
    #Sort List
    odd.sort()
    even.sort(reverse=True)
    #Rearrange result
    for j in checker:
        if j:
            result.append(even[0])
            even.pop(0)
        else:
            result.append(odd[0])
            odd.pop(0)
    return result

a = [5,3,2,8,1,4]
print(sort_odd_even(a))
##########################################################################
#Soal No.4
def hollowTriangle(height=int(input("Input height: "))):
    left = height-2
    right = height

    if height == 1:
        print("#")
        return 0
    for i in range(height-1):
        listUnder = list("_"*(height*2-1))
        if i == 0:
            listUnder[height-1] = "#"
            print("".join(listUnder))
        else:
            listUnder[left] = "#"
            listUnder[right] = "#"
            print("".join(listUnder))
            right += 1
            left -= 1
    print("".join(list("#"*(height*2-1)))) 
hollowTriangle()
