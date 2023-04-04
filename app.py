import streamlit as st
# from img_classification import teachable_machine_classification
from PIL import Image, ImageOps

st.title("使用谷歌的可教机器进行图像分类")
st.header("苹果病")
st.text("上传彩色蚂苹果叶子图片")

uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='上传了图片。', use_column_width=True)
    st.write("")
    st.write("分类...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.write("苹果结痂")
    elif label == 1:
        st.write("黑腐病")
    elif label == 2:
        st.write("雪松苹果锈")
    else:
        st.write("健康苹果")



#         0 apple_scrab
# 1 black_rot
# 2 cedar_apple_rust
# 3 apple_healthy
