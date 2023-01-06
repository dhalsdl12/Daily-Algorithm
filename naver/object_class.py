class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center " % \
            (self.name, self.position)


jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print(jinhyun)