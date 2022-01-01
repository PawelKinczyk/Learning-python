from Autodesk.Revit.DB import Transaction

doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc,"Deleting All Walls")
t.Start()

# all your create, update or delete actions

t.Commit()

res = t.GetStatus()

res = TransactionStatus.Commited
