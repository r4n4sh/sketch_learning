# Step1: Import required packages
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC



# Step2: Load dataset
cache_data = read_csv('cache_input.csv')

# Step 3: Split the data in training and testing subsets
D = cache_data.values
x = D[:,0:30]
y = D[:,30]
x_tr, x_ts, y_tr, y_ts = train_test_split(x,y,test_size=0.20)

# Step 4: Classifier training using Support Vector Machine 
model = SVC()
model.fit(x_tr,y_tr)

# Step 5: Check classifier accuracy on test data and see result 
predict_flower = model.predict(x_ts)
print("Accuracy: ",accuracy_score(y_ts, predict_flower))

