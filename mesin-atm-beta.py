import os
import termcolor as tc

nasabah = {
    "ahan" : {
        "saldo" : 0,
        "password" : "123"
    }, 
    "dhiya" : {
        "saldo" : 0,
        "password" : "123"
    },
    "azello" : {
        "saldo" : 0,
        "password" : "123"
    },
    "akira" : {
        "saldo" : 0,
        "password" : "123"
    }
}

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

print("\n" + "=" * 80)
print("🔒 Login Mesin Atm Python".center(80))
print("=" * 80)
username = input("Username : ")
password = input("Password : ")

if username not in nasabah :
     print("-" * 80)
     print(tc.colored("❌ Username Belum Terdaftar!".center(80), "red"))
     print("")
else :
    if password == nasabah[username]['password'] :
        clear()
        print("-" * 80)
        print(tc.colored("✅ Login Berhasil!".center(80), "green"))
        
        while True :
            print("\n" + "=" * 80)
            print("💵 Mesin Atm Python".center(80))
            print("Kamu mau ngapain nih, silahkan pilih menu 😁".center(80))
            print("=" * 80)
            print("1. Cek Saldo")
            print("2. Setor Saldo")
            print("3. Tarik Saldo")
            print(tc.colored("4. Logout", "red"))
            nomor_menu = input("\nSilahkan Pilih Menu (1 - 4) : ")
            
            if nomor_menu == "1" :
                print('-' * 80)
                print(tc.colored(f"Saldo rekening kamu sekarang adalah : Rp.{nasabah[username]['saldo']}", "green"))
                print('-' * 80)
                input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                clear()
            elif nomor_menu == "2" :
                print("-" * 80)
                while True :
                    try :
                        print(tc.colored(f"Saldo rekening kamu sekarang adalah : Rp.{nasabah[username]['saldo']}", "green"))
                        jumlah_setor = int(input("Masukan jumlah uang yang ingin disetor : Rp."))
                    except ValueError :
                        print('-' * 80)
                        print(tc.colored("Input harus berupa angka❗".center(80), "red"))
                        print('-' * 80)
                        continue
                    if jumlah_setor <= 0 :
                        print('-' * 80)
                        print(tc.colored("Jumlah uang yang disetor tidak boleh kurang atau sama dengan 0❗".center(80), "red"))
                        print('-' * 80)
                    else :
                        nasabah[username]['saldo'] += jumlah_setor
                        print("-" * 80)
                        print(tc.colored(f"Setor uang sebasar Rp.{jumlah_setor} berhasil! ✅", "green"))
                        print(tc.colored(f"Saldo rekening kamu sekarang adalah : Rp.{nasabah[username]['saldo']}", "green"))
                        print("-" * 80)
                        input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                        clear()
                        break
            elif nomor_menu == "3" :
                print("-" * 80)
                while True :
                    try :
                        print(tc.colored(f"Saldo rekening kamu sekarang adalah : Rp.{nasabah[username]['saldo']}", "green"))
                        jumlah_tarik = int(input("Masukan jumlah yang ingin ditarik : Rp."))
                    except ValueError :
                        print('-' * 80)
                        print(tc.colored("Input harus berupa angka❗".center(80), "red"))
                        print('-' * 80)
                        continue
                    if jumlah_tarik <= 0 :
                        print('-' * 80)
                        print(tc.colored("Jumlah uang yang ditarik tidak boleh kurang atau sama dengan 0❗".center(80), "red"))
                        print('-' * 80)
                    elif jumlah_tarik > nasabah[username]['saldo'] :
                        print('-' * 80)
                        print(tc.colored("Saldo kamu tidak cukup untuk menarik uang sebesar itu❗".center(80), "red"))
                        print('-' * 80)
                    else :
                        nasabah[username]['saldo'] -= jumlah_tarik
                        print("-" * 80)
                        print(tc.colored(f"Tarik uang sebasar Rp.{jumlah_tarik} berhasil! ✅", "green"))
                        print(tc.colored(f"Saldo rekening kamu sekarang adalah : Rp.{nasabah[username]['saldo']}", "green"))
                        print("-" * 80)
                        input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                        clear()
                        break
            elif nomor_menu == "4" :
                clear()
                print("=" * 80)
                print(tc.colored("✅ Logout berhasil".center(80), "green"))
                print("-" * 80)
                print("💵 Mesin Atm Python".center(80))
                print("TERIMAKASIH TELAH MENGGUNAKAN ATM KAMI".center(80))
                print("-" * 80)
                print("")
                break
            else :
                 clear()
                 print('-' * 80)
                 print(tc.colored("Menu itu tidak ada❗".center(80), "red"))
                 print('-' * 80)
      
    else :
        print("-" * 80)
        print("❌ Password Salah!".center(80))
        print("")