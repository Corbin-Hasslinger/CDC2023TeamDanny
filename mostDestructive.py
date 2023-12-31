import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

with open('dataset.pkl', 'rb') as file:
    df = joblib.load(file)

class_counts= df["FIRE_SIZE_CLASS"].value_counts()

total_fire_sizes = {fire_class: 0 for fire_class in df['FIRE_SIZE_CLASS'].unique()}

for i in range(len(df['FIRE_SIZE'])):
    fire_size = df.at[i, 'FIRE_SIZE']
    fire_class = df.at[i, 'FIRE_SIZE_CLASS']
    
    total_fire_sizes[fire_class] += fire_size

myKeys = list(total_fire_sizes.keys())
myKeys.sort()
sorted_dict = {i: total_fire_sizes[i] for i in myKeys}

def total_damage_count():
    x  = [int(x) for x in list(sorted_dict.values())]
    y = list(sorted_dict.keys())
    data = pd.DataFrame({'Classes': y, 'Damage': x})

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Classes", y="Damage", data=data, palette="Blues_d", orient='x')
    plt.xlabel('Total Damage Acreage', fontsize=12)
    plt.ylabel('Classes', fontsize=12)
    plt.title('Most Damaging Classes of Fire', fontsize=14)

    plt.show()

total_damage_count()