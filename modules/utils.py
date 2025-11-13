import os
import termcolor as tc

def menu(username) :
    print("=" * 80)
    print("💵 Mesin Atm Python".center(80))
    print(f"Hallo {tc.colored(username, "blue")}, Kamu mau ngapain nih, silahkan pilih menu".center(80))
    print("=" * 80)
    print("1. Cek Saldo")
    print("2. Setor Saldo")
    print("3. Tarik Saldo")
    print("4. Transfer Saldo")
    print(tc.colored("5. Logout", "red"))
    print("-" * 80)
    
def clear() :
    os.system('cls' if os.name == 'nt' else 'clear') 