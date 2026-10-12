import functools
def cell_metabolism(glucose,oxygen):
 def energy_output():
        glucose_batches=glucose//1
        oxygen_batches=oxygen//6
        limiting_cycles=functools.reduce(lambda x,y:x if x<y else y,[glucose_batches,oxygen_batches])
        atp_produced=limiting_cycles*38
        return atp_produced
 return energy_output()

print(cell_metabolism(2,15))
print(cell_metabolism(2,10))