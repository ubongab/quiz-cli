import typer
from classes import *

app = typer.Typer()

@app.command()
def mcq(cat:Category, level:Difficulty,total:int = typer.Argument(10)):
    '''Multiple Choice quiz rendering'''
    play = True
    while play:
        print('\nNo. of Questions: ',total)
        q = Questions(cat,level, total)
        q.quizer_mcq()
        again = input('\nPress any key to quit \n(Press y to play again): ')
        if again not in ['y','Y']:
            print('Thanks for playing, goodbye!')
            play = False

@app.command()
def tf(cat:Category, level:Difficulty, total:int = typer.Argument(10)): 
    '''True of False quiz rendering'''
    play = True
    while play:
        print('\nNo. of Questions: ',total)
        q = Questions(cat,level,total)
        q.quizer_tf()
        again = input('\nPress any key to quit \n(Press y to play again): ')
        if again not in ['y','Y']:
            print('Thanks for playing, goodbye!')
            play = False


if __name__ == '__main__':
    app()




