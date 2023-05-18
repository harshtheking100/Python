class Temperature:

    def __init__(self):
        self.c = None
        self.f = None

    def convertfarenheit(self):
        self.c = float(input('Enter Temperature in Celcius: '))
        celcius = (self.c * (9/5)) + 32
        return celcius

    def convertcelcius(self):
        self.f = float(input('Enter Temperature in farenheit: '))
        farenheit = (self.f - 32) * (5/9)
        return farenheit


t = Temperature()
print(t.convertcelcius())
print(t.convertfarenheit())
