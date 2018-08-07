class IndividualGene:
    def __init__(self, configuration):
        self.configuration = configuration

    def mutate(self):
        pass

    def crossover(self, other):
        pass

    def fitness(self):
        pass

    def path(self):
        pass


class Configuration:
    def __init__(self, board_size, start_row, start_col, generation_max):
        self.board_size = board_size
        self.start_row = start_row
        self.start_col = start_col
self.generation_max = generation_max
