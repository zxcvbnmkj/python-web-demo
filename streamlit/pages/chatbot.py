import streamlit as st

st.title("聊天框")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("请在这里输入"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = f"【模拟回复】刚刚收到了你发送的 '{prompt}' "
        message_placeholder.markdown(assistant_response)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
