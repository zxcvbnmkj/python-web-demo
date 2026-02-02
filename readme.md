## 环境问题
- 查看当前 python 版本： `pdm run python --version`，输出 `Python 3.9.23`，应该是 python 版本导致最高只能安装 `streamlit==1.12.0`，最新版本的 streamlit 的 github 显示 `requires-python = ">=3.10"`
- 同时还遇到该库依赖 `PyArrow` 库，它需要 `cmake`，尝试安装 `cmake` 后也有点问题，需要降低版本
```commandline
brew install cmake
```
- 删除 3 个 pdm 文件，创建 python 310 的环境
  - `conda create -n py310 python=3.10`
  - `pdm init --python /opt/miniforge3/envs/py310/bin/python`
  - `pdm add pyarrow==15.0.2`，默认的 23.0.0 版本没有 mac11 对应的预编译 wheel 包，需要从头构建，依赖 cmake，其他操作系统应该没有这个问题
  - `pdm add streamlit`
  - 成功安装最新版本的 1..53.1
  - `source /Users/xxx/venv/python-web-demo-K0cGvqI--3.10/bin/activate
  - `streamlit run streamlit/app.py`
- `gradio==4.29.0` 和 `fastapi==0.112.4` 可以兼容，这两个库都不能随意改版本，非常容易有冲突

## gradio
- 可参考[教程](https://blog.csdn.net/Hfengxiang/article/details/140783921?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-140783921-blog-140050236.235%5Ev43%5Epc_blog_bottom_relevance_base8&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-140783921-blog-140050236.235%5Ev43%5Epc_blog_bottom_relevance_base8&utm_relevant_index=5)

1. 在启动应用时设置 `share=True` 参数就可创建公开链接
2. 可以在 jupyter 中直接展示页面
3. `python app.py` 是普通启动方式，`gradio app.py` 是可以热重载

### 组件
- 应用界面：gr.Interface(简易场景，不可设置Row、Column等布局), gr.Blocks(定制化场景)
- 输入输出：gr.Image(图像), gr.Textbox(文本框), gr.DataFrame(数据框), gr.Dropdown(下拉选项), gr.Number(数字), gr.Markdown("xxx"),
 gr.Files, gr.Chatbot()
- 控制组件：gr.Button(按钮)
- 布局组件：gr.Tab(标签页), gr.Row(行布局), gr.Column(列布局), gr.Accordion(折叠内容)，gr.Group()

### 事件
1. `.click`
2. `.upload`: 多与 `gr.Files` 配合，上传文件
3. `.submit`（当提交时）: 多用于 `Textbox`，填写内容然后上传
4. `.change`（当变化时）: 多用于下拉框、`checkbox` 等组件

### 其他
1. 一个应用程序里面只能有一个Block，它是最高级别的应用程序容器
2. 队列: 如果函数推理时间较长，比如目标检测；或者应用程序处理流量过大，则需要使用 queue 方法进行排队。queue 方法使用 websockets，可以防止网络超时。如：`demo.queue().launch()`
3. 表示处理过程的函数，经常定义在 block 组件之内