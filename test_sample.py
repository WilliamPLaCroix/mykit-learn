import pytest

import sklearn as sk
from sklearn.linear_model import LinearRegression as sklr
import numpy as np
import pandas as pd
import linear_model as lm


import random

class TestLinearRegression:
    X = np.array([random.randint(-100, 100) for i in range(10)]).reshape(-1, 1)
    y = np.array([random.randint(-10, 10) for i in range(10)])
    test_model = lm.LinearRegression()
    test_model.fit(X, y)
    verification_model = sk.linear_model.LinearRegression()
    verification_model.fit(X, y)

    def test_coef(self):
        assert format(self.test_model.coef_.item(), '.14f') == format(self.verification_model.coef_[0], '.14f')
    
    def test_intercept(self):
        assert format(self.test_model.intercept_, '.14f') == format(self.verification_model.intercept_, '.14f')

    def test_predict(self):
        passed = True
        for pair in zip(self.test_model.predict(self.X), self.verification_model.predict(self.X)):
            if format(pair[0], '14f') != format(pair[1], '14f'):
                passed = False
        assert passed == True

    def test_score(self):
        assert format(self.test_model.score(self.X, self.y), '.14f') == format(self.verification_model.score(self.X, self.y), '.14f')

    def test_score_weights(self):
        with pytest.raises(NotImplementedError):
            self.test_model.score(self.X, self.y, np.ones((len(self.y), 1)))
