# 2. zadanie: zarovnaj
# autor: Tomáš Kozák
# datum: 16.11.2018

def dlzkaZnakovPola(array):
    pocet = 0
    for i in range(len(array)):
        pocet += len(array[i])
    return pocet

def pridajMedzery(array, sirka, f = False):
    if array == []:
        return
    if dlzkaZnakovPola(array) < sirka and f == True:
        return ' '.join(array)
    else:
        while dlzkaZnakovPola(array) < sirka:
            if len(array) == 1:
                return array[0]
            for i in range(len(array) - 1):
                array[i] = array[i] + ' '
                if dlzkaZnakovPola(array) == sirka:
                    break
        return ''.join(array)


def spravZarovanie(array, sirka):
    #print(array)
    i = p =0
    f = False
    for k in range(len(array)):
        if f: #i == len(array) - 1:
            break
        pole = []
        if len(array[i]) > sirka and i <= k:
            #print('to ja pisem')
            pole.append(array[i])
            print(array[i])
            pole = []
            i += 1

        if i <= k:
            while ( dlzkaZnakovPola(pole) + len(array[i]) < ( sirka - (len(pole) - 1))):
                #print('while cyklus zbehne')
                pole.append(array[i])
                if ( i == len(array) - 1 ):
                    #print('posledny >>>', array[i])
                    f = True
                    #print('kontrola>>>', pole)
                    break
                i += 1
            print((pridajMedzery(pole, sirka, f)))

def vypis(subor, sirka):
    t = open(subor, 'r', encoding='utf-8-sig')
    zoznam = []
    riadok = (t.readline())
    while riadok != '':
        while riadok != '\n' and riadok != '':
            zoznam = zoznam + riadok.split()
            riadok = t.readline()
            if riadok == '':
                break
        if zoznam != []:
            spravZarovanie(zoznam, sirka)
            if riadok != '':
                print()
        zoznam.clear()
        if riadok == '':
            break
        riadok = t.readline()
    t.close()




if __name__ == '__main__':
    vypis('subor1.txt', 15)
