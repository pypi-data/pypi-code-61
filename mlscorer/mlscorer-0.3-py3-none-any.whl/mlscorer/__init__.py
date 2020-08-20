"""
Author = Avishek Das,
Email = avishek.das.ayan@gmail.com
"""

def get_scores(y_test, y_pred):
  from sklearn.metrics import accuracy_score,f1_score, precision_score, recall_score
  # accuracy: (tp + tn) / (p + n)
  accuracy = accuracy_score(y_test, y_pred)

  # f1: 2 tp / (2 tp + fp + fn)
  f1 = f1_score(y_test, y_pred,  average=None)

  # precision:  tp / (tp + fp)
  precision = precision_score(y_test, y_pred,  average=None)

  # recall:  tp / (tp + fn)
  recall = recall_score(y_test, y_pred,  average=None)

  return {
      'accuracy':accuracy,
      'f1':f1, 
      'precision':precision, 
      'recall':recall
  }

def get_score_table(y_test=None, y_pred=None,  map_class=None, metrics=None):
    """
    # ML Scorer
    ML Scorer is the solution to your classification scores of ML algorithms.

    ## Installation
        pip install mlscorer
        
    ## Preperation
    Make a class mapping dictionary(map_class) using **Method1** or **Method2**

    ###  *Method 1*
    Make all the data categorical using following code snippet

    map_class = dict(zip(df.classes.astype("category").cat.codes, df.classes))
    print(map_class)

    > output:
    > {1: 'positive', 0: 'negative'}

    here, df is the **Dataframe** and **classes** is  a column which may have class values like
     - positive
     - negative
     
     [**N.B.** Don't change "category",  it's a datatype]
    ### or
    ###  *Method 2*
    Make the Dictionary manually according to your classes

        map_class = {
            1: 'positive',
            0: 'negative'
        }

    # Usage

        from sklearn.linear_model import LogisticRegression
        import mlscorer as ms
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        ms.get_score_table(y_test, y_pred, map_class)

    *Output:*
    <img src="https://i.ibb.co/L0SQgKW/Capture.png" alt="drawing" width="700"/>

    ### Parameters
    **y_test** : target values of test set
    **y_pred** : predicted target values
    **map_class** : *dict* : your categoricl class mapping
    **metrics** : *list* : use one or more evaluation metric from f1, precision, recall or accuracy
    eg:
    ```py
        ms.get_score_table(y_test, y_pred, map_class, metrics=['precision', 'recall'])
    ```
    <img src="https://i.ibb.co/hdsHbB3/metric.png" alt="drawing" width="700"/>
    """
    if map_class is None:
      return "map_class is not provided"
    elif y_test is None:
      return "y_test is not provided"
    elif y_pred is None:
      return "y_pred is not provided"
    else: pass

    from prettytable import PrettyTable

    if metrics is None : metrics = ['f1', 'precision', 'recall', 'accuracy']
    dc= get_scores(y_test, y_pred)
    if 'accuracy' in metrics:
      print('Accuracy: {}'.format(dc['accuracy']))
      metrics.remove('accuracy')
    t = PrettyTable(['class']+metrics)
    for i in range(len(map_class)):
        t.add_row([map_class[i]]+[dc[d][i] for d in metrics])
    print(t)