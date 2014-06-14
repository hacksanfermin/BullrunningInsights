import json

# Fecha;Ganaderia;Duracion;Heridos_asta;Traumatismos;Atendidos;Piso

## VERTICAL
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

## HORIZONTAL
# [ 
#   {
#     "key": "Series1",
#     "color": "#d62728",
#     "values": [
#       { 
#         "label" : "Group A" ,
#         "value" : -1.8746444827653
#       } ,

vertical = False

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


        #day = fecha.split('/')[0]
        #year = int(day)
        
        year = fecha.split('/')[2]
        if int(year) >= 15:
            year = "19" + year
        else:
            year = "20" + year
        year = int(year)

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

    if vertical:
        l1 = 'y'
        l2 = 'x'
    else:
        l1 = "value"
        l2 = "label"

    for key, value in mDict.items():
        Atendidos['values'].append({l1: value['Atendidos'], l2: key})
        Traumatismos['values'].append({l1: value['Heridos_asta'], l2: key})
        Heridos_asta['values'].append({l1: value['Traumatismos'], l2: key})


    mList = [Atendidos, Traumatismos, Heridos_asta]

    with open('asserts/encierros_year_hor.json', 'wb') as fp:
        json.dump(mList, fp, sort_keys=True, indent=4, separators=(',', ': '))


