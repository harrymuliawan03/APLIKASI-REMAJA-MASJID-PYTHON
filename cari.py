import PySimpleGUI as sg
import pandas as pd
from datetime import date
import math


def hasil_cari(nama, ktp, bpjs, tlp, alamat, tgl_lahir, jekel, no_dok):
    sg.theme('DarkGreen4')

    EXCEL_FILE = 'data_pasien.xlsx'
    EXCEL_FILE_PENGOBATAN = 'data_pengobatan.xlsx'

    df = pd.read_excel(EXCEL_FILE)
    df2 = pd.read_excel(EXCEL_FILE_PENGOBATAN)
    layout_hasil = [
        [sg.Text('Cari Data')],
        [sg.Text('No. BPJS / Ktp', size=(15, 1)), sg.Input(key="-cari-")],
        [sg.Push(), sg.Button('Cari'), sg.Exit(), sg.Push()],
        [sg.Text('No Dokumen', size=(15, 1)), sg.InputText(
            default_text=int(no_dok), disabled=True, text_color='Black')],
        [sg.Text('Nama', size=(15, 1)), sg.InputText(
            default_text=nama, disabled=True, text_color='Black')],
        [sg.Text('KTP', size=(15, 1)), sg.InputText(
            default_text=int(ktp), disabled=True, text_color='Black')],
        [sg.Text('BPJS', size=(15, 1)), sg.InputText(
            default_text=int(bpjs), disabled=True, text_color='Black')],
        [sg.Text('Telp', size=(15, 1)), sg.InputText(
            default_text=int(tlp), disabled=True, text_color='Black')],
        [sg.Text('Alamat', size=(15, 1)), sg.InputText(
            default_text=alamat, disabled=True, text_color='Black')],
        [sg.Text('Tgl_lahir', size=(15, 1)), sg.InputText(
            default_text=tgl_lahir, disabled=True, text_color='Black')],
        [sg.Text('Jekel', size=(15, 1)), sg.InputText(
            default_text=jekel, disabled=True, text_color='Black')]
    ]
    window_hasil = sg.Window('Cari Data Pasien', layout_hasil, finalize=True)
    while True:
        event_hasil, values = window_hasil.read()
        if event_hasil == sg.WIN_CLOSED or event_hasil == 'Exit':
            window_hasil.close()
            break
        if event_hasil == 'Cari':
            cek = df['Ktp'].where(df['Ktp'] == int(values["-cari-"]))
            hasil_ktp = -1
            for i in range(len(cek)):
                if (math.isnan(cek[i]) == True):
                    continue
                elif (math.isnan(cek[i]) == False):
                    hasil_ktp = i
                    break
            if (hasil_ktp >= 0):
                nama = df['Nama'].where(df['Ktp'] == int(values["-cari-"]))
                ktp = df['Ktp'].where(df['Ktp'] == int(values["-cari-"]))
                bpjs = df['Bpjs'].where(df['Ktp'] == int(values["-cari-"]))
                tlp = df['Tlp'].where(df['Ktp'] == int(values["-cari-"]))
                alamat = df['Alamat'].where(df['Ktp'] == int(values["-cari-"]))
                tgll = df['Tgl Lahir'].where(
                    df['Ktp'] == int(values["-cari-"]))
                jekel = df['Jekel'].where(df['Ktp'] == int(values["-cari-"]))
                no = df['no dokumen'].where(df['Ktp'] == int(values["-cari-"]))
                tanggal = date.today()
                dict = {"Nama": nama[hasil_ktp],
                        "Ktp": int(ktp[hasil_ktp]),
                        "Bpjs": int(bpjs[hasil_ktp]),
                        "Tlp": int(tlp[hasil_ktp]),
                        "Alamat": alamat[hasil_ktp],
                        "Tgl Lahir": tgll[hasil_ktp],
                        "Jekel": jekel[hasil_ktp],
                        "no dokumen": int(no[hasil_ktp]),
                        "Tanggal Berobat": tanggal}
                window_hasil.close()
                hasil_cari(nama[hasil_ktp], ktp[hasil_ktp], bpjs[hasil_ktp], tlp[hasil_ktp],
                             alamat[hasil_ktp], tgll[hasil_ktp], jekel[hasil_ktp], no[hasil_ktp])
            else:
                sg.popup('Data Tidak Ditemukan !')


def cari():
    sg.theme('DarkGreen4')

    EXCEL_FILE = 'data_pasien.xlsx'
    EXCEL_FILE_PENGOBATAN = 'data_pengobatan.xlsx'

    df = pd.read_excel(EXCEL_FILE)
    df2 = pd.read_excel(EXCEL_FILE_PENGOBATAN)

    layout_cari = [
        [sg.Text('Cari Data')],
        [sg.Text('No. BPJS / Ktp', size=(15, 1)), sg.Input(key="-cari-")],
        [sg.Push(), sg.Button('Cari'), sg.Exit(), sg.Push()],
        [sg.Text('No Dokumen', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('Nama', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('KTP', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('BPJS', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('Telp', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('Alamat', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('Tgl_lahir', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')],
        [sg.Text('Jekel', size=(15, 1)), sg.InputText(
            disabled=True, text_color='Black')]
    ]
    window_cari = sg.Window('Form Data Pembayaran Iuran',
                            layout_cari, element_justification='c')

    while True:
        event_cari, values = window_cari.read()
        if event_cari == sg.WIN_CLOSED or event_cari == 'Exit':
            window_cari.close()
            break
        if event_cari == 'Cari':
            cek = df['Ktp'].where(df['Ktp'] == int(values["-cari-"]))
            nan = float("NaN")
            hasil_ktp = -1
            for i in range(len(cek)):
                if (math.isnan(cek[i]) == True):
                    continue
                elif (math.isnan(cek[i]) == False):
                    hasil_ktp = i
                    break
            if (hasil_ktp >= 0):
                nama = df['Nama'].where(df['Ktp'] == int(values["-cari-"]))
                ktp = df['Ktp'].where(df['Ktp'] == int(values["-cari-"]))
                bpjs = df['Bpjs'].where(df['Ktp'] == int(values["-cari-"]))
                tlp = df['Tlp'].where(df['Ktp'] == int(values["-cari-"]))
                alamat = df['Alamat'].where(df['Ktp'] == int(values["-cari-"]))
                tgll = df['Tgl Lahir'].where(
                    df['Ktp'] == int(values["-cari-"]))
                jekel = df['Jekel'].where(df['Ktp'] == int(values["-cari-"]))
                no = df['no dokumen'].where(df['Ktp'] == int(values["-cari-"]))
                tanggal = date.today()
                dict = {"Nama": nama[hasil_ktp],
                        "Ktp": int(ktp[hasil_ktp]),
                        "Bpjs": int(bpjs[hasil_ktp]),
                        "Tlp": int(tlp[hasil_ktp]),
                        "Alamat": alamat[hasil_ktp],
                        "Tgl Lahir": tgll[hasil_ktp],
                        "Jekel": jekel[hasil_ktp],
                        "no dokumen": int(no[hasil_ktp]),
                        "Tanggal Berobat": tanggal}
                window_cari.close()
                hasil_cari(nama[hasil_ktp], ktp[hasil_ktp], bpjs[hasil_ktp], tlp[hasil_ktp],
                             alamat[hasil_ktp], tgll[hasil_ktp], jekel[hasil_ktp], no[hasil_ktp])
            else:
                sg.popup('Data Tidak Ditemukan !')


# df_new_row = pd.DataFrame(dict, index=[0])
# df2 = pd.concat([df2, df_new_row])
# df2.to_excel(EXCEL_FILE_PENGOBATAN, index=False)

# ktp = df['Ktp'].where(df['Ktp'] == values["-cari-"])
#         bpjs = df['Bpjs'].where(df['Ktp'] == values["-cari-"])
#         tlp = df['Tlp'].where(df['Ktp'] == values["-cari-"])
#         alamat = df['Alamat'].where(df['Ktp'] == values["-cari-"])
#         tgll = df['Tgl Lahir'].where(df['Ktp'] == values["-cari-"])
#         jekel = df['Jekel'].where(df['Ktp'] == values["-cari-"])
#         no_dokumen = df['no dokumen'].where(df['Ktp'] == values["-cari-"])

#     print(nama.values)
#     print(ktp.dropna())
#     print(bpjs.dropna())
#     print(tlp.dropna())
#     print(alamat.dropna())
#     print(tgll.dropna())
#     print(jekel.dropna())
#     print(no_dokumen.dropna())
