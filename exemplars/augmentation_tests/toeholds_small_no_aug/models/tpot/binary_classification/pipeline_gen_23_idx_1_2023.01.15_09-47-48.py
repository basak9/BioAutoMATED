import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import OneHotEncoder, StackingEstimator
from xgboost import XGBClassifier
from sklearn.preprocessing import FunctionTransformer
from copy import copy

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

# Average CV score on the training set was: 0.8299122807017543
exported_pipeline = make_pipeline(
    make_union(
        FunctionTransformer(copy),
        OneHotEncoder(minimum_fraction=0.2, sparse=False, threshold=10)
    ),
    XGBClassifier(learning_rate=1.0, max_depth=1, min_child_weight=14, n_estimators=100, n_jobs=1, subsample=1.0, verbosity=0)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
