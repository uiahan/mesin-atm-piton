import modules.utils as utils
import termcolor as tc

def login() :
    print("=" * 80)
    print("🔒 Login Mesin Atm Python".center(80))
    print("Silahkan masukan username dan PIN anda".center(80))
    print("=" * 80)
    username = input(f"{'Username':<50} : ")
    pin = input(f"{'PIN':<50} : ")
    print("=" * 80)
    return username, pin

def logout() :
    utils.clear()
    print("-" * 80)
    print(tc.colored("✅ Logout berhasil".center(80), "green"))   