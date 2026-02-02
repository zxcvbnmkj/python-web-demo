import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import io
import numpy as np


def add_gaussian_noise(img, level=0.2):
    img_array = np.array(img)
    mean = 0
    sigma = level * 100
    gauss = np.random.normal(mean, sigma, img_array.shape).astype('uint8')
    noisy_array = img_array + gauss
    noisy_array = np.clip(noisy_array, 0, 255).astype('uint8')
    return Image.fromarray(noisy_array)

def add_salt_pepper_noise(img, prob=0.05):
    img_array = np.array(img)
    output = np.copy(img_array)
    num_salt = np.ceil(prob * img_array.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img_array.shape]
    output[tuple(coords)] = 0
    num_pepper = np.ceil(prob * img_array.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img_array.shape]
    output[tuple(coords)] = 255
    return Image.fromarray(output)


with st.expander("选择效果", expanded=True):
    cols = st.columns(5)
    use_bw = cols[0].checkbox("黑白")
    use_gauss = cols[1].checkbox("高斯噪声")
    use_salt = cols[2].checkbox("椒盐噪声")
    use_blur = cols[3].checkbox("模糊")
    use_sharpen = cols[4].checkbox("锐化")

c2, c3 = st.columns(2)
with c2:
    brightness = st.slider("亮度", 0.5, 2.0, 1.0)
with c3:
    contrast = st.slider("对比度", 0.5, 2.0, 1.0)

st.divider()

col_left, col_right = st.columns(2)

image = None

# 左侧列逻辑
with col_left:
    st.subheader("原始图片")

    img_placeholder = st.empty()
    uploader_container = st.container()

    with uploader_container:
        uploaded_file = st.file_uploader("上传新图片", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
    else:

        image = Image.open("img/img1.png")

    if image is not None:
        img_placeholder.image(image, use_container_width=True)

with col_right:
    st.subheader("处理结果")

    result_img_placeholder = st.empty()
    download_container = st.container()
    
    if image is not None:
        processed_image = image.copy()

        if use_bw:
            processed_image = processed_image.convert("L").convert("RGB")
        if use_gauss:
            processed_image = add_gaussian_noise(processed_image, level=0.2)
        if use_salt:
            processed_image = add_salt_pepper_noise(processed_image, prob=0.05)
        if use_blur:
            processed_image = processed_image.filter(ImageFilter.GaussianBlur(radius=2))
        if use_sharpen:
            processed_image = processed_image.filter(ImageFilter.SHARPEN)

        processed_image = ImageEnhance.Brightness(processed_image).enhance(brightness)
        processed_image = ImageEnhance.Contrast(processed_image).enhance(contrast)

        result_img_placeholder.image(processed_image, use_container_width=True)

        buf = io.BytesIO()
        processed_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        with download_container:
            st.download_button(
                label="下载处理后的图片",
                data=byte_im,
                file_name="processed_image.png",
                mime="image/png"
            )
