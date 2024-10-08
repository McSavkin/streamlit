import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

st.title('Исследование по чаевым')





tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

st.write(tips)

date_range = pd.date_range(start='2023-01-01', end='2023-01-31')

tips['time_order'] = np.random.choice(date_range, size=len(tips))

tips_daily = tips.groupby('time_order')['tip'].sum()

st.write('### График показывающий динамику чаевых во времени')



st.line_chart(tips_daily, x_label='Date', y_label='Total Tips')

st.write('### Гистограмма Total Bill')

fig, ax = plt.subplots()
sns.histplot(tips['total_bill'], bins=20, kde=True)

ax.set_xlabel('Сумма счета')
ax.set_ylabel('Частота')
st.pyplot(fig)

st.write('### Scatterplot, показывающий связь `total_bill` and `tip`')

st.scatter_chart(data=tips, x='total_bill', y='tip', x_label='Сумма счета', y_label='Чаевые')

st.write('### График, связывающий `total_bill`, `tip`, и `size`')

st.scatter_chart(data=tips, x='total_bill', y='tip', size='size', x_label='Сумма счета', y_label='Чаевые')
