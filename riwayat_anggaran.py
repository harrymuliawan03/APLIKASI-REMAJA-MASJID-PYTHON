import pandas as pd
import PySimpleGUI as sg


def riwayat_anggaran():
    # membaca file data_anggaran
    EXCEL_FILE = 'excel/data_anggaran.xlsx'
    df = pd.read_excel(EXCEL_FILE)

    headers = df.columns.to_numpy()
    data_array = df.to_numpy()

    def create_table(headings, data):

        grade_information_window_layout = [
            [sg.Table(
                values=data,
                headings=headings,
                display_row_numbers=True,
                max_col_width=35,
                auto_size_columns=True,
                justification='right',
                num_rows=10,
                key='-TABLE-',
                row_height=35,
                tooltip="Grades Table"
            )]
        ]

        grade_information_window = sg.Window(
            "Grades Table", grade_information_window_layout, modal=True)

        while True:
            event, values = grade_information_window.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break

        grade_information_window.close()

    create_table(headers.tolist(), data_array.tolist())
