import numpy as np
import pandas as pd

a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 4, 3, 2, 1])
aM = np.mean(a)
aMax = np.max(a)
aMin = np.min(a)
a_b_dot = np.dot(a, b)
reshape = np.reshape(a, (5, 1))
reshape2 = a.reshape(5, 1)


print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("Mean of a =", aM)
print("Max of a =", aMax)
print("Min of a =", aMin)
print("Dot product of a and b =", a_b_dot)
print("Reshaped a (5, 1):\n", reshape)
print("Reshaped a (5, 1) using method:\n", reshape2)

print("Pandas Series:\n")

df = pd.DataFrame({
"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
"Age": [20, 22, 19, 21, 20],
"Grade": ["A", "B", "A", "C", "B"],
"Marks": [85,78,92,64,74]

})
print(df)
print(df[1:4])
print(df[["Name", "Marks"]])
print(df[df["Grade"] == "A"])
