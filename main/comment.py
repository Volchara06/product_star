from datetime import date
from model.user import User

class Comment:
    def __init__(self, comment_body: str, author: User, post_id: str):
        self.comment_body = comment_body
        self.author = author
        self.day = date.today()
        self.post_id = post_id

