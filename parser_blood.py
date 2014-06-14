import json
import datetime
import random


fallecido = []
fallecido.append("10/07/09;27;Madrid, ES;Telefonica")
fallecido.append("08/07/03;63;Pamplona, ES;Mercaderes")
fallecido.append("13/07/95;22;Illinois, USA;Plaza del Ayuntamiento")
fallecido.append("13/07/80;29;Badajoz, ES;Plaza de Toros")
fallecido.append("13/07/80;26;Navarra, ES;Plaza del Ayuntamiento")


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

        day = int(fecha.split('/')[0])
        
        month = int(fecha.split('/')[1])
        
        year = fecha.split('/')[2]
        if int(year) >= 15:
            year = "19" + year
        else:
            year = "20" + year
        year = int(year)

        date = int((datetime.datetime(year,month,day,0,0) - datetime.datetime(1970,1,1)).total_seconds()) * 1000
        #date = str(date * 1000)

        blood = Heridos_asta * random.uniform(0.1, 0.4) + Traumatismos * random.uniform(0.0, 0.05) + Atendidos * random.uniform(0.0, 0.01)

        if date in mDict:
            mDict[date] += blood
        else:
            mDict[date] = blood

        # counter += 1
        # if counter >=5:
        #    break

for x in range(0, len(fallecido)):

    fecha = fallecido[x].split(';')[0]

    day = int(fecha.split('/')[0])
        
    month = int(fecha.split('/')[1])
    
    year = fecha.split('/')[2]

    
    if int(year) >= 15:
        year = "19" + year
    else:
        year = "20" + year
    year = int(year)

    date = int((datetime.datetime(year,month,day,0,0) - datetime.datetime(1970,1,1)).total_seconds()) * 1000
    #date = str(date * 1000)
    blood = random.uniform(0.4, 0.6)

    if date in mDict:
        mDict[date] += blood
    else:
        mDict[date] = blood



mList = []
for key, value in mDict.items():
    mList.append([key, value])

# sorted mList hay que hacerla cummulative
mList = sorted(mList)
blood = 0

for x, val in enumerate(mList):
    blood += mList[x][1]
    mList[x][1] = blood

out = [{"key": "Blood Losses", "values": mList}]


with open('asserts/encierros_blood.json', 'wb') as fp:
    json.dump(out, fp, sort_keys=True, indent=4, separators=(',', ': '))
    

# [ 
#   { 
#     "key" : "Consumer Staples" , 
#     "values" : [ [ 1138683600000 , 0] , [ 1141102800000 , 0] , [ 1143781200000 , 0] , [ 1146369600000 , 0] , [ 1149048000000 , 0] , [ 1151640000000 , 0] , [ 1154318400000 , 0] , [ 1156996800000 , 0] , [ 1159588800000 , 0] , [ 1162270800000 , 0] , [ 1164862800000 , 0] , [ 1167541200000 , -0.24102139376003] , [ 1170219600000 , -0.69960584365035] , [ 1172638800000 , -0.67365051426185] , [ 1175313600000 , 0] , [ 1177905600000 , 0] , [ 1180584000000 , 0] , [ 1183176000000 , -0.31429312464988] , [ 1185854400000 , -0.90018700397153] , [ 1188532800000 , -0.96926214328714] , [ 1191124800000 , -1.1343386468131] , [ 1193803200000 , -1.1335426595455] , [ 1196398800000 , -1.2327663032424] , [ 1199077200000 , -0.41027135492155] , [ 1201755600000 , -0.41779167524802] , [ 1204261200000 , -0.38133883625885] , [ 1206936000000 , 0] , [ 1209528000000 , -0.32550520320253] , [ 1212206400000 , -0.33185144615505] , [ 1214798400000 , -0.68609668877894] , [ 1217476800000 , -0.70001207744308] , [ 1220155200000 , -0.68378680840919] , [ 1222747200000 , -0.40908783182034] , [ 1225425600000 , -0.39074266525646] , [ 1228021200000 , -0.40358490474562] , [ 1230699600000 , -0.85752207262267] , [ 1233378000000 , -0.74395750438805] , [ 1235797200000 , -0.70718832429489] , [ 1238472000000 , -0.76244465406965] , [ 1241064000000 , -0.67618572591984] , [ 1243742400000 , -0.67649596761402] , [ 1246334400000 , -0.94618002703247] , [ 1249012800000 , -0.95408485581014] , [ 1251691200000 , -0.96272139504276] , [ 1254283200000 , 0] , [ 1256961600000 , 0] , [ 1259557200000 , 0] , [ 1262235600000 , 0] , [ 1264914000000 , 0] , [ 1267333200000 , 0] , [ 1270008000000 , -0.25516420149471] , [ 1272600000000 , -0.24106264576017] , [ 1275278400000 , -0.22802547751448] , [ 1277870400000 , -0.62187524046697] , [ 1280548800000 , -0.72155608677106] , [ 1283227200000 , -0.70221659944774] , [ 1285819200000 , -1.1117002584543] , [ 1288497600000 , -1.190911001336] , [ 1291093200000 , -1.1781082003972] , [ 1293771600000 , -1.2125860264875] , [ 1296450000000 , -1.7748010365657] , [ 1298869200000 , -1.8919594178596] , [ 1301544000000 , -1.7077946421533] , [ 1304136000000 , -2.024238803094] , [ 1306814400000 , -1.9769844081819] , [ 1309406400000 , -2.0730275464065] , [ 1312084800000 , -1.9690128240888] , [ 1314763200000 , -5.5557852269348] , [ 1317355200000 , -7.2527933190641] , [ 1320033600000 , -5.7367677053109] , [ 1322629200000 , -6.0409316206662] , [ 1325307600000 , -4.6511525539195] , [ 1327986000000 , -4.526116059083] , [ 1330491600000 , -4.846292325197] , [ 1333166400000 , -2.2663198779425] , [ 1335758400000 , -2.4172072568564] , [ 1338436800000 , -2.3204729601189]]
#   } ,