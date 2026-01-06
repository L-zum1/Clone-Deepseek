import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import uuid

# 使用内存存储替代本地文件存储，以适应 Vercel 无服务器环境
conversations_store: Dict[str, dict] = {}

CONVERSATIONS_FILE = 'conversations.json'

def load_conversations() -> Dict[str, dict]:
    # 在本地开发环境仍使用文件存储，便于测试
    if os.environ.get('VERCEL_ENV') is None:
        if not os.path.exists(CONVERSATIONS_FILE):
            return {}
        
        try:
            with open(CONVERSATIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    # 在 Vercel 环境使用内存存储
    else:
        return conversations_store

def save_conversations(conversations: Dict[str, dict]) -> None:
    # 在本地开发环境仍使用文件存储，便于测试
    if os.environ.get('VERCEL_ENV') is None:
        with open(CONVERSATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, ensure_ascii=False, indent=2)
    # 在 Vercel 环境更新内存存储
    else:
        global conversations_store
        conversations_store = conversations.copy()

def create_conversation(title: str = '新对话') -> str:
    conversations = load_conversations()
    conversation_id = str(uuid.uuid4())
    
    conversations[conversation_id] = {
        'id': conversation_id,
        'title': title,
        'messages': [],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    save_conversations(conversations)
    return conversation_id

def get_conversation(conversation_id: str) -> Optional[dict]:
    conversations = load_conversations()
    return conversations.get(conversation_id)

def update_conversation_title(conversation_id: str, title: str) -> bool:
    conversations = load_conversations()
    
    if conversation_id not in conversations:
        return False
    
    conversations[conversation_id]['title'] = title
    conversations[conversation_id]['updated_at'] = datetime.now().isoformat()
    save_conversations(conversations)
    return True

def add_message(conversation_id: str, role: str, content: str) -> bool:
    conversations = load_conversations()
    
    if conversation_id not in conversations:
        return False
    
    conversations[conversation_id]['messages'].append({
        'role': role,
        'content': content,
        'timestamp': datetime.now().isoformat()
    })
    conversations[conversation_id]['updated_at'] = datetime.now().isoformat()
    save_conversations(conversations)
    return True

def delete_conversation(conversation_id: str) -> bool:
    conversations = load_conversations()
    
    if conversation_id not in conversations:
        return False
    
    del conversations[conversation_id]
    save_conversations(conversations)
    return True

def get_all_conversations() -> List[dict]:
    conversations = load_conversations()
    return sorted(
        conversations.values(),
        key=lambda x: x['updated_at'],
        reverse=True
    )

def clear_conversation_messages(conversation_id: str) -> bool:
    conversations = load_conversations()
    
    if conversation_id not in conversations:
        return False
    
    conversations[conversation_id]['messages'] = []
    conversations[conversation_id]['updated_at'] = datetime.now().isoformat()
    save_conversations(conversations)
    return True