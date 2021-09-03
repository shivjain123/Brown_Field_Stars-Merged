import pandas as pd

df = pd.read_csv('D:/(4) WhiteHatJr/Third Module/Web Scraping and Analysis/Stars/brown.csv')

df = df.dropna()

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] *= 0.000954588

df["Radius"] = df["Radius"].astype(float)
df["Radius"] *= 0.102763

df.to_csv('D:/(4) WhiteHatJr/Third Module/Web Scraping and Analysis/Stars/brown_new.csv')