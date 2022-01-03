__author__ = 'Ehsan Iran-Nejad'

# for timing
from pyrevit.coreutils import Timer
timer = Timer()

import Autodesk.Revit.DB as DB

doc =__revit__.ActiveUIDocument.Document
uidoc=__revit__.ActiveUIDocument

heigh_param_id = DB.ElementId(DB.BuiltInParameter.WALL_USER_HEIGHT_PARAM)

heigh_param_prov = DB.ParameterValueProvider(heigh_param_id)

param_equality = DB.FilterNumericEquals()

heigh_value_rule = DB.FilterDoubleRule(heigh_param_prov
                                     ,param_equality
                                     ,10.0,1E-6)

param_filter = DB.ElementParameterFilter(heigh_value_rule)

walls = DB.FilteredElementCollector(doc) \
.WherePasses(param_filter) \
.ToElementIds()

uidoc.Selection.SetElementIds(walls)

# for timing
endtime = timer.get_time()
print(endtime)
