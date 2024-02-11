from flask import Flask, jsonify, request
import json
import model.storage
from model.post import Post
from model.comment import Comment


app = Flask(__name__)

my_storage = model.storage.Storage()
API_ROOT = '/api/blog'


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {"text": obj.text, "author": obj.author, "day": obj.day.isoformat(), "comments": obj.comments}
        elif isinstance(obj, Comment):
            return {"author": obj.author, "comment": obj.comment_body, "day": obj.day.isoformat()}
        else:
            return super().default(obj)


app.json_encoder = MyJSONEncoder



@app.route(API_ROOT + '/post/', methods=['POST'])  #создаем пост
def create_post():
    post_json = request.get_json()   #декодируем в словарь   body: {"text": "Excellent!", "author": "Grisha"}
    post = Post(post_json['text'], post_json['author'])
    post.id = my_storage.create_post(post)
    return jsonify({'status': 'success', 'message': f'id {post.id} created'})


@app.route(API_ROOT + '/post/<post_id>/', methods=['GET'])   #читаем добавленный пост
def read_post(post_id: str):
    try:
        return jsonify(my_storage.read_post(post_id))
    except Exception as ex:
        return f'{ex}'


@app.route(API_ROOT + '/post/', methods=['GET'])    #читаем все посты
def read_all_posts():
    return jsonify(my_storage.read_all_posts())



@app.route(API_ROOT + '/post/<post_id>/', methods=['PUT'])  #редактируем пост
def edit_post(post_id: str):
    try:
        post_json = request.get_json()   #декодируем в словарь    body: {"text": "Excellent!", "author": "Grisha"}
        post = Post(post_json['text'], post_json['author'])
        my_storage.edit_post(post_id, post)
        return jsonify({'status': 'success', 'message': f'id {post.id} edited'})
    except Exception as ex:
        return f'{ex}'

@app.route(API_ROOT + '/post/<post_id>/', methods=['DELETE'])   #удаляем пост
def delete_post(post_id: str):
    try:
        my_storage.delete_post(post_id)
        return jsonify({'status': 'success', 'message': f'id {post_id} deleted'})
    except Exception as ex:
        return f'{ex}'


@app.route(API_ROOT + '/post/<post_id>/', methods=['POST'])  #создаем коммент к посту
def create_comment(post_id: str):
    try:
        comment_json = request.get_json()   #декодируем в словарь   body: {"text": "Excellent!", "author": "Grisha"}
        comment = Comment(comment_json['text'], comment_json['author'], post_id)
        my_storage.create_comment(post_id, comment)
        return jsonify({'status': 'success', 'message': f'comment to the post: {post_id} created'})
    except Exception as ex:
        return f'{ex}'


if __name__ == '__main__':
    app.run(debug=True)