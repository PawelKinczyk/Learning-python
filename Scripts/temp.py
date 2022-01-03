import Autodesk.Revit.DB as DB
doc =__revit__ActiveUIDocument.Document

cl=DB.FilteredElementCollector(doc) \
                    .OffClass(clr.GetClrType(DB.Wall)) \
                    .ToElements()
