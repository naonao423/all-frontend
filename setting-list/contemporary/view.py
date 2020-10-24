__pragma__('alias','S','$')

class View:
    def render_todo_list(self,data):
        #この#はhtmlでのidを指示している。emptyで空にしている.
        S('#todo-list').empty()
        for todo in data:
            #このself._create_todo_rowはdataから呼び出したtodoをhtmlで表示できるように整える関数になる。
            S('#todo-list').append("""<tr><td><input type='checkbox' class='toggle-checkbox' id='check-{}' {}></td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td><button class='btn btn-outline-primary update-button' id='update-{}' data-toggle='modal' data-target='#input-form'>変更</button></td>
                    <td><button class='btn btn-outline-danger delete-button' id='delete-{}'>削除</button>
                    </td></tr>""".format(todo['id'],'checked' if todo['completed'] else '', todo['title'], todo['memo'],['低','中','高'][int(todo['priority'])-1],todo['id'],todo['id'])
                        )
