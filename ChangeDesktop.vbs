Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")

strPath = Wscript.ScriptFullName
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.GetFile(strPath)
strFinal = objFSO.GetParentFolderName(objFile) & "\ChangeDesktop.bat"

WinScriptHost.Run Chr(34) & strFinal & Chr(34), 0
Set WinScriptHost = Nothing
