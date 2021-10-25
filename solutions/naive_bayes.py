# Imports
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

# Split into train and test randomly
X_train, X_test, y_train, y_test = train_test_split(bow, data.target, test_size=0.2, random_state=42)

# Instantiate a default MiltinomialNB and train on train data
NB_model = MultinomialNB()
NB_model.fit(X_train, y_train)

# Predict the test set
y_pred = NB_model.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Visualize the confusion matrix
plt.figure()
# I use a logarithmic color scheme, so the few mismatches are visible!
plt.imshow(np.log(cm+1), interpolation='nearest', cmap=plt.cm.Blues)
tick_marks = np.arange(len(data.target_names))
plt.xticks(tick_marks, data.target_names, rotation=45, ha="right")
plt.yticks(tick_marks, data.target_names)
plt.xlabel('Predicted label')
plt.ylabel('True label')
cb = plt.colorbar()
cb.set_ticks([]);
