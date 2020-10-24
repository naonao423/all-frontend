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
        S('#input_data_start').on('change',self._model.load_all_todos())
        S('#input_data_stop').on('change',self._model.load_all_todos())

    def start(self):
        self._model.load_all_todos()

    def _on_todos_updated(self,event):
        self._view.render_todo_list(self._model.get_all_todos())
