# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EhM9OEc97HuzG9AOuWgvRsnJgTLQ7Gzy
"""

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy
import h5py
import matplotlib.pyplot as plt

# random seed for reproducibility
numpy.random.seed(2)

# loading load prima indians diabetes dataset, past 5 years of medical history
dataset = numpy.loadtxt("prima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables, splitting csv data
X = dataset[:, 0:8]
Y = dataset[:, 8]
x_train, x_validation, y_train, y_validation = train_test_split(
    X, Y, test_size=0.30, random_state=5)
# create model, add dense layers one by one specifying activation function
model = Sequential()
# input layer requires input_dim param
model.add(Dense(10, input_dim=8, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='relu'))
# sigmoid instead of relu for final probability between 0 and 1
model.add(Dense(1, activation='sigmoid'))

# compile the model, adam gradient descent (optimized)
model.compile(loss="binary_crossentropy",
              optimizer="adam", metrics=['accuracy'])

# call the function to fit to the data (training the network)
model.fit(x_train, y_train, epochs=1000, batch_size=10,
          validation_data=(x_validation, y_validation))

# evaluate the model

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))


model.save('diabetes_risk_nn.h5')

history = model.fit(x_train, y_train, epochs=1000, batch_size=10,
                    validation_data=(x_validation, y_validation))

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

from keras.models import load_model
import numpy as np

model = load_model('diabetes_risk_nn.h5')


def pickthistodo():
    """Pick what needs to be done next."""
    global x
    dothis = input('''Would you like to enter more data:(y/n )''')
    if dothis == 'y' or dothis == 'y':
        x = 1
    elif dothis == 'n' or dothis == 'N':
        x = -1
    else:
        print("Your input is not valid please input 1, 2, or 3")
        pickthistodo()


x = 1
while x == 1:
    print("Please Enter the Folowing Metrics one at a time")
    a = float(input("Enter Metric 1: "))  #Number of times pregnant
    b = float(input("Enter Metric 2: "))  #Plasma glucose concentration a 2 hours in an oral glucose tolerance test
    c = float(input("Enter Metric 3: "))  #Diastolic blood pressure (mm Hg)
    d = float(input("Enter Metric 4: "))  #Triceps skin fold thickness (mm)
    e = float(input("Enter Metric 5: "))  #2-Hour serum insulin (mu U/ml)
    f = float(input("Enter Metric 6: "))  #Body mass index (weight in kg/(height in m)^2)
    g = float(input("Enter Metric 7: "))  #Diabetes pedigree function
    h = float(input("Enter Metric 8: "))  #Age (years)


    makeprediction = np.array([a, b, c, d, e, f, g, h])
    makeprediction = makeprediction.reshape(1, -1)
    finalprediction = model.predict(makeprediction)
    print(finalprediction)
    pickthistodo()

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
y_pred = model.predict(x_validation)
y_pred_binary = (y_pred > 0.5).astype(int)  # Convert probabilities to binary predictions

# Calculate the confusion matrix
conf_matrix = confusion_matrix(y_validation, y_pred_binary)

# Print the confusion matrix
print("Confusion Matrix:")
print(conf_matrix)

# Calculate and print other classification metrics
accuracy = accuracy_score(y_validation, y_pred_binary)
precision = precision_score(y_validation, y_pred_binary)
recall = recall_score(y_validation, y_pred_binary)
f1 = f1_score(y_validation, y_pred_binary)

print("\nAccuracy: {:.2f}%".format(accuracy * 100))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("F1 Score: {:.2f}".format(f1))