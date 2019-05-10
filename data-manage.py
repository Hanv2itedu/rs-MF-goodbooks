import numpy
import sys
import os

import pandas as pd
from ipython_genutils.py3compat import xrange

userIDRequest = 0
bookIDRequest = 0
rating = 0
# 498x434
def addUser(userID):
    listA = []
    ratings_matrix = pd.read_csv('ratingmatrixfix.csv', sep=',', error_bad_lines=False, encoding="latin-1")
    # print(ratings_matrix.shape)
    # print("so hang:",ratings_matrix.shape[0])
    # print("so cot:",ratings_matrix.shape[1])
    # print(ratings_matrix.iloc[0, 1])
    listA.append(userID)
    for i in range(1,ratings_matrix.shape[1]):
        listA.append(0)
    ratings_matrix.loc[ratings_matrix.shape[0]] = listA
    # ratings_matrix.iloc[ratings_matrix.shape[0]] = userID
    print(ratings_matrix)
    os.remove("ratingmatrixfix.csv")
    ratings_matrix.to_csv('ratingmatrixfix.csv', encoding='utf-8',index=False)

def addItem(itemID):
    ratings_matrix = pd.read_csv('ratingmatrixfix.csv', sep=',', error_bad_lines=False, encoding="latin-1")
    bookIndex = ratings_matrix.shape[1]
    ratings_matrix[str(itemID)] = 0
    ratings_matrix = ratings_matrix.reindex(sorted(ratings_matrix.columns), axis=1)
    os.remove("ratingmatrixfix.csv")
    ratings_matrix.to_csv('ratingmatrixfix.csv', encoding='utf-8', index=False)

def update_rating(userID,bookID,rating):
    ratings_matrix = pd.read_csv('ratingmatrixfix.csv', sep=',', error_bad_lines=False, encoding="latin-1")
    ratings_matrix.iloc[userID-1, bookID] = rating
    print(ratings_matrix)
    os.remove("ratingmatrixfix.csv")
    ratings_matrix.to_csv('ratingmatrixfix.csv', encoding='utf-8', index=False)


# addUser(500)
# addItem(500)
# update_rating(3,3,9)
