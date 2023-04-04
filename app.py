import streamlit as st
from img_classification import teachable_machine_classification
from PIL import Image, ImageOps




page = st.sidebar.selectbox("探索或预测", ("苹果病分类","葡萄病分类","马铃薯病分类","番茄病分类"))

if page == "苹果病分类":
    st.title("使用谷歌的可教机器进行图像分类")
    st.header("苹果病")
    st.text("上传彩色苹果叶子图片")

    uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='上传了图片。', use_column_width=True)
        st.write("")
        st.write("分类...")
        label = teachable_machine_classification(image, 'keras_model_apple.h5')
        if label == 0:
            st.write("苹果结痂")
        elif label == 1:
            st.write("黑腐病")
        elif label == 2:
            st.write("雪松苹果锈")
        else:
            st.write("健康苹果")

    st.text("类:苹果结痂, 黑腐病, 雪松苹果锈, 健康苹果")

    # 0 apple_scrab
    # 1 black_rot
    # 2 cedar_apple_rust
    # 3 apple_healthy

elif page == "葡萄病分类":
    st.title("使用谷歌的可教机器进行图像分类")
    st.header("葡萄病")
    st.text("上传彩色葡萄叶子图片")

    uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='上传了图片。', use_column_width=True)
        st.write("")
        st.write("分类...")
        label = teachable_machine_classification(image, 'keras_model_grape.h5')
        if label == 0:
            st.write("葡萄埃斯卡黑麻疹")
        elif label == 1:
            st.write("葡萄黑腐病")
        else:
            st.write("健康苹果")

    st.text("类:葡萄埃斯卡黑麻疹, 葡萄黑腐病, 健康葡萄")

    # 0 grape_esca_black_measles
    # 1 grape_black_rot
    # 2 graph_healty

elif page == "马铃薯病分类":
    st.title("使用谷歌的可教机器进行图像分类")
    st.header("马铃薯病")
    st.text("上传彩色马铃薯叶子图片")

    uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='上传了图片。', use_column_width=True)
        st.write("")
        st.write("分类...")
        label = teachable_machine_classification(image, 'keras_model_potato.h5')
        if label == 0:
            st.write("马铃薯早疫病")
        elif label == 1:
            st.write("健康马铃薯")
        else:
            st.write("马铃薯晚疫病")

    st.text("类:马铃薯早疫病, 健康马铃薯, 马铃薯晚疫病")

    # 0 potato_early_blight
    # 1 potato_healthy
    # 2 potato_late_blight
elif page == "番茄病分类":
    st.title("使用谷歌的可教机器进行图像分类")
    st.header("番茄病")
    st.text("上传彩色番茄叶子图片")

    uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='上传了图片。', use_column_width=True)
        st.write("")
        st.write("分类...")
        label = teachable_machine_classification(image, 'keras_model_tomato.h5')
        if label == 0:
            st.write("番茄细菌斑点")
        elif label == 1:
            st.write("番茄早疫病")
        elif label == 2:
            st.write("健康番茄")
        elif label == 3:
            st.write("番茄晚疫病")
        elif label == 4:
            st.write("番茄叶霉")
        elif label == 5:
            st.write("番茄隔叶斑病")
        elif label == 6:
            st.write("番茄蜘蛛螨")
        elif label == 7:
            st.write("番茄靶点")
        elif label == 8:
            st.write("番茄花叶病毒")
        else:
            st.write("番茄黄叶卷曲病毒")

    st.text("类:番茄细菌斑点, 番茄早疫病, 番茄蜘蛛螨, 番茄靶点, 番茄花叶病毒, 番茄黄叶卷曲病毒, 番茄隔叶斑病, 番茄叶霉, 健康番茄")

# 0 tomato_bacterial_spot
# 1 tomato_early_blight
# 2 tomato_healthy
# 3 tomato_late_blight
# 4 tomato_leaf_mold
# 5 tomato_septorial_leaf_spot
# 6 tomato_spider_mite
# 7 tomato_target_spot
# 8 tomato_mosaic_virus
# 9 tomato_yellow_leaf_curl_virus




