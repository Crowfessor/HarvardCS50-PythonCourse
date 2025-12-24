from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit('Invalid usage')

if len(sys.argv) == 3:
    if(sys.argv[1] not in ['-f','-font'] or sys.argv[2] not in figlet.getFonts()):
        sys.exit('Invalid usage')

text = input('Input: ')

if len(sys.argv) == 1:
    r = random.choice(figlet.getFonts())
    figlet.setFont(font = r)
else:
    figlet.setFont(font = sys.argv[2])

print(figlet.renderText(text))
