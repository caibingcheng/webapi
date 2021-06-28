import random


class Dog():
    def __init__(self, leancloud):
        self.dog = leancloud.Object.extend("Dog")
        self.dog_query = self.dog.query
        self.dog_query.select('content')
        self.dog_max = self.dog_query.count()

    def dog_getone(self, counts):
        if counts < 1:
            counts = 1
        elif counts > self.dog_max:
            counts = self.dog_max

        dog_skip = random.randint(0, self.dog_max - counts)
        self.dog_query.skip(dog_skip)
        self.dog_query.limit(counts)

        dog_msg = self.dog_query.find()
        dog_msg = [msg.get("content") for msg in dog_msg if dog_msg]
        dog_msg = [msg.encode("utf-8").decode("utf-8")
                   for msg in dog_msg if dog_msg]

        if len(dog_msg) == 0:
            return ""
        elif len(dog_msg) == 1:
            return dog_msg[0]
        else:
            return dog_msg
