class Client:
    def __init__(self, id, name, age):
        self.id = id 
        self.name = name
        self.age = age


class Trainer:
    def __init__(self, id, name, specialization):
        self.id = id 
        self.name = name 
        self.specialization = specialization

class Workout:
    def __init__(self, workout_name, id, schedule):
        self.workout_name = workout_name
        self.id = id
        self.schedule = schedule

        