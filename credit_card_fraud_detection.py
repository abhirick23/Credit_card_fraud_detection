# -*- coding: utf-8 -*-
"""Credit card fraud detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QknOFtkOyHXUq-2_R6ywXuhUA1gAPoD8
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive/')
# %cd /gdrive

ls

cd /gdrive/MyDrive/Credit card fraud detection

ls

"""# Importing Libraries"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier as rf
import warnings

"""# Uploading Dataset"""

df=pd.read_csv('creditcard.csv')
df.head()

df.info()

df.describe()

"""# EDA"""

df.isna().sum().sum()

df.columns

df.Class.value_counts()

columns = df.columns
binary_cols = []

for col in columns:
    if df[col].value_counts().shape[0] == 2:
        binary_cols.append(col)

binary_cols

sns.countplot("Class", data=df)

corrmat = df.corr()
fig = plt.figure(figsize = (12, 9))
sns.heatmap(corrmat, vmax = .8, square = True)
plt.show()

sns.distplot(df["Time"])

X = df.drop(['Class'], axis = 1)
Y = df["Class"]
x_Data = X.values
y_Data = Y.values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_Data, y_Data, test_size = 0.2, random_state = 42)

"""# Naive Bayes"""

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)

model.score(X_test,y_test)

from sklearn.model_selection import cross_val_score
print(cross_val_score(GaussianNB(),X_train, y_train, cv=5))

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

pred = model.predict(X_train) 
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

predicted_test = model.predict(X_test)
p=accuracy_score(y_test, predicted_test)

from sklearn.metrics import roc_curve, auc
import numpy as np

fpr, tpr, thresholds =roc_curve(y_test, predicted_test)
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve : %f" % roc_auc)

i = np.arange(len(tpr)) # index for df
roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), '1-fpr' : pd.Series(1-fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
roc.iloc[(roc.tf-0).abs().argsort()[:1]]

# Plot tpr vs 1-fpr
fig, ax = plt.subplots()
plt.plot(roc['tpr'])
plt.plot(roc['1-fpr'], color = 'purple')
plt.xlabel('1-False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
ax.set_xticklabels([])

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

print(classification_report(y_test, predicted_test))

cma = confusion_matrix(y_test, predicted_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap=plt.cm.Blues, alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Random forest Classifier"""

clf_forest = rf(n_estimators=100, max_depth=10)
clf_forest.fit(X_train, y_train)

pred = clf_forest.predict(X_train)
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

pred_test = clf_forest.predict(X_test)
q=accuracy_score(y_test, pred_test)

from sklearn.metrics import roc_curve, auc
import numpy as np

fpr, tpr, thresholds =roc_curve(y_test, pred_test)
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve : %f" % roc_auc)

i = np.arange(len(tpr)) # index for df
roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), '1-fpr' : pd.Series(1-fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
roc.iloc[(roc.tf-0).abs().argsort()[:1]]

# Plot tpr vs 1-fpr
fig, ax = plt.subplots()
plt.plot(roc['tpr'])
plt.plot(roc['1-fpr'], color = 'red')
plt.xlabel('1-False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
ax.set_xticklabels([])

from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

print(classification_report(y_test, pred_test))

cma = confusion_matrix(y_test, pred_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Decision Tree Classifier"""

from sklearn import tree

clf = tree.DecisionTreeClassifier()
 clf = clf.fit(X_train, y_train)

pred1 = clf.predict(X_train)
accuracy_score(y_train, pred1)

confusion_matrix(y_train, pred1)

pred1_test = clf.predict(X_test)
r=accuracy_score(y_test, pred1_test)

from sklearn.metrics import roc_curve, auc
import numpy as np

fpr, tpr, thresholds =roc_curve(y_test, pred1_test)
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve : %f" % roc_auc)

i = np.arange(len(tpr)) # index for df
roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), '1-fpr' : pd.Series(1-fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
roc.iloc[(roc.tf-0).abs().argsort()[:1]]

# Plot tpr vs 1-fpr
fig, ax = plt.subplots()
plt.plot(roc['tpr'])
plt.plot(roc['1-fpr'], color = 'green')
plt.xlabel('1-False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
ax.set_xticklabels([])

print(classification_report(y_test, pred1_test))

cma = confusion_matrix(y_test, pred1_test)

fig, ax = plt.subplots(figsize=(5, 5))
ax.matshow(cma, cmap ="coolwarm_r", alpha=0.3)
for i in range(cma.shape[0]):
    for j in range(cma.shape[1]):
        ax.text(x=j, y=i,s=cma[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

"""# Comparative analysis"""

import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'NB':p, 'RF':q, 'DT':r}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))

plt.plot(courses, values) 
plt.xlabel("Algorithms")
plt.ylabel("Accuracy")
plt.title("Compaaritive analysis of algorithm on the basis of the acccuracy")
plt.show()

activities = ['NB', 'RF', 'DT'] 
# portion covered by each label
slices = [p, q, r ]
 
# color for each label
colors = ['r', 'b', 'g']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.1),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()