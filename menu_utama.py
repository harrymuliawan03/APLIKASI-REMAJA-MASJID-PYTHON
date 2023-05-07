
import PySimpleGUI as sg
from saldo import *
from tambah import *
from anggaran import *
from riwayat_anggaran import *

# kode untuk tema program : background, warna, dan lainnya
my_new_theme = {'BACKGROUND': '#2c3e50',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('#ecf0f1', '#16a085'),
                'PROGRESS': ('      #01826B', '#D0D0D0'),
                'BORDER': 5,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Menambahkan tema ke pysimplegui object
sg.theme_add_new('MyNewTheme', my_new_theme)

# Ganti tema untuk menggunakan tema yang baru ditambahkan. (bisa menggunakan spasi supaya lebih mudah dibaca)
sg.theme('My New Theme')


# Function untuk menu layout utama
def layout_utama():
    l_menu_utama = [
        [sg.Push(), sg.Image(r'logo1.png'), sg.Push()],
        [sg.Push(), sg.Text('Remaja Masjid Baiturrahman',
                            font='Courier 16 italic bold'), sg.Push()],
        [sg.Push(), sg.Button('Saldo Kas', size=(15, 3), key='-saldo-'), sg.Button('Tambah Kas', size=(
            15, 3), key='-tambah-'), sg.Push()],
        [sg.Push(), sg.Button('Anggaran Kas', size=(15, 3), key='-anggaran_kas-'), sg.Button('Riwayat Anggaran', size=(
            15, 3), key='-riwayat_anggaran-'), sg.Push()],
        [sg.VPush()]
    ]
    return sg.Window('Menu Utama', l_menu_utama, size=(
        500, 400), element_justification='c')


# Function untuk menutup layout menu utama
def close():
    window_utama.close()


# Inisialisasi layout utama ke variabel window_utama
window_utama = layout_utama()

# Ketika kondisi true maka variabel window_utama akan dibaca / read()
while True:
    event, values = window_utama.read()

    # Jika user mengeklik exit / window close maka program berhenti
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Jika user mengeklik saldo maka akan tampil layout saldo
    if event == '-saldo-':
        saldo()
        close()
        new_window = layout_utama()
        close()
        window_utama = new_window

    # Jika user mengeklik tambah maka akan tampil layout tambah saldo
    if event == '-tambah-':
        tambah()
        close()
        new_window = layout_utama()
        close()
        window_utama = new_window

    # Jika user mengeklik anggaran kas maka akan tampil layout anggaran kas
    if event == '-anggaran_kas-':
        anggaran()
        close()
        new_window = layout_utama()
        close()
        window_utama = new_window

    # Jika user mengeklik riwayat anggaran maka akan tampil layout riwayat anggaran
    if event == '-riwayat_anggaran-':
        riwayat_anggaran()
        close()
        new_window = layout_utama()
        close()
        window_utama = new_window
