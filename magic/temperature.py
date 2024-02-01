
import pandas as pd

path = "datasets/underwater_temperature.csv"
my_temp_file = pd.read_csv(path, encoding='unicode_escape')

my_temp_file.head(10)
