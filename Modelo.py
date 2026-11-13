
class Colmena:

    def __init__(self):
        self.apiario = 0
        self.colmena = 0
        self.fecha = ""
        self.salidas = 0
        self.entradas = 0
        self.ataques = 0

    # Tengo que crear una función para poder imprimir las que son tipo colmena
    def __str__(self):
        return str(self.apiario) + ',' + str(self.colmena) + "," + str(self.fecha) + ',' + str(self.salidas) + ',' + str(self.entradas) + ',' + str(self.ataques)
    
    
    def cargar_datos(self, archivo):
    #Este comando lee la matriz línea por línea y quita los enters entre las filas de la matriz.
        linea = archivo.readline().strip()
        # print(linea)
        if linea == "":
    #Si la linea es igual a un espacio, haga esto:
            return False
        # Por cada elemento (linea del archivo), lo separo por comas y sustituyo los valores del self de cada linea por elemento [n]
        elemento = linea.split(",")
        self.apiario = elemento[0]
        self.colmena = elemento[1]
        self.fecha = elemento [2]
        self.salidas = float(elemento[3])
        self.entradas = int(elemento[4])
        self.ataques = int(elemento[5])
        return True

    def imprimir_salidas_abejitas(self):
    # Este es para imprimir las abejas totales de cada colmena
    # Aquí lo que se hace es tomar el atributo característica de colmena (numero de cada colmena)
    # Recibe los selfs y sus atributos
        colmena = self.colmena
        salida = self.salidas * 2.5
        print(f"Colmena {colmena}: {salida}")


    def devolver_ataques_abejitas(self, total_ataques):
            ataque = self.ataques
            total_ataques += ataque
            return total_ataques


    # def imprimir_promedio_muertes_abejitas(self, perdidas, key, salidas_totales, entradas_totales):

            # salida = self.salidas
            # salidas_totales += salida
            # entradas = self.entradas
            # entradas_totales += entradas
            # promedio = (salidas_totales - entradas_totales) / perdidas
        
            # return promedio


