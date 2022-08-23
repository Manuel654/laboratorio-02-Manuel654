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
    print(list[1])
    for i in list:
        list2.append({"Nro. Región": i[0], 
        "Región": i[1],
        "Provincia": i[2],
        "Circunscripción senatorial": i[3],
        "Distrito": i[4],
        "Comuna": i[5],
        "Circunscripción electoral": i[6],
        "Local": i[7]})
    return list
import_data()

def export_tables_by_region(data, filename):

    


