__pragma__('alias','S','$')

from model import Model
from view import View

class Presenter:
    def __init__(self):
        self._model = Model()
        self._view = View()
        self._bind()

    def _bind(self):
        S('body').on('todos-updated',self._on_todos_updated)
        S('#input-form').on('show.bs.modal',self._on_show_modal)
        S('#register-button').on('click',self._on_click_register)

    def start(self):
        self._model.load_all_todos()

    def _on_todos_updated(self,event):
        self._view.render_todo_list(self._model.get_all_todos())

    #モーダルが画面に出た時に入っていた値を初期化する関数
    def _on_todos_updated(self):
        S('#modal-title').val("新規登録")
        S('#modal-todo-id').val("")
        S('#modal-todo-title').val("")
        S('#modal-todo-memo').val("")
        S('#modal-todo-priority').val(1)

