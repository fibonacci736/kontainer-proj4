class Bay(list[int]):
    def __init__(self,N_stacks):
        super().__init__(0 for i in range(N_stacks))


    @property
    def N_stacks(self):
        return len(self)

    def is_empty_bay(self):
        return not any(self)

    def is_empty(self,i_stack):
        return not self[i_stack]

    def is_accessible(self,i_stack):
        if self.is_empty_bay() or i_stack in [0,self.N_stacks-1]:
            return True
        #stack needs to be next to exactly 1 empty stack
        return self.is_empty(i_stack-1) ^ self.is_empty(i_stack+1)

class Yard(list[Bay]):
    def __init__(self,N_bays,N_stacks):
        super().__init__(Bay(N_stacks) for i in range(N_bays))

    @property
    def N_bays(self):
        return len(self)

    @classmethod
    def from_list(cls, yard_list):
        N_bays = len(yard_list)
        yard = cls(N_bays,0)
        for i,bay_list in enumerate(yard_list):
            yard[i].extend(bay_list)
        return yard

    def locations(self):
        for i in range(self.N_bays):
            for j in range(self[i].N_stacks):
                yield (i ,j)

    def __hash__(self):
        summary = tuple( self[i][j] for i,j in self.locations() )
        return hash(summary)
    def copy(self):
        clone = Yard(self.N_bays,0)
        for i in range(self.N_bays):
            clone[i].extend(self[i])
        return clone


