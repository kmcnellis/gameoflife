#! /usr/bin/env python3

class GameOfLife():

    def run(self):
        print("I don't do much, yet.")

    def init(self,pattern):
        self.pattern = pattern

    def evolve(self,x,y):
        neighbors = [(-1,-1), (-1,0), (0,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        count = 0
        for (nx, ny) in neighbors:
            if (x+nx, y+ny) in self.pattern:
                count +=1
        if count < 2:
            return 0
        print("I don't do much, yet.")
        return 0


if __name__ == "__main__":
    GameOfLife().run()
