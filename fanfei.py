from itertools import groupby
class FastaFile:
    def __init__(self, path):
        self.path = path
        self._map = {}
        self.__fasta_iter()
    def __str__(self):
        return self._map.__str__()
    def __fasta_iter(self):
        fh = open(self.path)
        faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
        for header in faiter:
            header = header.next()[1:].strip()
            seq = "".join(s.strip() for s in faiter.next())
            self._map[header] = seq
ff = FastaFile("z.fa")
print (ff)
