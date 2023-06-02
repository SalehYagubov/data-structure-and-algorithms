##ARRAY (LİST) İE BAĞLI METHODLAR

#evvelce lst adında bir list tanımladıq
lst = [1,2,3,4,5]
#for ile lst-nın içindekı reqemlerı yazdırdıq
for i in lst:
    print(i) 
#asagıda ise lst-in içindekı 3 cu ındexdekı elemanı yazdırdıq
print("step2")
print(lst[3])
#3 cü adımda ise lst-e 6 reqemini elave eledık
print("step3")
lst.append(6)
print(lst)
#4 -cu adımda insert ile lst-in 3 cu indeksıne 11 reqemını elave eledık
print("step4")
lst.insert(3,11)
print(lst)
#extend ile lst1 adındakı listenı lst-e elave etdık
print("step5")
lst1 = [10,11,12]
lst.extend(lst1)
print(lst)

#fromlist ile bir list içindekı elementlerı lst-e eave edirik
print("step6")
#lst2 = [20,21,22]
#lst.fromlist(lst2)  --->>>fromlist işlemedi onu bir soruş

#print(lst)

#remove() methodu ile lst-den 12 reqemını sılırık
print("step7")
lst.remove(12)
print(lst)

#pop() methodu ile lst-nin sonuncu elementını sılırık.eger belli bir indexdekı reqemı sılmek istesek pop() moterıze içine o reqemın indeksını yazırıq
print("step8")
lst.pop()
print(lst)

#index() methodu ile lst-dekı bir elementın indexkını tapaq
print("step9")
print(lst.index(10))

#reverse() ile lst-ni tersden sıralayaq
print("step10")
lst.reverse()
print(lst)

#buffer_info methodu işlemedı soruş
print("step11")
#lst.buffer_info()
#print(lst)

#count() methodu ile lst-in içinde hangi rakamın kaç kere geçtıgını ögrene biliriz.asagıdakı ornekte 11 1 kez geçmiş
print("step12")
print(lst.count(11))

#slice: listin içinden belirli parçaları almak 

print("step16")
print(lst[1:4])



#TwoDimensialArray
#Day 1 - 11,15,10,6
#Day 2 - 10,14,11,5
#Day 3 - 12,17,12,8
#Day 4 - 15,18,14,9 


import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])

print(twoDArray)

#Two Dimensional Array de bir sayı elave elemek istesek :
#1 ci yol sutunlara,2 ci yol satırlara eklemektir


#şimdi bir satır ekleyelım : [1,2,3,4]
#bu işlemi yaptığımızda yeni satır birinci satırın yerine geçer ve satırlar aşagı kayar
#Ve bu süreç zaman aldığı için Time Complexity = O(mn)

#Aşagıdakı kodda 0 yazaraq neçenci indekse elave etmek istedıyımızı yazırıq
#axis = 1 ise sütuna elave etmek istedıyımızı bildirir

newTwoDArray = np.insert(twoDArray,0,[[1,2,3,4]],axis=1)
print(newTwoDArray)




#şimdi bir sütun ekleyelım : [1,2,3,4]
#bu işlemi yaptığımızda yeni sütun birinci sütunun yerine geçer ve sütunlar sağa kayar
#Ve bu süreç zaman aldığı için Time Complexity = O(mn)
new_TwoDArray = np.insert(twoDArray,0,[[1,2,3,4]],axis=0)
print(new_TwoDArray)


#Yuxardakı ekleme işini append() ile ede bilerık ama append her zaman sona ekleme yapar
new_two_DArray = np.append(twoDArray,[[1,2,3,4]],axis=0) 


########### ACCCESSİNG an element of two dimensional Array 
#a[i][j]--->>>> # i burda setirin indeksını j ise sutunun indeksını temsıl edir

def accessElement(array,rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array):
        print("Incorrect index")

    else:
        print(array[rowIndex][colIndex])



accessElement(twoDArray,2,2)




print("eeeeeeeeeeeeeee")

#YUXARDAKI BU METHOD O(1) time complexitydir


########## TRAVERSİNG two dimensional array

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j])

traverseTDArray(twoDArray)



############   39-- SEARCHİNG FOR ELEMENT İN  TWO DİMENSİONAL ARRAY
def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == value:
                return 'The value is located at index ' +str(i) + " " +str(j)
    return "The element is not found"

print(searchTDArray(twoDArray,14))

#Yukardakı fonksiyonun time complexity  = O(mn*2)


########### 40-- Deletion - Two Dimensional Array
#bunun üçün delete komutunu istifade edirik: ve ordakı o 0 indeksındekı setırı silmek ıstedıyımızı bildirir
#axis  = 0 ile setırı seçırık  -->> axis  =  1 ise sütunları
#
delete_TDArray = np.delete(twoDArray,0,axis=0)
print(delete_TDArray)
#yukardakı fonksiyonun time complexity is O(mn)













































