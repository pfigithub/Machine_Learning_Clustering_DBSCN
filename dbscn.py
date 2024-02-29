# importing packages
import numpy as np 
from sklearn.cluster import DBSCAN  
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 

# reading
import pandas as pd

pdf = pd.read_csv('youdata')
pdf.head(5)