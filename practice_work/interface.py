import variables as var

def helpme():
	f = open(var.global_destination+'/bin/help().txt','r')
	for line in f:
		print(line)
	f.close()	
	return		
def show_prjs():
	return
def set_prj():
	return
def add_prj():
	return
def set_ver():
	return
def set_file():
	return
def add():
	return
def commit():
	return
def del_in_index():
	return
def del_file():
	return
def get_status():
	return
def logout(username):
	if input("Вы уверены, что хотите выйти из текущей сессии пользователя </"+username+"/>?(д/н) ").lower() in ["yes","да","y","д"]:
		return True
	else:
		return False

dict_command = {
	'help':helpme,
	'show_prjs':show_prjs,
	'set_prj':set_prj,
	'add_prj':add_prj,
	'set_ver':set_ver,
	'set_file':set_file,
	'add':add,
	'commit':commit,
	'del_in_index':del_in_index,
	'del_file':del_file,
	'get_status':get_status,
	'logout':logout
}

<<<<<<< HEAD
def interface(username):
	print("выберите команду(чтобы узнать список команд, наберите help)")
	while 1:
		command = input(">> ")
		if dict_command.get(command) != None and command != 'logout':
			dict_command[command]()
		elif command == 'logout':
			if dict_command[command](username):
				return	
		else:
			print('Такой команды нет. Пожалуйста, повторите ввод.')
			helpme()

=======
#import commands
# def interface(user):
# 	print("выберите команду(чтобы узнать список команд, наберите help)")
# 	print('>>', end=' ')
# 	while True:
# 		command = input()
# 		if dict_command.get(command) != None:
# 			dict_command[command]()
# 		else:
# 			print('Такой команды нет. Пожалуйста, повторите ввод.')
# 			help()
# 		if command == 'exit':
# 			break
# 		print('>>', end=' ')
>>>>>>> origin/master
