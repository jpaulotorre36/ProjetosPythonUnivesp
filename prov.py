class Horario:
    def__init__(self, ho,minu, seg):
        self.ho = ho 
        self.minu = minu
        self.seg = seg

    def __repr__(self):
        return str(self.ho) + ':' + str(self.minu) + ':' + str(self.seg)

ho = input("Escrevaas horas: ")

minu = input("Escreva min: ")

seg = input("segubdos:")

h = Horario(ho, minu, seg)

print(h)
