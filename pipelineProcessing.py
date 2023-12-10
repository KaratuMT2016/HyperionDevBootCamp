'''
Preprocessing Pipeline:

Drop Name Feature
Inpute Ages
Turn Gender into Binary/Numeric
One Hot Encode Jobs

• With pipeline we have one element passing to the next element 
• That is one pipeline feeds it output into the next pipeline 
• In pipelines we have estimators Estimators enable us to have elements fit - transform - fit - transform 
• A classifier is an estimator - K-nearest neigbours 
• In a pipeline we need estimators, in order to create estimators, we need to:
    • extend from the base estimator class, 
    • create a new class and 
    • we need to have a function fit and transform 
    • TransformerMixin means basically:
        • when we define fix and transform 
        • its going to authomatically create fit_transform(), 
        • without us having to transform it manually.
'''


import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder


class NameDropper(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self
        
    def transform(self, x):
        return x.drop(['Name'], axis=1)


class AgeImputer(BaseEstimator, TransformerMixin):
    def fit(self,x, y=None):
        return self
    def transform(self, x):
        imputer = SimpleImputer(strategy="mean") # use mean of the age to fill all missing values of age
        x['Age'] = imputer.fit_transform(x[['Age']])
        return x

class FeatureEncoder(BaseEstimator, TransformerMixin):
    def fit(self,x, y=None):
        return self
        
    def transform(self, x):
        # Change Gender into a numeric feature
        gender_dict = {"m": 0, "f": 1}
        x['Gender'] = [gender_dict[g] for g in x['Gender']]

        # OneHotEncode Jobs
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(x[['Job']]).toarray()

        column_names = ["Acountant", "Engineer", "Doctor", "Teacher", "Programmer"]

        for i in range(len(matrix.T)):
            x[column_names[i]] = matrix.T[i]

        return x.drop(['Job'], axis=1)


data = {
    "Name":["Adamu","Dauda","Isah","Bily","Victor"],
    "Age": [46, 40, None, None, 24],
    "Gender": ["m", "m", "f", "f", "m"],
    "Job": ["Economics", "Physics", "Education", "Statistics", "Programmer"]
}

df2 = pd.DataFrame(data)
print(df2)

'''
dropper = NameDropper()
imp = AgeImputer()
enc = FeatureEncoder()
print(enc.fit_transform(imp.fit_transform(dropper.fit_transform(df2))))
'''
    
pipe = Pipeline([
    ("dropper", NameDropper()), # this drops the name column
    ("imputer", AgeImputer()), # This imputes missing age values with the mean of the age
    ("encoder", FeatureEncoder()) # This transforms the Job column and make its values attributes
])

transformed_pipeline = pipe.fit_transform(df2) # The pipe is fit and transformed 
print(transformed_pipeline)
