from sklearn.ensemble import GradientBoostingRegressor
from sklearn.grid_search import GridSearchCV
from sklearn.datasets import load_boston

data = load_boston()

x = data['data']
y = data['target']

# tune hyper parameters first
model = GradientBoostingRegressor(n_estimators=3000)
parameters = {'learning_rate' : [0.1, 0.05, 0.02, 0.01], 
              'max_depth': [4, 6],
              'min_samples_leaf': [3, 5, 9, 17],
              'max_features': [1.0, 0.3, 0.1]}

gscv = GridSearchCV(model, parameters, verbose=10, n_jobs=-1, cv=4)
gscv.fit(x, y)
print "best score=", gscv.best_score_

# tune learning rate with higher n_estimators
model = gscv.best_estimator_
model.set_params(n_estimators=100000)
parameters = {'learning_rate' : [0.1, 0.05, 0.02, 0.01]}
gscv = GridSearchCV(model, parameters, verbose=10, n_jobs=-1, cv=4)
gscv.fit(x, y)
print "best score=", gscv.best_score_

