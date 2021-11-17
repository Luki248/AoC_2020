#!/usr/bin/env python3

# Advent of Code
# Day 24
# https://adventofcode.com/2020/day/24


input = [line.rstrip('\n') for line in open("input.txt")]

# Geometry of Hexagonal Tiles
DIST_HOR = 1
DIST_VER = 1
DIST_DIA_HOR = (DIST_HOR / 2)
DIST_DIA_VER = DIST_VER
DIR_E = [DIST_HOR,      0]
DIR_W = [-DIST_HOR,      0]
DIR_SE = [DIST_DIA_HOR, -DIST_HOR]
DIR_SW = [-DIST_DIA_HOR, -DIST_HOR]
DIR_NW = [-DIST_DIA_HOR,  DIST_VER]
DIR_NE = [DIST_DIA_HOR,  DIST_VER]
GRID_MAX = 100


class TileCoord:
    x = 0
    y = 0
    is_tile_white = True

    def __init__(self):
        self.x = 0
        self.y = 0
        self.is_tile_white = True

    def add(self, dist):
        self.x += dist[0]
        self.y += dist[1]


def generate_all_tiles(all_tiles):
    for x in range(-GRID_MAX, GRID_MAX):
        for y in range(-GRID_MAX, GRID_MAX):
            tile = TileCoord()
            tile.y = y
            if y % 2 == 0:
                tile.x = x
            else:
                tile.x = x + 0.5
            all_tiles.append(tile)


def get_tile_coordinate(line):
    coord = TileCoord()
    i = 0
    while i < len(line):
        if line[i] == "e":
            coord.add(DIR_E)
            i += 1
        elif line[i] == "w":
            coord.add(DIR_W)
            i += 1
        elif line[i] == "s":
            if line[i+1] == "e":
                coord.add(DIR_SE)
                i += 2
            else:
                coord.add(DIR_SW)
                i += 2
        elif line[i] == "n":
            if line[i+1] == "w":
                coord.add(DIR_NW)
                i += 2
            else:
                coord.add(DIR_NE)
                i += 2
        else:
            assert False, "Unknown Direction"
    return coord


def flip_tile(all_tiles, coord):
    for tile in all_tiles:
        if (tile.x == coord.x) and (tile.y == coord.y):
            if tile.is_tile_white:
                tile.is_tile_white = False
            else:
                tile.is_tile_white = True


def get_color_of_tile(all_tiles, tile_adj):
    for tile in all_tiles:
        if (tile.x == tile_adj.x) and (tile.y == tile_adj.y):
            return tile.is_tile_white
    #assert False, "Code Line should not be reached!"
    print(tile_adj.x, tile_adj.y)
    return True


def flip_tiles_after_day(all_tiles):
    for x in range(-GRID_MAX + 1, GRID_MAX - 1):
        for y in range(-GRID_MAX + 1, GRID_MAX - 1):
            tile = TileCoord()
            tile.y = y
            if y % 2 == 0:
                tile.x = x
            else:
                tile.x += 0.5

            count = 6
            tile_adj = TileCoord()  # E
            tile_adj.add([tile.x, tile.y])
            tile_adj.add(DIR_E)
            is_white = get_color_of_tile(all_tiles, tile_adj)
            if is_white == False:
                count -= 1
            tile_adj = TileCoord()  # W
            tile_adj.add([tile.x, tile.y])
            tile_adj.add(DIR_W)
            is_white = get_color_of_tile(all_tiles, tile_adj)
            if is_white == False:
                count -= 1
            tile_adj = TileCoord()  # SE
            tile_adj.add([tile.x, tile.y])
            tile_adj.add(DIR_SE)
            is_white = get_color_of_tile(all_tiles, tile_adj)
            if is_white == False:
                count -= 1
            tile_adj = TileCoord()  # SW
            tile_adj.add([tile.x, tile.y])
            tile_adj.add(DIR_SW)
            is_white = get_color_of_tile(all_tiles, tile_adj)
            if is_white == False:
                count -= 1
            tile_adj = TileCoord()  # NW
            tile_adj.add([tile.x, tile.y])
            tile_adj.add(DIR_NW)
            is_white = get_color_of_tile(all_tiles, tile_adj)
            if is_white == False:
                count -= 1
            tile_adj = TileCoord()  # NE
            tile_adj.add([tile.x, tile.y])
            tile_adj.add(DIR_NE)
            is_white = get_color_of_tile(all_tiles, tile_adj)
            if is_white == False:
                count -= 1

            for item in all_tiles:
                if (item.x == tile.x) and (item.y == tile.y):
                    if item.is_tile_white:
                        if count == 2:
                            item.is_tile_white = False
                    else:
                        if count == 0 or count > 2:
                            item.is_tile_white = True


if __name__ == "__main__":
    all_tiles = []
    generate_all_tiles(all_tiles)

    # Puzzle 1
    for line in input:
        coord = get_tile_coordinate(line)
        flip_tile(all_tiles, coord)
        count_black_side_up = 0
        for tile in all_tiles:
            if tile.is_tile_white == False:
                count_black_side_up += 1
    print("First Puzzle:", count_black_side_up)


    # Puzzle 2
    for i in range(100):
        print("Day " + str(i))
        flip_tiles_after_day(all_tiles)
    count_black_side_up = 0
    for tile in all_tiles:
        if tile.is_tile_white == False:
            count_black_side_up += 1
    print("Second Puzzle:", count_black_side_up)
