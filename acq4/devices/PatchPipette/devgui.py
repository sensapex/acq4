from __future__ import print_function
from ..Pipette import PipetteDeviceGui
from acq4.util import Qt


class PatchPipetteDeviceGui(PipetteDeviceGui):
    def __init__(self, dev, win):
        self.cleanFuture = None

        PipetteDeviceGui.__init__(self, dev, win)

        self.cleanBtn = Qt.QPushButton('Clean Pipette')
        self.setCleanBtn = Qt.QPushButton('Set Clean Pos')
        self.setRinseBtn = Qt.QPushButton('Set Rinse Pos')
        self.cleanBtnLayout = Qt.QHBoxLayout()
        self.cleanBtnLayout.addWidget(self.cleanBtn)
        self.cleanBtn.setCheckable(True)
        self.cleanBtnLayout.addWidget(self.setCleanBtn)
        self.cleanBtnLayout.addWidget(self.setRinseBtn)
        row = self.layout.rowCount()
        self.layout.addLayout(self.cleanBtnLayout, row, 0)

        self.cleanBtn.clicked.connect(self.cleanClicked)
        self.setCleanBtn.clicked.connect(self.setCleanClicked)
        self.setRinseBtn.clicked.connect(self.setRinseClicked)

    def cleanClicked(self):
        if self.cleanBtn.isChecked():
            self.cleanBtn.setText("Cleaning..")
            self.cleanFuture = self.dev.cleanPipette()
            self.cleanFuture.sigFinished.connect(self.cleaningFinished)
        else:
            if self.cleanFuture is not None and not self.cleanFuture.isDone():
                self.cleanFuture.stop()
            self.cleanBtn.setText("Clean Pipette")

    def cleaningFinished(self):
        self.cleanBtn.setText("Clean Pipette")
        self.cleanBtn.setChecked(False)

    def setCleanClicked(self):
        self.dev.savePosition('clean')

    def setRinseClicked(self):
        self.dev.savePosition('rinse')
