class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.age = []
    
    

    def append(self, item):
        
        if len(self.storage) == self.capacity:
            oldest_element = self.age.pop(0)
            for i, element in enumerate(self.storage):
                if element == oldest_element:
                    self.storage[i] = item
                    self.age.append(item)
                    return

        else:
            self.storage.append(item)
            self.age.append(item)

            

    def get(self):
        return self.storage

