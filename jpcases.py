import pandas as pd
import matplotlib.pyplot as plt
import subprocess as sp
#URL = "https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv"
sp.call("wget https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv", shell=True)
df = pd.read_csv("newly_confirmed_cases_daily.csv")
#df = df.sort_values('Tokyo')
x_dt = pd.to_datetime(df['Date'])
def main():
 plt.figure(figsize=(16,6))
 plt.bar(x_dt,df['Tokyo'])
 plt.savefig('result.png')
 plt.show()
main()
#if __name__ == "__main__":
#  main()
