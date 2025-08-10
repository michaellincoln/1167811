import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

class Test:
    def __init__(self):
        self.data = pd.DataFrame({
            'A': np.random.rand(10),
            'B': np.random.rand(10)
        })

    def plot_data(self):
        sns.scatterplot(data=self.data, x='A', y='B')
        plt.title('Sample Scatter Plot')
        plt.show()

    def split_data(self):
        x = self.data['A']
        y = self.data['B']
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    test_instance = Test()
    X_train, X_test, y_train, y_test = test_instance.split_data()
    print("Training data:", X_train)
    print("Test data:", X_test)
    print("Training labels:", y_train)
    print("Test labels:", y_test)
    test_instance.plot_data()
