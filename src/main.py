'''
Created on Dec 19, 2017

@author: pbarwis@capturehighered.com
'''

import pandas as pd
import numpy as np
from recodes import SatRecodes

# instantiate SatRecodes to get recode mapping dictionaries
sat_maps = SatRecodes()

# define function to generate sample data for examples
def example_df(lower_limit, upper_limit, colname, round_val):
    df = pd.DataFrame(np.random.randint(lower_limit,upper_limit,size=(10, 1)), columns=[colname])
    df = df.round({colname : round_val})
    return(df)


# ------------------
# Usage examples
# ------------------

print('Recode new SAT (1600 scale) to old SAT (2400 scale)')    
# generate sample data
df = example_df(400, 1600, 'new_sat_vals', -1)
# apply map
df['old_sat_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_to_old_sat_2400())
print(df)



print('Recode new SAT (1600 scale) to old SAT (1600 scale)')    
# generate sample data
df = example_df(400, 1600, 'new_sat_vals', -1)
# apply map
df['old_sat_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_to_old_sat_1600())
print(df)



print('Recode new SAT math section to old SAT math section')    
# generate sample data
df = example_df(200, 800, 'new_sat_vals', -1)
# apply map
df['old_sat_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_math_to_old_sat_math())
print(df)



print('Recode new SAT writing and language test to old SAT writing section')    
# generate sample data
df = example_df(10, 40, 'new_sat_vals', 1)
# apply map
df['old_sat_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_writing_to_old_sat_writing())
print(df)



print('Recode new SAT reading test to old SAT critical reading section')    
# generate sample data
df = example_df(10, 40, 'new_sat_vals', 1)
# apply map
df['old_sat_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_reading_to_old_sat_reading())
print(df)



print('Recode new SAT EBRW section to old SAT writing plus critical reading sections')    
# generate sample data
df = example_df(200, 800, 'new_sat_vals', -1)
# apply map
df['old_sat_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_ebrw_to_old_writingreading())
print(df)



print('Recode new SAT (1600 scale) to ACT')    
# generate sample data
df = example_df(560, 1600, 'new_sat_vals', -1)
# apply map
df['act_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_to_act())
print(df)



print('Recode new SAT writing and language section to ACT Enlish/Writing test')    
# generate sample data
df = example_df(17, 40, 'new_sat_vals', 1)
# apply map
df['act_vals'] = df['new_sat_vals'].map(sat_maps.new_sat_writing_to_act_english())
print(df)



print('Recode old SAT (2400 scale) to new SAT (1600 scale)')    
# generate sample data
df = example_df(600, 2400, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_to_new_sat_2400())
print(df)



print('Recode old SAT (1600 scale) to new SAT (1600 scale)')    
# generate sample data
df = example_df(400, 1600, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_to_new_sat_1600())
print(df)



print('Recode old SAT writing plus critical reading sections to new SAT EBRW section')    
# generate sample data
df = example_df(400, 1600, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_writingreading_to_new_ebrw())
print(df)



print('Recode old SAT math section to new SAT math section (200-800 scale)')    
# generate sample data
df = example_df(200, 800, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_math_to_new_sat_math_section())
print(df)



print('Recode old SAT math section to new SAT math test (10-40 scale)')    
# generate sample data
df = example_df(200, 800, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_math_to_new_sat_math_test())
print(df)



print('Recode old SAT writing test to new SAT writing and language section')    
# generate sample data
df = example_df(200, 800, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_writing_to_new_sat_writing())
print(df)



print('Recode old SAT critical reading test to new SAT reading section')    
# generate sample data
df = example_df(200, 800, 'old_sat_vals', -1)
# apply map
df['new_sat_vals'] = df['old_sat_vals'].map(sat_maps.old_sat_reading_to_new_sat_reading())
print(df)



print('Recode ACT to new SAT (1600 scale)')    
# generate sample data
df = example_df(11, 36, 'act_vals', 1)
# apply map
df['new_sat_vals'] = df['act_vals'].map(sat_maps.act_to_new_sat())
print(df)



print('Recode ACT English/Writing test to new SAT writing and language section')    
# generate sample data
df = example_df(11, 36, 'act_vals', 1)
# apply map
df['new_sat_vals'] = df['act_vals'].map(sat_maps.act_to_new_sat())
print(df)



if __name__ == '__main__':
    pass