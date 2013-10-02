__author__ = 'Izzat'
import wx

class DialogTrans(wx.Dialog):
    def __init__(self, prefix, NF, parent=None):
        super(DialogTrans, self).__init__(parent, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        self.NF = NF
        self.InitUI()
        self.SetTitle(prefix + ": Transformation matrix (trm)")

    def InitUI(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        horSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(horSizer, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        # Insert, Delete buttons and comboboxes
        grid = wx.GridBagSizer(hgap=40, vgap=11)
        lab_top = wx.StaticText(self, label='Original frame')
        lab_bottom = wx.StaticText(self, label='Destination frame')
        grid.Add(lab_top, pos=(0, 0), flag=wx.ALIGN_CENTER_HORIZONTAL)
        grid.Add(lab_bottom, pos=(2, 0), flag=wx.ALIGN_CENTER_HORIZONTAL)
        self.cmb_i = wx.ComboBox(self, size=(80, -1), choices=[str(i) for i in range(self.NF)], style=wx.CB_READONLY)
        self.cmb_i.SetSelection(0)
        self.cmb_j = wx.ComboBox(self, size=(80, -1), choices=[str(i) for i in range(self.NF)], style=wx.CB_READONLY)
        self.cmb_j.SetSelection(self.NF - 1)
        grid.Add(self.cmb_i, pos=(1, 0), flag=wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, border=40)
        grid.Add(self.cmb_j, pos=(3, 0), flag=wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, border=10)
        insertButton = wx.Button(self, wx.ID_ANY, "Insert ->")
        insertButton.Bind(wx.EVT_BUTTON, self.OnInsert)
        deleteButton = wx.Button(self, wx.ID_ANY, "Delete <-")
        deleteButton.Bind(wx.EVT_BUTTON, self.OnDelete)
        grid.Add(insertButton, pos=(1, 1))
        grid.Add(deleteButton, pos=(3, 1))
        horSizer.Add(grid)

        # Transformations label and list
        verSizer = wx.BoxSizer(wx.VERTICAL)
        horSizer.AddSpacer(40)
        horSizer.Add(verSizer)
        lab_trans = wx.StaticText(self, label='Transformations')
        verSizer.Add(lab_trans, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        verSizer.AddSpacer(10)
        self.listBox = wx.ListBox(self, size=(80, 120), style=wx.LB_SINGLE)
        self.result = set()
        verSizer.Add(self.listBox)

        self.check_short = wx.CheckBox(self, label='Trigonometric short form')
        mainSizer.Add(self.check_short, 0, wx.LEFT | wx.ALIGN_LEFT, 25)
        mainSizer.AddSpacer(15)

        # OK Cancel
        horSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(horSizer2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 12)
        okButton = wx.Button(self, wx.ID_OK, "OK")
        okButton.Bind(wx.EVT_BUTTON, self.OnOK)
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
        horSizer2.Add(okButton)
        horSizer2.AddSpacer(22)
        horSizer2.Add(cancelButton)

        self.SetSizerAndFit(mainSizer)

    def OnOK(self, e):
        self.EndModal(wx.ID_OK)

    def OnCancel(self, e):
        self.EndModal(wx.ID_CANCEL)

    def OnInsert(self, e):
        trans = (int(self.cmb_i.Value), int(self.cmb_j.Value))
        if trans not in self.result:
            self.listBox.Insert(str(trans), len(self.result), trans)
            self.result.add(trans)

    def OnDelete(self, evt):
        sel_index = self.listBox.GetSelection()
        if sel_index >= 0:
            trans = self.listBox.GetClientData(sel_index)
            self.result.remove(trans)
            self.listBox.Delete(sel_index)

    def GetValues(self):
        return self.result, self.check_short.Value


class DialogFast(wx.Dialog):
    def __init__(self, prefix, NF, parent=None):
        super(DialogFast, self).__init__(parent, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        self.NF = NF
        self.InitUI()
        self.SetTitle(prefix + ": Fast geometric model (fgm)")

    def InitUI(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        #title
        label_main = wx.StaticText(self, label="Calculation of iTj")

        #input
        grid = wx.GridBagSizer(hgap=25, vgap=5)
        lab_left = wx.StaticText(self, label='Frame i')
        lab_right = wx.StaticText(self, label='Frame j')
        grid.Add(lab_left, pos=(0, 0), flag=wx.ALIGN_CENTER_HORIZONTAL)
        grid.Add(lab_right, pos=(0, 1), flag=wx.ALIGN_CENTER_HORIZONTAL)
        self.cmb_i = wx.ComboBox(self, size=(50, -1), choices=[str(i) for i in range(self.NF)], style=wx.CB_READONLY)
        self.cmb_i.SetSelection(0)
        self.cmb_j = wx.ComboBox(self, size=(50, -1), choices=[str(i) for i in range(self.NF)], style=wx.CB_READONLY)
        self.cmb_j.SetSelection(self.NF - 1)
        grid.Add(self.cmb_i, pos=(1, 0), flag=wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, border=20)
        grid.Add(self.cmb_j, pos=(1, 1), flag=wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, border=20)
        okButton = wx.Button(self, wx.ID_OK, "OK")
        okButton.Bind(wx.EVT_BUTTON, self.OnOK)
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
        grid.Add(cancelButton, pos=(2, 1))
        grid.Add(okButton, pos=(2, 0))

        mainSizer.AddSpacer(30)
        mainSizer.Add(label_main, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 60)
        mainSizer.AddSpacer(30)
        mainSizer.Add(grid, flag=wx.ALIGN_CENTER)
        mainSizer.AddSpacer(20)

        self.SetSizerAndFit(mainSizer)

    def OnOK(self, e):
        self.EndModal(wx.ID_OK)

    def OnCancel(self, e):
        self.EndModal(wx.ID_CANCEL)

    def GetValues(self):
        return int(self.cmb_i.Value), int(self.cmb_j.Value)


class DialogPaul(wx.Dialog):
    def __init__(self, prefix, endeffs, EMPTY, parent=None):
        super(DialogPaul, self).__init__(parent, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        self.endeffs = endeffs
        self.InitUI(EMPTY)
        self.SetTitle(prefix + ": IGM Paul Method (pau)")

    def InitUI(self, EMPTY):
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        #title
        label_cmb = wx.StaticText(self, label="For frame :")
        mainSizer.Add(label_cmb, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 20)
        self.cmb = wx.ComboBox(self, size=(80, -1), choices=[str(i) for i in self.endeffs], style=wx.CB_READONLY)
        self.cmb.SetSelection(0)
        mainSizer.AddSpacer(5)
        mainSizer.Add(self.cmb, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 10)
        label_main = wx.StaticText(self, label="Components taken into account :")
        mainSizer.Add(label_main, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        #input
        grid = wx.GridBagSizer(hgap=15, vgap=15)
        names = ['S', 'N', 'A', 'P']
        for i, name in enumerate(names):
            check_box = wx.CheckBox(self, wx.ID_ANY, label='   ' + name, name=name)
            check_box.SetValue(True)
            check_box.Bind(wx.EVT_CHECKBOX, self.OnVectorChecked)
            grid.Add(check_box, pos=(0, i), flag=wx.ALIGN_CENTER_HORIZONTAL)
            for j in range(1, 4):
                w_name = name + str(j)
                cmb = wx.ComboBox(self, choices=[EMPTY, '-1', '0', '1', w_name],
                                  name=w_name, style=wx.CB_READONLY, size=(90, -1), id=(j-1)*4 + i)
                cmb.SetSelection(4)
                cmb.Bind(wx.EVT_COMBOBOX, self.OnComboBox)
                grid.Add(cmb, pos=(j, i))
            label = wx.StaticText(self, label=(' 1' if i == 3 else ' 0'), id=12 + i)
            grid.Add(label, pos=(4, i))

        mainSizer.Add(grid, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 35)
        mainSizer.AddSpacer(20)

        #buttons
        horSizer = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, wx.ID_OK, "OK")
        okButton.Bind(wx.EVT_BUTTON, self.OnOK)
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
        horSizer.Add(okButton, 0, wx.ALL, 15)
        horSizer.Add(cancelButton, 0, wx.ALL, 15)
        mainSizer.Add(horSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.SetSizerAndFit(mainSizer)

    def OnOK(self, e):
        self.EndModal(wx.ID_OK)

    def OnCancel(self, e):
        self.EndModal(wx.ID_CANCEL)

    def OnVectorChecked(self, evt):
        name = evt.EventObject.Name
        index = 4 if evt.EventObject.Value else 0
        for i in range(1, 4):
            cmb = self.FindWindowByName(name + str(i))
            cmb.SetSelection(index)

    def OnComboBox(self, evt):
        name = evt.EventObject.Name
        if evt.EventObject.GetSelection() != 4:
            check_box = self.FindWindowByName(name[0])
            check_box.SetValue(False)

    def GetValues(self):
        lst = []
        for i in range(16):
            widget = self.FindWindowById(i)
            if isinstance(widget, wx.ComboBox):
                lst.append(widget.Value)
            else:
                lst.append(widget.LabelText)
        return lst, int(self.cmb.Value)