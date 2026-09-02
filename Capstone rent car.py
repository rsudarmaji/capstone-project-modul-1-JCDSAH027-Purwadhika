
from datetime import date, timedelta

car_database = [
    {
        'id_car': 'CTA001',
        'car_brand': 'Toyota',
        'car_type': 'Avanza',
        'car_year': 2023,
        'rent_rate': 550000,
        'passenger': 6,
        'with_driver': False
    },
    {
        'id_car': 'CTA002',
        'car_brand': 'Toyota',
        'car_type': 'Avanza',
        'car_year': 2025,
        'rent_rate': 550000,
        'passenger': 6,
        'with_driver': False
    },
    {
        'id_car': 'CTA003',
        'car_brand': 'Toyota',
        'car_type': 'Avanza',
        'car_year': 2026,
        'rent_rate': 600000,
        'passenger': 6,
        'with_driver': False
    },
    {
        'id_car': 'CTI001',
        'car_brand': 'Toyota',
        'car_type': 'Innova',
        'car_year': 2024,
        'rent_rate': 750000,
        'passenger': 6,
        'with_driver': False
    },
    {
        'id_car': 'CTI002',
        'car_brand': 'Toyota',
        'car_type': 'Innova Zenix',
        'car_year': 2025,
        'rent_rate': 850000,
        'passenger': 6,
        'with_driver': False
    },
    {
        'id_car': 'CTI003',
        'car_brand': 'Toyota',
        'car_type': 'Innova',
        'car_year': 2024,
        'rent_rate': 750000,
        'passenger': 6,
        'with_driver': False
    },
    {
        'id_car': 'CTH001',
        'car_brand': 'Toyota',
        'car_type': 'Hiace',
        'car_year': 2025,
        'rent_rate': 1200000,
        'passenger': 10,
        'with_driver': True
    },
    {
        'id_car': 'CTH002',
        'car_brand': 'Toyota',
        'car_type': 'Hiace',
        'car_year': 2026,
        'rent_rate': 1400000,
        'passenger': 10,
        'with_driver': True
    },
    {
        'id_car': 'CTAL001',
        'car_brand': 'Toyota',
        'car_type': 'Alphard',
        'car_year': 2024,
        'rent_rate': 1500000,
        'passenger': 6,
        'with_driver': True
    },
    {
        'id_car': 'CTAL002',
        'car_brand': 'Toyota',
        'car_type': 'Alphard',
        'car_year': 2026,
        'rent_rate': 1800000,
        'passenger': 6,
        'with_driver': True
    }
]

rented_car_database = []

admin_username = "adminrent"
password_admin = "1234abcd"
login_attemp = 3

def header_table():
    print("=" * 95)
    print(
        f"{'No':<5} "
        f"{'ID':<10} "
        f"{'Brand':<10} "
        f"{'Type':<15} "
        f"{'Year':<8} "
        f"{'Passenger':<12} "
        f"{'Rate':<15}"
    )

    print("=" * 95)

def footer_table():
    print("=" * 95)

def show_cars(cars):
    header_table()
    for no, car in enumerate(cars, start=1):
        print(
            f"{no:<5} "
            f"{car['id_car']:<10} "
            f"{car['car_brand']:<10} "
            f"{car['car_type']:<15} "
            f"{car['car_year']:<8} "
            f"{car['passenger']:<12} "
            f"Rp{car['rent_rate']:,}"
        )
    footer_table()


def customer_car_menu(with_driver):
    available_cars = []
    for car in car_database:
        if car['with_driver'] == with_driver:
            available_cars.append(car)

    if len(available_cars) == 0:
        print("\nMaaf, tidak ada unit yang tersedia.")
        return

    print("\nUnit yang tersedia:")

    show_cars(available_cars[:5])

    if len(available_cars) > 5:
        print("\n0. Lihat lebih lengkap")
        choice = input(
            "\nMasukkan nomor unit yang ingin disewa "
            "atau 0 untuk melihat semua unit: "
        )

        if choice == '0':
            print("\n")
            print("=== SELURUH UNIT YANG TERSEDIA ===")
            show_cars(available_cars)

            choice = input(
                "\nMasukkan nomor unit yang ingin disewa: "
            )

    else:
        choice = input(
            "\nMasukkan nomor unit yang ingin disewa: "
        )

    try:
        choice = int(choice)
        if choice < 1 or choice > len(available_cars):
            print("\nNomor unit tidak tersedia.")
            return

    except ValueError:
        print("\nMasukkan nomor unit berupa angka.")
        return

    selected_car = available_cars[choice - 1]

    while True:
        try:
            rent_days = int(input("\nBerapa hari ingin menyewa unit ini? "))

            if rent_days <= 0:
                print("Jumlah hari harus lebih dari 0")

            else:
                break

        except ValueError:
            print("Masukkan jumlah hari dalam angka.")

    total_price = (selected_car['rent_rate'] * rent_days)

    print("\n")
    print("=" * 80)
    print("                 DETAIL UNIT YANG DIPILIH")
    print("=" * 80)
    print(
        f"ID Unit       : "
        f"{selected_car['id_car']}"
    )
    print(
        f"Brand         : "
        f"{selected_car['car_brand']}"
    )
    print(
        f"Tipe          : "
        f"{selected_car['car_type']}"
    )
    print(
        f"Tahun         : "
        f"{selected_car['car_year']}"
    )
    print(
        f"Jumlah Kursi  : "
        f"{selected_car['passenger']} orang"
    )
    print(
        f"Harga / Hari  : "
        f"Rp{selected_car['rent_rate']:,}"
    )
    print(
        f"Lama Sewa     : "
        f"{rent_days} hari"
    )

    print("-" * 80)

    print(
        f"Harga Sewa    : "
        f"Rp{selected_car['rent_rate']:,} "
        f"x {rent_days} hari"
    )

    print(
        f"TOTAL         : "
        f"Rp{total_price:,}"
    )

    print("=" * 80)

    while True:
        print("""
Apakah anda yakin akan menyewa unit ini?

1. Ya
2. Tidak
""")
        confirmation = input(
            "Masukkan pilihan anda (1/2): "
        )

        if confirmation == '1':
            selected_car['rent_days'] = rent_days
            selected_car['total_price'] = total_price

            car_database.remove(selected_car)

            rented_car_database.append(selected_car)

            print("\n")
            print("=" * 80)
            print("              UNIT BERHASIL DISEWA")
            print("=" * 80)
            print(
                f"ID                : {selected_car['id_car']}\n"
                f"Brand             : {selected_car['car_brand']}\n"
                f"Type              : {selected_car['car_type']}\n"
                f"Year              : {selected_car['car_year']}\n"
                f"Lama sewa         : {rent_days} hari\n"
                f"Harga per hari    : Rp{selected_car['rent_rate']:,}\n"
                f"Total pembayaran  : Rp{total_price:,}"
            )
            print("=" * 80)
            return

        elif confirmation == '2':
            print("\nPenyewaan dibatalkan.")
            return
        
        else:
            print("\nMasukkan pilihan yang benar (1/2)")


def admin_login():
    attempts = 0
    while attempts < login_attemp:
        print("\n")
        print("=" * 50)
        print("              ADMIN LOGIN")
        print("=" * 50)

        username = input("Username : ")
        password = input("Password : ")

        if (
            username == admin_username
            and
            password == password_admin
        ):
            print("\nLogin berhasil.")
            print("Selamat datang, Admin!")
            return True
        else:
            attempts += 1
            print("\nUsername atau password salah.")
            print(
                f"Sisa percobaan login: "
                f"{login_attemp - attempts}"
            )

    print("\n")
    print("=" * 50)
    print("Login gagal 3 kali.")
    print("Anda akan kembali ke menu awal.")
    print("=" * 50)
    return False

def admin_create():
    print("\n")
    print("=" * 50)
    print("             CREATE UNIT BARU")
    print("=" * 50)

    id_car = input("ID Unit              : ")

    all_cars = (car_database + rented_car_database)
    for car in all_cars:
        if car['id_car'] == id_car:
            print("\nID unit sudah digunakan.")
            return

    car_brand = input("Brand                : ")
    car_type = input("Tipe                 : ")

    while True:
        try:
            car_year = int(input("Tahun                : "))
            if car_year <= 0:
                print("Tahun tidak valid.")
            else:
                break
        except ValueError:
            print("Tahun harus berupa angka")

    while True:
        try:
            rent_rate = int(input("Harga sewa per hari  : "))
            if rent_rate <= 0:
                print("Harga harus lebih dari 0")
            else:
                break
        except ValueError:
            print("Harga harus berupa angka")

    while True:
        try:
            passenger = int(input("Jumlah penumpang     : "))
            if passenger <= 0:
                print("Jumlah penumpang harus lebih dari 0")
            else:
                break
        except ValueError:
            print("Jumlah penumpang harus berupa angka")

    while True:
        with_driver_input = input("Dengan driver? (y/n) : ").lower()
        if with_driver_input == 'y':
            with_driver = True
            break
        elif with_driver_input == 'n':
            with_driver = False
            break
        else:
            print("Masukkan y atau n")

    new_car = {
        'id_car': id_car,
        'car_brand': car_brand,
        'car_type': car_type,
        'car_year': car_year,
        'rent_rate': rent_rate,
        'passenger': passenger,
        'with_driver': with_driver

    }

    car_database.append(new_car)
    print("\nUnit berhasil ditambahkan")

def admin_read():
    while True:
        print("\n")
        print("=" * 50)
        print("              READ DATABASE")
        print("=" * 50)
        print("""
1. Lihat unit yang tersedia
2. Lihat unit yang sedang disewa
3. Lihat seluruh unit
4. Kembali
""")
        choice = input("Masukkan pilihan (1/2/3/4): ")
        if choice == '1':
            print("\n=== UNIT YANG MASIH TERSEDIA ===")
            if len(car_database) == 0:
                print("Tidak ada unit yang tersedia.")
            else:
                show_cars(car_database)

        elif choice == '2':
            print("\n=== UNIT YANG SEDANG DISEWA ===")
            if len(rented_car_database) == 0:
                print("Belum ada unit yang sedang disewa.")
            else:
                show_cars(rented_car_database)
                print("\nDetail penyewaan:")
                for car in rented_car_database:
                    print(
                        f"ID Unit      : "
                        f"{car['id_car']}"
                    )

                    print(
                        f"Lama Sewa    : "
                        f"{car['rent_days']} hari"
                    )

                    print(
                        f"Total Harga  : "
                        f"Rp{car['total_price']:,}"
                    )

                    print("-" * 50)

        elif choice == '3':
            print("\n=== SELURUH UNIT ===")

            all_cars = (car_database + rented_car_database)

            if len(all_cars) == 0:
                print("Database unit kosong")
            else:
                show_cars(all_cars)

        elif choice == '4':
            return

        else:

            print("Masukkan pilihan yang benar (1/2/3/4).")

def admin_update():
    print("\n")
    print("=" * 50)
    print("             UPDATE HARGA UNIT")
    print("=" * 50)

    if len(car_database) == 0:
        print("\nTidak ada unit yang tersedia.")
        return

    show_cars(car_database)

    try:
        choice = int(input("\nMasukkan nomor unit yang ingin di update: "))
    except ValueError:
        print("\nMasukkan nomor berupa angka.")
        return

    if choice < 1 or choice > len(car_database):
        print("\nNomor unit tidak ditemukan.")
        return

    selected_car = car_database[choice - 1]
    print("\nUnit yang dipilih:")
    print(
        f"ID Unit      : "
        f"{selected_car['id_car']}"
    )
    print(
        f"Brand        : "
        f"{selected_car['car_brand']}"
    )
    print(
        f"Tipe         : "
        f"{selected_car['car_type']}"
    )
    print(
        f"Harga Lama   : "
        f"Rp{selected_car['rent_rate']:,}"
    )

    while True:
        try:
            new_rate = int(input("\nMasukkan harga baru : "))
            if new_rate <= 0:
                print("Harga harus lebih dari 0")
            else:
                break
        except ValueError:
            print("Harga harus berupa angka")

    selected_car['rent_rate'] = new_rate

    print("\nHarga unit berhasil di-update.")
    print(
        f"Harga baru : "
        f"Rp{new_rate:,}"
    )

def admin_delete():
    print("\n")
    print("=" * 50)
    print("              DELETE UNIT")
    print("=" * 50)

    if len(car_database) == 0:
        print("\nTidak ada unit yang tersedia")
        return

    show_cars(car_database)

    try:
        choice = int(input("\nMasukkan nomor unit yang ingin dihapus: "))
    except ValueError:
        print("\nMasukkan nomor berupa angka")
        return

    if choice < 1 or choice > len(car_database):
        print("\nNomor unit tidak ditemukan")
        return

    selected_car = car_database[choice - 1]

    print("\nUnit yang akan dihapus:")
    print(
        f"ID Unit      : "
        f"{selected_car['id_car']}"
    )
    print(
        f"Brand        : "
        f"{selected_car['car_brand']}"
    )
    print(
        f"Tipe         : "
        f"{selected_car['car_type']}"
    )
    print(
        f"Tahun        : "
        f"{selected_car['car_year']}"
    )

    while True:
        confirmation = input("\nYakin ingin menghapus unit ini? (y/n): ").lower()
        if confirmation == 'y':
            car_database.remove(selected_car)
            print("\nUnit berhasil dihapus.")
            break
        elif confirmation == 'n':
            print("\nPenghapusan dibatalkan")
            break
        else:
            print("Masukkan y atau n.")

def admin_menu():
    while True:
        print("\n")
        print("=" * 50)
        print("                ADMIN MENU")
        print("=" * 50)
        print("""
1. Tambah unit
2. Lihat database
3. Update harga unit
4. Hapus unit
5. Kembali
""")
        
        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == '1':
            admin_create()

        elif choice == '2':
            admin_read()

        elif choice == '3':
            admin_update()

        elif choice == '4':
            admin_delete()

        elif choice == '5':
            return

        else:
            print("\nMasukkan pilihan yang benar (1/2/3/4/5).")

while True:
    print("\n")
    print("=" * 50)
    print("       WELCOME TO TOYOTA LOVER'S RENT")
    print("=" * 50)
    print("""
    Masuk sebagai:

    1. Customer
    2. Admin
    3. Keluar
    """)

    try:
        input_login = int(input("Masuk sebagai (1/2/3): "))
    except ValueError:
        print("Masukkan angka 1, 2, atau 3.")
        continue

    if input_login == 1:
        print("\n")
        print("=" * 50)
        print("              CUSTOMER MENU")
        print("=" * 50)
        print("""
        1. Unit tersedia dengan driver
        2. Unit tersedia lepas kunci
        """)
        try:
            input_car_driver = int(input("Masukkan pilihan anda (1/2): "))
        except ValueError:
            print("Masukkan angka 1 atau 2.")
            continue

        if input_car_driver == 1:
            print("\n=== UNIT TERSEDIA DENGAN DRIVER ===")
            customer_car_menu(True)
        elif input_car_driver == 2:
            print("\n=== UNIT TERSEDIA LEPAS KUNCI ===")
            customer_car_menu(False)
        else:
            print("Masukkan input yang benar (1/2).")

    elif input_login == 2:
        if admin_login():
            admin_menu()

    elif input_login == 3:
        print("\nTerima kasih telah menggunakan Toyota Lover's Rent.")
        break

    else:
        print("\nMasukkan input yang benar (1/2/3)")
