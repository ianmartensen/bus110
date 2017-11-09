import seaborn
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt

allWines = pd.read_csv('winequality-both.csv', sep=',', header=0)
red = allWines.loc[allWines['type'] == 'red', :]
white = allWines.loc[allWines['type'] == 'white', :]

from pylab import savefig

def option_1(charX, charY):
    try:
        WineCharX = charX
        WineCharY = charY
        allWines = pd.read_csv('winequality-both.csv')
        # no white wine criteria
        getCorr = scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("For white wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)

        seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print('Please check the spelling of the wine characteristics you want to test')

def option_2(charX, charY):
     try:
         WineCharX = charX
         WineCharY = charY
         allWines = pd.read_csv('winequality-both.csv')
         red = allWines.loc[allWines['type'] == 'red', :]
         getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
         correlation = str(getCorr[0])
         pValue = str(getCorr[1])
         print("For red wine, the correlationbetween " + WineCharX + " and " + WineCharY + " is " + correlation)
         print("With p value of: " + pValue)
 
         seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
         plt.xlabel(WineCharX)
         plt.ylabel(WineCharY)
         plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
         savefig("scatterplit1.png")
         plt.show()
     except (KeyError) as e:
         print('Please check the spelling of the wine characteristics you want to test')

def menuOptions():
    print("\nA) Test Volitile acidity and Wine Quality for White Wine")
    print("\nB) Test Volitile acidity and Wine Quality for Red Wine")
    print("\nC) Test Fixed Acidity and Wine Quality for White Wine")
    print("\nD) Test Fixed Acidity and Wine Quality for Red Wine")
    print("\nE) Test Alcohol and Wine Quality for White Wine")
    print("\nF) Test Alcohol and Wine Quality for Red Wine")
    print("\nG) Test Residual Sugar and Wine Quality for White Wine")
    print("\nH) Test Residual Sugar and Wine Quality for Red Wine")

    menu_option = input("\nPlease select an option to continue: ")
    menu_option = menu_option.lower()

    if menu_option == "a":
        option_1(charX = "quality", charY = "volatile acidity")
    if menu_option == "b":
        option_2(charX = "quality", charY = "volatile acidity")
    if menu_option == "c":
        option_1(charX = "quality", charY = "fixed acidity")
    if menu_option == "d":
        option_2(charX = "quality", charY = "fixed acidity")
    if menu_option == "e":
        option_1(charX = "quality", charY = "alcohol")
    if menu_option == "f":
        option_2(charX = "quality", charY = "alcohol")
    if menu_option == "g":
        option_1(charX = "quality", charY = "residual sugar")
    if menu_option == "h":
        option_2(charX = "quality", charY = "residual sugar")


if __name__ == "__main__":
    menuOptions()