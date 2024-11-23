import subprocess

# default
install_dir = 'c:/LDPlayer/LDPlayerVK'
picture_dir = "/sdcard/Pictures"

class LDPlayer:
    name = ''
    def __init__(self, name):
        self.name = name

    def ldconsole(self, cmd, params=''):
        print(f'{install_dir}/ldconsole {cmd} --name {self.name} {params}')
        return subprocess.run(f'{install_dir}/ldconsole {cmd} --name {self.name} {params}', shell=True, capture_output=True, text=True)

    def is_running(self):
        return self.ldconsole('isrunning').stdout == 'running'

    def quit(self):
        if self.is_running():
            self.ldconsole('quit')

    def launch(self):
        if not self.is_running():
            self.ldconsole('launch')
    
    def reboot(self):
        if self.is_running():
            self.ldconsole('reboot')

    def kill_app(self, package_name='jp.pokemon.pokemontcgp'):
        self.ldconsole('killapp', f'--packagename {package_name}')

    def run_app(self, package_name='jp.pokemon.pokemontcgp'):
        self.ldconsole('runapp', f'--packagename {package_name}')

    def adb(self, cmd):
        self.ldconsole('adb', f'--command "shell {cmd}"')

    def screenshot(self, name="ss.png"):
        self.adb(f'screencap -p {picture_dir}/{name}')

    def tap(self, x, y):
        self.adb(f'input tap {x} {y}')

    def swipe(self, x1, y1, x2, y2, duration):
        self.adb(f'input swipe {x1} {y1} {x2} {y2} {duration}')

    def long_press(self, x, y, duration):
        self.swipe(x, y, x, y, duration)

    def input_text(self, text):
        self.adb(f'input text {text}')
    
 