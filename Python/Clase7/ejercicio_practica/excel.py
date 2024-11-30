import openpyxl

def leer_excel(archivo):
    wb = openpyxl.load_workbook(archivo)
    hoja = wb.active

    for fila in hoja.iter_rows(values_only=True):
        print(fila)
        print(fila[0])

archivo = "ejercicio_excel.xlsx"
leer_excel(archivo)