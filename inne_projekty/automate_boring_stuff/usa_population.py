# usa_population.py - counts the total population of usa and its biggest state

import census2010 # a module with data prepared in read_census_excel.py code

all = census2010.allData

# the dictionary with total population for each state
st_pop = {}
for state in all.keys():
    if state not in st_pop:
        st_pop[state] = 0
    
    for county in all[state].keys():
            st_pop[state] += all[state][county]['pop']
            #st_pop[state] += state[county['pop']]
print(st_pop,'\n\n')

# counting total population of usa in 2010
total = 0
for key, value in st_pop.items():
    total += value

max_pop = max(st_pop.values()) # the population of the biggest state
max_st = max(st_pop, key=st_pop.get) # the state with biggest population

print('USA total population =', total, 'people')
print('The biggest state is: ', max_st, 'with', max_pop, 'people')
print('The smallest state is: ', min(st_pop, key=st_pop.get), 'with', min(st_pop.values()), 'people')

    
