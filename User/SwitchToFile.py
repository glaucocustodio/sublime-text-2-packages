import sublime_plugin, os
class SwitchToFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.display_list = []
        self.views = []
        for view in self.window.views():
            path = view.file_name()
            if view.is_scratch():
                name = view.name()
                path = '(view id = %d)' % (view.id())
            elif not path:
                name = 'Untitled'
                path = '(view id = %d)' % (view.id())
            else:
                name = os.path.split(path)[1]
            self.display_list.append([name, path])
            self.views.append(view)

        self.window.show_quick_panel(self.display_list, self.switch_to_view, False)

    def switch_to_view(self, index):
        if index >= 0 and len(self.views) > index:
            self.window.focus_view(self.views[index])