__pragma__('alias','S','$')

from const import BASE_URL
class Model:
    def __init__(self):
        self._todos = []
        self.start_time = S('#input_data_start').val()
        self.end_time = S('#input_data_stop').val()

    #まず最初にbackendのhttp://127.0.0.1:8000/にgetリクエストをして得たjsonをself._todosに入れる。
    def load_all_todos(self):
        self.start_time = S('#input_data_start').val()
        self.end_time = S('#input_data_stop').val()
        S.ajax({
            'url':"{}events/otherlists/{}/{}".format(BASE_URL,self.start_time,self.end_time),
            'type':'GET',
            }).done(self._success_load_all_todos
                    ).fail(
                            lambda d: alert("サーバに接続できませんでした。"))

    #成功したときのself.success_load_all_todosの読み込み
    def _success_load_all_todos(self,data):
        #ここでgetしたデータをself._todosに格納する
        self._todos = data
        #ここでtodo-updatedというイベントをpresentatorに送っているpresentatorはそれをviewに送る。
        S('body').trigger('todos-updated')


    def get_all_todos(self):
        return self._todos

    def get_todo(self,todo_id):
        for todo in self._todos:
            if todo['id'] == todo_id:
                return todo
        return None


