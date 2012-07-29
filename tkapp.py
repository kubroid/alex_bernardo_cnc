# tkapp.py: specify inifile entry [DISPLAY]USER_COMMAND_FILE = path_to_tkapp.py
# specify tk applications as inifile entries like:
#   [DISPLAY]TKAPP = ngcgui_app.tcl

# note: USER_COMMAND_FILE supersedes ~/.axisrc so source it here, once only
try:
    first_tkapp
except NameError:
    first_tkapp = True

user_rcfile = os.path.expanduser("~/.axisrc")
if first_tkapp and os.path.exists(user_rcfile):
    first_tkapp = False
    import traceback
    try:
        execfile(user_rcfile)
    except:
        tb = traceback.format_exc()
        print >>sys.stderr, tb
        root_window.tk.call("nf_dialog", ".error", _("Error in ~/.axisrc"),
            tb, "error", 0, _("OK"))

class moreTclCommands(nf.TclCommands):
    
    def dynamic_tab(name, text):
        tab = widgets.right.insert("end", name, text=text)
        tab.configure(borderwidth=1, highlightthickness=0)
        return tab

    # for emc2.5, _dynamic_tab is in axis.py, so do this instead:
    #def dynamic_tab(name, text):
    #    return _dynamic_tab(name,text) # ccaller: make a frame and pack

    def inifindall(section,item):
        # support USER_COMMAND_FILE that uses tcl, return tcl list
        answer = inifile.findall(section,item)
        tlist = ""
        for x in answer:
            if len(answer) == 1:
                tlist = x
            else:
                tlist = tlist + "{" + x + "} "
        return tlist

moreTclCommands(root_window)

tkapp = inifile.findall("DISPLAY","TKAPP") or ""

for app in tkapp:
    root_window.tk.call("source",app)
