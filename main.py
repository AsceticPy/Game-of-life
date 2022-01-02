from dataclasses import dataclass
import random

@dataclass
class Cell:
   coordX:int 
   coordY:int 
   alive: bool = False

earth: Cell = []

def create_earth(width: int = 10, height: int = 10) -> Cell:
   for n in range(height):
      land: Cell = []
      for i in range(width):
         land.append(Cell(i, n))
      earth.append(land)

def avaible_positions(matrice: Cell, coordX: int, coordY: int) -> int:
   positions = [[coordX - 1, coordY],[coordX + 1, coordY]
               ,[coordX, coordY - 1],[coordX, coordY + 1]
               ,[coordX - 1, coordY - 1],[coordX + 1, coordY + 1]
               ,[coordX - 1, coordY + 1],[coordX + 1, coordY - 1]]
   positions_to_test = []
   n_error = 0
   for position in positions:
      try:
         if position[0] < 0 or position[1] < 0:
            ERROR = 1 / 0

         positions_to_test.append(matrice[position[1]][position[0]])
      except:
         n_error += 1
      
   return positions_to_test
   
def destiny(alternative_earth: Cell, cell: Cell) -> bool:   
   neighbor_alive = sum(1 for neighbor in avaible_positions(alternative_earth, cell.coordX, cell.coordY) if neighbor.alive)
   
   if cell.alive:
      if neighbor_alive <= 1:
         return False
      elif neighbor_alive >= 4:
         return False
      elif neighbor_alive in [2, 3]:
         return True
   else:
      if neighbor_alive == 3:
         return True
      else:
         return False

def new_day():
   earth_copy: Cell = earth
   
   for n in range(len(earth_copy)):
      for i in range(len(earth_copy[n])):
         earth[n][i].alive = destiny(earth_copy, earth_copy[n][i])

def populating_earth(number_of_people: int = 50):
   for n in range(number_of_people):
      x_random = random.randint(0, len(earth) - 1)
      y_random = random.randint(0, len(earth[0]) - 1)
      
      earth[y_random][x_random].alive = True
   
def main():
   number_days = 4
   create_earth()
   populating_earth()
   
   for n in range(number_days):
      new_day()
      print("DAY ", n, " : ")
      for i in range(10):
         for x in range(10):
            if earth[i][x].alive:
               print('X', end = '')
            else:
               print('O', end = '')
         print('\n')

main()