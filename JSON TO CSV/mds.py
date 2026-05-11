import pandas as pd

df = pd.read_json("mds.json")

df.to_csv("mds.csv", index=False, encoding="utf-8")
print("DONE")