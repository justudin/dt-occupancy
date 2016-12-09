# decision trees: scikit-learn + pandas [![Build Status](https://travis-ci.org/justudin/dt-occupancy.svg?branch=master)](https://travis-ci.org/justudin/dt-occupancy)

This script provides an example of learning a decision tree with
scikit-learn.  Pandas is used to read data and custom functions are employed
to investigate the decision tree after it is learned.  Grab the code and try
it out. 


## Requirements

* python -- version 2.7.6 or 3.x.x just fine
* sckit-learn
* pandas
* numpy

and to create the graphic of the tree you must have graphviz/dot installed.

## Usage

### 1. Run script from command line

This provides an example of using the available functions.

```bash
$ python Occupancy.py
```

This:

* Fetches the data using pandas, or grabs the local copy.
* Outputs the *head* of the pandas data frame.
* Fits the decision tree and outputs the *pseudo code* for the decision tree.
* Uses pandas to show that the first branch at *Light <= 365.125* is easily
  verified.

The resulting output is:

```
-- get data:
-- data.csv found locally

-- df.head():
                  Unnamed: 0  Temperature  Humidity  Light     CO2  \
date                                                                 
2015-02-04 17:51           1        23.18   27.2720  426.0  721.25   
2015-02-04 17:51           2        23.15   27.2675  429.5  714.00   
2015-02-04 17:53           3        23.15   27.2450  426.0  713.50   
2015-02-04 17:54           4        23.15   27.2000  426.0  708.25   
2015-02-04 17:55           5        23.10   27.2000  426.0  704.50   

                  HumidityRatio  Occupancy  Target  
date                                                
2015-02-04 17:51       0.004793          1       0  
2015-02-04 17:51       0.004783          1       0  
2015-02-04 17:53       0.004779          1       0  
2015-02-04 17:54       0.004772          1       0  
2015-02-04 17:55       0.004757          1       0  

-- get_code:
if ( Light <= 365.125 ) {
    if ( Humidity <= 37.7399978638 ) {
        if ( Light <= 289.25 ) {
            if ( CO2 <= 844.75 ) {
                return 0 ( 5963 examples )
            }
            else {
                if ( Light <= 190.0 ) {
                    if ( Light <= 29.8333320618 ) {
                        return 0 ( 184 examples )
                    }
                    else {
                        if ( CO2 <= 1244.66674805 ) {
                            return 0 ( 22 examples )
                        }
                        else {
                            return 1 ( 1 examples )
                        }
                    }
                }
                else {
                    return 1 ( 1 examples )
                }
            }
        }
        else {
            if ( CO2 <= 469.208312988 ) {
                if ( HumidityRatio <= 0.00321291247383 ) {
                    return 0 ( 150 examples )
                }
                else {
                    return 1 ( 1 examples )
                    return 0 ( 5 examples )
                }
            }
            else {
                return 1 ( 4 examples )
            }
        }
    }
    else {
        return 1 ( 2 examples )
    }
}
else {
    if ( CO2 <= 456.333312988 ) {
        return 1 ( 1 examples )
        return 0 ( 10 examples )
    }
    else {
        if ( Temperature <= 22.2112503052 ) {
            if ( CO2 <= 493.333343506 ) {
                if ( Light <= 398.5 ) {
                    return 0 ( 3 examples )
                }
                else {
                    if ( Light <= 421.333312988 ) {
                        if ( HumidityRatio <= 0.00272014457732 ) {
                            return 0 ( 1 examples )
                        }
                        else {
                            if ( Humidity <= 33.3150024414 ) {
                                return 1 ( 16 examples )
                            }
                            else {
                                return 1 ( 5 examples )
                                return 0 ( 1 examples )
                            }
                        }
                    }
                    else {
                        return 1 ( 2 examples )
                        return 0 ( 4 examples )
                    }
                }
            }
            else {
                if ( Humidity <= 19.4037494659 ) {
                    if ( CO2 <= 646.5 ) {
                        return 1 ( 30 examples )
                    }
                    else {
                        return 1 ( 9 examples )
                        return 0 ( 6 examples )
                    }
                }
                else {
                    if ( Light <= 458.75 ) {
                        if ( Light <= 423.083312988 ) {
                            if ( Light <= 420.75 ) {
                                return 1 ( 113 examples )
                            }
                            else {
                                return 1 ( 5 examples )
                                return 0 ( 1 examples )
                            }
                        }
                        else {
                            return 1 ( 691 examples )
                        }
                    }
                    else {
                        if ( Light <= 459.125 ) {
                            return 1 ( 8 examples )
                            return 0 ( 2 examples )
                        }
                        else {
                            if ( HumidityRatio <= 0.00328950257972 ) {
                                if ( HumidityRatio <= 0.00328860292211 ) {
                                    if ( CO2 <= 805.833374023 ) {
                                        return 1 ( 103 examples )
                                    }
                                    else {
                                        if ( CO2 <= 806.125 ) {
                                            return 1 ( 2 examples )
                                            return 0 ( 1 examples )
                                        }
                                        else {
                                            return 1 ( 17 examples )
                                            return 0 ( 1 examples )
                                        }
                                    }
                                }
                                else {
                                    return 0 ( 2 examples )
                                }
                            }
                            else {
                                if ( Temperature <= 22.0416660309 ) {
                                    return 1 ( 338 examples )
                                }
                                else {
                                    if ( Temperature <= 22.0583343506 ) {
                                        return 1 ( 4 examples )
                                        return 0 ( 2 examples )
                                    }
                                    else {
                                        return 1 ( 143 examples )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else {
            if ( CO2 <= 893.125 ) {
                if ( Light <= 441.0 ) {
                    return 1 ( 17 examples )
                }
                else {
                    if ( CO2 <= 809.75 ) {
                        return 1 ( 3 examples )
                        return 0 ( 11 examples )
                    }
                    else {
                        return 0 ( 25 examples )
                    }
                }
            }
            else {
                if ( Temperature <= 22.6416664124 ) {
                    return 1 ( 200 examples )
                }
                else {
                    if ( CO2 <= 1105.375 ) {
                        if ( HumidityRatio <= 0.00448297848925 ) {
                            return 1 ( 2 examples )
                        }
                        else {
                            if ( Light <= 681.125 ) {
                                if ( Temperature <= 22.6583328247 ) {
                                    return 1 ( 2 examples )
                                    return 0 ( 1 examples )
                                }
                                else {
                                    return 0 ( 17 examples )
                                }
                            }
                            else {
                                return 1 ( 2 examples )
                            }
                        }
                    }
                    else {
                        return 1 ( 7 examples )
                        return 0 ( 2 examples )
                    }
                }
            }
        }
    }
}

```

### 2. Use interactively with (i)python

This code can also be used interactively by importing the available functions.
I do this by importing `Occupancy as occ` and using a *function* like so
`occ.function()`. Follow along:

```python
>>> import Occupancy as occ
>>> df = occ.get_data()
-- data.csv found locally
>>> df.head()
                  Unnamed: 0  Temperature  Humidity  Light     CO2  \
date                                                                 
2015-02-04 17:51           1        23.18   27.2720  426.0  721.25   
2015-02-04 17:51           2        23.15   27.2675  429.5  714.00   
2015-02-04 17:53           3        23.15   27.2450  426.0  713.50   
2015-02-04 17:54           4        23.15   27.2000  426.0  708.25   
2015-02-04 17:55           5        23.10   27.2000  426.0  704.50   

                  HumidityRatio  Occupancy  Target  
date                                                
2015-02-04 17:51       0.004793          1       0  
2015-02-04 17:51       0.004783          1       0  
2015-02-04 17:53       0.004779          1       0  
2015-02-04 17:54       0.004772          1       0  
2015-02-04 17:55       0.004757          1       0  

>>> df.columns
Index(['Unnamed: 0', 'Temperature', 'Humidity', 'Light', 'CO2',
       'HumidityRatio', 'Occupancy'],
      dtype='object')
>>> features = list(df.columns[1:6])
>>> features
['Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio']

>>> df, targets = occ.encode_target(df, "Name")
>>> y = df["Target"]
>>> X = df[features]
>>> dt = occ.DecisionTreeClassifier(min_samples_split=20, random_state=99)
>>> dt.fit(X,y)
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=1,
            min_samples_split=20, min_weight_fraction_leaf=0.0,
            random_state=99, splitter='best')
>>> occ.get_code(dt, features, targets)
if ( Light <= 365.125 ) {
    if ( Humidity <= 37.7399978638 ) {
        if ( Light <= 289.25 ) {
            if ( CO2 <= 844.75 ) {
                return 0 ( 5963 examples )
            }
            else {
                if ( Light <= 190.0 ) {
                    if ( Light <= 29.8333320618 ) {
                        return 0 ( 184 examples )
                    }
                    else {
                        if ( CO2 <= 1244.66674805 ) {
                            return 0 ( 22 examples )
                        }
                        else {
                            return 1 ( 1 examples )
                        }
                    }
                }
                else {
                    return 1 ( 1 examples )
                }
            }
        }
        else {
            if ( CO2 <= 469.208312988 ) {
                if ( HumidityRatio <= 0.00321291247383 ) {
                    return 0 ( 150 examples )
                }
                else {
                    return 1 ( 1 examples )
                    return 0 ( 5 examples )
                }
            }
            else {
                return 1 ( 4 examples )
            }
        }
    }
    else {
        return 1 ( 2 examples )
    }
}
else {
    if ( CO2 <= 456.333312988 ) {
        return 1 ( 1 examples )
        return 0 ( 10 examples )
    }
    else {
        if ( Temperature <= 22.2112503052 ) {
            if ( CO2 <= 493.333343506 ) {
                if ( Light <= 398.5 ) {
                    return 0 ( 3 examples )
                }
                else {
                    if ( Light <= 421.333312988 ) {
                        if ( HumidityRatio <= 0.00272014457732 ) {
                            return 0 ( 1 examples )
                        }
                        else {
                            if ( Humidity <= 33.3150024414 ) {
                                return 1 ( 16 examples )
                            }
                            else {
                                return 1 ( 5 examples )
                                return 0 ( 1 examples )
                            }
                        }
                    }
                    else {
                        return 1 ( 2 examples )
                        return 0 ( 4 examples )
                    }
                }
            }
            else {
                if ( Humidity <= 19.4037494659 ) {
                    if ( CO2 <= 646.5 ) {
                        return 1 ( 30 examples )
                    }
                    else {
                        return 1 ( 9 examples )
                        return 0 ( 6 examples )
                    }
                }
                else {
                    if ( Light <= 458.75 ) {
                        if ( Light <= 423.083312988 ) {
                            if ( Light <= 420.75 ) {
                                return 1 ( 113 examples )
                            }
                            else {
                                return 1 ( 5 examples )
                                return 0 ( 1 examples )
                            }
                        }
                        else {
                            return 1 ( 691 examples )
                        }
                    }
                    else {
                        if ( Light <= 459.125 ) {
                            return 1 ( 8 examples )
                            return 0 ( 2 examples )
                        }
                        else {
                            if ( HumidityRatio <= 0.00328950257972 ) {
                                if ( HumidityRatio <= 0.00328860292211 ) {
                                    if ( CO2 <= 805.833374023 ) {
                                        return 1 ( 103 examples )
                                    }
                                    else {
                                        if ( CO2 <= 806.125 ) {
                                            return 1 ( 2 examples )
                                            return 0 ( 1 examples )
                                        }
                                        else {
                                            return 1 ( 17 examples )
                                            return 0 ( 1 examples )
                                        }
                                    }
                                }
                                else {
                                    return 0 ( 2 examples )
                                }
                            }
                            else {
                                if ( Temperature <= 22.0416660309 ) {
                                    return 1 ( 338 examples )
                                }
                                else {
                                    if ( Temperature <= 22.0583343506 ) {
                                        return 1 ( 4 examples )
                                        return 0 ( 2 examples )
                                    }
                                    else {
                                        return 1 ( 143 examples )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else {
            if ( CO2 <= 893.125 ) {
                if ( Light <= 441.0 ) {
                    return 1 ( 17 examples )
                }
                else {
                    if ( CO2 <= 809.75 ) {
                        return 1 ( 3 examples )
                        return 0 ( 11 examples )
                    }
                    else {
                        return 0 ( 25 examples )
                    }
                }
            }
            else {
                if ( Temperature <= 22.6416664124 ) {
                    return 1 ( 200 examples )
                }
                else {
                    if ( CO2 <= 1105.375 ) {
                        if ( HumidityRatio <= 0.00448297848925 ) {
                            return 1 ( 2 examples )
                        }
                        else {
                            if ( Light <= 681.125 ) {
                                if ( Temperature <= 22.6583328247 ) {
                                    return 1 ( 2 examples )
                                    return 0 ( 1 examples )
                                }
                                else {
                                    return 0 ( 17 examples )
                                }
                            }
                            else {
                                return 1 ( 2 examples )
                            }
                        }
                    }
                    else {
                        return 1 ( 7 examples )
                        return 0 ( 2 examples )
                    }
                }
            }
        }
    }
}
>>> occ.visualize_tree(dt, features)
```

Thanks for stopping by!
