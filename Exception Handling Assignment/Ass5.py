class InvalidAgeException(Exception):

    def __init__(self):
        self.msg = "Enter Valid Age"

    def __str__(self):
        return f"{self.msg}"



while 1:
    try:
        age = int(input('Enter Age: '))
        if age > 18:
            print('Eligible to vote')
        else:
            raise InvalidAgeException()
    except InvalidAgeException as e:
        print(e)
    else:
        break


