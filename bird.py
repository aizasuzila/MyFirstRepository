import numpy as np
import pandas as pd

st.write(data=pd.read_csv('/content/bird.csv'))

st.write(data)

st.write(dcopy=data.copy())

st.write(dcopy.shape)

st.write(dcopy.columns)

st.write(dcopy.dtypes)
