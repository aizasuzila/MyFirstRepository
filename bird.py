import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(data=pd.read_csv('/content/bird.csv'))

st.write(data)

st.write(dcopy=data.copy())

st.write(dcopy.shape)

st.write(dcopy.columns)

st.write(dcopy.dtypes)
