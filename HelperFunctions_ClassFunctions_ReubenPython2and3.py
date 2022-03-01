# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision D, 03/01/2022

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

###############
import os, sys, platform
import time, datetime
import threading
import collections
from copy import * #for deep_copy of dicts
import json
import math
import traceback
import socket, select, struct
import string
import keyboard #"sudo pip install keyboard"
import subprocess #for beep command line call
###############

###############
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###############

###############
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
###############

###############
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###############

#class HelperFunctions_ClassFunctions_ReubenPython2and3():

    #######################################################################################################################
    #######################################################################################################################
    #def __init__(self):
    #    pass
    #######################################################################################################################
    #######################################################################################################################

#IF FUNCTIONS ARE NOT CONTAINED WITHIN A CLASS, THEN THEY MUST NOT BE INDENTED AT ALL (WOULD WORK ON WINDOWS BUT NOT RASPBERY PI).

#######################################################################################################################
#######################################################################################################################
def GetMyPlatform(self):

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
            self.my_platform = "pi"
        else:
            self.my_platform = "linux"

    elif platform.system() == "Windows":
        self.my_platform = "windows"

    elif platform.system() == "Darwin":
        self.my_platform = "mac"

    else:
        self.my_platform = "other"

    print("The OS platform is: " + self.my_platform)
#######################################################################################################################
#######################################################################################################################

##########################################################################################################
##########################################################################################################
#https://stackoverflow.com/questions/28473415/is-it-possible-to-import-class-method-without-instantiating-class
#@staticmethod
#@classmethod
def ParseGUIparametersDict(self, setup_dict):

        ##########################################
        ##########################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            ##########################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = PassThrough0and1values_ExitProgramOtherwise(self, "USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("USE_GUI_FLAG = " + str(self.USE_GUI_FLAG))
            ##########################################

            ##########################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
                self.RootIsOwnedExternallyFlag = 1
            else:
                self.root = None
                self.RootIsOwnedExternallyFlag = 0

            print("RootIsOwnedExternallyFlag = " + str(self.RootIsOwnedExternallyFlag))
            ##########################################

            ##########################################
            if "GUI_RootAfterCallbackInterval_Milliseconds" in self.GUIparametersDict:
                self.GUI_RootAfterCallbackInterval_Milliseconds = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_RootAfterCallbackInterval_Milliseconds", self.GUIparametersDict["GUI_RootAfterCallbackInterval_Milliseconds"], 0.0, 1000.0))
            else:
                self.GUI_RootAfterCallbackInterval_Milliseconds = 30

            print("GUI_RootAfterCallbackInterval_Milliseconds = " + str(self.GUI_RootAfterCallbackInterval_Milliseconds))
            ##########################################

            ##########################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = PassThrough0and1values_ExitProgramOtherwise(self, "EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            ##########################################

            ##########################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = PassThrough0and1values_ExitProgramOtherwise(self, "PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            ##########################################

            ##########################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("NumberOfPrintLines = " + str(self.NumberOfPrintLines))
            ##########################################

            ##########################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = PassThrough0and1values_ExitProgramOtherwise(self, "UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            ##########################################

            ##########################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("GUI_ROW = " + str(self.GUI_ROW))
            ##########################################

            ##########################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("GUI_COLUMN = " + str(self.GUI_COLUMN))
            ##########################################

            ##########################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("GUI_PADX = " + str(self.GUI_PADX))
            ##########################################

            ##########################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("GUI_PADY = " + str(self.GUI_PADY))
            ##########################################

            ##########################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 0.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 0

            print("GUI_ROWSPAN = " + str(self.GUI_ROWSPAN))
            ##########################################

            ##########################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 0

            print("GUI_COLUMNSPAN = " + str(self.GUI_COLUMNSPAN))
            ##########################################

            ##########################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("GUI_STICKY = " + str(self.GUI_STICKY))
            ##########################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("URarm_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG = " + str(self.USE_GUI_FLAG))

        print("GUIparametersDict = " + str(self.GUIparametersDict))
        ##########################################
        ##########################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ComputeListNorm(self, InputList):
    #print("ComputeListNorm: InputList = " + str(InputList))

    norm = -1

    try:
        ElementsSquaredSum = 0.0
        for InputElement in InputList:
            InputElement = float(InputElement)
            ElementsSquaredSum = ElementsSquaredSum + InputElement * InputElement

        norm = math.sqrt(ElementsSquaredSum)

    except:
        exceptions = sys.exc_info()[0]
        print("ComputeListNorm Error, Exceptions: %s" % exceptions, 0)

    return norm
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def NormalizeListToUnitLength(self, InputList):
    OutputList = list(InputList)

    try:
        ElementsSquaredSum = 0.0
        for InputElement in InputList:
            InputElement = float(InputElement)
            ElementsSquaredSum = ElementsSquaredSum + InputElement * InputElement

        norm = math.sqrt(ElementsSquaredSum)

        for i, InputElement in enumerate(InputList):
            InputElement = float(InputElement)
            OutputList[i] = InputElement / norm

    except:
        exceptions = sys.exc_info()[0]
        print("NormalizeListToUnitLength Error, Exceptions: %s" % exceptions, 0)

    return OutputList
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
#@staticmethod
def MultiplyListOfNumbersByScalar(InputList, ScalarToMultiplyBy):
    OutputList = list(InputList)

    try:
        for i, OutputElement in enumerate(OutputList):
            OutputElementFloat = float(OutputElement)
            OutputList[i] = ScalarToMultiplyBy*OutputElementFloat

    except:
        exceptions = sys.exc_info()[0]
        print("MultiplyListOfNumbersByScalar Error, Exceptions: %s" % exceptions, 0)
        return list()

    return OutputList
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsInputList(self, InputToCheck):

    result = isinstance(InputToCheck, list)
    return result
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsInputListOfNumbers(self, InputToCheck):

    if isinstance(InputToCheck, list) == 1:
        for element in InputToCheck:
            if isinstance(element, int) == 0 and isinstance(element, float) == 0:
                return 0
    else:
        return 0

    return 1  # If InputToCheck was a list and no element failed to be a float or int, then return a success/1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers=4, number_of_decimal_places=3):
    IsListFlag = IsInputList(self, input)

    if IsListFlag == 0:
        float_number_list = [input]
    else:
        float_number_list = list(input)

    float_number_list_as_strings = []
    for element in float_number_list:
        try:
            element = float(element)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)
            float_number_list_as_strings.append(element_as_string)
        except:
            print(TellWhichFileWereIn(self) + ": ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput ERROR: " + str(element) + " cannot be turned into a float")
            return -1

    StringToReturn = ""
    if IsListFlag == 0:
        StringToReturn = float_number_list_as_strings[0].zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
    else:
        StringToReturn = "["
        for index, StringElement in enumerate(float_number_list_as_strings):
            if float_number_list[index] >= 0:
                StringElement = "+" + StringElement  # So that our strings always have either + or - signs to maintain the same string length

            StringElement = StringElement.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place

            if index != len(float_number_list_as_strings) - 1:
                StringToReturn = StringToReturn + StringElement + ", "
            else:
                StringToReturn = StringToReturn + StringElement + "]"

    return StringToReturn
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def MyPrint_WithoutLogFile(self, input_string):

    input_string = str(input_string)

    if input_string != "":

        #input_string = input_string.replace("\n", "").replace("\r", "")

        ################################ Write to console
        # Some people said that print crashed for pyinstaller-built-applications and that sys.stdout.write fixed this.
        # http://stackoverflow.com/questions/13429924/pyinstaller-packaged-application-works-fine-in-console-mode-crashes-in-window-m
        if self.PrintToConsoleFlag == 1:
            sys.stdout.write(input_string + "\n")
        ################################

        ################################ Write to GUI
        self.PrintToGui_Label_TextInputHistory_List.append(self.PrintToGui_Label_TextInputHistory_List.pop(0)) #Shift the list
        self.PrintToGui_Label_TextInputHistory_List[-1] = str(input_string) #Add the latest value

        self.PrintToGui_Label_TextInput_Str = ""
        for Counter, Line in enumerate(self.PrintToGui_Label_TextInputHistory_List):
            self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + Line

            if Counter < len(self.PrintToGui_Label_TextInputHistory_List) - 1:
                self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + "\n"
        ################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertListOfValuesDegToRad(self, ListOfValuesDegToRadToBeConverted):

    ListOfValuesRadToBeReturned = list()

    try:
        if IsInputList(self, ListOfValuesDegToRadToBeConverted) == 0:
            ListOfValuesDegToRadToBeConverted = list([ListOfValuesDegToRadToBeConverted])

        for index, value in enumerate(ListOfValuesDegToRadToBeConverted):
            ListOfValuesRadToBeReturned.append(value*math.pi/180.0)

        return ListOfValuesRadToBeReturned

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertListOfValuesDegToRad Exceptions: %s" % exceptions)
        return ListOfValuesRadToBeReturned
        #traceback.print_exc()

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertListOfValuesRadToDeg(self, ListOfValuesRadToDegToBeConverted):

    ListOfValuesDegToBeReturned = list()

    try:
        if IsInputList(self, ListOfValuesRadToDegToBeConverted) == 0:
            ListOfValuesDegToRadToBeConverted = list([ListOfValuesRadToDegToBeConverted])

        for index, value in enumerate(ListOfValuesRadToDegToBeConverted):
            ListOfValuesDegToBeReturned.append(value*180.0/math.pi)

        return ListOfValuesDegToBeReturned

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertListOfValuesRadToDeg Exceptions: %s" % exceptions)
        return ListOfValuesDegToBeReturned
        #traceback.print_exc()

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_DedicatedTxThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread - self.LastTime_CalculatedFromDedicatedTxThread

        if self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromDedicatedTxThread = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread

        self.LastTime_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_DedicatedTxThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_DedicatedRxThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread = self.CurrentTime_CalculatedFromDedicatedRxThread - self.LastTime_CalculatedFromDedicatedRxThread

        if self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromDedicatedRxThread = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread

        self.LastTime_CalculatedFromDedicatedRxThread = self.CurrentTime_CalculatedFromDedicatedRxThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_DedicatedRxThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_DedicatedKeyboardListeningThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread = self.CurrentTime_CalculatedFromDedicatedKeyboardListeningThread - self.LastTime_CalculatedFromDedicatedKeyboardListeningThread

        if self.DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromDedicatedKeyboardListeningThread = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread

        self.LastTime_CalculatedFromDedicatedKeyboardListeningThread = self.CurrentTime_CalculatedFromDedicatedKeyboardListeningThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_DedicatedKeyboardListeningThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(self):

    print("Exiting all threads for URarm_ReubenPython2and3Class object")

    self.EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def StartGUI(self, GuiParent=None):

    GUI_Thread_ThreadingObject = threading.Thread(target=self.GUI_Thread, args=(GuiParent,))
    GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
    GUI_Thread_ThreadingObject.start()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TellWhichFileWereIn(self):

    #We used to use this method, but it gave us the root calling file, not the class calling file
    #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

    frame = inspect.stack()[1]
    filename = frame[1][frame[1].rfind("\\") + 1:]
    filename = filename.replace(".py","")

    return filename
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString(self):
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GetMessageQueueLength_Tx(self):

    return self.TxMessageToSend_Queue.qsize()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GetMostRecentDataDict(self):

    self.MostRecentDataDict = dict()

    return self.MostRecentDataDict
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def SendTxMessage(self, MessageToSend):
    if self.TxMessageToSend_Queue.qsize() <= 1000:
        self.TxMessageToSend_Queue.put(MessageToSend)
    else:
        dummy = self.TxMessageToSend_Queue.get()
        self.TxMessageToSend_Queue.put(MessageToSend)
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def LimitTextEntryInput_IntOutputOnly(self, min_val, max_val, test_val, TextEntryObject):

    test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

    if test_val > max_val:
        test_val = max_val
    elif test_val < min_val:
        test_val = min_val
    else:
        test_val = test_val

    test_val = int(test_val)

    if TextEntryObject != "":
        if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
            TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        else:
            TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.

    return test_val
##########################################################################################################
##########################################################################################################

#######################################################################################################################
#######################################################################################################################
def LimitNumber_IntOutputOnly(self, min_val, max_val, test_val):
    if test_val > max_val:
        test_val = max_val

    elif test_val < min_val:
        test_val = min_val

    else:
        test_val = test_val

    test_val = int(test_val)

    return test_val
#######################################################################################################################
#######################################################################################################################

##########################################################################################################
##########################################################################################################
def LimitTextEntryInput_FloatOutputOnly(self, min_val, max_val, test_val, TextEntryObject):

    test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

    if test_val > max_val:
        test_val = max_val
    elif test_val < min_val:
        test_val = min_val
    else:
        test_val = test_val

    test_val = float(test_val)

    if TextEntryObject != "":
        if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
            TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        else:
            TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.

    return test_val
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

    try:
        InputNumber_ConvertedToFloat = float(InputNumber)
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

    try:
        if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
            return InputNumber_ConvertedToFloat
        else:
            input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                      InputNameString +
                      "' must be 0 or 1 (value was " +
                      str(InputNumber_ConvertedToFloat) +
                      "). Press any key (and enter) to exit.")

            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
    try:
        InputNumber_ConvertedToFloat = float(InputNumber)
    except:
        exceptions = sys.exc_info()[0]
        print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

    try:
        if InputNumber_ConvertedToFloat >= RangeMinValue and InputNumber_ConvertedToFloat <= RangeMaxValue:
            return InputNumber_ConvertedToFloat
        else:
            input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                      InputNameString +
                      "' must be in the range [" +
                      str(RangeMinValue) +
                      ", " +
                      str(RangeMaxValue) +
                      "] (value was " +
                      str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread_SetupGUI(self, parent):

    print("Starting the GUI_Thread for URarm_ReubenPython2and3Class object.")

    ###################################################
    if parent == None:  # This class object owns root and must handle it properly
        self.root = Tk()
        self.parent = self.root

        ################################################### SET THE DEFAULT FONT FOR ALL WIDGETS CREATED AFTTER/BELOW THIS CALL
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=8)
        self.root.option_add("*Font", default_font)
        ###################################################

    else:
        self.root = parent
        self.parent = parent
    ###################################################

    ###################################################
    self.myFrame = Frame(self.root)

    if self.UseBorderAroundThisGuiObjectFlag == 1:
        self.myFrame["borderwidth"] = 2
        self.myFrame["relief"] = "ridge"

    self.myFrame.grid(row=self.GUI_ROW,
                      column=self.GUI_COLUMN,
                      padx=self.GUI_PADX,
                      pady=self.GUI_PADY,
                      rowspan=self.GUI_ROWSPAN,
                      columnspan=self.GUI_COLUMNSPAN,
                      sticky = self.GUI_STICKY)
    ###################################################

    ###################################################
    self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150)  # RGB
    self.TKinter_LightBlueColor = '#%02x%02x%02x' % (150, 150, 255)  # RGB
    self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150)  # RGB
    self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
    self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
    self.TkinterScaleWidth = 10
    self.TkinterScaleLength = 250
    ###################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread_StartRootLoopAndHandleExitOfGUI(self):

        ########################
        if self.RootIsOwnedExternallyFlag == 0: #This class object owns root and must handle it properly
            self.root.protocol("WM_DELETE_WINDOW", HelperFunctions_ClassFunctions_ReubenPython2and3.ExitProgram_Callback)

            self.root.after(self.GUI_RootAfterCallbackInterval_Milliseconds, self.GUI_update_clock)
            self.GUI_ready_to_be_updated_flag = 1
            self.root.mainloop()
        else:
            self.GUI_ready_to_be_updated_flag = 1
        ########################

        ########################
        if self.RootIsOwnedExternallyFlag == 0: #This class object owns root and must handle it properly
            self.root.quit()  # Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
            self.root.destroy()  # Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
        ########################

##########################################################################################################
##########################################################################################################