# "Find a path between words" game

This is a simple projet to implement a CLI solution finder for this funny game.

## The rules of the game

Choose a source word and a destination word (they must be of the same length).
Then try to go from the source word to the destination by changing only one letter at a time.
But each step word must be a valid word!

## The project

### How to setup the game in your favorite language?

First, you have to have the latest version of Python3 for the program to work.

To make the game very customizable, and to allow the user to add his own words, it's up to you to choose the list of words. The default here is a list of 370 000 english words.

If you want to change it, you can just replace this file. It must be a file in which words are separated using line breaks. Change the name of your custom dictionnary to `words.txt`

Once this is done, you can run `setup.py`, it will setup the game and find links between words.
It should create a file called `words-graph.txt`.

(This step can take a couple of minutes)

### The game

Once `setup.py` has been run, you can run `main.py` and enjoy the game.

### If you want to play and find words that could work

There is a file called `find_close_words.py`, as its name suggest, it can help you find words that are related to one another.

## How it works

In `setup.py`, the program creates a graph where words are the vertices, if it is possible to go from one word to another, there is an edge between them.

Then, in `main.py`, using a Breadth First Search with Backtracking, we find a path from the source word to the destination word.

## By Maxence