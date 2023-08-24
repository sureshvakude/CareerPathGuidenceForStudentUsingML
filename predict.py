def PredictPath(allsubmark):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    import matplotlib.pyplot as plt

    data = pd.read_csv('aptitude_test.csv')

    X = data.iloc[:,:-1].values
    y = data.iloc[:,-1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, y_train)

    student_aptitude = [allsubmark]
    predicted_career_path = model.predict(student_aptitude)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Plotting the predicted career path
    plt.figure()
    plt.scatter(range(len(X_train)), y_train, color='green', label='Training Career Path')
    plt.scatter(range(len(X_test)), y_test, color='blue', label='Testing Career Path')
    plt.scatter(len(X_test), predicted_career_path, color='red', label='Predicted Career Path')
    plt.xlabel('Student')
    plt.ylabel('Career Path')
    plt.title('Predicted Career Path for Student')
    plt.legend()


    # Displaying the last predicted output
    plt.text(len(X_test), predicted_career_path, str(predicted_career_path), color='black', ha='center', va='center')

    plt.show()
    return predicted_career_path
