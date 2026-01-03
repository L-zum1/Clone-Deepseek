from flask import Flask, render_template, request, jsonify, session
from untils import get_chat_response
from langchain.memory import ConversationBufferMemory
from conversation_manager import (
    create_conversation,
    get_conversation,
    update_conversation_title,
    add_message,
    delete_conversation,
    get_all_conversations,
    clear_conversation_messages
)
import os

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    conversations = get_all_conversations()
    return jsonify({'conversations': conversations})

@app.route('/api/conversations', methods=['POST'])
def create_new_conversation():
    conversation_id = create_conversation()
    conversation = get_conversation(conversation_id)
    return jsonify({'conversation': conversation})

@app.route('/api/conversations/<conversation_id>', methods=['GET'])
def get_conversation_by_id(conversation_id):
    conversation = get_conversation(conversation_id)
    if conversation:
        return jsonify({'conversation': conversation})
    else:
        return jsonify({'error': '对话不存在'}), 404

@app.route('/api/conversations/<conversation_id>', methods=['DELETE'])
def delete_conversation_by_id(conversation_id):
    if delete_conversation(conversation_id):
        return jsonify({'success': True})
    else:
        return jsonify({'error': '对话不存在'}), 404

@app.route('/api/conversations/<conversation_id>/clear', methods=['POST'])
def clear_conversation_by_id(conversation_id):
    if clear_conversation_messages(conversation_id):
        return jsonify({'success': True})
    else:
        return jsonify({'error': '对话不存在'}), 404

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt', '')
    api_key = data.get('api_key', '')
    conversation_id = data.get('conversation_id')
    
    if not api_key:
        api_key = os.getenv("ARK_API_KEY")
        if not api_key:
            return jsonify({'error': '请提供 API Key'}), 400
    
    if not prompt:
        return jsonify({'error': '请输入问题'}), 400
    
    try:
        if not conversation_id:
            conversation_id = create_conversation()
        
        conversation = get_conversation(conversation_id)
        if not conversation:
            conversation_id = create_conversation()
            conversation = get_conversation(conversation_id)
        
        memory = ConversationBufferMemory(return_messages=True)
        
        for msg in conversation['messages']:
            if msg['role'] == 'user':
                memory.chat_memory.add_user_message(msg['content'])
            elif msg['role'] == 'assistant':
                memory.chat_memory.add_ai_message(msg['content'])
        
        response = get_chat_response(prompt, memory, api_key)
        
        if response:
            add_message(conversation_id, 'user', prompt)
            add_message(conversation_id, 'assistant', response)
            
            if conversation['title'] == '新对话':
                title = prompt[:20] + ('...' if len(prompt) > 20 else '')
                update_conversation_title(conversation_id, title)
            
            updated_conversation = get_conversation(conversation_id)
            
            return jsonify({
                'response': response,
                'conversation': updated_conversation
            })
        else:
            return jsonify({'error': 'API 调用失败'}), 500
            
    except Exception as e:
        app.logger.error(f"Chat API error: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_chat():
    data = request.json
    conversation_id = data.get('conversation_id')
    
    if conversation_id and clear_conversation_messages(conversation_id):
        return jsonify({'success': True})
    else:
        return jsonify({'error': '对话不存在'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
