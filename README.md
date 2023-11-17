# Squaredle-Answers
Simple solver for the popular online word hunt game [Squaredle](squaredle.app), by using DFS and a Trie to store a list of valid words which is originally from [this repository](https://github.com/dwyl/english-words/tree/master)
pruned to exclude words that are 3 words or less since Squaredle does not count them.

### Usage
when running [solve.py](solve.py) input squaredle board state as `abcd/efgh/ijkl/mnop` to indicate a board of:
```
a b c d
e f g h
i j k l
m n o p
```

*Note*: the words outputted will often times include more words than is recognized by Squaredle. This is because the word list used is not exactly Squaredle's word list, which is mostly based off of 
[NWL2020](https://scrabbleplayers.org/w/NWL2020), which has access restrictions.

*Disclaimer*: I am not affiliated with Squaredle in any way. Using this solver to dishonestly achieve a perfect score in a short amount of time in the interest of getting a high score 
on the leaderboard is considered cheating and strongly discouraged, of which is punishable by having such account be blocked from Squaredle's leaderboard.
