import os
import termcolor as tc

nasabah = {
    "farhan" : {
        "nomor_rekening" : "123",
        "saldo" : 700000,
        "pin" : "123"
    }, 
    "dika" : {
        "saldo" : 0,
        "nomor_rekening" : "321",
        "pin" : "123"
    },
    "alsani" : {
        "nomor_rekening" : "678",
        "saldo" : 0,
        "pin" : "123"
    }, 
}

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

while True :
    print("\n" + "=" * 80)
    print("🔒 Login Mesin Atm Python".center(80))
    print("Silahkan masukan username dan PIN anda".center(80))
    print("=" * 80)
    username = input(f"{'Username':<50} : ")
    pin = input(f"{'PIN':<50} : ")
    print("=" * 80)

    if username not in nasabah :
        clear()
        print("-" * 80)
        print(tc.colored("❌ Username Belum Terdaftar!".center(80), "red"))
    else :
        if pin == nasabah[username]['pin'] :
            clear()
            print("-" * 80)
            print(tc.colored("✅ Login Berhasil!".center(80), "green"))
            
            while True :
                print("=" * 80)
                print("💵 Mesin Atm Python".center(80))
                print("Kamu mau ngapain nih, silahkan pilih menu 😁".center(80))
                print("=" * 80)
                print("1. Cek Saldo")
                print("2. Setor Saldo")
                print("3. Tarik Saldo")
                print("4. Transfer Saldo")
                print(tc.colored("5. Logout", "red"))
                print("-" * 80)
                nomor_menu = input(f"{'Silahkan Pilih Menu (1 - 5)':<50} : ")
                
                if nomor_menu == "1" :
                    print('-' * 80)
                    print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
                    print('-' * 80)
                    input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                    clear()
                    
                elif nomor_menu == "2" :
                    print("-" * 80)
                    while True :
                        try :
                            print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
                            jumlah_setor = int(input(f"{'Masukan jumlah uang yang ingin disetor':<50} : Rp."))
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
                            print(tc.colored(f"{'Setor uang sebasar':<50} : Rp.{jumlah_setor} berhasil! ✅", "green"))
                            print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
                            print("-" * 80)
                            input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                            clear()
                            break
                        
                elif nomor_menu == "3" :
                    print("-" * 80)
                    while True :
                        try :
                            print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
                            jumlah_tarik = int(input(f"{'Masukan jumlah yang ingin ditarik':<50} : Rp."))
                            
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
                                print(tc.colored(f"{'Tarik uang sebasar':<50} : Rp.{jumlah_tarik} berhasil! ✅", "green"))
                                print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
                                print("-" * 80)
                                input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                                clear()
                                break
                        except ValueError :
                            print('-' * 80)
                            print(tc.colored("Input harus berupa angka❗".center(80), "red"))
                            print('-' * 80)
                        
                elif nomor_menu == "4" :
                    print("-" * 80)
                    proses_transfer = True
                    while True :
                        nomor_rekening = input(f"{'Masukan nomor rekening yang ingin kamu transfer':<50} : ")
                        for name, i in nasabah.items() :
                            if i.get("nomor_rekening") == nomor_rekening :
                                nama_penerima = name
                                break
                        if nama_penerima == username :
                            print('-' * 80)
                            print(tc.colored("Kamu gabisa mentransfer ke rekening kamu sendiri❗".center(80), "red"))
                            print('-' * 80)
                        elif nama_penerima in nasabah :
                            print(f"{'Nama penerima':<50} : {nama_penerima}")
                            print('-' * 80)
                            while True :
                                try :
                                    print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
                                    jumlah_transfer = int(input(f"{'Masukan jumlah uang yang ingin kamu transfer':<50} : Rp."))
                                    if jumlah_transfer > nasabah[username]['saldo'] :
                                        print('-' * 80)
                                        print(tc.colored("Saldo kamu tidak cukup❗".center(80), "red"))
                                        print('-' * 80)
                                    else :
                                        nasabah[nama_penerima]['saldo'] += jumlah_transfer
                                        nasabah[username]['saldo'] -= jumlah_transfer
                                        print('-' * 80)
                                        print(tc.colored(f"{'Transfer sebesar':<50} : Rp.{jumlah_transfer} berhasil ✅", "green"))
                                        print(tc.colored(f"{'Saldo rekening kamu sekarang tersisa':50} : Rp.{nasabah[username]['saldo']}", "green"))
                                        print('-' * 80)
                                        input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
                                        clear()
                                        proses_transfer = False
                                        nama_penerima = ""
                                        break
                                except ValueError :
                                    print('-' * 80)
                                    print(tc.colored("Input harus berupa angka❗".center(80), "red"))
                                    print('-' * 80)
                        else :
                            print('-' * 80)
                            print(tc.colored("Nomor rekening tidak ditemukan❗".center(80), "red"))
                            print('-' * 80)
                        if proses_transfer == False :
                            break
                        
                elif nomor_menu == "5" :
                    clear()
                    print("-" * 80)
                    print(tc.colored("✅ Logout berhasil".center(80), "green"))
                    break
                
                else :
                    clear()
                    print('-' * 80)
                    print(tc.colored("Menu itu tidak ada❗".center(80), "red"))
        else :
            clear()
            print("-" * 80)
            print(tc.colored("❌ PIN Salah!".center(80), "red"))