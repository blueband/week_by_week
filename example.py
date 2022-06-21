import pandas
from week_by_week import WeekRange

df = pandas.read_csv('./raw_events.csv')
w = WeekRange(df, 'timestamp', WK_start='mon')
print(w.getAllweeks())