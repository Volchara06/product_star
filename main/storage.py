from model.post import Post
from model.сomment import Comment

class StorageException(Exception):
    pass

class Storage:
    def __init__(self):
        self.dict = {}
        self.id_counter = 0



    def create_post(self, post: Post):    #записали пост в хранилище
        self.id_counter += 1
        self.dict[str(self.id_counter)] = post
        return str(self.id_counter)



    def read_post(self, post_id: str):    #выдаем пост из хранилища
        try:
            return self.dict[post_id]
        except Exception:
            raise StorageException('no such post')


    def read_all_posts(self):    #выдаем все посты
        return self.dict


    def edit_post(self, post_id: str, post: Post):    #перезаписываем пост
        if post_id in self.dict:
            self.dict[str(post_id)] = post
        else:
            raise StorageException('no such post')


    def delete_post(self, post_id: str):     #Удаляем пост
        try:
            del self.dict[post_id]
        except Exception:
            raise StorageException('no such post')


    def create_comment(self, post_id, comment: Comment):   #добавляем комментарий к посту
        try:
            self.dict[post_id].comments.append(comment)
            return self.dict[post_id].comments
        except Exception:
            raise StorageException('no such post')


