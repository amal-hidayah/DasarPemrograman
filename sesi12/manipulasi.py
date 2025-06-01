import pandas as pd

# 1. Membaca file Excel data_penjualan.xlsx dan menampilkan 5 baris pertama
data = pd.read_excel('data_penjualan.xlsx')
print("5 baris pertama:")
print(data.head())

# 2. Menambahkan Kolom Total Harga = Jumlah * Harga Satuan
data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']
print("\nData dengan kolom Total Harga:")
print(data.head())

# 3. Filter Data kategori Elektronik dan simpan ke elektronik.xlsx
data_elektronik = data[data['Kategori'] == 'Elektronik']
data_elektronik.to_excel('elektronik.xlsx', index=False)
print("\nData elektronik disimpan di elektronik.xlsx")

# 4. Rekap Penjualan per Kategori (total pendapatan)
rekap = data.groupby('Kategori')['Total Harga'].sum().reset_index()
rekap.columns = ['Kategori', 'Total Pendapatan']
print("\nRekap total pendapatan per kategori:")
print(rekap)

# 5. Sortir data berdasarkan Total Harga secara menurun dan simpan ke penjualan_terurut.xlsx
data_sorted = data.sort_values(by='Total Harga', ascending=False)
data_sorted.to_excel('penjualan_terurut.xlsx', index=False)
print("\nData telah diurutkan berdasarkan Total Harga dan disimpan di penjualan_terurut.xlsx")
