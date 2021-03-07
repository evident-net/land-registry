import land_registry
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df = land_registry.to_df('./tmp/pp-full.csv')
print(df)
line_plot = sns.lineplot(data=df.groupby('transfer_date').size(), linewidth=2.5)
fig = line_plot.get_figure()
fig.savefig("./tmp/group_by_transfer.png")

