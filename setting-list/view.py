__pragma__('alias','S','$')

class View:
    def render_todo_list(self,data):
        #この#はhtmlでのidを指示している。emptyで空にしている.
        S('#setting-table').empty()
        for item in data:
            pass
            #このself._create_todo_rowはdataから呼び出したtodoをhtmlで表示できるように整える関数になる。
            S('#setting-table').append("""<tr>
            <td id="subject-{}">{}</td>
                    <td><input id="input-{}" value="{}"></td>
                    </tr>""".format(item['sub'],item['sub'],item["sub"],item['goal'])
                        )

