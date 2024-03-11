class Node:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_menu(self, nama, harga):
        # Menambahkan menu ke keranjang
        if not self.head:
            self.head = Node(nama, harga)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(nama, harga)

    def tampilkan_pesanan(self):
        # Menampilkan pesanan yang sudah ditambahkan
        if not self.head:
            print("Keranjang kosong")
        else:
            current = self.head
            idx = 1
            while current:
                print(f"{idx}. {current.nama} {current.harga} rupiah")
                current = current.next
                idx += 1
                
    def hitung_total_harga(self):
        # Menghitung total harga pesanan
        total = 0
        current = self.head
        while current:
            total += current.harga
            current = current.next
        return total
        
menu_miexue = {
    "Miexue Ice Cream": 5000,
    "Boba Shake": 16000,
    "Mi Sundae": 14000,
    "Mi Ganas": 11000,
    "Creamy Mango Boba": 22000
}
keranjang = LinkedList()

while True:
    print("\nPilihan Menu:")
    print("1. Tambah pesanan ke keranjang")
    print("2. Tampilkan pesanan yang sudah ditambahkan")
    print("3. Bayar Pesanan")
    print("4. Keluar")
