import PySimpleGUI as sg
import pandas as pd
from openpyxl import Workbook



# function format rupiah
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp. ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p


def saldo():
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

    EXCEL_FILE = 'excel/saldo_kas.xlsx'

    df = pd.read_excel(EXCEL_FILE)
    saldo = int(df['saldo'].values)
    saldo_rupiah = formatrupiah(saldo)

    layout_saldo = [[sg.Text('Saldo Kas', size=(8, 1)), sg.InputText(
        default_text=saldo_rupiah, disabled=True, font='Courier 16 bold', text_color='Black', size=(50, 1), expand_y=True)],
        [sg.Push(), sg.Exit(), sg.Push()]]

    window_saldo = sg.Window('Saldo Kas', layout_saldo, size=(400, 90))

    while True:
        event_saldo, values = window_saldo.read()
        if event_saldo == sg.WIN_CLOSED or event_saldo == 'Exit':
            window_saldo.close()
            break
