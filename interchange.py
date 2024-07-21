def interchange(il):
    if len(il)>=1:
        il[0], il[-1] = il[-1], il[0]
il=[12,35,9,59,24]
print("input: ",il)
interchange(il)
print("output: ",il)
