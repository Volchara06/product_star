from model.post import Post
from model.сomment import Comment

class StorageException(Exception):
    pass

class Storage:
    def __init__(self):
        self.dict = {}
        self.id_counter = 0



    def create_post(self, post: Post):
        self.id_counter += 1
        self.dict[str(self.id_counter)] = post
        return str(self.id_counter)



    def read_post(self, post_id: str):
        try:
            return self.dict[post_id]
        except Exception:
            raise StorageException('no such post')


    def read_all_posts(self):
        return self.dict


    def edit_post(self, post_id: str, post: Post):
        if post_id in self.dict:
            self.dict[str(post_id)] = post
        else:
            raise StorageException('no such post')


    def delete_post(self, post_id: str):
        try:
            del self.dict[post_id]
        except Exception:
            raise StorageException('no such post')


    def create_comment(self, post_id, comment: Comment):
        try:
            self.dict[post_id].comments.append(comment)
            return self.dict[post_id].comments
        except Exception:
            raise StorageException('no such post')


