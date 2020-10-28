import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import datetime

# from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split, KFold, cross_val_score
# from sklearn.metrics import mean_squared_error , r2_score, accuracy_score,confusion_matrix, classification_report
# from sklearn.metrics import roc_curve, roc_auc_score, f1_score, precision_recall_curve
# from sklearn.metrics import plot_confusion_matrix, ConfusionMatrixDisplay
# from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
# from sklearn import model_selection
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# from sklearn.model_selection import KFold
# from sklearn.svm import SVC
# from xgboost import XGBClassifier
# from xgboost import plot_importance
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
# from sklearn.neural_network import MLPClassifier
# from IPython.display import Audio
# import scipy
# sound_file ="Neene Modalu.mp3"
# import time
import streamlit as st
import pickle
import os, io
import Definitions as lib

import os
port = int(os.environ.get(“PORT”, 5000))

if __name__ == "__main__":
    # execute only if run as a script
    st.title("""
     ** Predict Telecom Connection Status -  Attack or No-Attack ** !
    """)
