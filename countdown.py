from datetime import datetime

def countdown():

    dia_hoje = datetime.now()

    data_lancamento = datetime(2027, 2, 18)

    tempo_restante = data_lancamento - dia_hoje

    if tempo_restante.total_seconds() <= 0:
        return 0, 0, 0, 0

    total_segundos = int(tempo_restante.total_seconds())

    dias = total_segundos // 86400
    horas = (total_segundos % 86400) // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return dias, horas, minutos, segundos

