import json

import cachetools
L1 = 480 * 4
L2 = int(L1 / 2)
L4 = int(L1 / 4)
L8 = int(L1 / 8)
L16 = int(L1 / 16)

O3 = 12 * 3
O4 = 12 * 4 
O5 = 12 * 5
O6 = 12 * 6

C, Cp, D, Dp, E, F, Fp, G, Gp, A, Ap, B = [i for i in range(12)]

data = [
    {"note": O5 + C, "length": L8},
    {"note": O5 + D, "length": L8},
    {"note": O5 + E, "length": L8},
    {"note": O5 + F, "length": L8},
    {"note": O5 + E, "length": L8},
    {"note": O5 + D, "length": L8},
    {"note": O5 + C, "length": L4},
    {"note": O5 + E, "length": L8},
    {"note": O5 + F, "length": L8},
    {"note": O5 + G, "length": L8},
    {"note": O5 + A, "length": L8},
    {"note": O5 + G, "length": L8},
    {"note": O5 + F, "length": L8},
    {"note": O5 + E, "length": L4}
]

with open("kaeru-uta.json","w") as f:
    json.dump(data,f,indent=2)
print(json.dumps(data))
