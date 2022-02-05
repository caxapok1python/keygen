import argparse
import string
import random
from colorama import *

VERSION = 1.3

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--preset', type=int, default=2)

parser.add_argument('-q', '--quantity', type=int, default=1)
parser.add_argument('-o', '--output', type=str, default=None)
parser.add_argument('-v', '--verbose', action='count', default=0)
parser.add_argument('--version', action='version', version=f"Keygen by caxapok v{VERSION}")
args = parser.parse_args()

if args.verbose:
    print(args)


init()

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
SEP = '-' * 25

PRESETS = {
    1: {
        'length': 8,
        'lowercase': 4,
        'uppercase': 2,
        'digits': 2,
        'punctuation': 0
    },
    2: {
        'length': 10,
        'lowercase': 5,
        'uppercase': 2,
        'digits': 2,
        'punctuation': 1
    },
    3: {
        'length': 12,
        'lowercase': 5,
        'uppercase': 3,
        'digits': 2,
        'punctuation': 2
    },
    4: {
        'length': 15,
        'lowercase': 6,
        'uppercase': 3,
        'digits': 3,
        'punctuation': 3
    },
    5: {
        'length': 18,
        'lowercase': 7,
        'uppercase': 4,
        'digits': 4,
        'punctuation': 3
    },
    6: {
        'length': 20,
        'lowercase': 10,
        'uppercase': 5,
        'digits': 3,
        'punctuation': 2
    }
}


def main():
    settings = PRESETS[args.preset]
    if not args.output:
        for x in range(args.quantity):
            lowercase = set(''.join(random.sample(LOWERCASE, settings['lowercase'])))
            uppercase = set(''.join(random.sample(UPPERCASE, settings['uppercase'])))
            digits = set(''.join(random.sample(DIGITS, settings['digits'])))
            punctuation = set(''.join(random.sample(PUNCTUATION, settings['punctuation'])))
            all_symbols = lowercase | uppercase | digits | punctuation
            all_symbols = list(all_symbols)
            password = ''
            for i in range(len(all_symbols)):
                taken = random.choice(all_symbols)
                all_symbols.remove(taken)
                password += taken
            print(password)
    else:
        with open(args.output, 'w') as file:
            for x in range(args.quantity):
                lowercase = set(''.join(random.sample(LOWERCASE, settings['lowercase'])))
                uppercase = set(''.join(random.sample(UPPERCASE, settings['uppercase'])))
                digits = set(''.join(random.sample(DIGITS, settings['digits'])))
                punctuation = set(''.join(random.sample(PUNCTUATION, settings['punctuation'])))
                all_symbols = lowercase | uppercase | digits | punctuation
                all_symbols = list(all_symbols)
                password = ''
                for i in range(len(all_symbols)):
                    taken = random.choice(all_symbols)
                    all_symbols.remove(taken)
                    password += taken
                file.write(f'{password}\n')
            file.close()


main()
