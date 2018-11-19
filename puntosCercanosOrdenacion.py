###ALVARO BERRIO GALINDO###
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


# Clase Punto en dos dimensiones
class Point2D:
    # Inicializacion
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    # Comparar con otro punto
    def __eq__(self, p):
        if self.x == p.x and self.y == p.y:
            return True
        else:
            return False


# Clase Punto en tres dimensiones
class Point3D:
    # Inicializacion
    def __init__(self, coord_x, coord_y, coord_z):
        self.x = coord_x
        self.y = coord_y
        self.z = coord_z

    # Comparar con otro punto
    def __eq__(self, p):
        if self.x == p.x and self.y == p.y and self.z == p.z:
            return True
        else:
            return False


# Hacer un grafico en 2 dimensiones
def plot2D(puntos):
    a = []
    b = []
    for i in puntos:
        a.append(i.x)
        b.append(i.y)
    plt.plot(a, b, 'ro')
    plt.show()


# Hacer un grafico en 3 dimensiones
def plot3D(puntos):
    xs = []
    ys = []
    zs = []
    for i in puntos:
        xs.append(i.x)
        ys.append(i.y)
        zs.append(i.z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(xs, ys, zs)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


# Distancia euclidea entre dos puntos, en 2 o 3 dimensiones
def dist(point1, point2):
    if isinstance(point1, Point2D) and isinstance(point2, Point2D):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    elif isinstance(point1, Point3D) and isinstance(point2, Point3D):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)
    else:
        print("Se necesitan objetos de la clase Punto2D o Punto 3D")


# Muestra por pantalla los puntos en un vector
def print_points(array):
    if isinstance(array, list) and len(array) > 0:
        if isinstance(array[0], Point2D):
            for i in array:
                print(i.x, i.y)
        elif isinstance(array[0], Point3D):
            for i in array:
                print(i.x, i.y, i.z)
    else:
        print("Se necesitan vectores")


# Ordena los puntos segun la coordenada x o la y
def sort_points(array, string):
    if isinstance(array, list):
        if string == 'x':
            return sorted(array, key=lambda point: point.x)
        elif string == 'y':
            return sorted(array, key=lambda point: point.y)
    else:
        print("Se necesitan vectores")


# Fuerza bruta que halla las distancias entre todos los puntos
# y devuelve la minima yademas de cuales son estos puntos
def caso_base(array):
    d = 9999999
    p1 = None
    p2 = None
    for i in range(len(array)):
        for j in range(len(array)):
            aux = dist(array[i], array[j])
            if i < j and aux < d:
                d = aux
                p1 = array[i]
                p2 = array[j]
    return [d, p1, p2]


# Halla la distancia minima en la banda que divide a un conjunto de puntos en dos y los puntos entre
# los que se da esa distancia
def dist_banda(array, d, m):
    db = 999999999
    p1 = None
    p2 = None
    banda = []
    # la banda esta compuesta por los puntos que se encuentren a una distancia menor a d en la coordenada x,
    # es decir, (mediana-d, mediana+d)
    for i in array:
        if (m - d) < i.x < (m + d):
            banda.append(i)
    # Para cada punto en la banda, se hallan las distancias con los demas puntos en la caja, que seran 5 como mucho en dos
    # dimensiones y 17 en tres, y se devuelve la minima
    # En la caja de cada punto p1 entran puntos p2 tal que p2.x pertenece a [p1.x,p1.x+d) y p2.y a (p1.y-d,p1.y+d) en 2 dimensiones
    # y a mayores p2.z pertenece a (p1.z-d, p1.z+d) en 3 dimensiones
    if isinstance(array[0], Point2D):
        for i in range(len(banda)):
            for j in range(i + 1, i + 6):  # vale con poner array
                if j < len(banda) and dist(banda[i], banda[j]) < db:
                    db = dist(banda[i], banda[j])
                    p1 = banda[i]
                    p2 = banda[j]
    elif isinstance(array[0], Point3D):
        for i in range(len(banda)):
            for j in range(i + 1, i + 18):  # vale con poner array
                if (j < len(banda)) and (dist(banda[i], banda[j])) < db and ((banda[i].z - d) < banda[j].z < (banda[i].z + d)):
                    db = dist(banda[i], banda[j])
                    p1 = banda[i]
                    p2 = banda[j]
    return [db, p1, p2]


# Halla la distancia minima en un conjunto de puntos, funcion principal del programa que se llama a si misma
# (recursividad) para cada conjunto de mas de 3 puntos en 2 ocasiones con conjuntos de tamano n/2
def puntos_cercanos(puntos):
    array_x = puntos[0]
    array_y = puntos[1]
    if isinstance(array_x, list):
        p1 = None
        p2 = None
        long = len(array_x)
        s1y = []
        s2y = []
        # Para los conjuntos de puntos con 2 o 3 puntos se ejecuta el metodo de fuerza bruta
        if 1 < long <= 3:
            base = caso_base(array_x)
            return base
        elif long == 1:
            # Si solo hay un punto en el conjunto devolvera infinito
            return [999999999, None, None]
        else:
            # Para conjuntos con mas de tres puntos se halla la mediana para dividir en dos el conjunto
            middle = int(math.ceil(long / 2.0))
            # caso de que la longitud del vector de puntos sea par
            if long % 2 == 0:
                med = (array_x[middle - 1].x + array_x[middle].x) / 2
            # caso impar
            else:
                med = array_x[middle - 1].x
            # se crean los dos subconjuntos de tamano n/2 con ordenacion en x y luego en y
            s1_x = array_x[0:middle]
            s2_x = array_x[middle:long]
            for i in array_y:
                if i in s1_x:
                    s1y.append(i)
                elif i in s2_x:
                    s2y.append(i)
            # funcion recursiva con los subconjuntos
            izq = puntos_cercanos([s1_x, s1y])
            der = puntos_cercanos([s2_x, s2y])
            d1 = izq[0]  # distancia minima en el conjunto izquierdo
            d2 = der[0]  # distancia minima en el conjunto derecho
            # se comparan las distancias minimas de cada subconjunto y se actualizan los puntos candidatos
            if d1 == min(d1, d2):
                c1 = izq[1]
                c2 = izq[2]
            elif d2 == min(d1, d2):
                c1 = der[1]
                c2 = der[2]
            d = min(d1, d2)
            # Se llama a la funcion que halla la distancia minima en la banda pasando el vector de puntos, la mediana
            # y la distancia minima entre los dos subconjuntos del array
            banda = dist_banda(array_y, d, med)
            db = banda[0]  # distancia minima en la banda
            # candidatos en la banda
            cand_banda1 = banda[1]
            cand_banda2 = banda[2]
            # Se comparan la distancia de la banda con la minima del conjunto y se actualizan los candidatos
            if db == min(d, db):
                c1 = cand_banda1
                c2 = cand_banda2
            return [min(d, db), c1, c2]  # se devuelve la distancia minima total y los puntos entre los que se da


def ejecucion(puntos):
    # Ejecucion
    ordenados_x = sort_points(puntos, 'x')  # primeros se ordena el vector de puntos segun x y segun y
    ordenados_y = sort_points(puntos, 'y')
    sol = puntos_cercanos([ordenados_x, ordenados_y])

    # Solucion con el algoritmo divide y venceras
    print "La distancia minima es " + str(sol[0]) + " y se da entre los puntos"
    print_points([sol[1], sol[2]])
    print

    # Solucion con fuerza bruta (a modo de comprobacion)
    fuerza_bruta = caso_base(puntos)
    print "Comprobacion, distancia minima: " + str(fuerza_bruta[0]) + ", puntos: "
    print_points([fuerza_bruta[1], fuerza_bruta[2]])


puntos = []
dim = 2
n_puntos = 100
max_punto = 50

# creacion del vector de puntos
if dim == 2:
    for i in range(n_puntos):
        a = Point2D(round(random.uniform(0, max_punto), 2), round(random.uniform(0, max_punto), 2))
        t = False
        for j in puntos:
            if a.__eq__(j):
                t = True
        if not False:
            puntos.append(a)
    ejecucion(puntos)
    plot2D(puntos)
elif dim == 3:
    for i in range(n_puntos):
        a = Point3D(round(random.uniform(0, max_punto), 2), round(random.uniform(0, max_punto), 2),
                    round(random.uniform(0, max_punto), 2))
        t = False
        for j in puntos:
            if a.__eq__(j):
                t = True
        if not False:
            puntos.append(a)
    ejecucion(puntos)
    plot3D(puntos)
