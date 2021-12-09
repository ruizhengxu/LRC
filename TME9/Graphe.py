class Graph:

    def __init__(self, noeuds, relations):
        self.noeuds = noeuds
        self.relations = relations

    def getRelations(self, i, j):
        if (i, j) in self.relations.keys():
            return set(self.relations[(i, j)])
        if (j, i) in self.relations.keys():
            return set(self.relations[(j, i)]) # Mettre transposee à la place si existe
        return set()

    