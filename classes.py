
import sys
import html
from enum import Enum
import requests
from fake_headers import Headers

h = Headers()

class Options(Enum):
    true_ = 'T'
    false_ = 'F'

class OptionsABC(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

class Category(Enum):
    gen = 'gen'
    sports = 'sports'
    computing = 'computing'
    politics = 'politics'
    art = 'art'
    history = 'history'
    geography = 'geography'
    celebrities = 'celebrities'
    animals = 'animals'
    anime = 'anime'
    nature='nature'
    books = 'books'
    math = 'math'


class Difficulty(Enum):
    easy = 'easy'
    medium = 'medium'
    hard = 'hard'
    any1 = 'any' 

class Questions:
    # TOTAL = 10
    score = 0
    CATS = { 'gen':9, 'books':10,  'nature':17, 'computing':18, 'math':19, 'sports':21,'geography':22, 'history':23, 
    'politics':24, 'art':25, 'celebrities':26, 'animals':27, 'anime':32      }

    def __init__(self,cat,level,total):
        self.TOTAL = total
        cat_selected = self.CATS[cat.value]
        if level.value == 'any':
            url = f'https://opentdb.com/api.php?amount=10&category={cat_selected}&type=multiple'
        else:    
            url = f'https://opentdb.com/api.php?amount=10&category={cat_selected}&difficulty={level.value}&type=multiple'

        print(f"\nCATEGORY: {cat.value}, DIFFICULTY: {level.value}")
        self.r = requests.get(url, headers=h.generate())
        self.question_bank_ABC = []
        
        for item in self.r.json()['results']:
            opts = [html.unescape(i) for i in item['incorrect_answers']]
            opts.append(html.unescape(item['correct_answer']))

            self.question_bank_ABC.append({'Q':html.unescape(item['question']), 'A':item['correct_answer'], 
            'WA':item['incorrect_answers'], 
            'Options':sorted(opts)})

        self.level = level
        self.get_questions(self.level)
    

    def get_questions(self,level):
        url = f'https://opentdb.com/api.php?amount=10&category=9&difficulty={level.value}&type=boolean'
        self.r2 = requests.get(url, headers=h.generate()) 
        self.question_bank = [{'Q':html.unescape(i['question']), 'A':i['correct_answer']} for i in self.r2.json()['results']]

    def quizer_tf(self):
        '''True/False quiz brain '''
        if len(self.r2.json()['results']) > 0:
            for num, item in enumerate(self.question_bank):
                print(f"\n{num+1}. {item['Q']} \n(True or False. Enter T or F)")
                print('-------------------------------------------')
                user_answer = input('\nEnter your option: ').upper()
                while user_answer not in [i.value for i in Options]:
                    print('\n **** Invalid Input. *** \nPlease Enter T or F')
                    user_answer = input('Enter your option: ').upper()
                if user_answer == item['A'][0].upper():
                    self.score += 1
                    print(f'Correct. \nCurrent Score:\t{self.score}/{self.TOTAL}\n')
                    print('---------------------------------------')
                else:
                    print('---------------------------------------')
                    print(f"**** Oops, wrong answer. \n")
                
            print('\n****************************')
            print(f'\nFinal Score:\t{self.score}/{self.TOTAL}')
            print('\n****************************')
        else:
            print('Not available. Try another option')
            sys.exit()

    def quizer_mcq(self):
        '''multiple choice quiz brain '''
        if len(self.r.json()['results']) > 0:
            for num, item in enumerate(self.question_bank_ABC):
                print(f"\n\n{num+1}. {item['Q']}")
                print('-------------------------------------------')
                show_options = {'A': item['Options'][0], 'B':item['Options'][1],
                'C': item['Options'][2], 'D':item['Options'][3]}
                [print(f"{k}. {v}",sep='\n') for k,v in show_options.items()]
                user_answer = input('\nEnter your option (A, B, C, or D): ').upper()
                while user_answer not in [i.value for i in OptionsABC]:
                    print('\n **** Invalid Input. *** \nPlease Enter A, B, C, or D')
                    user_answer = input('Enter your option: ').upper()
                
                if show_options[user_answer] == item['A']:
                    self.score += 1
                    print(f'Correct. \nCurrent Score:\t{self.score}/{self.TOTAL}\n')
                    print('---------------------------------------')
                else:
                    print('---------------------------------------')
                    print(f"**** Oops, wrong answer. \n The Correct answer is: {item['A']}")

            print('\n****************************')
            print(f'\nFinal Score:\t{self.score}/{self.TOTAL}')
            print('\n****************************')
        else:
            print('Not available. Try another option')
            sys.exit()