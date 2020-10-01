from pycaret.datasets import get_data
dataset = get_data('diamond')

#check the shape of data
dataset.shape

data = dataset.sample(frac=0.9, random_state=786)
data_unseen = dataset.drop(data.index)

data.reset_index(drop=True, inplace=True)
data_unseen.reset_index(drop=True, inplace=True)

print('Data for Modeling: ' + str(data.shape))
print('Unseen Data For Predictions: ' + str(data_unseen.shape))

from pycaret.regression import *
exp_reg101 = setup(data = data, target = 'Price', session_id=123, html=False)

best = compare_models(exclude = ['ransac'])
print(models())


