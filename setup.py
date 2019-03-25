from cx_Freeze import setup, Executable
base = None
executables = [Executable("006.py", base=base)]
package = ["idna"]
options = {
	'build_exe': {
	'packages':packages,
	},
}

setup (
	name = "any name",
	options = options,
	version ="564564",
	description = "Any description",
	executables = executables
	)
