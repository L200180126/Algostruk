class MhsTIF(object):
    def __init__(self,nama, umur,kota,us):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.umur) \
            + ', Tinggal di ' + self.kotaTinggal \
            + ', Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('nana', 10, 'Yogyakarta', 280000)
c1 = MhsTIF('cika', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 200000)
c3 = MhsTIF('andra', 18, 'Solo', 235000)
c4 = MhsTIF('Eana', 4, 'Boyolali', 240000)
c5 = MhsTIF('lala', 31, 'Salatiga', 200000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 275000)
c8 = MhsTIF('umi', 23, 'Klaten', 245000)
c9 = MhsTIF('nurul', 64, 'Karanganyar', 270000)
c10 = MhsTIF('joko', 29, 'Boyolali', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#Tugas no 1
def cariKotaTinggal(list, target):
    kt = []
    for i in list:
        if i.kotaTinggal == target:
            kt.append(list.index(i))
    return kt

#Tugas no 2
def uangTerkecil(list):
    saku = list[0].uangSaku
    for us in list[1:]:
        if us.uangSaku < saku:
            saku = us.uangSaku
    return saku

#Tugas no 3
def uangTerkecilTarget(list):
    daftar = []
    saku = list[0].uangSaku
    for u in list:
        if u.uangSaku < saku:
            daftar.append((u.nama, u.umur, u.kotaTinggal, u.uangSaku))
    return daftar

#Tugas no 4
def uangTerkecil250(list):
    terkecil = 250000
    daftar = []

    for u in list:
        if u.uangSaku < 250000:
            daftar.append((u.nama, u.umur, u.kotaTinggal, u.uangSaku))
    for u in daftar:
        print(u)

#Tugas no 5
class Sambung:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def baru(self, data_baru):
        sambung_baru = Sambung(data_baru)
        sambung_baru.next = self.head
        self.head = sambung_baru
    def baruu(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Sambung(data)
        return self.head
    def insert(self, data, pos):
        sambung = Sambung(data)
        if not self.head:
            self.head = sambung
        elif posisi == 0:
            sambung.next = self.head
            self.head = sambung
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos += 1
            prev.next = sambung
            sambung.next = current
        return self.head
    def cari(self, c):
        current =  self.head
        while current != None:
            if current.data == c:
                return True
            current = current.next
        return False
    def tampil(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#Tugas no 6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1

    while low <= high:
        mid = (low + high) //2
        if kumpulan[mid] == target:
            return "Target berada pada index" + str(mid)
            break
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False

#Tugas 7
def binSee(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    list = []

    while low <= high:
       
        if kumpulan[low] == target:
            list.append(low)
            low += 1
        else:
            low += 1
    return list

#Tugas 8
def binSeee(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (low + high) //2
        if kumpulan[low] == target:
            return mid
        elif target > kumpulan[mid]:
            high = mid + 1
        else:
            low = mid - 1
    return -1
