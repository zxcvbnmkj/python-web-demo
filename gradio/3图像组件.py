import numpy as np
import gradio as gr


def sepia(input_img):
    # 处理图像
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


# shape设置输入图像大小
# Interface类的三个参数：fn、input、output 这里简写了
# gr.Image是一个图像组件，以此作为输入
# 参数3是"image"，表示期望 Gradio 接口将返回的结果呈现为图像。
demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
demo.launch()
