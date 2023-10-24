import os

os.system('cls')
inventory = {'Susu': {'price': 10000, 'stock': 10},
             'Roti': {'price': 8000, 'stock': 10},
             'Telur': {'price': 15000, 'stock': 10},
             'Beras': {'price': 20000, 'stock': 10},
             'Sereal': {'price': 12000, 'stock': 10},
             'Apel': {'price': 8000, 'stock': 10},
             'Jus Jeruk': {'price': 13000, 'stock': 10},
             'Pasta': {'price': 7000, 'stock': 10},
             'Kopi bubuk': {'price': 25000, 'stock': 10}, 
             'Mentega': {'price': 10000, 'stock': 10}}
#di atas sini adalah inventory default. dapat ditambah dan dikurang oleh admin

def add_item(item_name, item_price, item_stock): #menambah jenis item, diakses oleh admin
    if item_name not in inventory:
        inventory[item_name] = {'price': item_price, 'stock': item_stock}
        print(f'{item_name} dengan harga Rp. {item_price} telah ditambahkan dengan stok {item_stock}')
    else:
        print(f'{item_name} sudah ada.')
    print()
    dummy_input = input('klik Enter untuk melanjutkan . . .')

def remove_item(item_name): #menghapus jenis item, diakses oleh admin
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} telah dihapus. ")
    else:
        print(f'{item_name} tidak ada.')
    print()
    dummy_input = input('klik Enter untuk melanjutkan . . .')

def add_stock(item_name, quantity): #menambah stok, diakses oleh admin
    if item_name in inventory:
        inventory[item_name]['stock'] += quantity
        print(f"stok {inventory[item_name]} sekarang ada {inventory[item_name]['stock']}")
    else:
        print(f'{item_name} tidak ditemukan.')
    print()
    dummy_input = input('klik Enter untuk melanjutkan . . .')

def subtract_stock(item_name, quantity): #mengurangi stok (sebagai pembelian), diakses oleh employee (pegawai).
    if item_name in inventory:
        if inventory[item_name]['stock'] >= quantity: #hanya mengurangi jika stok lebih besar atau sama dengan kuantitas yg diinput
            inventory[item_name]['stock'] -= quantity
            print(f"Stok {inventory[item_name]} tersisa sebanyak {inventory[item_name]['stock']}")
        else:
            print(f'Stok {item_name} tidak cukup.') #print tidak cukup jika stok kurang dari kuantitas yg dimasukkan
            return False #mengembalikan false, jika stok kurang
    else:
        print(f'{item_name} tidak ada.')
        return False
    print()
    dummy_input = input()

def display_inventory(): #this is to display inventory
    print("List barang:")
    counter = 0
    for item, details in inventory.items():
        print(f"{counter+1}. ", end="")
        print(f"{item}: Harga: Rp{details['price']}, Stok: {details['stock']}")
        counter += 1
    print()
    dummy = (input("Ketik apapun untuk kembali . . ."))

def employee(): #employee function
  while True:
    os.system('cls')
    print()
    print("Selamat Datang di Menu Kasir!") #memilih mode yg dipakai
    print("1. Pembelian Barang")
    print("2. Kembali")
    choice = input("Masukkan pilihan: ")
    if choice == '1':  
      barangdibeli = {} #dictionary barang yang dibeli
      while True:
        item_name = input("Masukkan nama barang: ") 
        quantity = int(input("Masukkan jumlah: "))
        a = subtract_stock(item_name, quantity) #menyimpan true/false yg direturn tetapi tetap melaksanakan print di dalam fungsinya
        if a != False: #kalau a tidak bernilai False.
          if item_name not in barangdibeli:
            barangdibeli[item_name] = {'Harga Total Barang': (inventory[item_name]['price']*quantity), 'Jumlah': quantity}
          else:
            barangdibeli[item_name]['Harga Total Barang'] += (inventory[item_name]['price']*quantity)
            barangdibeli[item_name]['Jumlah'] += quantity
        print('Barang yand dibeli adalah:')
        print(barangdibeli)
        end = input("Akhiri Transaksi? (Y/N): ")
        if end == "Y":
          print('Barang yand dibeli adalah:')
          print(barangdibeli)
          hargatotal = 0
          for item in barangdibeli:
             hargatotal = hargatotal + barangdibeli[item]['Harga Total Barang']
          print(f'Harga Total: {hargatotal}')
          break
    elif choice == '2':  
      break
    else:
      print(("Invalid input!"))

def admin(): #admin function
  while True:
    os.system('cls')
    print()
    print("Selamat Datang di Menu Admin!")
    print("1. Tambah item")
    print("2. Kurangi item")
    print("3. Tambah Stok")
    print("4. Kurangi Stok")
    print("5. List barang")
    print("6. Kembali")
    choice = input("Masukkan pilihan: ")
    if choice == '1':
      item_name = input("Masukkan nama barang: ")
      item_price = int(input("Masukkan harga barang: "))
      item_stock = int(input("Masukkan Jumlah barang: "))
      add_item(item_name, item_price, item_stock)

    elif choice == '2':
      item_name = input("Masukkan nama barang: ")
      remove_item(item_name)

    elif choice == '3':
      item_name = input("Masukkan nama barang: ")
      quantity = int(input("Masukkan jumlah stok: "))
      add_stock(item_name, quantity)

    elif choice == '4':
      item_name = input("Masukkan nama barang: ")
      quantity = int(input("Masukkan jumlah stok: "))
      subtract_stock(item_name, quantity)

    elif choice == '5': #from here, it displays inventory
      display_inventory()

    elif choice == '6':
      break

    else:
      print(("Invalid input!")) 

def main():
  password_admin = "admin" #password admin
  password_employee = "pegawai" #password pegawai
  valid_input = True
  while (True):
    os.system('cls')
    if valid_input == False:
       print("Invalid Input")
    valid_input = True
    print()
    print("Login Menu")
    print("1. Admin [a]")
    print("2. Pegawai [p]")
    print("3. Exit [e]")
    status = input("Masukkan pilihan: ") #mengecek input user mengenai role/mode yang akan dipilih
    if status == 'a': #jika dipilih admin
      while (True): #infinite loop
        password_inp = input("Masukkan password: ") #meminta input password
        if password_inp == password_admin: #mengecek apakah password sudah sesuai dengan 
          break #kalau benar break, lanjut ke tahap berikutnya
        else: #lainnya, password salah, akan mengecek ulang
          print("Password salah!")
      admin() #masuk ke fungsi admin
    elif status == 'p':
      while (True):
        password_inp = input("Masukkan password: ")
        if password_inp == password_employee:
          break
        else:
          print("Password salah!")
      employee()
    elif status == 'e':
      break
    else:
      os.system('cls')
      valid_input = False 

main()




