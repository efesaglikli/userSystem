from user_data import *

def print_menu():
    print("""
    1-Giriş Yap
    2-Kaydol
    3-Kapat
    """)

def login_menu():
    print(f"""
    1-Kullanıcı arama
    2-Tüm kullanıcıları yazdır
    3-Hesabımı sil
    4-Çıkış yap
    """)


create_table()


while True:
    print_menu()

    secim = input("Seçim:")

    if secim == "1":
        username = input("Kullanıcı adı:")
        search = search_username(username)
        
        if search == None:
            print("Böyle bir kullanıcı yok!")
            continue

        while True:
            password = input("Şifre:")
            if password == search[4]:
                while True:
                    login_menu()
                    secim = input("Seçim:")
                    if secim == "1":
                        u = input("Kullanıcı adı:")
                        birisi = search_username(u)
                        if birisi == None:
                            print("Bu isimde bir kullanıcı yok")
                            continue
                        print(f"{birisi[1]} {birisi[2]} {birisi[3]}")
            
                    if secim == "2":
                        print_all()
                    if secim == "3":
                        delete_account(username)
                        break
                    if secim == "4":
                        break
                break
            else:
                print("Şifre yanlış, tekrar deneyin.")
                continue          

    if secim == "2":
        name = input("Adınız:")
        lastname = input("Soyadınız:")
        username = input("Kullanıcı adınız:")
        password = input("Şifreniz:")
        search = search_username(username)

        if search != None:
            print("Bu kullanıcı adı alınmış")
            continue
        else:
            insert(name, lastname, username, password)
            print("Kayıt başarılı")

    if secim == "3":
        break