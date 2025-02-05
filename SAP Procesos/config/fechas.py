import datetime

def obtener_primer_y_ultimo_dia_mes(formato=0):
    hoy = datetime.date.today()

    primer_dia_mes = hoy.replace(day=1)

    if hoy.month == 12:
        ultimo_dia_mes = hoy.replace(month=1, day=1, year=hoy.year + 1) - datetime.timedelta(days=1)
    else:
        ultimo_dia_mes = hoy.replace(month=hoy.month + 1, day=1) - datetime.timedelta(days=1)

    if formato == 0:
        formato_fecha = "%d-%m-%Y"
    elif formato == 1:
        formato_fecha = "%d.%m.%Y"
    else:
        raise ValueError("Formato no válido. Use 0 para '%d-%m-%Y' o 1 para '%d.%m.%Y'")

    primer_dia_mes_str = primer_dia_mes.strftime(formato_fecha)
    ultimo_dia_mes_str = ultimo_dia_mes.strftime(formato_fecha)

    return primer_dia_mes_str, ultimo_dia_mes_str

def obtener_primer_y_ultimo_dia_semana(fecha=None):
    if fecha is None:
        fecha = datetime.date.today()

    if not isinstance(fecha, datetime.date):
        raise ValueError("La fecha debe ser un objeto datetime.date")

    primer_dia_semana = fecha - datetime.timedelta(days=fecha.weekday())
    ultimo_dia_semana = primer_dia_semana + datetime.timedelta(days=6)

    formato = "%d-%m-%Y"
    primer_dia_semana_str = primer_dia_semana.strftime(formato)
    ultimo_dia_semana_str = ultimo_dia_semana.strftime(formato)

    return primer_dia_semana_str, ultimo_dia_semana_str

def diferencia_en_dias(fecha1, fecha2):
    if not isinstance(fecha1, datetime.date) or not isinstance(fecha2, datetime.date):
        raise ValueError("Ambas fechas deben ser objetos datetime.date")

    diferencia = abs((fecha2 - fecha1).days)

    return diferencia


"""
        Ejemplos 


from config.fechas_utiles import obtener_primer_y_ultimo_dia_mes, obtener_primer_y_ultimo_dia_semana, diferencia_en_dias

primer_dia_mes, ultimo_dia_mes = obtener_primer_y_ultimo_dia_mes()
print(f"Primer día del mes: {primer_dia_mes}")
print(f"Último día del mes: {ultimo_dia_mes}")

primer_dia_semana, ultimo_dia_semana = obtener_primer_y_ultimo_dia_semana()
print(f"Primer día de la semana: {primer_dia_semana}")
print(f"Último día de la semana: {ultimo_dia_semana}")

fecha1 = datetime.date(2024, 1, 1)
fecha2 = datetime.date(2024, 12, 31)
diferencia = diferencia_en_dias(fecha1, fecha2)
print(f"Diferencia en días entre {fecha1} y {fecha2}: {diferencia} días")


"""