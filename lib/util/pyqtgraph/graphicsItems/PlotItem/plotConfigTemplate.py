# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotConfigTemplate.ui'
#
# Created: Sat Apr 21 14:42:02 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(258, 605)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup = QtGui.QGroupBox(Form)
        self.averageGroup.setGeometry(QtCore.QRect(10, 200, 242, 182))
        self.averageGroup.setToolTip(QtGui.QApplication.translate("Form", "Display averages of the curves displayed in this plot. The parameter list allows you to choose parameters to average over (if any are available).", None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup.setTitle(QtGui.QApplication.translate("Form", "Average", None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup.setCheckable(True)
        self.averageGroup.setChecked(False)
        self.averageGroup.setObjectName(_fromUtf8("averageGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.averageGroup)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.avgParamList = QtGui.QListWidget(self.averageGroup)
        self.avgParamList.setObjectName(_fromUtf8("avgParamList"))
        self.gridLayout_5.addWidget(self.avgParamList, 0, 0, 1, 1)
        self.decimateGroup = QtGui.QGroupBox(Form)
        self.decimateGroup.setGeometry(QtCore.QRect(0, 70, 242, 160))
        self.decimateGroup.setTitle(QtGui.QApplication.translate("Form", "Downsample", None, QtGui.QApplication.UnicodeUTF8))
        self.decimateGroup.setCheckable(True)
        self.decimateGroup.setObjectName(_fromUtf8("decimateGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.decimateGroup)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.manualDecimateRadio = QtGui.QRadioButton(self.decimateGroup)
        self.manualDecimateRadio.setText(QtGui.QApplication.translate("Form", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.manualDecimateRadio.setChecked(True)
        self.manualDecimateRadio.setObjectName(_fromUtf8("manualDecimateRadio"))
        self.gridLayout_4.addWidget(self.manualDecimateRadio, 0, 0, 1, 1)
        self.downsampleSpin = QtGui.QSpinBox(self.decimateGroup)
        self.downsampleSpin.setMinimum(1)
        self.downsampleSpin.setMaximum(100000)
        self.downsampleSpin.setProperty("value", 1)
        self.downsampleSpin.setObjectName(_fromUtf8("downsampleSpin"))
        self.gridLayout_4.addWidget(self.downsampleSpin, 0, 1, 1, 1)
        self.autoDecimateRadio = QtGui.QRadioButton(self.decimateGroup)
        self.autoDecimateRadio.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.autoDecimateRadio.setChecked(False)
        self.autoDecimateRadio.setObjectName(_fromUtf8("autoDecimateRadio"))
        self.gridLayout_4.addWidget(self.autoDecimateRadio, 1, 0, 1, 1)
        self.maxTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.maxTracesCheck.setToolTip(QtGui.QApplication.translate("Form", "If multiple curves are displayed in this plot, check this box to limit the number of traces that are displayed.", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesCheck.setText(QtGui.QApplication.translate("Form", "Max Traces:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesCheck.setObjectName(_fromUtf8("maxTracesCheck"))
        self.gridLayout_4.addWidget(self.maxTracesCheck, 2, 0, 1, 1)
        self.maxTracesSpin = QtGui.QSpinBox(self.decimateGroup)
        self.maxTracesSpin.setToolTip(QtGui.QApplication.translate("Form", "If multiple curves are displayed in this plot, check \"Max Traces\" and set this value to limit the number of traces that are displayed.", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesSpin.setObjectName(_fromUtf8("maxTracesSpin"))
        self.gridLayout_4.addWidget(self.maxTracesSpin, 2, 1, 1, 1)
        self.forgetTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.forgetTracesCheck.setToolTip(QtGui.QApplication.translate("Form", "If MaxTraces is checked, remove curves from memory after they are hidden (saves memory, but traces can not be un-hidden).", None, QtGui.QApplication.UnicodeUTF8))
        self.forgetTracesCheck.setText(QtGui.QApplication.translate("Form", "Forget hidden traces", None, QtGui.QApplication.UnicodeUTF8))
        self.forgetTracesCheck.setObjectName(_fromUtf8("forgetTracesCheck"))
        self.gridLayout_4.addWidget(self.forgetTracesCheck, 3, 0, 1, 2)
        self.transformGroup = QtGui.QFrame(Form)
        self.transformGroup.setGeometry(QtCore.QRect(0, 0, 154, 79))
        self.transformGroup.setObjectName(_fromUtf8("transformGroup"))
        self.gridLayout = QtGui.QGridLayout(self.transformGroup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fftCheck = QtGui.QCheckBox(self.transformGroup)
        self.fftCheck.setText(QtGui.QApplication.translate("Form", "Power Spectrum (FFT)", None, QtGui.QApplication.UnicodeUTF8))
        self.fftCheck.setObjectName(_fromUtf8("fftCheck"))
        self.gridLayout.addWidget(self.fftCheck, 0, 0, 1, 1)
        self.logXCheck = QtGui.QCheckBox(self.transformGroup)
        self.logXCheck.setText(QtGui.QApplication.translate("Form", "Log X", None, QtGui.QApplication.UnicodeUTF8))
        self.logXCheck.setObjectName(_fromUtf8("logXCheck"))
        self.gridLayout.addWidget(self.logXCheck, 1, 0, 1, 1)
        self.logYCheck = QtGui.QCheckBox(self.transformGroup)
        self.logYCheck.setText(QtGui.QApplication.translate("Form", "Log Y", None, QtGui.QApplication.UnicodeUTF8))
        self.logYCheck.setObjectName(_fromUtf8("logYCheck"))
        self.gridLayout.addWidget(self.logYCheck, 2, 0, 1, 1)
        self.pointsGroup = QtGui.QGroupBox(Form)
        self.pointsGroup.setGeometry(QtCore.QRect(10, 550, 234, 58))
        self.pointsGroup.setTitle(QtGui.QApplication.translate("Form", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.pointsGroup.setCheckable(True)
        self.pointsGroup.setObjectName(_fromUtf8("pointsGroup"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.pointsGroup)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.autoPointsCheck = QtGui.QCheckBox(self.pointsGroup)
        self.autoPointsCheck.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.autoPointsCheck.setChecked(True)
        self.autoPointsCheck.setObjectName(_fromUtf8("autoPointsCheck"))
        self.verticalLayout_5.addWidget(self.autoPointsCheck)
        self.gridGroup = QtGui.QFrame(Form)
        self.gridGroup.setGeometry(QtCore.QRect(10, 460, 221, 81))
        self.gridGroup.setObjectName(_fromUtf8("gridGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.xGridCheck = QtGui.QCheckBox(self.gridGroup)
        self.xGridCheck.setText(QtGui.QApplication.translate("Form", "Show X Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.xGridCheck.setObjectName(_fromUtf8("xGridCheck"))
        self.gridLayout_2.addWidget(self.xGridCheck, 0, 0, 1, 2)
        self.yGridCheck = QtGui.QCheckBox(self.gridGroup)
        self.yGridCheck.setText(QtGui.QApplication.translate("Form", "Show Y Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.yGridCheck.setObjectName(_fromUtf8("yGridCheck"))
        self.gridLayout_2.addWidget(self.yGridCheck, 1, 0, 1, 2)
        self.gridAlphaSlider = QtGui.QSlider(self.gridGroup)
        self.gridAlphaSlider.setMaximum(255)
        self.gridAlphaSlider.setProperty("value", 70)
        self.gridAlphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gridAlphaSlider.setObjectName(_fromUtf8("gridAlphaSlider"))
        self.gridLayout_2.addWidget(self.gridAlphaSlider, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridGroup)
        self.label.setText(QtGui.QApplication.translate("Form", "Opacity", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.alphaGroup = QtGui.QGroupBox(Form)
        self.alphaGroup.setGeometry(QtCore.QRect(10, 390, 234, 60))
        self.alphaGroup.setTitle(QtGui.QApplication.translate("Form", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.alphaGroup.setCheckable(True)
        self.alphaGroup.setObjectName(_fromUtf8("alphaGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.alphaGroup)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.autoAlphaCheck = QtGui.QCheckBox(self.alphaGroup)
        self.autoAlphaCheck.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.autoAlphaCheck.setChecked(False)
        self.autoAlphaCheck.setObjectName(_fromUtf8("autoAlphaCheck"))
        self.horizontalLayout.addWidget(self.autoAlphaCheck)
        self.alphaSlider = QtGui.QSlider(self.alphaGroup)
        self.alphaSlider.setMaximum(1000)
        self.alphaSlider.setProperty("value", 1000)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setObjectName(_fromUtf8("alphaSlider"))
        self.horizontalLayout.addWidget(self.alphaSlider)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

