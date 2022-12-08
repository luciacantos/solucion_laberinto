
def laberinto(dimension, muros):
    #creamos lista
    laberinto = []

    for i in range(dimension):
        fila = []
        for j in range(dimension):
            fila.append('')
        laberinto.append(fila)

    for muro in muros:
        laberinto[muro[0]][muro[1]] = 'X'

    laberinto[dimension-1][dimension-1] = 'S'

    return laberinto

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
x = laberinto(5,muro)

def laberinto_final(laberinto):
    #inicializar fila y columna
    columna = 0
    fila = 0
    #inicializar lista para guardar los movimientos
    solucion = ['Inicio']
    #bucle para que mientras que no se salga del laberinto ni llegue a la salida'S'
    #seguira moviéndose hasta encontrar la salida ('S')
    while ( fila <= 5 and columna <= 5) and laberinto[fila][columna] != 'S': #5 es la longitud del laberinto tanto para sus filas y sus columanas ya que es un cuadrado
        #-----ABAJO--------------------------------------------------------
        #la casilla inferior de la que estás no puede ser mayor que el número de filas del laberinto (5)
        #la casilla tiene que tener '' para no tocar un muro  (definido como espacio en la amterior práctica del dibujo del laberinto)
        #para no volver a la casilla anterior por lo que hay que comprobar en la lista de movimientos que  el moviemto anterior no era hacia arriba
        if fila + 1 <= 5 and laberinto[fila + 1][columna] != 'X' and solucion[-1] != 'Arriba':
            solucion.append('Abajo')
            fila = fila + 1
        #-----DERECHA------------------------------------------------------
        #la casilla derecha de la que estás no puede ser mayor que el número de columnas del laberinto (5)
        #no puedes tocar un muro por lo que tiene que haber '' en la siguiente casilla
        #no se puede volver a la casilla anterior por lo que compruebas en la lista que el movimiento anterior no sea 'Izquierda'
        elif columna + 1 <= 5 and laberinto[fila][columna+1] != 'X' and solucion[-1] != 'Izquierda':
            solucion. append('Derecha')
            columna = columna + 1
        #-----ARRIBA----------------------------------------------------
        #la casilla superior de la que estás no puede ser inferior a 0 o estarías fuera del laberinto
        #la casilla tiene que tener '' para no tocar un muro
        #para no volver a la casilla anterior compruebas en la listade movimientos que el arterior no es ' Abajo'
        elif fila - 1 >= 0 and laberinto[fila - 1][columna] != 'X' and solucion[-1] != 'Abajo':
            solucion.append('Arriba')
            fila = fila - 1
        #-----IZQUIERDA--------------------------------------------------
        #la casilla a la izquierda no puede ser inferior a 0 porque estarías fuera del laberinto
        #la casilla tiene que tener '' para que no sea muro
        #para no volver a la casilla anterior se comprueba que en la lista de movimientos el anterior no sea 'Derecha'
        elif columna - 1 >= 0 and laberinto[fila][columna] != 'X' and solucion[-1] != 'Derecha':
            solucion.append('Izquierda')
            columna = columna - 1
        else:
            #si no se puede mover a ningún sitio
            solucion.append('No hay solución')
    solucion.append("Salida") #añadir 'Salida' al final de la lista
    return solucion

print('Movimientos para salir: ', laberinto_final(x))
