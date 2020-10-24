__pragma__('alias','S','$')

from model import Model
from view import View

class Presenter:
    def __init__(self):
        self._model = Model()
        self._view = View()
        self._bind()
        self.todo = []

    def _bind(self):
        S('body').on('todos-updated',self._on_todos_updated)
        S('#setting-change').on('click',self._on_change_setting)

    def start(self):
        self._model.load_all_todos()

    def _on_todos_updated(self,event):
        self._view.render_todo_list(self._model.get_all_todos())

    def _on_change_setting(self,event):
        data = _view.get_setting_change_data()
        self._model.change_setting(data)
        self._view.show_modal_message()
