import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def histPd(data, graphName, save_path=None):
    data.drop(['Chest','Original','Sex','Neck','Abdomen','Hip','Thigh','Knee','Ankle','Biceps','Forearm','Wrist'], axis=1).plot.line(title=graphName)

    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")

def scatterSns(data, xName, yName, graphName, save_path=None):
    sns.scatterplot(x=xName, y=yName, hue='Sex', data=data)
    
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")

def lineplotSns(data, save_path=None):
    sns.lineplot(data=data.drop(['Chest','Height','Weight','Original','Sex','Neck','Abdomen','Hip','Knee','Ankle','Biceps','Forearm'], axis=1))

    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved as {save_path}")


if __name__ == "__main__":
    dataSet = pd.read_csv("BodyFat.csv")
    scatterPlt(dataSet, 'BodyFat', 'Age', 'BodyFat DataSet', save_path='plots_image/BodyFat_Scatter_Matplotlib.png')
    histPd(dataSet, 'BodyFat', save_path='plots_image/BodyFat.png')
    scatterSns(dataSet, 'Weight', 'Height', 'BodyFat DataSet', save_path='plots_image/BodyFat_Scatter_Seaborn.png')
    lineplotSns(dataSet, save_path='plots_image/BodyFat_lineplot_Seaborn.png')