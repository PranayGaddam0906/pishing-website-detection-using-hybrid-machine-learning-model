from sklearn.neighbors import KNeighborsClassifier
import joblib

knn = KNeighborsClassifier(n_neighbors=19)  # Use the same k=19
knn.fit(X_train, y_train)

# Save the new model
joblib.dump(knn, "knn_model_new.joblib")
