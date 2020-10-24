__pragma__('alias','S','$')

class View:
    def render_todo_list(self,data):
        #この#はhtmlでのidを指示している。emptyで空にしている.
        S('#todo-list').empty()
        for todo in data:
            pass
            #このself._create_todo_rowはdataから呼び出したtodoをhtmlで表示できるように整える関数になる。
            S('#todo-list').append("""<tr>
            <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    </tr>""".format(todo['begin_date'],todo['sub'],todo['time_duration'],"None")
                        )

