import validacion
from Modelo import Colmena

class Controlador:
    
    def __init__(self):
        self._lista = []
        self.diccionario = {}
#Para imprimir la lista como un str y no la ubicación donde se encuentra esta
    def imprimir_lista(self):
        for i in range(len(self._lista)):
            print(self._lista[i].__str__())

    def iniciar_programa(self):
        error = True
        while error== True:
            try:
                nombre_de_archivo = input("Ingrese nombre del archivo: ")
                archivo = open(nombre_de_archivo, 'r')
                error = False
            except FileNotFoundError:
                print(f"No existe: {nombre_de_archivo}")
    #Esto tira el nombre y lo que contiene el archivo, de manera "codificada"
        #print(archivo)
    #Acá podemos ver la lista vacía
    #print(self._lista)
    #Esto agrega la matriz anteriormente verificada linea por linea mientras la va leyendo.
        self.agregar_elementos(archivo)
    #Y luego de agregar elementos esta está ahora llena, aunque nos da la ubucación de los elementos, mas no su valor en str.
        # print(self._lista)
    
        self.rellenar_diccionario()
        # Self para imprimir colmena (archivo completo)
        #self.imprimir_lista()
        self.menu()


    def agregar_elementos(self, archivo):
    #Lee la primer línea, la que contiene los enunciados para evitar errores.
        archivo.readline()
        valido = True
#El programa viene acá y lee de manera individual, las líneas de la matriz, hasta que se acabe y dé un valido = false
        while valido:
    #Este abre la clase "modelo" en colmena y crea la nueva matriz a partir de esta nueva lectura
            colmena_nueva = Colmena()
    #Esta parte del código llama a la clase creada por colmena_nueva e invita a la función "cargar_datos"
            valido = colmena_nueva.cargar_datos(archivo)
    #Si sale el código exitosamente de la función anterior (valido = True)...
            if valido:
    #...agréguelo a la lista vacía o con distintos valores, esto para cada una de las líneas en la matriz
    #Por ello, cuando el ciclo se vuelve a repetir "subscribe" los valores de la matriz encima de los otros, en la función modelo
    #pero acá gracias al append a la lista, estos se guardan allí, mientras va pasando el ciclo.
    #Este append agrega todo lo que hice en modelo, por ello, si yo llamo a una variable creada dentro de esta lista, el sistema la reconoce
    #y la llama
                self._lista.append(colmena_nueva)    
        archivo.close()


    def rellenar_diccionario(self):
        # Para que ya este el diccionario sin la necesidad de entrar a una función en específico.
        for i in range(len(self._lista)):
            # print(i)
    #Aquí puedo ver los valores de las colmenas ya que puedo llamar a los valores de la función que agregué al crear la lista
            print(self._lista[i].colmena)
            print(self._lista[i].colmena, self._lista[i])
            valores_nuevos = {self._lista[i].colmena : self._lista[i]}
            self.diccionario.update(valores_nuevos)

        return self.diccionario



    def total_de_abejita (self):
        colmenas_actualizadas = self.diccionario.values()
        # dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        # values= dic.values()
        # values→ [1,2,3,4] 
        for a in (colmenas_actualizadas):
            print(a)
            # salida = a.salidas * 2.5
            # print(a.colmena, ":" , salida)
            a.imprimir_salidas_abejitas()    

   

    def ataques_totales_por_colmena(self):
        numero_total_de_colmenas = self.diccionario.keys()
        # diccionario, que es? --> el número de colmenas (keys)  
        # dic =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
        # keys= dic.keys()
        # keys→ [‘a’,’b’,’c’,’d’]
        # key --> 1,2,3 (prueba)
        for key in numero_total_de_colmenas:
            ataques_totales = 0
            for i in self._lista:
                if i.colmena == key:
                    ataques_totales = i.devolver_ataques_abejitas(ataques_totales)
            print(f"Colmena {key}: {ataques_totales}")



    def perdida_promedio_abejitas(self):
        numero_total_de_colmenas = self.diccionario.keys()

        for key in numero_total_de_colmenas:

            colmenas_totales = 0
            salidas_totales = 0
            entradas_totales = 0

            for i in self._lista:
                if i.colmena == key:

                    colmenas_totales += 1
                    salidas_totales += i.salidas
                    entradas_totales += i.entradas
                    promedio = (salidas_totales-entradas_totales)/colmenas_totales
           
            print(f"Colmena {key}: {promedio}")

# def promedio
# Salen - Entradas + salen - entradas cada día 
# ---------------------------
#  Cantidad de días que se registraron en esa colmena



    def menu(self):
        salir = False
        print("\nBienvenido al programa de abejitas")

        while salir == False:
            print("\n1. Cantidad de abejitas.")
            print("2. Pérdida promedio de abejitas.")
            print("3. Ataques hacia las colmenas de abejitas.")
            print("4. Salir del programa de abejitas.\n")

            opcion = validacion.validar_numero_entero("Ingrese su opción: ")
            print("")

            if opcion == 1:
                self.total_de_abejita()

            elif opcion == 2:
                self.perdida_promedio_abejitas()

            elif opcion == 3:
                self.ataques_totales_por_colmena()
            
            elif opcion == 4:
                print("Gracias por usar el programa de abejitas.\n")
                salir = True
                
            else:
                if opcion == None:
                    opcion = "introducida"

                print(f"La opción {opcion} no es válida")
        
