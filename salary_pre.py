import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data_set = pd.read_csv('/Users/fatmabetulturan/Desktop/PROJELER/AI/Salary_Data.csv')

X = data_set[['YearsExperience']]
y = data_set['Salary']	

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(X_test, y_test, color='blue')          
plt.plot(X_test, y_pred, color='red')
plt.title('Linear Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')              
plt.show()            

#print(data_set)