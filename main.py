
import pandas as pd
# import glob as glb 
from glob import glob

quizes_data = sorted(glob('quizes_data/quiz*.csv'))
quizes_data

merge_data = pd.concat(pd.read_csv(datafile).assign(sourcefilename = datafile)
                       for datafile in quizes_data)
merge_data

merge_data.to_csv('quizes_data\merged_quizes.csv')

print(merge_data)