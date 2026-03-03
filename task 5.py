import pandas as pd

myList = {"cstID":[1,2,3,4,5], "cstName":["John","Jane","Doe","Smith","Brown"], "cstAge":[25,30,22,28,35]}
df = pd.DataFrame(myList)

df["ageClass"] = df["cstAge"].apply(lambda x: "Young" if x < 30 else "Old") 
#df.drop("ageClass", axis=1, inplace=True)
df.to_csv("customer_data.csv", index=False)
print(df)

lm = pd.read_csv("customer_data.csv")
print(lm)