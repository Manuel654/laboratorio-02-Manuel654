import csv
def import_data():
    list_info=[]
    list=[]
    list2=[]
    with open('Lab2\data.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            
            list_info.append(row)
    for i in list_info:
        list.append(i[0].replace(';', ','))
    for i in list:
        list2.append({"Nro. Región": i[0], 
        "Región": i[1],
        "Provincia": i[2],
        "Circunscripción senatorial": i[3],
        "Distrito": i[4],
        "Comuna": i[5],
        "Circunscripción electoral": i[6],
        "Local": i[7],
        "Nro. Mesa": i[8],
        "Tipo de mesa": i[9],
        "Mesas Fusionadas": i[10],
        "Electores": i[11],
        "Nro. en Voto": i[12],
        "Candidato": i[13],
        "Votos TRICEL": i[14]})
    return list
import_data()

def export_tables_by_region(data, filename):
    lista=[]
    t=data.count("DE TARAPACA")
    a=data.count("DE ANTOFAGASTA")
    at=data.count("DE ATACAMA")
    c=data.count("DE COQUIMBO")
    v=data.count("DE VALPARAISO")
    l=data.count("DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS")
    m=data.count("DEL MAULE")
    b=data.count("DEL BIOBIO")
    ar=data.count("DE LA ARAUCANIA")
    la=data.count("DE LOS LAGOS")
    ay=data.count("DE AYSEN DEL GENERAL CARLOS IBA��EZ DEL CAMPO")
    me=data.count("METROPOLITANA DE SANTIAGO")
    r=data.count("DE LOS RIOS")
    ap=data.count("DE ARICA Y PARINACOTA")
    n=data.count("DE ��UBLE")

    lista.append(t)
    lista.append(a)
    lista.append(at)
    lista.append(c)
    lista.append(v)
    lista.append(l)
    lista.append(m)
    lista.append(b)
    lista.append(ar)
    lista.append(la)
    lista.append(ay)
    lista.append(me)
    lista.append(r)
    lista.append(ap)
    lista.append(n)
        
    with open(filename + ".csv",'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimeter=' ', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        writer.writerow("DE TARAPACA" + lista[0]/
                        "DE ANTOFAGASTA" + lista[1]/
                        "DE ATACAMA" + lista[2]/
                        "DE COQUIMBO" + lista[3]/
                        "DE VALPARAISO" + lista[4]/
                        "DE LIBERTADOR GENERAL BERNARDO O'HIGGINS" + lista[5]/
                        "DEL MAULE" + lista[6]/
                        "DEL BIOBIO" + lista[7]/
                        "DE LA ARAUCANIA" + lista[8]/
                        "DE LOS LAGOS" + lista[9]/
                        "")

    


