# ca-1d
Elementary Cellular Automaton

`Usage: ./main.py <RULE> <OUTPUT_LENGTH> <DELAY_MS> <WRAP> [<START>]`

`<RULE>` - decimal number representing binary mask of production rules:
```
### | ##. | #.# | #.. | .## | .#. | ..# | ...
 0     0     0     0     0     0     0     0
```

`<OUTPUT_LENGTH>` - how long the output should be in characters  
`<DELAY_MS>`      - delay between next iteration of automaton  
`<WRAP>`          - if negative wrap cells around when considering neighbours, otherwise 0 or 1 as bounds  
`<START>` - optional starting configuration bitmask as decimal number. If not specified, starting configuration will be one cell in the middle of the line with `<OUTPUT_LENGTH>` // 2 length.

---

Example:

```

./main.py 110 80 50 -1

Starting configuration is 1099511627776:

.......................................#........................................


Current ruleset is 110:

### | ##. | #.# | #.. | .## | .#. | ..# | ... | 
 .  |  #  |  #  |  .  |  #  |  #  |  #  |  .  | 

.......................................#........................................
......................................##........................................
.....................................###........................................
....................................##.#........................................
...................................#####........................................
..................................##...#........................................
.................................###..##........................................
................................##.#.###........................................
...............................#######.#........................................
..............................##.....###........................................
.............................###....##.#........................................
............................##.#...#####........................................
...........................#####..##...#........................................
..........................##...#.###..##........................................
.........................###..####.#.###........................................
........................##.#.##..#####.#........................................
.......................########.##...###........................................
......................##......####..##.#........................................
.....................###.....##..#.#####........................................
....................##.#....###.####...#........................................
...................#####...##.###..#..##........................................
..................##...#..#####.#.##.###........................................
.................###..##.##...########.#........................................
................##.#.######..##......###........................................
...............#######....#.###.....##.#........................................
..............##.....#...####.#....#####........................................
.............###....##..##..###...##...#........................................
............##.#...###.###.##.#..###..##........................................
...........#####..##.###.######.##.#.###........................................
..........##...#.#####.###....########.#........................................
.........###..####...###.#...##......###........................................
........##.#.##..#..##.###..###.....##.#........................................
.......########.##.#####.#.##.#....#####........................................
......##......######...########...##...#........................................
.....###.....##....#..##......#..###..##........................................
....##.#....###...##.###.....##.##.#.###........................................
...#####...##.#..#####.#....##########.#........................................
..##...#..#####.##...###...##........###........................................
.###..##.##...####..##.#..###.......##.#........................................
##.#.######..##..#.#####.##.#......#####........................................
######....#.###.####...######.....##...#.......................................#
.....#...####.###..#..##....#....###..##......................................##
....##..##..###.#.##.###...##...##.#.###.....................................###
...###.###.##.########.#..###..#######.#....................................##.#
..##.###.######......###.##.#.##.....###...................................#####
.#####.###....#.....##.#########....##.#..................................##...#
##...###.#...##....#####.......#...#####.................................###..##
.#..##.###..###...##...#......##..##...#................................##.#.##.
##.#####.#.##.#..###..##.....###.###..##...............................########.
####...########.##.#.###....##.###.#.###..............................##......##
...#..##......########.#...#####.#####.#.............................###.....##.
..##.###.....##......###..##...###...###............................##.#....###.
.#####.#....###.....##.#.###..##.#..##.#...........................#####...##.#.
##...###...##.#....#######.#.#####.#####..........................##...#..#####.
##..##.#..#####...##.....#####...###...#.........................###..##.##...##
.#.#####.##...#..###....##...#..##.#..##........................##.#.######..##.
####...####..##.##.#...###..##.#####.###.......................#######....#.###.
#..#..##..#.########..##.#.#####...###.#......................##.....#...####.##
#.##.###.####......#.#######...#..##.###.....................###....##..##..###.
######.###..#.....####.....#..##.#####.#....................##.#...###.###.##.##
.....###.#.##....##..#....##.#####...###...................#####..##.###.######.
....##.######...###.##...#####...#..##.#..................##...#.#####.###....#.
...#####....#..##.####..##...#..##.#####.................###..####...###.#...##.
..##...#...##.#####..#.###..##.#####...#................##.#.##..#..##.###..###.
.###..##..#####...#.####.#.#####...#..##...............########.##.#####.#.##.#.
##.#.###.##...#..####..#####...#..##.###..............##......######...########.
######.####..##.##..#.##...#..##.#####.#.............###.....##....#..##......##
.....###..#.######.#####..##.#####...###............##.#....###...##.###.....##.
....##.#.####....###...#.#####...#..##.#...........#####...##.#..#####.#....###.
...#######..#...##.#..####...#..##.#####..........##...#..#####.##...###...##.#.
..##.....#.##..#####.##..#..##.#####...#.........###..##.##...####..##.#..#####.
.###....#####.##...####.##.#####...#..##........##.#.######..##..#.#####.##...#.
##.#...##...####..##..######...#..##.###.......#######....#.###.####...####..##.
####..###..##..#.###.##....#..##.#####.#......##.....#...####.###..#..##..#.####
...#.##.#.###.####.####...##.#####...###.....###....##..##..###.#.##.###.####...
..#########.###..###..#..#####...#..##.#....##.#...###.###.##.########.###..#...
.##.......###.#.##.#.##.##...#..##.#####...#####..##.###.######......###.#.##...
###......##.##############..##.#####...#..##...#.#####.###....#.....##.######...
#.#.....#####............#.#####...#..##.###..####...###.#...##....#####....#..#
###....##...#...........####...#..##.#####.#.##..#..##.###..###...##...#...##.##
..#...###..##..........##..#..##.#####...######.##.#####.#.##.#..###..##..#####.
.##..##.#.###.........###.##.#####...#..##....######...########.##.#.###.##...#.
###.#######.#........##.######...#..##.###...##....#..##......########.####..##.
#.###.....###.......#####....#..##.#####.#..###...##.###.....##......###..#.####
###.#....##.#......##...#...##.#####...###.##.#..#####.#....###.....##.#.####...
#.###...#####.....###..##..#####...#..##.######.##...###...##.#....#######..#..#
###.#..##...#....##.#.###.##...#..##.#####....####..##.#..#####...##.....#.##.##
..###.###..##...#######.####..##.#####...#...##..#.#####.##...#..###....#######.
.##.###.#.###..##.....###..#.#####...#..##..###.####...####..##.##.#...##.....#.
#####.#####.#.###....##.#.####...#..##.###.##.###..#..##..#.########..###....##.
#...###...#####.#...#######..#..##.#####.######.#.##.###.####......#.##.#...####
#..##.#..##...###..##.....#.##.#####...###....########.###..#.....#######..##...
#.#####.###..##.#.###....#######...#..##.#...##......###.#.##....##.....#.###..#
###...###.#.#######.#...##.....#..##.#####..###.....##.######...###....####.#.##
..#..##.#####.....###..###....##.#####...#.##.#....#####....#..##.#...##..#####.
.##.#####...#....##.#.##.#...#####...#..#######...##...#...##.#####..###.##...#.
#####...#..##...##########..##...#..##.##.....#..###..##..#####...#.##.####..##.
#...#..##.###..##........#.###..##.######....##.##.#.###.##...#..#######..#.####
#..##.
```
