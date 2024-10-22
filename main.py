import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from skimage import io
import numpy as np
from PIL import Image
import requests
from io import BytesIO


# Название 
# Описание 
st.title('Разложение изображения с помощью SVD')
st.write('Загрузи свою картинку')
 



# ## Шаг 1. Загрузка CSV файла


image_url = st.text_input("вставьте URL изображения")

if image_url:
    try:
        # Загружаем изображение с URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Изображение по ссылке", use_column_width=True)
        
        # Чтение изображения и извлечение одного канала (например, синего)
        image_np = io.imread(image_url)[:, :, 2]
        
        # Выполнение сингулярного разложения
        U, sing_vals, V = np.linalg.svd(image_np)
        
        # Запрос пользователя на количество сингулярных чисел
        top_k = st.number_input("Введите количество сингулярных чисел для сжатия", min_value=1, max_value=min(image_np.shape), value=10)

        # Создание матрицы sigma с top_k сингулярными числами
        sigma = np.zeros((U.shape[0], V.shape[0]))
        np.fill_diagonal(sigma, sing_vals[:top_k])
        
        # Восстановление сжатого изображения
        compressed_image = U[:, :top_k] @ sigma[:top_k, :top_k] @ V[:top_k, :]

        # Отображение сжатого изображения в диапазоне от 0 до 1
        plt.imshow(compressed_image, cmap='gray')
        plt.axis('off')  # Отключаем оси
        plt.title(f"Сжатое изображение с {top_k} сингулярными числами")

        # Отображение графика в Streamlit
        st.pyplot(plt)
    except Exception as e:
        st.error("Не удалось загрузить изображение. Проверьте URL.")