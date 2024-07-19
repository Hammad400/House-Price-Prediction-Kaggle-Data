import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv('train.csv')
numerical_features_2 = [feature for feature in df.columns if df[feature].dtypes != 'O']
df_n=df[numerical_features_2]
year_features= [feature for feature in numerical_features_2 if 'Yr' in feature or 'Year' in feature]
df_n=df_n.dropna()
df_n=df_n.drop(year_features,axis='columns')
df_n=df_n.drop(['Id'],axis='columns')

c_matrix=df_n.corr()
plus_fifty_features=[]
for feature in c_matrix['SalePrice'].sort_values(ascending=False).keys():
    if c_matrix['SalePrice'][feature]>=0.50:
        plus_fifty_features.append(feature)       
plus_fifty_features.remove('SalePrice')
df_8=df_n[plus_fifty_features]
X=df_8
y=df_n['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

model = RandomForestRegressor()
model.fit(X_train,y_train)

import pickle
pickle.dump(model, open('Random_forest_regressor.pkl','wb'))

model_ = pickle.load(open('Random_forest_regressor.pkl','rb'))
print(model_.predict([[6,1072,2,525,547,1072,2,5]]))
print((model.predict(X_test))[0])
