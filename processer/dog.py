import random
import os
import leancloud
from buffercache import BufferCache

class Dog():
    def __init__(self, size=100):
        self.buffer_manager = BufferCache(timeout=300000)
        self.dog_size = size

        def _dog_getter(self):
            self._dog_query()
            return (self.dog_size, self.dog_set)

        self.buffer_manager.set_getter(_dog_getter)

    def _dog_query(self):
        # init
        LCID = os.environ.get("APPID", default=None)
        LCKEY = os.environ.get("APPKEY", default=None)
        leancloud.init(LCID, LCKEY)
        self.dog = leancloud.Object.extend("Dog")
        self.dog_query = self.dog.query
        self.dog_query.select('content')
        self.dog_max = self.dog_query.count()
        self.dog_set = set(self._dog_get(self.dog_size))
        self.dog_size = len(self.dog_set)
        self.dog_async = False if self.dog_size >= self.dog_max else True

    def _dog_get(self, counts):
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

        return dog_msg

    def dog_get(self, counts):
        self.dog_size, self.dog_set = self.buffer_manager.update(self).get()
        if counts < 1:
            counts = 1
        elif counts > self.dog_size:
            counts = self.dog_size

        dog_skip = random.randint(0, self.dog_size - counts)
        dog_msg = list(self.dog_set)[dog_skip: dog_skip + counts]

        if self.dog_async:
            pass

        if len(dog_msg) == 0:
            return ""
        elif len(dog_msg) == 1:
            return dog_msg[0]
        else:
            return dog_msg
