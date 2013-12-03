#coding:utf-8
from numpy import *

def formatDataSet(XYlist): #lla = [[1,2],[3,4]]
    dataMat = []
    labelMat = []
    for item in XYlist:
        dataMat.append(item[0])
        labelMat.append(item[1])
    return dataMat,labelMat

#梯度下降
def gradDescent(dataMatIn, classLabels, mcycl):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = mcycl
    weights = ones((n,1))
    for k in range(maxCycles):
        h = dataMatrix*weights
        error = (labelMat - h)
        weights = weights - alpha * dataMatrix.transpose()* error
    return weights

#最小二乘
def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

if __name__=='__main__':
    testlist = [[[5486, 1], 76],[[3000, 1], 24],[[899, 1],45]]
    dataMat,labelMat=formatDataSet(testlist)
    print dataMat, labelMat
    print gradDescent(dataMat, labelMat, 3)
    print standRegres(dataMat, labelMat)
