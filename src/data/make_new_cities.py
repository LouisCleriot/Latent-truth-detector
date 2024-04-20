import pandas as pd
import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.flow as naf
import random

# Load the data
cities = pd.read_csv('data/true-false-datasets/curated/cities.csv')

actual_relation = "The city of {} is in {}"
new_relation = "{} is located in the country of {}"

city_list = list(cities['city'])
country_list = list(cities['country'])

# Data Augmentation
#key_aug = nac.KeyboardAug()
#cities['augm_key'] = cities['statement'].apply(lambda x: key_aug.augment(x) if len(x.split(' ')) > 3 else x)

augm = naf.Sometimes([
    naw.RandomWordAug(action="delete",stopwords = city_list + country_list + ['is','in']),
    naw.SynonymAug(aug_src='wordnet'),
    random.choice([
        naw.BackTranslationAug(from_model_name='facebook/wmt19-en-de',to_model_name='facebook/wmt19-de-en',device='cuda:0',max_length=15),
        naw.BackTranslationAug(from_model_name='facebook/wmt19-en-ru',to_model_name='facebook/wmt19-ru-en',device='cuda:0',max_length=15)])   
], aug_p=0.5)
# augm1 = naw.SynonymAug(aug_src='wordnet')
# augm2 = naw.RandomWordAug(action="delete",stopwords = city_list + country_list + ['is','in'])
# augm3 = naw.BackTranslationAug(from_model_name='facebook/wmt19-en-de',to_model_name='facebook/wmt19-de-en',device='cuda:0',max_length=20)
# augmentations = [augm1,augm2,augm3]
# for i,row in cities.iterrows():
#     n = random.randint(0,3)
#     if n == 3:
#         continue
#     augm = augmentations[n]
#     cities.at[i,'statement'] = augm.augment(row['statement'])[0]
#     print(row['statement'])
cities['statement'] = cities['statement'].apply(lambda x: augm.augment(x)[0])

    

# Create a new column with the new relation and cut the beginning The city of 
#cities['statement'] = cities['statement'].apply(lambda x: new_relation.format(x.split('The city of ')[1].split(' is in ')[0],x.split(' is in ')[1]))

# Save the new data

cities.to_csv('data/true-false-datasets/curated/cities_augm.csv',index=False)