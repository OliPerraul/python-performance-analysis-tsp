
class AlgorithmWrapper:
    def __init__(self, content):
        self.name = content[0]
        self.color = content[1]
        self.algorithm = content[2]

        # will contain data points to be plotted
        self.x = []
        self.correct = [] # contains data points to compute the algorithm correctness given a number of city x
        self.complex = [] # same with the complexity

        self.working_correct = [] # use to compute the average correctness
        self.working_complex = [] # use to compute the average complexity

        self.avg_x = []
        self.avg_correct = []
        self.avg_complex = []


    def get_closure(self, adj, order):
        def closure():
            return self.algorithm(adj, order)
        return closure