import csv
import os
from PIL import Image


with open('C:/Users/david/PycharmProjects/HackPoly2017/wheels.txt', 'rU') as inputfile: #whatever he called it
    reader = csv.reader(inputfile)
    dp = list(reader)



directory='car (sedan)' ##whatever place the png are in

def wheelFinder(square):
    for filename in os.listdir(directory):
        ##iterate over every pixel
        img = Image.open(os.path.join(directory, filename))
        SIDE = 1111
        SQUARE = square                                                            ## 0    1    2    3    4    5    6    7
        ##grab the corresponding data points of that file ( back and front wheel  fx1, fy1, fx2, fy2, bx1, bx1, bx2, by2) - list dp
        a = 0
        xList = []
        yList = []
        x2List = []
        y2List = []
        bList = []
        data = []
        for x in range(0,1101,10):
            for y in range(1, 1101, 10):

                xList.insert(a, x)
                x2List.insert(a, x+SQUARE)
                yList.insert(a, y)
                y2List.insert(a, y+SQUARE)

                bool1x = (x<=int(dp[a][0]) and int(dp[a][0])<=(x+SQUARE)and y<=int(dp[a][1]) and int(dp[a][1])<=(y+SQUARE))
                bool1y = (x<=int(dp[a][2]) and int(dp[a][2])<=(x+SQUARE) and y<=int(dp[a][3]) and int(dp[a][3])<=(y+SQUARE))
                bool2x = (x<=int(dp[a][4]) and int(dp[a][4])<=(x+SQUARE) and y<=int(dp[a][5]) and int(dp[a][5])<=(y+SQUARE))
                bool2y = (x<=int(dp[a][6]) and int(dp[a][6])<=(x+SQUARE) and y<=int(dp[a][7]) and int(dp[a][7])<=(y+SQUARE))
                bList.insert(a, ((bool1x and bool1y) or (bool2x and bool2y)))
                if a < 79:
                    a += 1
        coord1=zip(xList, yList)
        coord2=zip(x2List, y2List)
        coord=zip(coord1, coord2)
        data.extend(zip(coord, bList))
    print(*data, sep='\n')
for z in range (100, 200, 50):
    wheelFinder(z)