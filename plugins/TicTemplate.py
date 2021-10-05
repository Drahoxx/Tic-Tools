def main(argv : str[]):
	print(
	"""
	def main(argv : str[]):
		#The main function will be executed when the user uses the plugin
		#Note : if you are using files, please put them in "../results/<your plugin name>/"

	def setup():
		#This function will be executed when the user download your plugin
		#In this function, please make sure all depencies are installed

	def infos():
		plugin_name = "Dummy"	#The name of the plugin
		version = 0				#used in tic-pip
		creator = "John Doe"	#you :3
		github_repo = None		#if you share your code
		return (plugin_name,version,creator,github_repo)
	""")

def setup():
	print("TicTemplate is installed")

def infos():
	plugin_name = "TicTemplate"
	version = 1
	creator = "Drahoxx"
	github_repo = None
	return (plugin_name,version,creator,github_repo)