from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction, TransactionGroup

doc = __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the walls from the model
sheets_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)
                                            .WhereElementIsNotElementType().ToElements()
wall_id_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElementsIds()

tg = TransactionGroup(doc,"Update and delete")
tg.Start


t = Transaction(doc,"update sheet parameters")
t.Start()
for sheet in sheets_collector:
    custom_param = sheet.LookupParameter('COMMON_COMMENT')
    if custom_param:
        custom_param.Set("Example value")
t.Commit()

t = Transaction(doc,"Deleting all walls")
t.Start()

for wall_id in wall_id_collector:
    doc.Delete(wall_id)

t.Commit()
