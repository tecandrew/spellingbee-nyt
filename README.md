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
./spellingbee.py l tyiocd
OK - locked n' loaded! 🔫
OK -cross checking N possible words: 370106
INFO - attempting to find solutions...
INFO - allowed letters: ['t', 'y', 'i', 'o', 'c', 'd']
INFO - required letter: l
🐝 - DONE! Here are your possible answers:
        cycl - 1 points
        cyclic - 6 points
        cyclicity - 9 points
        ...
        ditolyl - 7 points
        docility - 15 points            <- is a pangram!
        ...
        tolly - 5 points
        tolt - 1 points
        tool - 1 points
OK - found 144 possible words! 4 are pangrams!
OK - estimated total score: 642
```
