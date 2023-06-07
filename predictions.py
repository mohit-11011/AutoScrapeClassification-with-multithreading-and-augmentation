import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

def pred(model,test_images,test_labels,mapping):
    # After obtaining the predicted labels from the model
    predicted_labels = model.predict(np.array(test_images))
    predicted_labels= np.argmax(predicted_labels, axis=1)
    predicted_labels=[mapping[label] for label in predicted_labels]
    cm = confusion_matrix(test_labels, predicted_labels)
    labels = np.unique(np.concatenate((test_labels, predicted_labels)))

    # Create a pandas DataFrame from the confusion matrix
    df = pd.DataFrame(cm, index=labels, columns=labels)

    # Add headers to the DataFrame
    df.index.name = 'Actual'
    df.columns.name = 'Predicted'

    return df

