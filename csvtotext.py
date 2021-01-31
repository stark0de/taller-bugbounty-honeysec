import pandas as pd
import sys
import re

print("First argument is CSV, second should be destination path")

col_list = ["subdomain"]
pd.set_option('display.max_rows', 100000)
csv_data = pd.read_csv(sys.argv[1], usecols=col_list, skipinitialspace=True)
limpio = csv_data.to_string(index=False)
final = limpio.replace(" ","")
f = open(sys.argv[2], "a")
f.write(final)
f.close()

print("Your clean subdomain list is in: " + sys.argv[2])

