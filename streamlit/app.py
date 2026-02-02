import streamlit as st


def app():
    st.title("主页")


pg = st.navigation({
    "主页": [
        st.Page(app, title="主页", icon="🏠"),
    ],
    "功能": [
        st.Page("pages/docs.py", title="文档显示", icon="📄"),
        st.Page("pages/chatbot.py", title="聊天框", icon="🤖"),

    ],
    "图像": [
        st.Page("pages/photo.py", title="图像处理", icon="📷"),
    ],
    "其他": [
        st.Page("pages/jupyter.py", title="代码和输入展示", icon=":material/my_location:"),
    ]
})

pg.run()
