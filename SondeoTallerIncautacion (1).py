import sys
import csv

import db
from ModelosTaller import *

#Requerimientos: archivo.csv cant de datos a mostrar
#python3 sondeoTabla2.py incautacion.csv
#arg[0] sondeo.py, arg[1] incautacion.csv,

DEPARTAMENTOS = []
MUNICIPIOS = []

def New_Info(data):
    """Inserta una fila"""
    db.session.add(data)
    db.session.commit()

def id_departamento(departamentos):
    dept = db.session.query(Departamentos).where(Departamentos.departamentos==departamentos).first()
    return dept.id

def id_municipio(municipios):
    muni = db.session.query(Municipios).where(Municipios.municipios==municipios).first()
    return muni.codigodane


def Add_Depto(dpt):
    dept = Departamentos(departamentos = dpt)
    return dept

def Add_Mun(cd, mn, id_dept):
    muni = Municipios(
    codigodane = cd,
    municipios = mn,
    id_dept = id_dept)
    return muni

def incautacion_DATA(cb, fch, cant, cd):
    incautacion = Incautacion(
        clasebien=cb,
        fecha=fch,
        cantidad=cant,
        id_mnp=cd
    )
    return incautacion

if __name__ == '__main__':
    arg = sys.argv #Va a hacer como una lista nombre del programa y argumentos
    db.Base.metadata.create_all(db.motor)

    if  len(arg) == 2:
        nom_ar = arg[1]
        print('Iniciamos prueba con el archivo: ', nom_ar)
        archivo = open(nom_ar, 'r')
        con = 0
        ignorar = True
        #Para saber donde para
        for linea in archivo:
            linea = linea.strip()#Quitamos espacio al principio y al final
            cmp = linea.split(',')
            if ignorar:
                ignorar = False
            else:

                if cmp[0] not in DEPARTAMENTOS:
                    DEPARTAMENTOS.append(cmp[0])
                    new_Dept = Add_Depto(dpt = cmp[0])
                    New_Info(new_Dept)

                if cmp[1] not in MUNICIPIOS:
                    MUNICIPIOS.append(cmp[1])
                    id_Dept = id_departamento(cmp[0])
                    if id_Dept:
                        new_Muni = Add_Mun(cd = cmp[2], mn = cmp[1], id_dept=id_Dept )
                        New_Info(new_Muni)
                    else:
                        print(f'Error! No se encontro {cmp[0]}')

                idMuni = id_municipio(cmp[1])
                if idMuni:
                    new_Incautacion = incautacion_DATA(cb=cmp[3], fch=cmp[4] , cant=cmp[5], cd=idMuni)
                    New_Info(new_Incautacion)
                else:
                    print(f'Error!,no se encontro {cmp[1]}' )
            con+=1
    else:
        print('### Argumentos INcorrectos!')
#Para hacer lo anterior podemos hacer con linux (head incautacion) si los datsos estan correctos
