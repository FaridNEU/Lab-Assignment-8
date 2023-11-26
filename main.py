import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv("BodyFat.csv")

def scatterPlt(data, xName, yName, graphName, save_path=None):
    fig, ax = plt.subplots()

    # scatter the xName against the yName
    ax.scatter(data[xName], data[yName])
    ax.set_title(graphName)
    ax.set_xlabel(xName)
    ax.set_ylabel(yName)

    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")

if __name__ == "__main__":
    scatterPlt(dataSet, 'BodyFat', 'Age', 'BodyFat DataSet', save_path='plots_image/BodyFat_Scatter_Matplotlib.png')