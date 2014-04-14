import sublime, sublime_plugin, os, stat

class BeforeSave(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		fileName = view.file_name()
		fileAtt = os.stat(fileName)[0]
		if ((os.name == 'nt') and (fileAtt != 33206)):
			sublime.set_clipboard(fileName)
			sublime.ok_cancel_dialog("Check it out:\n" + fileName)