class Animal:

    def __init__(self):
        print("Inhale, exhale")
        self.num_ojos = 2


class Pez(Animal):

    def __init__(self):
        super().__init__()
        super().num_ojos = 3


    def respirar(self):
        super().respirar()
        print("Glu glu")

    #Metodo propio
    def nadar(self):
        print("Nadaremos nadaremos en el mar el mar el mar")

nemo = Pez()
nemo.respirar()