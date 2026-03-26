import pandas as pd

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = "FAKE"
true["label"] = "REAL"

df = pd.concat([fake, true])

df = df[["title", "text", "label"]]

df.to_csv("fake_news.csv", index=False)

print("Dataset prepared!")