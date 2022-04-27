# 🐝 Solve for the NYT Spelling Bee game!

```
./spellingbee.py --help
usage: spellingbee.py [-h] [required_letter] [allowed_letters]

🐝 NYT Spelling Bee solutions' finder!

positional arguments:
  required_letter  required letter (default: u)
  allowed_letters  allowed letters (in any order) (default: iptnea)

optional arguments:
  -h, --help       show this help message and exit
```


### Example

```
./spellingbee.py f ioctne
creating possibilities for: [f, ioctne]
loading entire lexicon...
OK - locked n' loaded! cross checking N possible words: 267751
attempting to find solutions...
---
allowed letters: ['i', 'o', 'c', 't', 'n', 'e']
required letter: f
OK - found 48 possible words!
coeffect
coefficient
coffee
coffin
coffinite
coiffe
coinfect
confect
confection
confetti
confetto
confine
confit
effect
effete
efficience
efficient
enfeoff
fecit
feint
fence
fennec
feoff
feoffee
ficin
fiction
fient
fifteen
finfoot
finite
finito
fitte
footie
footnote
inefficient
infect
infection
infeft
infeoff
inficete
infinite
nonfiction
nonfinite
offence
office
often
tiffin
toffee
OK - predicted score: 60
```
