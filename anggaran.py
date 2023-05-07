# Kode untuk import library yang dibutuhkan
import PySimpleGUI as sg
import pandas as pd
from openpyxl import Workbook

# Function anggaran
def anggaran():
    sg.theme('DarkGreen4')

    # membaca file excel data_anggaran
    EXCEL_FILE = 'excel/data_anggaran.xlsx'
    df = pd.read_excel(EXCEL_FILE)

    # membaca file excel no_anggaran
    EXCEL_FILE2 = 'excel/no_anggaran.xlsx'
    df2 = pd.read_excel(EXCEL_FILE2)

    # membaca file excel saldo_kas
    EXCEL_FILE_SALDO = 'excel/saldo_kas.xlsx'
    df3 = pd.read_excel(EXCEL_FILE_SALDO)
    # Kode untuk membaca saldo kas saat ini
    saldo = int(df3['saldo'].values)

    # Kode untuk membaca no anggaran saat ini kemudian ditambah 1
    no_anggaran = int(df2['no anggaran'].values) + 1

    # Function untuk layout anggaran yang didalamnya ada parameter (no_anggaran) 
    def layout(no_anggaran):
        layout = [
            [sg.Text('Masukan Data Anggaran')],
            [sg.Text(f'No Anggaran {no_anggaran}')],
            [sg.Text('Jenis Anggaran', size=(15, 1)), sg.InputText(key='jenis')
             ],
            [sg.Text('Detail Anggaran', size=(15, 2)),
             sg.Multiline(key='detail', size=(45, 1), expand_y=True)],
            [sg.Text('Tgl (dd/mm/yyy)', size=(15, 1)),
             sg.InputText(key='tgl')],
            [sg.Text('Biaya Anggaran', size=(15, 1)),
             sg.InputText(key='biaya')],
            [sg.Push()],
            [sg.Push(), sg.Submit(), sg.Button('Clear'), sg.Exit(), sg.Push()]
        ]
        return sg.Window('Form Data Anggaran', layout, finalize=True)

    # Inisialisasi layout anggaran ke variabel window_anggaram
    window_anggaran = layout(no_anggaran)


    def clear_input():
        for key in values:
            if (key == 'no anggaran'):
                break
            else:
                window_anggaran[key]('')
        return None

    def close():
        window_anggaran.close()

    def prog_bar():
        layout_progress = [[sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
                           [sg.Cancel()]]
        window_progress = sg.Window('Loading', layout_progress)
        progress_bar = window_progress['progressbar']
        for i in range(500):
            # check to see if the cancel button was clicked and exit loop if clicked
            event_prog, values = window_progress.read(timeout=1)
            global cancel
            cancel = ''
            if event_prog == 'Cancel' or event_prog == sg.WIN_CLOSED:
                cancel = 'cancel'
                break
            # update bar with loop value +1 so that bar eventually reaches the maximum
            progress_bar.UpdateBar(i + 100)
        window_progress.close()

    while True:
        global values
        event_anggaran, values = window_anggaran.read()
        if event_anggaran == sg.WIN_CLOSED or event_anggaran == 'Exit':
            window_anggaran.close()
            break
        if event_anggaran == 'Clear':
            clear_input()
        if event_anggaran == 'Submit':

            # loading proses save data
            prog_bar()
            if cancel == 'cancel':
                continue
            # simpan values inputan user
            else:
                biaya = int(values['biaya'])
                if (biaya > saldo):
                    sg.popup('Biaya Anggaran melebihi saldo Kas')
                else:
                    values['no anggaran'] = [no_anggaran]
                    df_new_row = pd.DataFrame(values, index=[0])
                    df = pd.concat([df, df_new_row])
                    df.to_excel(EXCEL_FILE, index=False)

                    # simpan no anggaran ke no_anggaran.xlsx
                    wb = Workbook()
                    ws = wb.active
                    header = ['no anggaran']
                    no = [no_anggaran]
                    ws.append(header)
                    ws.append(no)
                    wb.save("excel/no_anggaran.xlsx")

                    # simpan no dokumen ke no_dokumen.xlsx

                    wb2 = Workbook()
                    ws2 = wb2.active
                    # penjumlahan = saldo awal + input kas
                    update_saldo = saldo - biaya
                    header = ['saldo']
                    isi = [update_saldo]
                    # proses save ke file saldo_kas
                    ws2.append(header)
                    ws2.append(isi)
                    wb2.save("excel/saldo_kas.xlsx")

                    # update saldo kas untuk variabel saldo
                    saldo = update_saldo

                    # increment untuk no anggaran
                    no_anggaran += 1

                    # notifikasi simpan data berhasil
                    sg.popup('Data Berhasil Di Simpan')
                    clear_input()
                    close()
                    new_window = layout(no_anggaran)
                    close()
                    window_anggaran = new_window
