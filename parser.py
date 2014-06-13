import json


# Fecha;Ganaderia;Duracion;Heridos_asta;Traumatismos;Atendidos;Piso

# [
#    {
#       "values":[
#          {
#             "y":3,
#             "x":"04/05/2013"
#          },
#          {
#             "y":1,
#             "x":"04/11/2013"
#          },
#          {
#             "y":3,
#             "x":"04/12/2013"
#          }
#       ],
#       "key":"Apples"
#    },

with open('asserts/encierros.csv') as f:

    first_line = f.readline().strip('\n')
    # headers = first_line.split(';')

    mDict = {}

    for line in f:
        line = line.split(';')
        fecha = line[0]
        Ganaderia = line[1]
        Duracion = line[2]
        Heridos_asta = int(line[3])
        Traumatismos = int(line[4])
        Atendidos = int(line[5])
        Piso = line[6]

        year = int(fecha.split('/')[2])
        #if year >= 83:
        #    break

        if year in mDict:
            mDict[year]['Heridos_asta'] += Heridos_asta
            mDict[year]['Traumatismos'] += Traumatismos
            mDict[year]['Atendidos'] += Atendidos
        else:
            mDict[year] = {'Heridos_asta': Heridos_asta, 'Traumatismos': Traumatismos, 'Atendidos': Atendidos}

    Atendidos = {
        "values": [],
        "key": "Atendidos"
    }

    Heridos_asta = {
        "values": [],
        "key": "Heridos_asta"
    }

    Traumatismos = {
        "values": [],
        "key": "Traumatismos"
    }

    for key, value in mDict.items():
        Atendidos['values'].append({'y': value['Atendidos'], 'x': key})
        Traumatismos['values'].append({'y': value['Heridos_asta'], 'x': key})
        Heridos_asta['values'].append({'y': value['Traumatismos'], 'x': key})

    mList = [Atendidos, Traumatismos, Heridos_asta]

    with open('encierros.json', 'wb') as fp:
        json.dump(mList, fp, sort_keys=True, indent=4, separators=(',', ': '))


