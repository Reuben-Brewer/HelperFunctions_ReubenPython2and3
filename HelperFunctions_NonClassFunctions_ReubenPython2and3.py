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

#######################################################################################################################
#######################################################################################################################
def GetMyPlatform():
    my_platform = "other"

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)

    return my_platform
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def PassThrough0and1values_ExitProgramOtherwise(InputNameString, InputNumber):

    try:
        InputNumber_ConvertedToFloat = float(InputNumber)
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber for variable_name '" + InputNameString + "' must be a float value, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

    try:
        if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
            return InputNumber_ConvertedToFloat
        else:
            input("PassThrough0and1values_ExitProgramOtherwise Error. '" + InputNameString + "' must be 0 or 1 (value was " + str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")
            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def PassThroughFloatValuesInRange_ExitProgramOtherwise(InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
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
            input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" + InputNameString + "' must be in the range [" + str(RangeMinValue) + ", " + str(RangeMaxValue) + "] (value was " + str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")
            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()
#######################################################################################################################
#######################################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(GlobalsDict):

    print("ExitProgram_Callback event fired!")

    GlobalsDict["EXIT_PROGRAM_FLAG"] = 1
##########################################################################################################
##########################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile(JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):

    try:
        #################################

        ##############
        with open(JSONfilepathFull) as ParametersToBeLoaded_JSONfileObject:
            ParametersToBeLoaded_JSONfileParsedIntoDict = json.load(ParametersToBeLoaded_JSONfileObject)

        ParametersToBeLoaded_JSONfileObject.close()
        ##############

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        ##############
        for key, value in ParametersToBeLoaded_JSONfileParsedIntoDict.items():
            if USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS == 1:
                if key.upper().find("_FLAG") != -1:
                    PassThrough0and1values_ExitProgramOtherwise(key, value)

            if PrintResultsFlag == 1:
                print(key + ": " + str(value))

        ##############
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        return ParametersToBeLoaded_JSONfileParsedIntoDict
        #################################
    except:
        #################################
        exceptions = sys.exc_info()[0]
        print("LoadAndParseJSONfile_Advanced Error, Exceptions: %s" % exceptions)
        return dict()
        #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):

    try:
        #################################

        ##############
        with open(JSONfilepathFull) as ParametersToBeLoaded_JSONfileObject:
            ParametersToBeLoaded_JSONfileParsedIntoDict = json.load(ParametersToBeLoaded_JSONfileObject)

        ParametersToBeLoaded_JSONfileObject.close()
        ##############

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        ##############
        for key, value in ParametersToBeLoaded_JSONfileParsedIntoDict.items():
            if USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS == 1:
                if key.upper().find("_FLAG") != -1:
                    GlobalsDict[key] = PassThrough0and1values_ExitProgramOtherwise(key, value)
                else:
                    GlobalsDict[key] = value
            else:
                GlobalsDict[key] = value

            if PrintResultsFlag == 1:
                print(key + ": " + str(value))

        ##############
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        return ParametersToBeLoaded_JSONfileParsedIntoDict
        #################################
    except:
        #################################
        exceptions = sys.exc_info()[0]
        print("LoadAndParseJSONfile_Advanced Error, Exceptions: %s" % exceptions)
        return dict()
        #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ParseColonCommaSeparatedVariableString(line, print_line_flag = 0, numeric_values_only = 0):

    if print_line_flag == 1:
        print("ParseColonCommaSeparatedVariableString input: " + line)

    line_as_dict = dict()

    if len(line) > 0:
        try:
            line = line.replace("\n", "").replace("\r", "")
            line_as_list = filter(None, re.split("[,:]+", line))
            #print(line_as_list)

            toggle_counter = 0
            key = ""
            for element in line_as_list:
                if toggle_counter == 0:  # Every other element is a key, every other element is the value
                    key = element.strip()
                    toggle_counter = 1
                else:
                    if numeric_values_only == 1:
                        try:
                            line_as_dict[key] = float(element)
                            #print(key + " , " + element)
                        except:
                            line_as_dict[key] = "ERROR"
                    else:
                        line_as_dict[key] = element
                    toggle_counter = 0

            return line_as_dict
        except:
            exceptions = sys.exc_info()[0]
            print("ParseColonCommaSeparatedVariableString ERROR: Exceptions: %s" % exceptions)
            traceback.print_exc()
            return line_as_dict
    else:
        print("ParseColonCommaSeparatedVariableString WARNING: input string was zero-length")
        return line_as_dict
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def getTimeStampString():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%m_%d_%Y---%H_%M_%S')

    return st
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def IsTheTimeCurrentlyAM():
    ts = time.time()
    hour = int(datetime.datetime.fromtimestamp(ts).strftime('%H'))
    if hour < 12:
        return 1
    else:
        return 0
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def UpdateFrequencyCalculation_CalculatedFromMainThread(LoopCounter_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread, LastTime_CalculatedFromMainThread, DataStreamingFrequency_CalculatedFromMainThread, DataStreamingDeltaT_CalculatedFromMainThread):

    try:

        DataStreamingDeltaT_CalculatedFromMainThread = CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread

        ##########################
        if DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
            DataStreamingFrequency_CalculatedFromMainThread = 1.0/DataStreamingDeltaT_CalculatedFromMainThread
        ##########################

        LastTime_CalculatedFromMainThread = CurrentTime_CalculatedFromMainThread

        LoopCounter_CalculatedFromMainThread = LoopCounter_CalculatedFromMainThread + 1

        return [LoopCounter_CalculatedFromMainThread, LastTime_CalculatedFromMainThread, DataStreamingFrequency_CalculatedFromMainThread, DataStreamingDeltaT_CalculatedFromMainThread]

    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_CalculatedFromMainThread ERROR, exceptions: %s" % exceptions)
        return [-11111.0]*4
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LimitNumber_IntOutputOnly(min_val, max_val, test_val):
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

#######################################################################################################################
#######################################################################################################################
def TellWhichFileWereIn():

    #We used to use this method, but it gave us the root calling file, not the class calling file
    #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

    frame = inspect.stack()[1]
    filename = frame[1][frame[1].rfind("\\") + 1:]
    filename = filename.replace(".py","")

    return filename
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def IsInputList(input, print_result_flag = 0):

    result = isinstance(input, list)

    if print_result_flag == 1:
        print("IsInputList: " + str(result))

    return result
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def IsListAllNumbers(InputList):

    for item in InputList:
        try:
            FloatNumber = float(only_numerics(str(item))) #only_numerics needs the str of the number for it to convert properly
        except:
            return 0

    return 1
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def AddAnumberToEveryElementInAlist(ListInput, NumberToBeAddedToEveryElement):

    if IsInputList(ListInput) == 1:
        if IsListAllNumbers(ListInput) == 1:
            NewListWithNumberAddedToEveryElement = list([x + NumberToBeAddedToEveryElement for x in ListInput])
            return NewListWithNumberAddedToEveryElement
        else:
            print("AddAnumberToEveryElementInAlist: ERROR, ListInput must be all numbers!")
            return list()
    else:
        print("AddAnumberToEveryElementInAlist: ERROR, ListInput must be type 'List'; currently it is type " + str(type(ListInput)))
        return list()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def MultiplyAnumberWithEveryElementInAlist(ListInput, NumberToBeMultipliedWithEveryElement):

    if IsInputList(ListInput) == 1:
        if IsListAllNumbers(ListInput) == 1:
            NewListWithNumberMultipliedWithEveryElement = list([x * NumberToBeMultipliedWithEveryElement for x in ListInput])
            return NewListWithNumberMultipliedWithEveryElement
        else:
            print("MultiplyAnumberWithEveryElementInAlist: ERROR, ListInput must be all numbers!")
            return list()
    else:
        print("MultiplyAnumberWithEveryElementInAlist: ERROR, ListInput must be type 'List'; currently it is type " + str(type(ListInput)))
        return list()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input, number_of_leading_numbers=4, number_of_decimal_places=3):
    IsListFlag = IsInputList(input)

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
            print(TellWhichFileWereIn() + ": ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput ERROR: " + str(element) + " cannot be turned into a float")
            return -1

    NumberOfZeroesToAddForSign = 0
    if input < 0:
        NumberOfZeroesToAddForSign = 1

    StringToReturn = ""
    if IsListFlag == 0:
        StringToReturn = float_number_list_as_strings[0].zfill(number_of_leading_numbers + number_of_decimal_places + NumberOfZeroesToAddForSign + 1)  # +1 for sign, +1 for decimal place
    else:
        StringToReturn = "["
        for index, StringElement in enumerate(float_number_list_as_strings):
            if float_number_list[index] >= 0:
                StringElement = "+" + StringElement  # So that our strings always have either + or - signs to maintain the same string length

            StringElement = StringElement.zfill(number_of_leading_numbers + number_of_decimal_places + NumberOfZeroesToAddForSign + 1)  # +1 for sign, +1 for decimal place

            if index != len(float_number_list_as_strings) - 1:
                StringToReturn = StringToReturn + StringElement + ", "
            else:
                StringToReturn = StringToReturn + StringElement + "]"

    return StringToReturn
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName(CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction):

    TimerObject = threading.Timer(CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction) #Must pass arguments to callback-function via list as the third argument to Timer call
    TimerObject.daemon = True #Without the daemon=True, this recursive function won't terminate when the main program does.
    TimerObject.start()

    print("TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName event fired to call function: '" + str(FunctionToCall_NoParenthesesAfterFunctionName.__name__) + "' at time " + str(getPreciseSecondsTimeStampString()))

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def TimerCallbackFunctionWithFunctionAsArgument_Repeating_NoParenthesesAfterFunctionName(CycleTimeDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName):

    #print("TimerCallbackFunctionWithFunctionAsArgument_Repeating_NoParenthesesAfterFunctionName event fired to call function: '" + str(FunctionToCall_NoParenthesesAfterFunctionName.__name__) + "' at time " + str(getPreciseSecondsTimeStampString()))
    FunctionToCall_NoParenthesesAfterFunctionName()

    TimerObject = threading.Timer(CycleTimeDeltaTseconds, TimerCallbackFunctionWithFunctionAsArgument_Repeating_NoParenthesesAfterFunctionName, [CycleTimeDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName]) #Must pass arguments to callback-function via list as the third argument to Timer call
    TimerObject.daemon = True #Without the daemon=True, this recursive function won't terminate when the main program does.
    TimerObject.start()
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ConvertListOfValuesDegToRad(ListOfValuesDegToRadToBeConverted):

    ListOfValuesRadToBeReturned = list()

    try:
        if IsInputList(ListOfValuesDegToRadToBeConverted) == 0:
            ListOfValuesDegToRadToBeConverted = list([ListOfValuesDegToRadToBeConverted])

        for index, value in enumerate(ListOfValuesDegToRadToBeConverted):
            ListOfValuesRadToBeReturned.append(value*math.pi/180.0)

        return ListOfValuesRadToBeReturned

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertListOfValuesDegToRad Exceptions: %s" % exceptions)
        return ListOfValuesRadToBeReturned
        #traceback.print_exc()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ConvertListOfValuesRadToDeg(ListOfValuesRadToDegToBeConverted):

    ListOfValuesDegToBeReturned = list()

    try:
        if IsInputList(ListOfValuesRadToDegToBeConverted) == 0:
            ListOfValuesDegToRadToBeConverted = list([ListOfValuesRadToDegToBeConverted])

        for index, value in enumerate(ListOfValuesRadToDegToBeConverted):
            ListOfValuesDegToBeReturned.append(value*180.0/math.pi)

        return ListOfValuesDegToBeReturned

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertListOfValuesRadToDeg Exceptions: %s" % exceptions)
        return ListOfValuesDegToBeReturned
        #traceback.print_exc()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GUI_Thread_CreateRootAndSetRootParameters(GlobalsDict):

    ########################################################### KEY GUI LINE
    ###########################################################
    GlobalsDict["root"] = Tk()
    ###########################################################
    ###########################################################

    ################################################### SET THE DEFAULT FONT FOR ALL WIDGETS CREATED AFTTER/BELOW THIS CALL
    ###################################################
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=8)
    GlobalsDict["root"].option_add("*Font", default_font)
    ###################################################
    ###################################################

    ###################################################
    ###################################################
    GlobalsDict["TKinter_LightRedColor"] = '#%02x%02x%02x' % (255, 150, 150)  # RGB
    GlobalsDict["TKinter_LightGreenColor"] = '#%02x%02x%02x' % (150, 255, 150)  # RGB
    GlobalsDict["TKinter_LightBlueColor"] = '#%02x%02x%02x' % (150, 150, 255)  # RGB
    GlobalsDict["TKinter_LightYellowColor"] = '#%02x%02x%02x' % (255, 255, 150)  # RGB
    GlobalsDict["TKinter_DefaultGrayColor"] = '#%02x%02x%02x' % (240, 240, 240)  # RGB
    ###################################################
    ###################################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GUI_Thread_StartRootLoopAndHandleExitOfGUI(GlobalsDict):

    ###########################################################
    root = GlobalsDict["root"]
    ExitProgram_Callback = GlobalsDict["ExitProgram_Callback"]
    GUI_update_clock = GlobalsDict["GUI_update_clock"]
    ###########################################################

    ###########################################################
    if "GUI_RootAfterCallbackInterval_Milliseconds" in GlobalsDict:
        GUI_RootAfterCallbackInterval_Milliseconds = GlobalsDict["GUI_RootAfterCallbackInterval_Milliseconds"]
    else:
        GUI_RootAfterCallbackInterval_Milliseconds = 30
    ###########################################################

    ###########################################################
    if "GUItitleString" in GlobalsDict:
        GUItitleString = GlobalsDict["GUItitleString"]
    else:
        GUItitleString = ""
    ###########################################################

    ###########################################################
    if "root_width" in GlobalsDict:
        root_width = GlobalsDict["root_width"]
    else:
        root_width = 1820
    ###########################################################

    ###########################################################
    if "root_height" in GlobalsDict:
        root_height = GlobalsDict["root_height"]
    else:
        root_height = 1000
    ###########################################################

    ###########################################################
    if "root_Xpos" in GlobalsDict:
        root_Xpos = GlobalsDict["root_Xpos"]
    else:
        root_Xpos
    ###########################################################

    ###########################################################
    if "root_Ypos" in GlobalsDict:
        root_Ypos = GlobalsDict["root_Ypos"]
    else:
        root_Ypos = 0
    ###########################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title(GUItitleString)
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.mainloop()
    #################################################

    ################################################# THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GUI_Thread_CreateAndStart(GlobalsDict):

    print("Starting GUI thread...")
    GlobalsDict["GUI_Thread_ThreadingObject"] = threading.Thread(target=GlobalsDict["GUI_Thread"])
    GlobalsDict["GUI_Thread_ThreadingObject"].setDaemon(True)  # Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
    GlobalsDict["GUI_Thread_ThreadingObject"].start()
    time.sleep(0.5)  # Allow enough time for 'root' to be created that we can then pass it into other classes.

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ParseARGV_USE_GUI_and_SOFTWARE_LAUNCH_METHOD():

    try:
        USE_GUI_FLAG_ARGV_OVERRIDE = -1
        SOFTWARE_LAUNCH_METHOD = -1

        if len(sys.argv) >= 2:
            ARGV_1 = sys.argv[1].strip().lower()

            print("ARGV_1: " + str(ARGV_1))
            ARGV_1_ParsedDict = ParseColonCommaSeparatedVariableString(ARGV_1)

            if "use_gui_flag" in ARGV_1_ParsedDict:
                USE_GUI_FLAG_ARGV_OVERRIDE = PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG_ARGV_OVERRIDE", int(ARGV_1_ParsedDict["use_gui_flag"]))

            if "software_launch_method" in ARGV_1_ParsedDict:
                SOFTWARE_LAUNCH_METHOD = ARGV_1_ParsedDict["software_launch_method"]

    except:
        exceptions = sys.exc_info()[0]
        print("Parsing ARGV_1, exceptions: %s" % exceptions)
        traceback.print_exc()
        time.sleep(0.25)

    print("ARGV_1, USE_GUI_FLAG_ARGV_OVERRIDE: " + str(USE_GUI_FLAG_ARGV_OVERRIDE))
    print("ARGV_1, SOFTWARE_LAUNCH_METHOD: " + str(SOFTWARE_LAUNCH_METHOD))

    return [USE_GUI_FLAG_ARGV_OVERRIDE, SOFTWARE_LAUNCH_METHOD]

#######################################################################################################################
#######################################################################################################################