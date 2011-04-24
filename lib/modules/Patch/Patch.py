# -*- coding: utf-8 -*-
from lib.modules.Module import *
from PatchWindow import *

class Patch(Module):
    def __init__(self, manager, name, config):
        Module.__init__(self, manager, name, config)
        self.ui = PatchWindow(manager, config['clampDev'])
    
    def window(self):
        return self.ui

    def quit(self):
        self.ui.quit()