#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:37:22 2024

@author: pramitiii
"""
import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, grid):
        potential_moves = [(i, j) for i in range(len(grid)) for j in range(len(grid[i]))
                           if grid[i][j] is None]
        if potential_moves:
            new_x, new_y = random.choice(potential_moves)
            grid[self.x][self.y] = None 
            grid[new_x][new_y] = self  
            self.x, self.y = new_x, new_y  
            return True
        return False

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []
        for _ in range(num_agents):
            self.add_agent()

    def add_agent(self):
        while True:
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            if self.grid[x][y] is None:
                agent = Agent(x, y)
                self.grid[x][y] = agent
                self.agents.append(agent)
                break

    def update(self):
        for agent in self.agents:
            agent.move(self.grid)

def main():
    grid_width = 10
    grid_height = 10
    num_agents = 5
    num_iterations = 20

    world = World(grid_width, grid_height, num_agents)

    try:
        for iteration in range(num_iterations):
            world.update()
            print(f"--- Iteration {iteration + 1} ---")
            for i, row in enumerate(world.grid):
                print(" ".join(["A" if cell else "." for cell in row]))
            print("\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Simulation has completed.")

if __name__ == "__main__":
    main()