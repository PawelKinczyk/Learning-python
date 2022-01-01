from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the walls from the model
sheets_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()
