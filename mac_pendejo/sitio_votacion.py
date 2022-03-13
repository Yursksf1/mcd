import pandas as pd
## define mappaing puestos

mapping_puestos = {}
path = './puestos_departamento_municipio.xlsx'
df = pd.read_excel(path)
for index, row in df.iterrows():
    mapping_puestos[row["Puesto"]] = {
        "departamento": row["DEPARTAMENTO"],
        "municipio": row["MUNICIPIO"],
    }
print("show df")
print(df)
print('mapping_puestos', mapping_puestos)

path = './RENE_GARZON.xlsx'
df = pd.read_excel(path)
print("show df")
print(df)
f = open("result.csv", "a")
f.write("{}\n".format('sep=,'))
f.write("{}\n".format(r'"received_message","pattern_matching","reply_message","multiple_replies","multiple_reply_delay","multiple_reply_delay_max","recipients","contacts","ignored_contacts","reply_delay","reply_delay_max","specific_times","monday","tuesday","wednesday","thursday","friday","saturday","sunday","pause_type","pause_value","disabled","subrule_of","go_to_rule","req_screen_off","req_charging","req_silent","req_do_not_disturb","req_car_mode","prev_rule_timeout","priority_alert","probability"'))
f.write("{}\n".format(r'"René","similar","*%name%* Bienvenido(a) a la\nOrganización de *René Garzón* 🚩<#>Te saluda *Mac 🤖* soy tu asistente virtual. Escribe tu número de cédula. \n*Ej: 1095933743* - _sin espacios ni puntos._","all","1","1","c","","","1","1","0","","","","","","","","seconds","0","0","","",,,,,,,,'))

for index, row in df.iterrows():
    # aca esta la magia
    map = mapping_puestos.get(row['PUESTO'])
    if not map:
        print('not found', row['PUESTO'])

    message = r'"{cedula}","none","*{nombre}* \n\n*LUGAR DE VOTACIÓN* 🗳️ \nDepartamento: \n*{departamento}* \nMunicipio: \n*{municipio}* \nPuesto: \n*{puesto}* \nMesa: *{mesa}*<#>*MARQUE ASÍ:*\n\n*SENADO* 🚩\n*L - 13* Jaime Duran. \n\n*CÁMARA* 🚩\n*L - 107* Álvaro Rueda.<#>Para consultar otra cédula escribe *0*","all","1","1","c","","","1","1","0","","","","","","","","seconds","0","0","1","",,,,,,,,'.format(
        cedula=row['CÉDULA'],
        nombre=row['NOMBRE'],
        departamento=map.get('departamento') if map else row['DEPARTAMENTO'],
        municipio=map.get('municipio') if map else row['MUNICIPIO'],
        puesto=row['PUESTO'],
        mesa=row['MESA'],
    )
    f.write("{} \n".format(message))

f.write("{}\n".format(r'"0","none","Escribe tu número de cédula. \n*Ej: 1095933743* - _sin espacios ni puntos._","single","","","c","","","1","1","0","","","","","","","","seconds","0","0","","1",,,,,,,,'))
f.write("{}\n".format(r'"*","none","*""%message%""* no se encuentra en base de datos 💾🔍<#>Escribe otro número de cédula. \n*Ej: 1095933743* - _sin espacios ni puntos._","all","1","1","c","","","1","1","0","","","","","","","","seconds","0","0","1","1",,,,,,,,'))

f.close()