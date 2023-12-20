# Ideas
- Workout Tracker
- TV Show tracker
- ASCII Paint
- ASCII Map editor and game
- ASCII r/place

# ASCII Map editor and game

## Concept

### Editor

```mermaid
graph LR
a[ascii]--java-->b[encoded game]
```
```
  o
    o
      o  o o
       o o
```

- `o` = coin
- `./game upload file.txt`

### Game

```mermaid
graph LR
a[encoded game]--java-->b[ascii]
```

- Player can move left, right, and falls constantly
- Renders line of player-1 and ~5 lines more

- `./game play name`
- `./game list`

## Tables

- Maps(name)

## Encoding

### What needs to be stored?
- x and y values of coins

### How to read it?
- y=line number
- x=char number

### How to store it?
- Coin(x, y, map)

## Decoding

- for every line, if `SELECT * FROM Coin WHERE map=? AND y=?` yields a result, print `o` at `Coin.x`.
- Alternatively, cache coins `SELECT * FROM Coin WHERE map=?`.

## Game

### Event loop

- Every tick, call render, clearing the screen and printing the new frame

### Render

- Keep track of player's x and y position in memory
- First rendered line is reserved for player, python: `" " * x-1 + "V"`
- print lines $[y+1; y+5]$ similarly to player line

### Logic

- if exists coin with position equals player position, increment score
- Only print score to keep it simple
- every tick, increase player's y position

# ASCII Place

```
############################################################################
#      .                  *                     *                   
#            *        .          *        .           *        .       .
#    .         .            .          .     *            .         *
# *     ,_          *   .-.-------.               .           .          .
#     __(_\   .        //^\\       \  *      .         . *           . 
#   ~( _ )    ___      \\_//_______/                    .--------.-.
#^^^ // >>^^,/ _ )~ ^^/[_=/]______]^^^^^^^^^^^^^^^^^^^^/        //^\\^^^^^^^
#          /_/< \\   /_(=/ (o)  (o)                    \________\\=//
#                           ~    ~             ^^      [________[\__]\
#    ^^^               ^^          .="=.               (o)    (o)`\=)_\
#                             /\_ /|6 6|\ _/\           ~      ~
#          )     ^^           \_//O\_+_/O\\_/
#        o ,( o                \\\/`"""`\///                      ^^
#      o =(_,)= o               \   ($)   /     ^^^
#      o ="  "= o      ^^^     ./---/_\---\.
#        o oo o               /`"---------"`\          ^^  
#                            /   /   |   \   \                     ^^^
#     ^^                     /   /   |   \   \   ^^
#jgs              ^^^        `._._.-'-._.-'-.'            ^^
##############################################################################
```

- Players can replace a character every 10 seconds
- 100x100 canvas
- History is stored in db as well

## UX

- up/right/left/down controls, cursor is indicated by (blinking?) #
- screen is refreshed continuously
- press character key to insert