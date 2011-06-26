# -*- coding: utf-8 -*-
import template
from PyQt4 import QtCore, QtGui

class FileLoader(QtGui.QWidget):
    """Interface for 1) displaying directory tree and 2) loading a file from the tree.
    You must call setHost, and the widget will call host.loadFileRequested whenever 
    the user requests to load a file."""
    
    
    sigFileLoaded = QtCore.Signal(object)
    sigBaseChanged = QtCore.Signal(object)
    
    def __init__(self, dataManager, host=None, showFileTree=True):
        self.dataManager = dataManager
        QtGui.QWidget.__init__(self)
        self.ui = template.Ui_Form()
        self.ui.setupUi(self)
        self.setHost(host)
        self.ui.setDirBtn.clicked.connect(self.setBaseClicked)
        self.ui.loadBtn.clicked.connect(self.loadClicked)
        self.ui.fileTree.setVisible(showFileTree)
        
    def setHost(self, host):
        self.host = host
        
    def setBaseClicked(self):
        dh = self.dataManager.selectedFile()
        if dh is None:
            raise Exception("No directory selected in data manager")
        self.ui.dirTree.setBaseDirHandle(dh)
        self.sigBaseChanged.emit(dh)
        
    def loadClicked(self):
        fh = self.ui.dirTree.selectedFiles()
        self.loadFile(fh)
        
    def loadFile(self, files):
        for fh in files:
            if self.host is None:
                self.sigFileLoaded.emit(fh)

            elif self.host.loadFileRequested([fh]):
                name = fh.name(relativeTo=self.ui.dirTree.baseDirHandle())
                item = QtGui.QTreeWidgetItem([name])
                item.file = fh
                self.ui.fileTree.addTopLevelItem(item)
                self.sigFileLoaded.emit(fh)
        #self.emit(QtCore.SIGNAL('fileLoaded'), fh)
        
    def selectedFile(self):
        return self.ui.fileTree.currentItem().file
        
    #def setSelectedFile(self, fh):
        
        