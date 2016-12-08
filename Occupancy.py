"""
    !/usr/bin/env python
    -*- coding: utf-8 -*-

    Occupancy.py -- probe a decision tree found with scikit-learn.

    Dataset from https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+

    Compatible with Python 3.x

    Required libraries: pandas, numpy sklearn, PIL, graphviz (dot)

    Copyright © 2016 Udin <just.udin@yahoo.com>
    Distributed under terms of the MIT license.

"""""

from __future__ import print_function
import os
import subprocess
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from PIL import Image


def get_code(tree, feature_names, target_names, spacer_base="    "):
    """Produce psuedo-code for decision tree.

    Args
    ----
    tree -- scikit-leant DescisionTree.
    feature_names -- list of feature names.
    target_names -- list of target (class) names.
    spacer_base -- used for spacing code (default: "    ").

    """
    left = tree.tree_.children_left
    right = tree.tree_.children_right
    threshold = tree.tree_.threshold
    features = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value

    def recurse(left, right, threshold, features, node, depth):
        spacer = spacer_base * depth
        if (threshold[node] != -2):
            print(spacer + "if ( " + features[node] + " <= " + \
                  str(threshold[node]) + " ) {")
            if left[node] != -1:
                recurse(left, right, threshold, features, left[node],
                        depth + 1)
            print(spacer + "}\n" + spacer + "else {")
            if right[node] != -1:
                recurse(left, right, threshold, features, right[node],
                        depth + 1)
            print(spacer + "}")
        else:
            target = value[node]
            for i, v in zip(np.nonzero(target)[1], target[np.nonzero(target)]):
                target_name = target_names[i]
                target_count = int(v)
                print(spacer + "return " + str(target_name) + " ( " + \
                      str(target_count) + " examples )")

    recurse(left, right, threshold, features, 0, 0)


def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt-occu.dot", 'w') as f:
        export_graphviz(tree, out_file=f, feature_names=feature_names)

    command = ["dot", "-Tpng", "dt-occu.dot", "-o", "dt-occu.png"]
    try:
        subprocess.call(command, shell=True)
    except:
        exit("dot is'nt installed yet, please install graphviz, to produce visualization")


def encode_target(df, target_column):
    """Add column to df with integers for the target.

    Args
    ----
    df -- pandas DataFrame.
    target_column -- column to map to int, producing new Target column.

    Returns
    -------
    df -- modified DataFrame.
    targets -- list of target names.
    """
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)


def get_data():
    """Get the data, from local csv or pandas repo."""
    if os.path.exists("data.csv"):
        print("-- data.csv found locally")
        df = pd.read_csv("data.csv", index_col=1)
    else:
        print("-- trying to download from github")
        fn = "http://justudin.github.com/files/uploads/data.csv"
        try:
            df = pd.read_csv(fn)
        except:
            exit("-- Unable to download data.csv")

        with open("data.csv", 'w') as f:
            print("-- writing to local data.csv file")
            df.to_csv(f)

    return df


if __name__ == '__main__':
    print("\n-- get data:")

    df = get_data()

    print("\n-- df.head():")

    print(df.columns)

    ff = list(df.columns[1:6])

    print(ff)


    print(df.head(), end="\n\n")

    # set of features
    features = ["Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]

    # target output
    df, targets = encode_target(df, "Occupancy")

    y = df["Target"]
    X = df[features]

    # apply DecisionTree Classifier
    dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
    dt.fit(X, y)

    print("\n-- get_code:")
    # get the pseudo code
    get_code(dt, features, targets)

    # visualize the Tree
    visualize_tree(dt, features)

    print("* df.head()", df.head(), sep="\n", end="\n\n")
    print("* df.tail()", df.tail(), sep="\n", end="\n\n")

    print("* Occupancy types:", df["Occupancy"].unique(), sep="\n")

    # Open the DT image
    img = Image.open('dt-occu.png')
    img.show()