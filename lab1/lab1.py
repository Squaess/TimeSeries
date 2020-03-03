import pandas as pd


df = pd.read_csv('co2.csv', delimiter=";", index_col=0)
df = df[df.index >= "1950"]
df.index = pd.to_datetime(df.index, format="%Y-%m-%d")

annual_mean = df.groupby(df.index.year).mean()
annual_mean.plot()


import seaborn as sns
import matplotlib.pyplot as plt


monthly_df = df
nh_df = pd.DataFrame(df['data_mean_nh'])
nh_df['geo'] = "data_mean_nh"
nh_df.columns = ['value', 'geo']
gl_df = pd.DataFrame(df['data_mean_global'])
gl_df['geo'] = "data_mean_global"
gl_df.columns = ['value', 'geo']
sh_df = pd.DataFrame(df['data_mean_sh'])
sh_df['geo'] = "data_mean_sh"
sh_df.columns = ['value', 'geo']
monthly_df = pd.concat([nh_df, gl_df, sh_df])
monthly_df['month'] = monthly_df.index.strftime('%b')



sns.boxplot(
    x='month',y='value',hue='geo', data=monthly_df,
    palette="Set3")
plt.show()


monthly_df['geo'].unique()



monthly_df.info()



sns.boxplot(x='month',y='value', data=monthly_df.loc[monthly_df['geo'] == 'data_mean_nh'], palette="Set3")



sns.boxplot(x='month',y='value', data=monthly_df.loc[monthly_df['geo'] == 'data_mean_sh'], palette="Set3")



sns.boxplot(x='month',y='value', data=monthly_df.loc[monthly_df['geo'] == 'data_mean_global'], palette="Set3")