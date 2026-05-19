class Personi:
    def __init__(self, emri, vjet,kg,gjatsia):
        self.emri = emri
        self.vjet = vjet
        self.kg = kg
        self.gjatsia = gjatsia

    def emriPersonit(self):
        print(f"emri i personit eshte {self.emri}" )


    def njeri(self):
        if self.vjet > 16:
            print("personi eshte i rritur ")

        else :

            print("personi eshte femije")

    def bmi(self):
       return self.kg / (self.gjatsia **2)

    def get_bmi(self):
        Bmi = self.bmi()

        if Bmi < 18:
            return"i holle"
        elif 24 <=Bmi <30:
            return "je nvij"
        else:
            return"po plas"

     












