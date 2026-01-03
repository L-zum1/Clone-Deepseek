# 导入库
import streamlit as st
from untils import get_chat_response
from langchain.memory import ConversationBufferMemory
import os

# 设置页面标题
st.title("JUN")

#加入侧边栏获取API密钥
ARK_API_KEY =  os.getenv("ARK_API_KEY") or st.sidebar.text_input("请输入ARK_API_KEY", type="password")

#初始化记忆
if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(return_messages=True)

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{'role': 'system', 'content': '你是一个专业的助手'},{'role': 'ai', 'content': '你好！有什么我可以帮助你的吗？'}]

for message in st.session_state['chat_history']:
    st.chat_message(message['role']).write(message['content'])

#创建聊天输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    if not ARK_API_KEY:
        ARK_API_KEY = os.getenv("ARK_API_KEY")
        if not ARK_API_KEY:
            st.info("请输入ARK_API_KEY")
            st.stop()
    st.session_state['chat_history'].append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    with st.spinner("JUN正在思考..."):
        response = get_chat_response(prompt,st.session_state['memory'],ARK_API_KEY)

    msg = {'role': 'ai', 'content': response}
    st.session_state['chat_history'].append(msg)
    st.chat_message('ai').write(response)

