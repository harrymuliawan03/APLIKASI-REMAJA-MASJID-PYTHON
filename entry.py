import PySimpleGUI as sg
import pandas as pd
from openpyxl import Workbook


def entry():
    sg.theme('DarkGreen4')

    EXCEL_FILE = 'data_pasien.xlsx'
    df = pd.read_excel(EXCEL_FILE)

    EXCEL_FILE2 = 'no_dokumen.xlsx'
    df2 = pd.read_excel(EXCEL_FILE2)

    no_dokumen = int(df2['no dokumen'].values) + 1

    def layout(no_dokumen):
        layout = [
            [sg.Text('Masukan Data Pasien')],
            [sg.Text(f'No Dokumen {no_dokumen}')],
            [sg.Text('Nama', size=(15, 1)), sg.InputText(key='Nama')
             ],
            [sg.Text('No KTP', size=(15, 1)), sg.InputText(key='Ktp')],
            [sg.Text('No BPJS', size=(15, 1)), sg.InputText(key='Bpjs')],
            [sg.Text('No Tlp', size=(15, 1)), sg.InputText(key='Tlp')],
            [sg.Text('Alamat', size=(15, 1)), sg.Multiline(key='Alamat')],
            [sg.Text('Tgl Lahir(dd/mm/yyy)', size=(15, 1)),
             sg.InputText(key='Tgl Lahir')],
            [sg.Text('Jenis Kelamin', size=(15, 1)),
             sg.Combo(['pria', 'wanita'], key='Jekel')],
            [sg.Submit(), sg.Button('Clear'), sg.Exit()]
        ]
        return sg.Window('Form Data Pasien', layout, finalize=True)

    window_entry = layout(no_dokumen)

    def clear_input():
        for key in values:
            print(key)
            if (key == 'no dokumen'):
                break
            else:
                window_entry[key]('')
        return None

    def close():
        window_entry.close()

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
        event_entry, values = window_entry.read()
        if event_entry == sg.WIN_CLOSED or event_entry == 'Exit':
            window_entry.close()
            break
        if event_entry == 'Clear':
            clear_input()
        if event_entry == 'Submit':

            # loading proses save data
            prog_bar()
            if cancel == 'cancel':
                continue
            # simpan values inputan user
            else:
                values['no dokumen'] = [no_dokumen]
                df_new_row = pd.DataFrame(values, index=[0])
                df = pd.concat([df, df_new_row])
                df.to_excel(EXCEL_FILE, index=False)

                # simpan no dokumen ke no_dokumen.xlsx
                wb = Workbook()
                ws = wb.active
                header = ['no dokumen']
                no = [no_dokumen]
                ws.append(header)
                ws.append(no)
                wb.save("no_dokumen.xlsx")

                # increment untuk no dokumen
                no_dokumen += 1

                # notifikasi simpan data berhasil
                sg.popup('Data Berhasil Di Simpan')
                clear_input()
                close()
                new_window = layout(no_dokumen)
                close()
                window_entry = new_window