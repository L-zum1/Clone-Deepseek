# Clone-Deepseek

一个基于 DeepSeek API 的 AI 聊天助手应用，采用豆包风格的现代化界面设计。

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 功能特性

- 🤖 **智能对话**: 基于 DeepSeek API 的强大 AI 对话能力
- 💬 **多对话管理**: 支持创建、切换、删除多个对话
- 📝 **对话历史**: 自动保存对话记录，支持 JSON 格式持久化存储
- 🎨 **现代化界面**: 采用豆包风格的 UI 设计，响应式布局
- 📱 **移动端适配**: 完美支持手机和平板设备
- 🔒 **API Key 管理**: 安全的 API 密钥输入和管理
- 🚀 **快速部署**: 支持 Vercel 一键部署

## 技术栈

### 后端
- **Flask 3.0.2**: 轻量级 Web 框架
- **LangChain**: AI 应用开发框架
- **ConversationBufferMemory**: 对话记忆管理

### 前端
- **HTML5/CSS3**: 现代化界面设计
- **JavaScript (Vanilla)**: 原生 JavaScript 实现
- **响应式设计**: 移动端优先的布局策略

### AI 服务
- **DeepSeek API**: 先进的 AI 语言模型
- **OpenAI 兼容接口**: 标准化的 API 调用

## 项目结构

```
kelong/
├── flask_app.py              # Flask 主应用
├── conversation_manager.py   # 对话历史管理模块
├── untils.py                 # DeepSeek API 调用工具
├── requirements.txt          # Python 依赖
├── vercel.json              # Vercel 部署配置
├── templates/
│   └── index.html           # 前端界面
├── .gitignore              # Git 忽略文件
└── README.md               # 项目文档
```

## 安装步骤

### 本地开发

1. **克隆仓库**
   ```bash
   git clone https://github.com/L-zum1/Clone-Deepseek.git
   cd Clone-Deepseek
   ```

2. **创建虚拟环境**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置环境变量**
   
   创建 `.env` 文件并添加你的 DeepSeek API Key：
   ```env
   ARK_API_KEY=your_deepseek_api_key_here
   ```

5. **启动应用**
   ```bash
   python flask_app.py
   ```

6. **访问应用**
   
   打开浏览器访问：http://localhost:5001

## 使用方法

### 基本使用

1. 在左侧边栏的输入框中输入你的 DeepSeek API Key
2. 点击"新建对话"按钮创建新对话
3. 在输入框中输入问题并点击"发送"
4. AI 将自动回复并保存对话历史

### 对话管理

- **新建对话**: 点击左侧"新建对话"按钮
- **切换对话**: 点击左侧对话列表中的任意对话
- **删除对话**: 鼠标悬停在对话上，点击删除按钮
- **清空对话**: 点击顶部"清空对话"按钮清空当前对话内容

## 部署到 Vercel

### 方法一：使用 Vercel CLI

1. **安装 Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **登录 Vercel**
   ```bash
   vercel login
   ```

3. **部署项目**
   ```bash
   vercel
   ```

4. **配置环境变量**
   
   在 Vercel 控制台中添加环境变量：
   - `ARK_API_KEY`: 你的 DeepSeek API Key

### 方法二：通过 GitHub 集成

1. 将代码推送到 GitHub
2. 在 Vercel 控制台中导入项目
3. 配置环境变量
4. 自动部署

## API 接口

### 获取所有对话
```
GET /api/conversations
```

### 创建新对话
```
POST /api/conversations
```

### 获取特定对话
```
GET /api/conversations/<conversation_id>
```

### 删除对话
```
DELETE /api/conversations/<conversation_id>
```

### 清空对话内容
```
POST /api/conversations/<conversation_id>/clear
```

### 发送消息
```
POST /api/chat
Content-Type: application/json

{
  "prompt": "你的问题",
  "api_key": "你的API密钥",
  "conversation_id": "对话ID（可选）"
}
```

## 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `ARK_API_KEY` | DeepSeek API 密钥 | 是 |
| `SECRET_KEY` | Flask 会话密钥 | 否（自动生成） |

## 开发说明

### 添加新功能

1. 在 `flask_app.py` 中添加新的 API 端点
2. 在 `conversation_manager.py` 中添加数据管理逻辑
3. 在 `templates/index.html` 中更新前端界面

### 调试模式

应用默认以调试模式运行，可以在 `flask_app.py` 中修改：
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

## 常见问题

### Q: 如何获取 DeepSeek API Key？
A: 访问 [DeepSeek 官网](https://www.deepseek.com/) 注册账号并获取 API Key。

### Q: 虚拟环境太大怎么办？
A: 项目已优化依赖，虚拟环境大小约为 133MB。如需进一步优化，可以移除不必要的依赖。

### Q: 部署到 Vercel 后无法访问？
A: 检查环境变量是否正确配置，确保 `ARK_API_KEY` 已在 Vercel 控制台中设置。

## 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- 项目链接: [https://github.com/L-zum1/Clone-Deepseek](https://github.com/L-zum1/Clone-Deepseek)
- 问题反馈: [Issues](https://github.com/L-zum1/Clone-Deepseek/issues)

## 致谢

- [DeepSeek](https://www.deepseek.com/) - 提供 AI API 服务
- [Flask](https://flask.palletsprojects.com/) - Web 框架
- [LangChain](https://langchain.com/) - AI 应用开发框架
- [Galaxy UI](https://github.com/L-zum1/galaxy) - UI 设计灵感

---

**注意**: 请妥善保管你的 API Key，不要将其提交到公共仓库。
