inventaris = {}

def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga: "))
    stok = int(input("Masukkan stok: "))

    inventaris[nama_barang] = (harga,stok)
    print("Barang berhasil ditambahkan")

def tampilkan_barang():
    if not inventaris:
        print("Tidak ada barang dalam invenaris")
    else:
        print("\nDaftar Barang:")
        print(f"{'Nama Barang':<20} {'Harga':<10} {'Stok':<10}")
        print("-" * 40)
        for nama, (harga,stok) in inventaris.items():

            barang_info = (nama, harga, stok)
            print(f"{barang_info[0]:<20} {barang_info[1]:<10} {barang_info[2]:<10}")

def cari_barang():
    nama_barang = input("Masukkan nama barang untuk diperbaharui stok: ")
    if nama_barang in inventaris:
        stok_baru = int(input("Masukkan jumlah stok baru: "))
        harga = inventaris[nama_barang][0] 
        inventaris[nama_barang] = (harga, stok_baru)
        print("Stok barang berhasil diperbaharui")
    else:
        print("Barang tidak ditemukan")

def analisis_data():
    if not inventaris:
        print("Tidak ada barang dalam inventaris untuk analisis ")
        return
    
    harga_barang = [(nama, info[0]) for nama, info in inventaris.items()]
    harga_tertinggi = max(harga_barang, key=lambda x: x[1])
    harga_terendah = min(harga_barang, key=lambda x: x[1])

    total_nilai_stok = sum(harga * stok for harga, stok in inventaris.values())

    print(f"Barang dengan harga tertinggi: {harga_tertinggi[0]} -Harga:{harga_tertinggi[1]}")
    print(f"Barang dengan harga terendah: {harga_terendah[0]} - Harga:{harga_terendah[1]}")
    print(f"Total nilai stok: {total_nilai_stok}")

def main():
    while True:
        print("\nMenu Manajemen Inventaris Barang")
        print("1. Tambah Barang Baru")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang")
        print("4. Update Stok Barang")
        print("5. Hapus Barang")
        print("6. Analisis Data")
        print("7. Keluar")

        pilihan = input("Pilih opsi (1-7): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            cari_barang()
        elif pilihan == '4':
            update_barang()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            analisis_data()
        elif pilihan == '7':
            print("Terima Kasih! Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi")

if __name__ == "__main__":
    main()