import modules.utils as utils
import termcolor as tc

def cek_saldo(nasabah, username) :
    print('-' * 80)
    print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
    print('-' * 80)
    input(tc.colored("Tekan (ENTER) untuk kembali ke menu utama".center(80), 'blue'))
    utils.clear()
    
def setor_saldo(nasabah, username) :
    print("-" * 80)
    while True :
        try :
            print(tc.colored(f"{'Saldo rekening kamu sekarang adalah':<50} : Rp.{nasabah[username]['saldo']}", "green"))
            jumlah_setor = int(input(f"{'Masukan jumlah uang yang ingin disetor':<50} : Rp."))
        except :
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
            utils.clear()
            break
        
def tarik_saldo(nasabah, username) :
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
                utils.clear()
                break
        except :
            print('-' * 80)
            print(tc.colored("Input harus berupa angka❗".center(80), "red"))
            print('-' * 80)
            
def transfer_saldo(nasabah, username) :
    print("-" * 80)
    proses_transfer = True
    while True :
        nomor_rekening = input(f"{'Masukan nomor rekening yang ingin kamu transfer':<50} : ")
        for name, i in nasabah.items() :
            if i.get("nomor_rekening") == nomor_rekening :
                nama_penerima = name
                break
            else :
                nama_penerima = ""
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
                        utils.clear()
                        proses_transfer = False
                        nama_penerima = ""
                        break
                except :
                    print('-' * 80)
                    print(tc.colored("Input harus berupa angka❗".center(80), "red"))
                    print('-' * 80)
        elif nomor_rekening == "batal" :
            utils.clear()
            break
        else :
            print('-' * 80)
            print(tc.colored("Nomor rekening tidak ditemukan❗".center(80), "red"))
            print('-' * 80)
        if proses_transfer == False :
            break             