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
