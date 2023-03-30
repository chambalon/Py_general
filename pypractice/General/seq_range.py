
num_rng=list(range(1,21))
print(num_rng)

avg=sum(num_rng)/len(num_rng)
print("average= ", avg)

print("-----------------------------")

print("average= {}".format(sum(num_rng)/len(num_rng)))

print("-----------------------------")

total=0
for e in num_rng:
    total+=e
print("average= {}".format(total/len(num_rng)))