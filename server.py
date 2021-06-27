from flask import Flask, render_template

from cards import Cards
from cards import Units
from cards import Effects
from cards import Player

app = Flask(__name__)

red_ninja = Units('Red Belt Ninja', 3, 3, 4)
black_ninja = Units('Black Belt Ninja', 4, 5, 4)
yellow_ninja = Units('Yellow Belt Ninja', 4, 4 ,4)
hard_algorithm = Effects('Hard Algorithm', 2, 'resistance', 3)
unhandled_promise = Effects('Unhandled Promise', 1, 'resistance', -2)
pair_programming = Effects('Pair Programming', 3, 'power', 2)

# red_ninja.play(1)
# hard_algorithm.affect(red_ninja)
# black_ninja.play(2)
# unhandled_promise.affect(red_ninja)
# pair_programming.affect(red_ninja)
# red_ninja.attack(black_ninja)

list = [
red_ninja,
black_ninja,
yellow_ninja,
hard_algorithm,
unhandled_promise,
pair_programming
]

player1 = Player('Player One')
player2 = Player('player Two')

player1.add_unit(red_ninja).add_unit(black_ninja).add_unit(yellow_ninja).add_effect(hard_algorithm).add_effect(unhandled_promise).add_effect(pair_programming)

player2.add_unit(red_ninja).add_unit(black_ninja).add_unit(yellow_ninja).add_effect(hard_algorithm).add_effect(unhandled_promise).add_effect(pair_programming)

def main():
  
  while True:
    print('Battle begins!\n ')

    which_player = input('Who is playing?\n\n1: For player 1 \t2: For player 2 \t0: Stop playing\n\n')
    if which_player == '0':
      break
    elif which_player == '1':
      player = player1
    elif which_player == '2':
      player = player2
    else:
      print('Invalid option')
      continue
    
    while True:
      
      choice = input(f'\nWellcome {player}!\n\nPlease select an action: \n\n1: attack \t2: deck info \t3: pass\n\n')

      if choice == '1':
        print('\nSelect one of the following units:\n')
        for i in range(len(player.units)):
          print(f'{i+1}: {player.units[i].name}')
        which_unit = int(input('\n'))-1
        print(f'\nPlayer has summoned {player.units[which_unit]}!')
      
        play = input('\n1: Use effect \t 2:Attack\n\n')
        
        if play == '1':
          
          print('\nSelect one of the following Effect cards:\n')
          for i in range(len(player.effects)):
            print(f'{i+1}: {player.effects[i].name}')
          which_effect = int(input('\n'))-1
          
          print('\nSelect Effect target\n')
          
          which_target = int(input('1: Self \t 2: Oponent\n\n'))
          
          if which_target == '1':
          
            player.effects[which_effect].affect(player.units[which_unit])
            print(f'{player.units[which_unit].show_stats()}')

          elif which_target == '2':
            
            if player == player1:
              for i in range(len(player2.units)):
                print(f'{i+1}: {player2.units[i].name}')
            which_oponent = int(input('\n'))-1
            # player.effects[which_effect].affect(player2.units[which_oponent

          print(f'\nPlayer has used {player.effects[which_effect]} on {player.units[which_unit]}!')

      if choice == '2':
        print('\n--Unit cards--\t\t --Effect cards--\n')
        for i in range(len(player.units)):
          print(f'{player.units[i].name}    \t {player.effects[i].name}')

      if choice =='3':
        break

@app.route("/")
def hello_world():
    return render_template('index.html', list=list)


app.run(debug=True)

main()