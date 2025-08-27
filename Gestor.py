import xml.etree.ElementTree as ET  # Libreria ElementTree

class Gestor:
    def __init__(self):
        pass
    
    def leer_archivo(self,ruta_entrada):
        tree = ET.parse(ruta_entrada)
        root = tree.getroot() 
        print(root.tag)#camposAgricolas
        
        for campo_elem in root.findall("campo"):
            id_campo = campo_elem.get("id")
            nombre_campo = campo_elem.get("nombre")
            print("---------------------------------------------------------------")
            print("El id del campo es: ",id_campo, "nombre: ",nombre_campo)
            
            #estacionesBase
            for estaciones_elem in campo_elem.find("estacionesBase").findall("estacion"):
                id_estacion = estaciones_elem.get("id")
                nombre_estacion = estaciones_elem.get("nombre")
                print("El id de la estacion es: ",id_estacion, "nombre: ",nombre_estacion)
            
            #sensoresSuelo
            for sensoresS_elem in campo_elem.find("sensoresSuelo").findall("sensorS"):
                id_sensorS = sensoresS_elem.get("id")
                nombre_sensorS = sensoresS_elem.get("nombre")
                print(" ")
                print("El id del sensor de suelo es: ",id_sensorS, "nombre: ",nombre_sensorS)
                for frecuencia_elem in sensoresS_elem.findall("frecuencia"):
                    id_estacionS = frecuencia_elem.get("idEstacion") 
                    #Frecuencia de las estaciones para los sensores de suelo
                    frecuenciaS = int(sensoresS_elem.find("frecuencia").text)   
                    print("El id de la estacion para el Sensor de suelo: ", id_estacionS, "con una frecuencia de: ",frecuenciaS)
                                
            #sensoresCultivo     
            for sensoresT_elem in campo_elem.find("sensoresCultivo").findall("sensorT"):
                id_sensorT = sensoresT_elem.get("id")
                nombre_sensorT = sensoresT_elem.get("nombre")
                print("El id del sensor de cultivo es: ",id_sensorT, "nombre: ",nombre_sensorT)
                for frecuencia_elem in sensoresT_elem.findall("frecuencia"):
                    id_estacionT = frecuencia_elem.get("idEstacion") 
                    #Frecuencia de las estaciones para los sensores de suelo
                    frecuenciaT = int(sensoresS_elem.find("frecuencia").text)   
                    print("El id de la estacion para el Sensor de cultivo: ", id_estacionT, "con una frecuencia de: ",frecuenciaT)
                    
    def exportar_archivo(self):
        pass