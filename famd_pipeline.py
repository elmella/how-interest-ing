import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
# load the data without the index column
tpot_data = pd.read_csv('famd_data.csv', index_col=0)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

# Average CV score on the training set was: 0.8322558922558922
exported_pipeline = make_pipeline(
    SelectPercentile(score_func=f_classif, percentile=39),
    GradientBoostingClassifier(learning_rate=0.1, max_depth=5, max_features=0.9000000000000001, min_samples_leaf=13, min_samples_split=9, n_estimators=100, subsample=0.9500000000000001)
)

exported_pipeline.fit(training_features, training_target)
# results = exported_pipeline.predict(testing_features)
