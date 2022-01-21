import PySimpleGUI as sg

from analyser import count_analyser, sum_sales, value_analyser

sg.theme("DarkGrey4")


def select_csv():
    layout = [
        [sg.Text("Selecione o arquivo CSV")],
        [sg.Input(key="CSV"), sg.FileBrowse()],
        [sg.Button("Analisar")],
    ]

    window = sg.Window("Selecionar CSV", layout, element_justification="c")

    event, values = window.read()

    csv_file = values["CSV"]

    window.close()

    return csv_file


def analyser(csv_file):
    # Análise por valores (melhor e pior dia)
    values = value_analyser(csv_file)
    # Análise por quantidade (melhor e pior dia)
    count = count_analyser(csv_file)
    # Agrupamento de vendas (valor total) por dia
    grouped = sum_sales(csv_file).values.tolist()

    # [[225, '1/10/2021'], [70, '5/10/2021']]
    # [[4, '5/10/2021'], [1, '4/10/2021']]

    frame_table = [
        [
            sg.Table(
                values=grouped,
                headings=["Data", "Valor em Vendas"],
                num_rows=min(10, len(grouped)),
            ),
        ],
    ]

    frame_values = [
        [sg.Text(f"- Melhor dia ({values[0][1]}): R$ {values[0][0]:.2f}")],
        [sg.Text(f"- Pior Dia ({values[1][1]}): R$ {values[1][0]:.2f}")],
    ]

    frame_count = [
        [sg.Text(f"- Melhor dia ({count[0][1]}): {count[0][0]} vendas")],
        [sg.Text(f"- Pior dia ({count[1][1]}): {count[1][0]} vendas")],
    ]

    layout = [
        [sg.Frame("Tabela de Vendas Agrupadas", frame_table)],
        [sg.Frame("Análise de Valor de Vendas", frame_values)],
        [sg.Frame("Análise de Quantidade de Vendas", frame_count)],
    ]

    window = sg.Window("Resultado", layout, element_justification="c")

    event, values = window.read()

    csv_file = values["CSV"]

    window.close()

    return csv_file


csv_file = select_csv()
analyser(csv_file)
