import pandas as pd
import numpy as np
import random
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'visitor': [139, 237, 326, 456]}
visitors_1 = pd.DataFrame(data)
print(visitors_1)
visitors_2=visitors_1.groupby(by="weekday")['visitor'].mean()
print(visitors_2)
print("===========================================================")
# =================================================================
cities = ['Taiwan', 'Japan', 'Austin', 'Dallas']
Populations = np.random.randint(80000000,size=4)
list_labels = ['city', 'population']
list_cols = [cities, Populations]
Combined = list(zip(list_labels, list_cols))
data=pd.DataFrame({
    "city": cities,
    "population": Populations
})
print("人口表:\n",data)
column=data["population"]
MaxP=column.idxmax()
city_list=data["city"]
MaxP_city=city_list[MaxP]
print("人口最多城市:\n",MaxP_city)