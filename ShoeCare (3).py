# Penilaian Akhir
import csv
from pwinput import pwinput
from prettytable import PrettyTable


YTTA = '143712228'

def home():
    print('')
    print("=" * 37)
    print("SELAMAT DATANG DI SHOECARE AND REPAIR")
    print("=" * 37)
    print('\nPILIHAN:')
    print('1.Lanjut')
    print('2.Keluar')
    while True:
        try:
            piluser = input('\nPILIHAN: ')
            if piluser == '1':
                tampilanawal()
            elif piluser == '2':
                print('','=' * 24)
                print('👋 SAMPAI BERJUMPA LAGI👋')
                print('','=' * 24)
                raise SystemExit
            else:
                print('\nSILAHKAN MASUKKAN PILIHAN YANG TERSEDIA (1/2)')
        
        except ValueError:
            None
        except KeyboardInterrupt:
            None
    

def tampilanawal():
    while True:
        try:
            print("\nAPAKAH ANDA SUDAH MEMILIKI AKUN ? (Ya/Tidak)")
            pilihanawal = input('(MASUKKAN "0" JIKA INGIN KELUAR) : ')
            pilihanawal_lower = pilihanawal.lower()
            if pilihanawal_lower == "ya":
                login()
                break
            elif pilihanawal_lower == "tidak":
                print('')
                print("SILAHKAN MEMBUAT AKUN TERLEBIH DAHULU")
                print('')
                register()
                break
            
            elif pilihanawal_lower == "0":
                print('\n👋 SEMOGA KITA BERJUMPA LAGI 👋')
                break
            
            elif pilihanawal_lower == YTTA:
                print("\nANDA MEMASUKKAN KODE LOGIN ADMIN\n")
                print("SILAHKAN MASUKKAN USERNAME DAN PASSWORD ADMIN\n")
                print('JIKA ANDA MELAKUKAN KESALAHAN, MASUKKAN "0" UNTUK KEMBALI KE TAMPILAN AWAL')
                loginadmin()
                break

            else:
                print("\nTIDAK VALID, SILAHKAN MASUKKAN YA/TIDAK")
        except:
            break

    raise SystemExit


def register():
        while True:
            try:
                print('')
                print("ANDA MASUK KE HALAMAN PENDAFTARAN AKUN")
                print("SILAHKAN BUAT AKUN DENGAN NAMA DAN PASSWORD")
                print('')
                username = input("MASUKAN USERNAME : ")
                pw = input("MASUKAN PASSWORD : ")
                
                if not username or not pw:
                    print("\nUSERNAME ATAU PASSWORD TIDAK BOLEH KOSONG!")
                else:
                    registerprocess(username, pw)
                    break  

            except KeyboardInterrupt:
                return


def registerprocess(username, pw):
        try:
            with open('dataUser.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == username:
                        print("\nUSERNAME SUDAH DIGUNAKAN, SILAHKAN COBA LAGI")
                        register()  
                    elif row and row[0] == '':
                        print("ERROR, SILAHKAN COBA LAGI")
                        register()  
                        
                    
            with open('dataUser.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, pw])
                print("\nPENDAFTARAN AKUN BERHASIL")

        except Exception as e:
            print(f"Error: {e}")
            return
        
        tampilanawal()

            
def login():
    print("\nSILAHKAN MASUKKAN USERNAME DAN PASSWORD AKUN ANDA")
    print('')
    username = input("MASUKAN USERNAME : ")
    pw = pwinput("MASUKAN PASSWORD : ")
    if not username or not pw:
            print("\nUSERNAME ATAU PASSWORD TIDAK BOLEH KOSONG!")
            login()
    loginprocess(username, pw)

def loginadmin():
    print("\nSILAHKAN MASUKKAN USERNAME DAN PASSWORD AKUN ANDA")
    print('')
    username = input("MASUKAN USERNAME : ")
    if username == "0":
        tampilanawal()
    pw = pwinput("MASUKAN PASSWORD : ")
    loginprocessadmin(username, pw)

def loginprocess(username, pw):
        while True:
            try:
                with open('dataUser.csv', 'r') as file:
                    reader = csv.reader(file)
                    for col in reader:
                        if col and col[0] == username and col[1] == pw:
                            print('\nLOGIN BERHASIL, ANDA DIARAHKAN KE MENU\n')
                            menu()
                            break
            except:
                break
        
            print('\nUSERNAME ATAU PASSWORD ANDA SALAH, SILAHKAN COBA LAGI')
            login()

def loginprocessadmin(username, pw):
    loginberhasil = False
    try:
            with open('AdminData.csv', 'r') as file:
                reader = csv.reader(file)
                for col in reader:
                    if col and col[0] == username and col[1] == pw:
                        print('\nLOGIN BERHASIL SEBAGAI ADMIN, ANDA DIARAHKAN KE MENU ADMIN\n')
                        loginberhasil = True
                        break
    except:
            pass
    if not loginberhasil:
        print('\nUSERNAME ATAU PASSWORD ANDA SALAH, SILAHKAN COBA LAGI')
        loginadmin()

    else:
        menuadmin1()
    
def create():
    tabellayanan()
    print('')
    nama_layanan = input("MASUKAN NAMA LAYANAN YANG INGIN DI TAMBAHKAN : ")
    harga_layanan = input("MASUKAN HARGA LAYANAN YANG INGIN DI TAMBAHKAN : ")
    deskripsi = input("MASUKAN DESKRIPSI LAYANAN YANG INGIN DI TAMBAHKAN : \n")
    print(f"\nLAYANAN {nama_layanan} TELAH BERHASIL DI TAMBAHKAN\n")

    with open('dataLayanan.csv', 'a', newline='') as file:
        fieldnames = ['Nama Layanan', 'Harga', 'Deskripsi']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'Nama Layanan': nama_layanan,
            'Harga': harga_layanan,
            'Deskripsi': deskripsi
        })
    
    menuadmin1()


def tabellayanan():
    try:
        with open("dataLayanan.csv", 'r') as f:
            csvreader = csv.reader(f)
            headers = next(csvreader)
            table = PrettyTable(["Kode Layanan"] + headers)  

            for i, row in enumerate(csvreader, start=1):
                table.add_row([i] + row)


        print("")
        print(table)
    except Exception as e:
        print(f"Error during reading: {e}")


def beli_layanan():
    lanjut = False
    print('\nLAYANAN YANG TERSEDIA DI SHOECARE AND REPAIR\n')
    tabellayanan()

    print('\nPilihan:')
    print('1.Ya')
    print('2.Tidak')
    konfir_user1 = input('\nAPAKAH ANDA INGIN MENGGUNAKAN LAYANAN KAMI? (1/2): ')

    if konfir_user1 == '1':
        lanjut = True
    elif konfir_user1 == '2':
        print('\ANDA DIKEMBALIKAN KE MENU')
    else:
        print('INPUT TIDAK VALID, ANDA DIKEMBALIKAN KE MENU')

    if lanjut == True:
        try:
            pil_user_layanan = int(input('SILAHKAN MASUKKAN KODE LAYANAN YANG INGIN DIGUNAKAN: ')) - 1
        
        except ValueError:
            print('\nERROR, ANDA DIKEMBALIKAN KE MENU')
            menu()
        
        with open('dataLayanan.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if 0 <= pil_user_layanan < len(data):
            nama_layanan = data[pil_user_layanan]["Nama Layanan"]
            harga_layanan = int(data[pil_user_layanan]["Harga"])
            

            print(f"\nAnda memilih layanan {nama_layanan} dengan harga Rp {harga_layanan:,.0f}".replace(',', '.'))

            if harga_layanan > cek_saldo():
                print("Saldo tidak mencukupi untuk membeli layanan ini.")
            else:
                kurangi_saldo(harga_layanan)
                total_harga = invoice(nama_layanan, harga_layanan)  # Dapatkan total_harga dari fungsi invoice
                print("\nPembelian berhasil!")
                print(f"Total Harga: Rp {total_harga:,.0f}".replace(',', '.'))  # Tampilkan total harga
                menu()
                # Tambahkan opsi untuk menampilkan invoice
                # tampilkan_invoice = input("Apakah Anda ingin menampilkan invoice? (Ya/Tidak): ").lower()
                # if tampilkan_invoice == 'ya':
                #     print("\nMenampilkan Invoice:")
                #     print(f"Total Harga: Rp {total_harga:,.0f}".replace(',', '.'))
        else:
            print("KODE LAYANAN TIDAK VALID")
            print('\nANDA DIKEMBALIKAN KE MENU')
            menu()
    else:
        print('\nAnda dikembalikan ke menu')
        menu()
    




def invoice(nama_layanan, harga_layanan):
    invoice_table = PrettyTable(["Item", "Harga"])
    invoice_table.add_row([nama_layanan, f"Rp {harga_layanan:,.0f}".replace(',', '.')])

    total_harga = harga_layanan

    print("\n======== INVOICE ========")
    print(invoice_table)
    print("==============================")

    # Kembalikan total_harga dari fungsi invoice
    return total_harga
# ...




def buat_emoney(saldo_awal=0):
    emoney = {'saldo': saldo_awal}

    def cek_saldo():
        return emoney["saldo"]

    def tambah_saldo():
        while True:
            print('\nJUMLAH NOMINAL TOP UP: ')
            print('1.Rp50.000')
            print('2.Rp100.000')
            print('3.Rp300.000')
            print('4.Rp500.000')
            jumlah = int(input("\nMasukkan pilihan jumlah saldo yang ingin ditambahkan (1/2/3/4): "))
            if jumlah == 1:
                emoney["saldo"] += 50000
                print(f"\nSaldo berhasil ditambahkan sebesar: Rp50.000")
                return

            elif jumlah == 2:
                emoney["saldo"] += 100000
                print(f"\nSaldo berhasil ditambahkan sebesar: Rp100.000")
                return
            
            elif jumlah == 3:
                emoney["saldo"] += 300000
                print(f"\nSaldo berhasil ditambahkan sebesar: Rp300.000")
                return
            
            elif jumlah == 4:
                emoney["saldo"] += 500000
                print(f"\nSaldo berhasil ditambahkan sebesar: Rp500.000")
                return

            else:
                print('\nMASUKKAN PILIHAN YANG TERSEDIA')
            
    def kurangi_saldo(jumlah):
        if jumlah > emoney["saldo"]:
            return "Saldo tidak mencukupi"
        else:
            emoney["saldo"] -= jumlah
            return f"Saldo dikurangi: {jumlah}. Saldo sekarang: {format_rupiah(cek_saldo())}"

    def format_rupiah(angka):
        return f"Rp {angka:,.0f}".replace(',', '.')

    return cek_saldo, tambah_saldo, kurangi_saldo

cek_saldo, tambah_saldo, kurangi_saldo = buat_emoney(0)



    
def infosaldo():
    while True:
        try:
            print(f"Saldo anda sekarang berjumlah:", "Rp", cek_saldo())
            print('')
            print("1. Tambah Saldo")
            print("2. Kembali")
            pil_user_saldo = int(input('\nPilihan: '))
            if pil_user_saldo == 1:
                tambah_saldo()
            elif pil_user_saldo == 2:
                menu()
            else:
                print('\nMASUKKAN PILIHAN YANG TERSEDIA')
        except ValueError:
            print('\nTERJADI KESALAHAN')
            print('\nSILAHKAN MASUKKAN PILIHAN YANG TERSEDIA')
        except Exception as e:
            print('\nTERJADI KESALAHAN')
            print(f'Error: {e}')
            

cek_saldo, tambah_saldo, kurangi_saldo = buat_emoney(0)

    

def read():
    tabellayanan()
    menuadmin1()


def update() :
    while True:
        try:
            print('\nBerikut adalah tampilan layanan sekarang:')
            read()
            kodelayanan_update = int(input('MASUKKAN KODE LAYANAN YANG INGIN DIPERBARUI: ')) 
            updateprocess(kodelayanan_update)
            break
        except:
            print('= * 47')
            print('\n=YANG ANDA MASUKKAN BUKAN KODE LAYANAN (ANGKA)=')
            print('= * 47')


def updateprocess(kodelayanan):
    updatestatus = False
    while True:
            with open('dataLayanan.csv', 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

            if 0 < kodelayanan < len(rows):
                namalayanan_baru = input("Masukkan Nama Layanan baru: ")
                harga_baru = input("Masukkan Harga baru: ")
                deskripsi_baru = input("Masukkan Deskripsi baru: ")

                data_baru = [namalayanan_baru, harga_baru, deskripsi_baru]
                rows[kodelayanan] = data_baru

                with open('dataLayanan.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

                print('')
                print('=' * 27)
                print("LAYANAN BERHASIL DIPERBARUI")
                print('=' * 27)
                updatestatus = True
                break

            else:
                print('')
                print('=' * 28)
                print("KODE LAYANAN TIDAK DITEMUKAN")
                print('=' * 28)
                break

    if updatestatus == True:
            menuadmin1()
    
    else:
        print('\nANDA DIKEMBALIKAN KE MENU ADMIN\n')
        menuadmin1()


def deleteprocess(kodelayanan):
    prosesdel = False
    while True:
            with open('dataLayanan.csv', 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            if 0 <= kodelayanan < len(data):
                data.pop(kodelayanan)
                print('=' * 25)
                print(f"LAYANAN BERHASIL DIHAPUS:")
                print('=' * 25)


                with open('dataLayanan.csv', 'w', newline='') as file:
                    fieldnames = ['Nama Layanan', 'Harga', 'Deskripsi']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)
                    prosesdel = True
                    break

            else:
                print('')
                print('=' * 45)
                print(f"Tidak ada layanan dengan kode yang dimasukkan")
                print('=' * 45)

                break
    if prosesdel == True:
        menuadmin1()
    else:
        print('\nANDA DIKEMBALIKAN KE MENU ADMIN')
        menuadmin1
            

def delete():
    while True:
        try:
            print('\nBerikut adalah tampilan layanan sekarang:')
            read()
            kodelayanan = int(input("Masukkan Kode Layanan yang ingin dihapus: ")) - 1
            deleteprocess(kodelayanan)
        except:
            print("\nYANG ANDA MASUKKAN BUKAN KODE LAYANAN (ANGKA)")
            print("SILAHKAN COBA LAGI")
    

def menuadmin1():
    while True:
        print("PILIHAN MENU : \n")
        print("1. TAMPILKAN LAYANAN YANG TERSEDIA")
        print("2. TAMBAHKAN LAYANAN")
        print("3. HAPUS LAYANAAN")
        print("4. PERBARUI LAYANAN")
        print("5. KELUAR")
        pilmenuadmin = input("\nPILIHAN MENU (1/2/3/4/5): ")
        if pilmenuadmin == '1':
            read()
            break
        elif pilmenuadmin == '2':
            create()
            break
        elif pilmenuadmin == '3':
            delete()
            break
        elif pilmenuadmin == '4':
            update()
            break
        elif pilmenuadmin == '5':
            tampilanawal()
            break
        else:
                print('Silahkan masukkan angka yang tertera dalam pilihan menu')


def menu():
    while True:
        try:
            print("\nPILIHAN MENU : ")
            print('')
            print("1. LAYANAN")
            print("2. INFO SALDO")
            print("3. KELUAR")

            pilmenuuser = int(input('\nPILIHAN MENU (1/2/3): '))
            if pilmenuuser == 1:
                beli_layanan()
                break
            elif pilmenuuser == 2:
                infosaldo()
                break
            elif pilmenuuser == 3:
                home()
                break
            else:
                print('\nTERJADI KESALAHAN')
                print('\nSILAHKAN MASUKKAN PILIHAN MENU YANG TERSEDIA')

        except ValueError:
            print('\nTERJADI KESALAHAN')
            print('\nSILAHKAN MASUKKAN ANGKA YANG VALID')

        except Exception as e:
            print('\nTERJADI KESALAHAN')
            print(f'Error: {e}')
            

home()