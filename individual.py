import random

class individual:
    
    # The solutions's genome, a list of moves
    gene = list()

    # Possible moves
    moves = ['nnw', 'nne', 'een', 'ees', 'sse', 'ssw', 'wws', 'wwn']

    # Mutation percentage
    mPercentage = 0.25
    
    def __init__(self, configuration, gene=None):
        self.configuration = configuration
        if gene is None:
            self.gene = self.create()
        else:
            if len(gene) != configuration.board_size * configuration.board_size:
                raise Exception
            self.gene = gene
        self.cost = self.fitness()
    
    def mutate(self):
        newGene = self.gene
        
        for i in range(int(self.configuration.board_size * self.configuration.board_size * self.mPercentage)):
            randomNo = random.randint(1, self.configuration.board_size * self.configuration.board_size - 1)
            replace = self.moves[random.randint(0, 7)]
            while replace == newGene[randomNo]:
                replace = self.moves[random.randint(0, 7)]
            newGene[randomNo] = replace
        
        return individual(self.configuration, newGene)

    def crossover(self, other):
        randomNo = random.randint(1, self.configuration.board_size * self.configuration.board_size - 1)
        newGene = self.gene[0:randomNo] + other.gene[randomNo:]
        return individual(self.configuration, newGene)

    def create(self):
        t = ''
        for i in range(self.configuration.start_row):
            t = t + 's'
        for i in range(self.configuration.start_col):
            t = t + 'e'
        created_list = [t]
        for i in range(self.configuration.board_size * self.configuration.board_size - 1):
            created_list.append(self.moves[random.randint(0, 7)])
        return created_list
    
    def fitness(self):
        count = 0
        point = [self.configuration.start_row, self.configuration.start_col]
        fitCount = 0
        traversedList = []
        for i in self.gene:
            count += 1
            if count == 1:
                continue
            
            if i[0:1] == 'n':
                point[0] -= 2
            elif i[0:1] == 's':
                point[0] += 2
            elif i[0:1] == 'e':
                point[1] += 2
            elif i[0:1] == 'w':
                point[1] -= 2

            if i[2:3] == 'n':
                point[0] -= 1
            elif i[2:3] == 's':
                point[0] += 1
            elif i[2:3] == 'e':
                point[1] += 1
            elif i[2:3] == 'w':
                point[1] -= 1
            
            # Has to be a valid point
            if not (point[0] > 0 and point[0] <= self.configuration.board_size
                and point[1] > 0 and point[1] <= self.configuration.board_size):
                break

            # has to be not traversed already
            pt = str(point[0]) + str(point[1])
            if pt in traversedList:
                break
            
            fitCount += 1
            traversedList.append(pt)
        
        return fitCount
    
    def path(self):
        count = 0
        point = [self.configuration.start_row, self.configuration.start_col]
        traversedList = []
        for i in self.gene:
            count += 1
            if count == 1:
                pt = "[" + str(point[0]) + "," + str(point[1]) + "]"
                traversedList.append(pt)
                continue
            
            if i[0:1] == 'n':
                point[0] -= 2
            elif i[0:1] == 's':
                point[0] += 2
            elif i[0:1] == 'e':
                point[1] += 2
            elif i[0:1] == 'w':
                point[1] -= 2

            if i[2:3] == 'n':
                point[0] -= 1
            elif i[2:3] == 's':
                point[0] += 1
            elif i[2:3] == 'e':
                point[1] += 1
            elif i[2:3] == 'w':
                point[1] -= 1
            
            # Has to be a valid point
            if not (point[0] > 0 and point[0] <= self.configuration.board_size
                and point[1] > 0 and point[1] <= self.configuration.board_size):
                break

            # has to be not traversed already
            pt = "[" + str(point[0]) + "," + str(point[1]) + "]"
            if pt in traversedList:
                break
            
            traversedList.append(pt)
        
        return traversedList


class Configuration:
    def __init__(self, board_size, start_row, start_col, generation_max):
        self.board_size = board_size
        self.start_row = start_row
        self.start_col = start_col
        self.generation_max = generation_max


config = Configuration(10, 5, 5, 1)
g = individual(config)
print("g", g.fitness())
h = individual(config)
print("h", h.fitness())
i = g.crossover(h)
print("crossover", i.fitness())
j = g.mutate()
print("mutate", j.fitness())
print("path", j.path())