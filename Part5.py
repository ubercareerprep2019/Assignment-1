class TowerOfHanoi
    def __init__(self, n):
        self.RodA = [i for i in range(n, 0, -1)]
        self.RodB = []
        self.RodC = []
        self.n = n
        self.moves = 0
        self.RodCount = 3
        
