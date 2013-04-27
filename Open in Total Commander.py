import os
import subprocess
import sublime
import sublime_plugin


class SelectInTotalCommanderCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        self.settings = sublime.load_settings("Open in Total Commander.sublime-settings")
        env_name = self.settings.get("path_environment_variable")
        #print('env_name: ', env_name)
        env = ''

        exe = self.settings.get("executable")
        #print('exe: ', exe)	
        if env_name:
            env = os.environ[env_name]
            print('env: ', env)
            self.exe = os.path.join(env, exe)
        else:
            self.exe = exe
        self.args = self.settings.get("aruments")

    def run(self, edit):
        path = self.view.file_name()
        if path is None:
            sublime.error_message('No file in view')
            return
        print('path: ', path)
        print('self.args: ', self.args)
        args = self.args.format(**locals())
        print('args: ', args)
        cmd = '{self.exe} {args}'.format(**locals())
        print('cmd: ', cmd)
        if os.name == 'posix':
            subprocess.call([self.exe, args])
        else:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            proc = subprocess.Popen(cmd, startupinfo=startupinfo)
