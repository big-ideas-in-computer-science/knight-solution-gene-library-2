import random

class IndividualGene:
    
    # The solutions's genome, a list of moves
    gene = list()

    # Possible moves
    moves = ['nnw', 'nne', 'een', 'ees', 'sse', 'ssw', 'wws', 'wwn']

    # Mutation percentage
    mPercentage = 0.1
    
    # Init function. It takes a configuration which defines board size and start position. And also a gene. If a blank gene is given then a new random gene is created.
    def __init__(self, configuration, gene=None):
        self.configuration = configuration
        if gene is None:
            self.gene = self.create()
        else:
            if len(gene) != configuration.board_size * configuration.board_size:
                raise Exception
            self.gene = gene
        self.cost = self.fitness()
      
    # Mutation algo. The function mutates a percentage of the gene, given by mPercentage variable. Mutation is to change a perticular move to some other random valid move.
    def mutate(self):
        newGene = self.gene
        
        # Since the gene contains board size * board size moves, we loop to set percentage of the gene size.
        for i in range(int(self.configuration.board_size * self.configuration.board_size * self.mPercentage)):
            # Choose a random move to switch
            randomNo = random.randint(1, self.configuration.board_size * self.configuration.board_size - 1)
            # Find a random new move
            replace = self.moves[random.randint(0, 7)]
            while replace == self.gene[randomNo]:
                replace = self.moves[random.randint(0, 7)]
            # Change the gene to have the new move
            self.gene[randomNo] = replace

    # Crossover algo. The function finds a random point. Then takes the first half from first gene and second half from second gene, and combine them to form a new one.
    def crossover(self, other):
        randomNo = random.randint(1, self.configuration.board_size * self.configuration.board_size - 1)
        newGene = self.gene[0:randomNo] + other.gene[randomNo:]
        self.gene = newGene

    # Create a random gene
    def create(self):
        # Change the initial co-ordinate in the move format
        t = ''
        for i in range(self.configuration.start_row):
            t = t + 's'
        for i in range(self.configuration.start_col):
            t = t + 'e'
        created_list = [t]
        # Create random moves and append in gene
        for i in range(self.configuration.board_size * self.configuration.board_size - 1):
            created_list.append(self.moves[random.randint(0, 7)])
        return created_list
    
    # Fitness function returns the length of valid path
    def fitness(self):
        path = self.path()
        return len(path)
    
    # Path function finds a valid path in the gene. The path becomes invalid when we wander off the board or when we traverse an already traversed index.
    def path(self):
        count = 0
        point = [self.configuration.start_row, self.configuration.start_col]
        traversedList = []
        for i in self.gene:
            count += 1
            if count == 1:
                pt = [] + point
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
            pt = [] + point
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

# Testing code
# config = Configuration(10, 5, 5, 1)
# g = IndividualGene(config)
# print("g", g.fitness())
# h = IndividualGene(config)
# print("h", h.fitness())
# i = g.crossover(h)
# print("crossover", i.fitness())
# j = g.mutate()
# print("mutate", j.fitness())
# print("path", j.path())
