import random
from infections import *

class Infections:

    def __init__(self):
        
        self.traces_type_list = TRACE_TYPES
        self.persistance_type_list = PERSISTENCE_TYPES

        self.applied_traces = random.sample(list(self.traces_type_list.keys()), random.randint(5, min(9, len(self.traces_type_list))))
        self.persistance = list(self.persistance_type_list.keys())[random.randint(0, len(self.persistance_type_list)-1)]


    def get_infection(self, id: str):

        if id in self.applied_traces:
            infec = self.traces_type_list.get(id, None)
            if infec: return infec
        elif id == self.persistance:
            infec = self.persistance_type_list.get(id, None)
            if infec: return infec
        else:
            return "Invalid Infection"
