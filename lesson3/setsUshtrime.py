my_set = {1,2,3}
my_set.add(7)

print(my_set)
my_set.remove(3)
print(my_set)


my_set.discard(8)
print(my_set)

print(len(my_set))

my_set.clear()
print(my_set)

print(len(my_set))

my_list = [1,2,2,3]
print(my_list)

listaUnike = set(my_list)
print(listaUnike)

listaUnike = set(my_list)
listaUnike2 = list(listaUnike)

print(listaUnike)
print(listaUnike2)

user1_interest={"music","movies","travel"}
user2_interest={"music","movies","cooking"}

rezultati = user1_interest.intersection(user2_interest)

print(rezultati)


users = {"lisa","edeni","ensari"}
personi = "lisa"
print(personi in users)

