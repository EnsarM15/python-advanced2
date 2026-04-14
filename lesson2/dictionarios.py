numrat={
    "ks":"+383",
    "it":"+39",
    "al":"+355"
}

kosova =numrat["ks"]

print(kosova)

numrat ["ks"]="+299"
print(numrat["ks"])

del numrat["al"]
print(numrat)

keys = numrat.keys()
values = numrat.values()
print(keys)
print(values)