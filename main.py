import modules.utils as utils
import termcolor as tc
import modules.auth as auth
import modules.transaction as transaction
from modules.data import nasabah

while True :
    username, pin = auth.login()
    if username not in nasabah :
        utils.clear()
        print("-" * 80)
        print(tc.colored("❌ Username Belum Terdaftar!".center(80), "red"))
    else :
        if pin == nasabah[username]['pin'] :
            utils.clear()
            print("-" * 80)
            print(tc.colored("✅ Login Berhasil!".center(80), "green"))
            while True :
                utils.menu(username)
                nomor_menu = input(f"{'Silahkan Pilih Menu (1 - 5)':<50} : ")
                if nomor_menu == "1" :
                    transaction.cek_saldo(nasabah, username)
                elif nomor_menu == "2" :
                    transaction.setor_saldo(nasabah, username)
                elif nomor_menu == "3" :
                    transaction.tarik_saldo(nasabah, username)
                elif nomor_menu == "4" :
                    transaction.transfer_saldo(nasabah, username)
                elif nomor_menu == "5" :
                    auth.logout()
                    break
                else :
                    utils.clear()
                    print('-' * 80)
                    print(tc.colored("Menu itu tidak ada❗".center(80), "red"))
        else :
            utils.clear()
            print("-" * 80)
            print(tc.colored("❌ PIN Salah!".center(80), "red"))