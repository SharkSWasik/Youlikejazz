import pandas as pd
import matplotlib.pyplot as plt

def draw_point(csv, image):
    read_csv = pd.read_csv(csv, sep=',', header=None, names=['col1', 'col2'])
    for x, y in zip(read_csv["col1"], read_csv["col2"]):
        plt.scatter(y, x, s=10, c='red')
        plt.imshow(image, cmap="gray")
