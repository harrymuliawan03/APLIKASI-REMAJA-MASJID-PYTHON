import PySimpleGUI as sg
import pandas as pd
from openpyxl import Workbook


my_new_theme = {'BACKGROUND': '#2c3e50',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('#ecf0f1', '#16a085'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 5,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('MyNewTheme', my_new_theme)

# Switch your theme to use the newly added one. You can add spaces to make it more readable
sg.theme('My New Theme')


def tambah():

    def clear_input():
        for key in values:
            window_tambah[key]('')
        return None

    def close():
        window_tambah.close()

    EXCEL_FILE = 'excel/saldo_kas.xlsx'

    df = pd.read_excel(EXCEL_FILE)
    saldo = int(df['saldo'].values)

    # function untuk buka layout_tambah
    def layout():
        layout_tambah = [[sg.Text('Tambah Kas', size=(8, 1)), sg.InputText(font='Courier 16 bold', key='tambah_saldo',  text_color='Black', size=(50, 1), expand_y=True)],
                         [sg.Push(), sg.Button('Tambah'), sg.Exit(), sg.Push()]]

        return sg.Window(
            'Saldo Kas', layout_tambah, size=(400, 90), finalize=True)

    window_tambah = layout()

    while True:
        # variabel filter supaya tidak ada huruf / karakter
        filter = 'bisa'
        event_tambah, values = window_tambah.read()
        if event_tambah == sg.WIN_CLOSED or event_tambah == 'Exit':
            close()
            break
        if event_tambah == 'Tambah':
            # perulangan untuk cek apakah ada huruf / karakter
            for char in values['tambah_saldo']:
                if char.isalpha():
                    filter = 'tidak bisa'
                    break
                else:
                    continue
            if (filter == 'tidak bisa'):
                sg.popup('Tidak boleh mengandung huruf / karakter')
            else:
                # simpan no dokumen ke no_dokumen.xlsx
                wb = Workbook()
                ws = wb.active
                # penjumlahan = saldo awal + input kas
                hasil = int(values['tambah_saldo']) + saldo
                header = ['saldo']
                isi = [hasil]
                # proses save ke file saldo_kas
                ws.append(header)
                ws.append(isi)
                wb.save("excel/saldo_kas.xlsx")

                # update saldo kas untuk variabel saldo
                saldo = hasil

                # notifikasi simpan data berhasil
                sg.popup('Data Berhasil Di Simpan')
                clear_input()
                close()
                new_window = layout()
                close()
                window_tambah = new_window
