import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Название 
# Описание 
st.title('Data analisys applicaion')
st.write('Загрузи свой датасет')
 



# ## Шаг 1. Загрузка CSV файла


uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()


## Шаг 2. Проверка наличия пропусков в файле

missed_values = df.isna().sum()
missed_values = missed_values[missed_values > 0]

if len(missed_values) > 0:
    # fig, ax = plt.subplots()
    # sns.barplot(x=missed_values.index, y=missed_values.values, color='purple')
    # ax.set_title('Пропуски в столбцах')
    # ax.set_ylabel('Количество пропусков')
    # ax.set_xlabel('Название столбцов')
    st.bar_chart(missed_values, x_label='Количество пропусков', y_label='Название столбцов', color='#ffaa0088', horizontal=True)

## Шаг 3. Заполнить пропуски
    button = st.sidebar.button('Заполнить пропуски')
    if button:
        df_filled = df[missed_values.index].copy()

        for col in df_filled.columns:
            if df_filled[col].dtype == 'object': # Категориальные признаки
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
            else: # Численные признаки
                df_filled[col] = df_filled[col].fillna(df_filled[col].median())

        st.write(df_filled.head(5))

## Шаг 4. Выгрузить заполнный от прпусков CSV файл

        download_button = st.sidebar.download_button(label='Скачать CSV файл', 
                   data=df_filled.to_csv(), 
                   file_name='filled_dataf.csv')
        
else:
    st.write('Нет пропусков в данных')
    st.stop()