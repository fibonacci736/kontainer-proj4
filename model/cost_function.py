def cost_function(yard):
    yard = [list(bay) for bay in yard] # make a copy
    all_containers = []
    for i in yard:
        all_containers = all_containers + i
    all_numbers = list(set(all_containers))
    verplaatsingen = 0
    for n in all_numbers:
        for b in yard:
            l = 0
            while n in b:
                v = False
                if b[l] == n:
                    del b[l]
                    v = True
                    verplaatsingen += 2*l
                if len(b) > 0 and b[-(l+1)] == n:
                    del b[-(l+1)]
                    v = True
                    verplaatsingen += 2*l
                if v == False:
                    l += 1
    return verplaatsingen