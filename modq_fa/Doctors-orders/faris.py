# Fusion360API Python script

from cmath import pi
import traceback
import adsk.fusion
import adsk.core
import os

_app: adsk.core.Application = None
_ui: adsk.core.UserInterface = None
_handlers = []
wristwidht = 5
wristhight = 8
clearance = 9
ABsection = 7
Bwidth = 8
Bhight = 9
castthikness = 8
BCsection = 7
Chight = 0
Cwidth = 0
circulediameter = 0
hangangle = 0
leftpump = 0
handtip = 0
rightpump = 8
midhandthikness = 9
palmlength = 8
palmwidth = 9
thumby = 8


class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args: adsk.core.CommandCreatedEventArgs):
        adsk.core.Application.get().log(args.firingEvent.name)
        try:
            global _handlers
            cmd: adsk.core.Command = adsk.core.Command.cast(args.command)
            inputs: adsk.core.CommandInputs = cmd.commandInputs

            onDestroy = MyCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            _handlers.append(onDestroy)

            onExecute = MyExecuteHandler()
            cmd.execute.add(onExecute)
            _handlers.append(onExecute)

            inputs.addTextBoxCommandInput(
                'txtOutIpt',
                'text',
                'Outside',
                1,
                True
            )

            # Create a tab input.
            tabCmdInput1 = inputs.addTabCommandInput('tab_1', 'Tab 1')
            tab1ChildInputs = tabCmdInput1.children

            tab1ChildInputs.addValueInput('value1', 'wristwidht', 'mm', adsk.core.ValueInput.createByReal(wristwidht))
            tab1ChildInputs.addValueInput('value2', 'wristhight', 'mm', adsk.core.ValueInput.createByReal(wristhight))
            tab1ChildInputs.addValueInput('value3', 'clearance', 'mm', adsk.core.ValueInput.createByReal(clearance))
            tab1ChildInputs.addValueInput('value4', 'ABsection', 'mm', adsk.core.ValueInput.createByReal(ABsection))
            tab1ChildInputs.addValueInput('value5', 'Bwidth', 'mm', adsk.core.ValueInput.createByReal(Bwidth))
            tab1ChildInputs.addValueInput('value6', 'Bhight', 'mm', adsk.core.ValueInput.createByReal(Bhight))
            tab1ChildInputs.addValueInput('value7', 'castthikness', 'mm',
                                          adsk.core.ValueInput.createByReal(castthikness))
            tab1ChildInputs.addValueInput('value8', 'BCsection', 'mm', adsk.core.ValueInput.createByReal(BCsection))

            tab1ChildInputs.addValueInput('value9', 'Chight', 'mm', adsk.core.ValueInput.createByReal(Chight))
            tab1ChildInputs.addValueInput('value10', 'Cwidth', 'mm', adsk.core.ValueInput.createByReal(Cwidth))
            tab1ChildInputs.addValueInput('value11', 'circulediameter', 'mm',
                                          adsk.core.ValueInput.createByReal(circulediameter))
            tab1ChildInputs.addValueInput('value12', 'hangangle', 'deg', adsk.core.ValueInput.createByReal(hangangle))

            tab1ChildInputs.addValueInput('value13', 'leftpump', 'mm', adsk.core.ValueInput.createByReal(leftpump))
            tab1ChildInputs.addValueInput('value14', 'handtip', 'mm', adsk.core.ValueInput.createByReal(handtip))
            tab1ChildInputs.addValueInput('value15', 'rightpump', 'mm', adsk.core.ValueInput.createByReal(rightpump))
            tab1ChildInputs.addValueInput('value16', 'midhandthikness', 'mm',
                                          adsk.core.ValueInput.createByReal(midhandthikness))

            tab1ChildInputs.addValueInput('value17', 'palmlength', 'mm', adsk.core.ValueInput.createByReal(palmlength))
            tab1ChildInputs.addValueInput('value18', 'palmwidth', 'mm', adsk.core.ValueInput.createByReal(palmwidth))
            tab1ChildInputs.addValueInput('value19', 'thumby', 'mm', adsk.core.ValueInput.createByReal(thumby))
            design = adsk.fusion.Design.cast(_app.activeProduct)
            exportMgr = design.exportManager
            scriptDir = os.path.dirname(
                os.path.realpath("C:/Users/fares sh/Desktop/web/orange-madq-fe/modq_fa/Casts/designtest-1.py"))
            allComps = design.allComponents
            for comp in allComps:
                compName = comp.name
                fileName = scriptDir + "/" + compName
                # export the component with F3D format
                archOptions = exportMgr.createFusionArchiveExportOptions(fileName, comp)
                exportMgr.execute(archOptions)

            ############################################################################################
            # Create group input.
            groupCmdInput = tab1ChildInputs.addGroupCommandInput('group', 'Group')
            groupCmdInput.isExpanded = True
            groupCmdInput.isEnabledCheckBoxDisplayed = True
            groupChildInputs = groupCmdInput.children
            '''
            # Create radio button group input.
            radioButtonGroup = groupChildInputs.addRadioButtonGroupCommandInput('radioButtonGroup', 'Radio button group')
            radioButtonItems = radioButtonGroup.listItems
            radioButtonItems.add("RIGHT", True)
            radioButtonItems.add("LIFT", False)
            '''









        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


class MyExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args: adsk.core.CommandEventArgs):
        adsk.core.Application.get().log(args.firingEvent.name)
        #######################################################################################################################
        DISTANCE_PARAMETER = 'wristwidht'
        ID_VALUE_INPUT = 'value1'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression

        #####################################################################################################################
        DISTANCE_PARAMETER = 'wristhight'
        ID_VALUE_INPUT = 'value2'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        DISTANCE_PARAMETER = 'clearance'
        ID_VALUE_INPUT = 'value3'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        DISTANCE_PARAMETER = 'ABsection'
        ID_VALUE_INPUT = 'value4'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'Bwidth'
        ID_VALUE_INPUT = 'value5'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'Bhight'
        ID_VALUE_INPUT = 'value6'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        #######################################################################################################################
        DISTANCE_PARAMETER = 'castthikness'
        ID_VALUE_INPUT = 'value7'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression

        #####################################################################################################################
        DISTANCE_PARAMETER = 'BCsection'
        ID_VALUE_INPUT = 'value8'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        DISTANCE_PARAMETER = 'Chight'
        ID_VALUE_INPUT = 'value9'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        DISTANCE_PARAMETER = 'Cwidth'
        ID_VALUE_INPUT = 'value10'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'circulediameter'
        ID_VALUE_INPUT = 'value11'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'hangangle'
        ID_VALUE_INPUT = 'value12'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        #######################################################################################################################
        DISTANCE_PARAMETER = 'leftpump'
        ID_VALUE_INPUT = 'value13'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression

        #####################################################################################################################
        DISTANCE_PARAMETER = 'handtip'
        ID_VALUE_INPUT = 'value14'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        DISTANCE_PARAMETER = 'rightpump'
        ID_VALUE_INPUT = 'value15'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        DISTANCE_PARAMETER = 'midhandthikness'
        ID_VALUE_INPUT = 'value16'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'palmlength'
        ID_VALUE_INPUT = 'value17'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'palmwidth'
        ID_VALUE_INPUT = 'value18'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################
        ####################################################################################################################
        DISTANCE_PARAMETER = 'thumby'
        ID_VALUE_INPUT = 'value19'  # <-- replace by the id of the valueInput

        # . . .

        design = adsk.fusion.Design.cast(_app.activeProduct)
        valInp: adsk.core.ValueCommandInput = args.command.commandInputs.itemById(ID_VALUE_INPUT)

        distParam = design.userParameters.itemByName(DISTANCE_PARAMETER)
        if not distParam:
            # parameter doesn't exists -> lets creat it
            distVal = adsk.core.ValueInput.createByString(valInp.expression)
            distParam = design.userParameters.add(DISTANCE_PARAMETER, distVal, design.unitsManager.defaultLengthUnits,
                                                  '')
        else:
            # paremeter already exists -> lest update its expression attribute
            distParam.expression = valInp.expression
        ####################################################################################################################


class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args: adsk.core.CommandEventArgs):
        adsk.core.Application.get().log(args.firingEvent.name)
        adsk.terminate()


def bring_the_design():
    product = _app.activeProduct
    design = adsk.fusion.Design.cast(product)

    importManager = _app.importManager
    rootComp = design.rootComponent

    filename = "C:/Users/fares sh/Desktop/web/orange-madq-fe/modq_fa/Doctors-orders/moh1.f3d"

    importOption = importManager.createFusionArchiveImportOptions(filename)
    importManager.importToTarget(importOption, rootComp)
    pulleyOccurance = rootComp.occurrences.item(rootComp.occurrences.count - 1)
    ##############################################


def run(context):
    try:
        global _app, _ui
        _app = adsk.core.Application.get()
        _ui = _app.userInterface

        bring_the_design()

        # Get the existing command definition or create it if it doesn't already exist.
        cmdDef = _ui.commandDefinitions.itemById('cmdInputsSample')
        if not cmdDef:
            cmdDef = _ui.commandDefinitions.addButtonDefinition('cmdInputsSample', 'Command Inputs Sample',
                                                                'Sample to demonstrate various command inputs.')

        # Connect to the command created event.
        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        _handlers.append(onCommandCreated)

        # Execute the command definition.
        cmdDef.execute()

        # Prevent this module from being terminated when the script returns, because we are waiting for event handlers to fire.
        adsk.autoTerminate(False)
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
