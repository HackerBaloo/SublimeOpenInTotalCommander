import os
import os.path
import subprocess
import sublime
import sublime_plugin


class SelectInTotalCommanderCommand(sublime_plugin.TextCommand):
    def set_exe(self, exe):
        if os.path.exists(exe):
            #print('exe: ', exe)
            self.exe = exe
            return True
        return False    

    def __init__(self, view):
        self.view = view
        settings = sublime.load_settings("Open in Total Commander.sublime-settings")
        self.args = settings.get("aruments")
        env_name = settings.get("path_environment_variable")
        #print('env_name: ', env_name)
        variable = ''
        if os.environ.has_key(env_name):
            variable = os.environ[env_name]
        if not self.set_exe(variable):
            if not self.set_exe(settings.get("executable")):
                if not self.set_exe(settings.get("executable2")):
                    sublime.error_message('No executable found, check Open in Total Commander.sublime-settings!')


    def run(self, edit):
        path = self.view.file_name()
        if path is None:
            sublime.error_message('No file in view')
            return
        #print('path: ', path)
        #print('self.args: ', self.args)
        args = self.args.format(**locals())
        #print('args: ', args)
        cmd = '{self.exe} {args}'.format(**locals())
        print('cmd: ', cmd)
        if os.name == 'posix':
            subprocess.call([self.exe, args])
        else:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            proc = subprocess.Popen(cmd, startupinfo=startupinfo)
