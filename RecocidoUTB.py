import math
import random as rd


distancias = [
    [0, 35.44, 118.63, 84.73, 53.84, 134.48, 146.68, 174.35, 201.03, 160.27, 160.07, 150.67, 292.4, 298.26,331.76],
    [35.44, 0, 81.24, 46.73, 19.63, 100.71, 112.3, 133.28, 156.94, 123.83, 16.27, 115.28, 274.37, 274.15, 299.56],
    [118.63, 81.24, 0, 35.25, 80.31, 84.9, 31.02, 57.34, 76.77, 110.69, 115.65, 102.3, 251.56, 254.87, 283.84],
    [84.73, 46.73, 35.25, 0, 46.02, 51.62, 66.99, 88.89, 114.08, 75.29, 78.03, 67.85, 220.02, 222.34, 252.04],
    [53.84, 19.63, 80.31, 46.02, 0, 96.91, 107.41, 131.78, 158.62, 118.11, 125.31, 110.77, 259.02, 265.18, 297.16],
    [134.48, 100.71, 84.9, 51.62, 96.91, 0, 43.38, 96.21, 121.33, 20.81, 30.82, 14.48, 174.26, 180.48, 206.01],
    [146.68, 112.3, 31.02, 66.99, 107.41, 43.38, 0, 45.65, 65.6, 62.41, 75.3, 27.84, 188.54, 190.78, 218.53],
    [174.35, 133.28, 57.34, 88.89, 131.78, 96.21, 45.65, 0, 72.97, 111.11, 117.97, 76.05, 238.75, 243.44, 268.38],
    [201.03, 156.94, 76.77, 114.08, 158.62, 121.33, 65.6, 72.97, 0, 128.23, 129.86, 82.54, 225, 240.64, 258.37],
    [160.27, 123.83, 110.69,75.29, 118.11, 20.81, 62.41, 111.11, 128.23, 0, 32.95, 36.97, 186.34, 186.64, 220.82],
    [160.07, 16.27, 115.65, 78.03, 125.31, 30.82, 75.3, 117.97, 129.86, 32.95, 0, 33.86, 189.32, 192.69, 22.3],
    [150.67, 115.28, 102.3, 67.85, 110.77, 14.48, 27.84, 76.05, 82.54, 36.97, 33.86, 0, 164.78, 163.7, 198.39],
    [292.4, 274.37, 251.56, 220.02, 259.02, 174.26, 188.54, 238.75, 225, 186.34, 189.32, 164.78, 0, 76.53, 77.38],
    [298.26, 274.15, 254.87, 222.34, 265.18, 180.48, 190.78, 243.44, 240.64, 186.64, 192.69, 163.7, 76.53, 0, 71.12],
    [331.76, 299.56, 283.84, 252.04, 297.16, 297.16, 206.01, 218.53, 258.37, 220.82, 22.3, 198.39, 77.38, 71.12,0]]

lugares = [
  'Entrada','Entrada Principal','Fin de Bohios','Puente','Entrada A2',
  'A1','Parqueadero A1','Zona T','Comedor','Biblioteca','Coliseo',
  'Pasillo Memoroa','A4','A3','A5']

def pert(caminoN, camino):
  caminoN = camino.copy()
  r1= rd.sample(caminoN,1)
  r2 = rd.sample(caminoN,1)
  while r1[0] == 0 or r2[0] == 0:
     r1= rd.sample(caminoN,1)
     r2= rd.sample(caminoN,1)

  i = caminoN.index(r1[0])
  j =  caminoN.index(r2[0])

  aux=caminoN[i]
  caminoN[i] = caminoN[j]
  caminoN[j] = aux
  return caminoN


def sol(caminoN, camino, T):
  L = []
  ite=0
  print(camino)
  while(T >= 0.1 ):
    caminoN=pert(caminoN,camino)
    ite= ite+1
    valoreR1 = 0.0
    valoreR2 = 0.0
    for i in range(len(distancias)-1):
      valoreR1 += distancias[caminoN[i]][caminoN[i+1]]
      valoreR2 += distancias[camino[i]][camino[i+1]]
    if (valoreR1 < valoreR2):
      camino=caminoN.copy()
      T *= 0.9999
    else:
      fact_enfriamiento=rd.uniform(0.8,0.99)
      if(fact_enfriamiento < math.exp(-( (valoreR1 - valoreR2) / T))):
          camino=caminoN.copy()
          T *= 0.9999
    print("T: ", T, "iteracion: ", ite)
  print("Mejor ruta:",camino)
  print("Mejor solucion:",valoreR2)
  for i in camino:
    L.append(lugares[i])
  print("Mejor ruta:",L)


if __name__ == '__main__':
  # distancias = distancesFromCoords()
  camino = [i for i in range(15)]
  caminoN=[]
  T=1
  camino.append(0)
  sol(caminoN,camino, T)

