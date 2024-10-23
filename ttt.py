import streamlit as st
from skimage import io
import requests
from PIL import Image
from io import BytesIO

st.title("Тестовая страница для проверки импортов")

image_url = st.text_input("Введите URL изображения")

if image_url:
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Изображение", use_column_width=True)
        st.success("Изображение успешно загружено!")
    except Exception as e:
        st.error(f"Не удалось загрузить изображение: {e}")
