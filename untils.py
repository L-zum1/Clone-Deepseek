#导入库
import os
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# 调用OpenAI API获取聊天响应
def get_chat_response(prompt,memory,ARK_API_KEY):
#获取API密钥
    ARK_API_KEY = ARK_API_KEY or os.getenv("ARK_API_KEY")
    if not ARK_API_KEY:
        print("错误: 未提供API密钥")
        return None
# 定义OpenAI模型
    llm = ChatOpenAI(
        model_name="deepseek-v3-2-251201",
        openai_api_key=ARK_API_KEY,
        openai_api_base="https://ark.cn-beijing.volces.com/api/v3",
        temperature=0.7
    )
#创造对话
    conversation = ConversationChain(llm=llm, memory=memory)

    response = conversation.invoke({"input": prompt})
    return response['response']