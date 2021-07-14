#dice simulator

import random

def diceing():
 tries = input('LETS PLAY - say dice:  ')
 while True:
     if tries == 'dice':
         dice = random.randint(1,6)
         print(f"you got {dice}")
         tries = input("play more - say 'dice' to play OR -> 'exit' to quit the game")
         if tries == 'exit':
             break
         elif tries == 'dice':
             pass
         else:
            pass

     else:
         print('type corectly please')
         return diceing()
diceing()
