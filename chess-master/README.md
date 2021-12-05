# chess
A simple chess made specially for termux

# features
Pure Bash script

Chess engine / computer enemy (and even computer versus computer)

Unicode support (nice Figures)

Coloured output (using ANSI Codes)

Network support (aka Multiplayer)

Permanent transposition tables (import/export)

Keyboard cursor and mouse support

Partial redraw (by cursor movements)

"Graphical" configuration (dialog utils)

# installation and usage

> git clone https://github.com/TermuxHackz/chess

> cd chess

> chmod +x chess.sh

> ./chess.sh
This will start a player versus computer game.

Additional modes and settings are available; to list them just take a look at

./chess.sh -h


*Controls*: Simply input the coordinates (first the row denoted by the letters [A]-[H], then the column according to the numbers [1]-[8]) from the figure you want to move, afterwards the target coordinates (in the same format)

# Tips and Tricks
Invalid figure selections/moves are discarded with an warning message. If you've chosen the wrong figure at the input, just re-enter the same coordinates and now you can select another figure.
For a better gaming experience (= bigger and nicer figures), use Ubunto Mono or Droid Sans Mono.
If you start a multiplayer game, the first player (with the script parameter -b "remote") should run the game script first, because he acts as server.


# Rules

For simplicity, there are some cutbacks on the implemented chess rules (yet). Besides the basic movement of figures only the pawn promotion is considered - with the limitation that pawns automatically become queens.

At the moment no special regard is taken to check/checkmate - the game ends, when one loses his king.

These limitations are at the moment mainly based on the lack of an easy incorporation with the input, but might be solved in future releases.

