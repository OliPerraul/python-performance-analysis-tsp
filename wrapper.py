
class AlgorithmWrapper:
    def __init__(self, content):
        self.name = content[0]
        self.color = content[1]
        self.algorithm = content[2]

        # will contain data points to be plotted
        self.x = []
        self.correct = []
        self.complex = []

        self.working_correct = [] # use to compute the average
        self.working_complex = []

        self.avg_x = []
        self.avg_correct = []
        self.avg_complex = []


    def get_closure(self, adj, order):
        def closure():
            return self.algorithm(adj, order)
        return closure