import os
import pickle
import variables as var
import stack_commands as sc
import py_detour as py_dtour
import find_changes as find_ch
import changes_in_global as chingl
from datetime import datetime
import interface as intf
# def commit(username):
# 	stack = get_stack()
# 	stack.append(updates)
# 	f = open("stack.txt","wb")
# 	pickle.dump(stack,f)
# 	f.close()
# 
def commit(username,project_name):
	# check = check_updates(username,project_name)
	element = {}
	element["user"] = username
	element["date-time"] = datetime.now()
	element["changes"]=chingl.global_changes(username,project_name)
	if element["changes"]=={}:
		print("Не было внесено никаких изменений")
		return
	path_to_stack = var.users_destination+username+"/"+project_name+"/"+"stack.txt"
	f = open(path_to_stack,"rb")
	stack = pickle.load(f)
	stack.append(element)
	f = open(path_to_stack,"wb")
	pickle.dump(stack,f)
	f.close()

def check_updates(username,project_name):
	global_stack = sc.load_g(project_name)
	
	local_stack = sc.load_l(username,project_name)
	if len(global_stack)>len(local_stack):
		return False
	elif global_stack[-1] in local_stack:
		return True
	else:
		return False




def push(username,project_name):
	check = check_updates()
	if check:
		global_stack = sc.load_g(project_name)
		local_stack = sc.load_l(username,project_name)



		list_of_changes = []
		for stack_element in reversed(local_stack):
			if stack_element not in global_stack:
				list_of_changes.append(stack_element)
			else:
				break
		while len(list_of_changes)!=0:
			global_stack.append(list_of_changes.pop())
		f = open(var.global_destination+project_name+"/stack.txt","wb")
		pickle.dump(global_stack,f)
		f.close()


def del_last_commit(username,project_name):
	global_stack = sc.load_g(project_name)
	local_stack = sc.load_l(username, project_name)
	if local_stack in global_stack:
		print("невозможно удалить последний коммит, обратитесь к администратору")
		return
	else:
		print("вы уверены, что хотите удалить последний коммит?(д/н)")
		if input().lower() in ["да","д","yes","y"]:
			local_stack = local_stack[:-1]
			sc.dump_l(username,project_name,local_stack)
			print("удаление прошло успешно")
			return 0




def make_project(username,project_name):
	try:
		os.mkdir(var.global_destination+project_name+'/')
	except:
		print("такое название уже есть, назвать по-другому или создать заново проект с данным именем?\n1-выбрать другое имя;\n2-создать заново;")
		while 1:
			print("ha")
			try:
				if int(input()) == 1:
					new_project_name = input("введите новое название проекта\n")
					make_project(username,new_project_name)
					return 0
				elif int(input()) == 2:
					# shutil.rmtree('/folder_name')
					shutil.rmtree(var.global_destination+project_name)
					try:
						shutil.rmtree(var.users_destination+"/"+username+"/"+project_name+"/")
						make_project(username,project_name)
						return 0
					except:
						print("error!")
						return 1
						pass
					break
			except:
				pass

	os.chdir(var.global_destination+project_name+'/')
	global_stack = sc.make_stack(username,project_name)
	f = open("stack.txt","wb")
	pickle.dump(global_stack,f)
	f.close()
	local_stack = global_stack
	try:
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	except:
		shutil.rmtree(var.users_destination+"/"+username+"/"+project_name+"/")
	os.chdir(var.users_destination+"/"+username+"/"+project_name+"/")
	f = open("stack.txt","wb")
	pickle.dump(local_stack,f)
	f.close()
	return 0
    
def show_com_username(username, project_name, num):
	dirs_in_user = os.listdir(var.users_destination+username)
	isEmpty = True
	for dir_in_user in dirs_in_user:
		isEmpty = False
		if os.path.isdir(var.users_destination+username+'/'+dir_in_user+'/') == True and project_name == dir_in_user:
			path_to_project = var.users_destination + username + '/' + project_name + '/'
			os.chdir(path_to_project)
			f = open('stack.txt', 'rb')
			stack = pickle.load(f)
			print('Изменения в проекте', project_name, 'были сделаны пользователем', stack[num]['user'])
			f.close()
			return stack[num]['user']
	if isEmpty:
		print('В VCS ещё не зарегистрирован ни один пользователь')
		return
def show_com_date_time(username, project_name, num):
	dirs_in_user = os.listdir(var.users_destination+username)
	isEmpty = True
	for dir_in_user in dirs_in_user:
		isEmpty = False
		if os.path.isdir(var.users_destination+username+'/'+dir_in_user+'/') == True and project_name == dir_in_user:
			path_to_project = var.users_destination + username + '/' + project_name + '/'
			os.chdir(path_to_project)
			f = open('stack.txt', 'rb')
			stack = pickle.load(f)
			print('Проект ', project_name, 'был изменён', stack[num]['date-time'], 'пользователем', stack[num]['user'])
			f.close()
			return stack[num]['date-time']
	if isEmpty:
		print('В VCS ещё не зарегистрирован ни один пользователь')
		return
def show_commit(username, project_name, num):
    dirs_in_user = os.listdir(var.users_destination + username)
    if os.path.exists(var.users_destination + username + '/' + project_name + '/'):
        path_to_project = var.users_destination + username + '/' + project_name + '/'
        os.chdir(path_to_project)
        f = open('stack.txt', 'rb')
        stack = pickle.load(f)
        f.close()
        if len(stack) < num:
            print('Коммита с таким номером нет!')
            return
        elif len(stack) == 1:
            print('Коммит пуст!')
            return
        print('Изменения в проекте', project_name, 'были сделаны ', stack[num]['date-time'])
        print()
        print('Изменения:')
        print()
        isSmthChange = False
        for change in stack[num]['changes']: # ['changes'][1:] -> Error: unhashable type: 'slice'
            isSmthChange = True
            print(stack[num]['changes'][change][0], change)
            if change[0] == '+' or change[0] == '...': # Если файл добавлен или изменён
                if stack[num]['changes'][change][0] == '+' or stack[num]['changes'][change][0] == '-':
                    for line_in_change in stack[num]['changes'][change][1]:
                        if line_in_change[0] == '+' or line_in_change[0] == '-':
                            print('\t  ', stack[num]['changes'][change][0], stack[num]['changes'][change][1])
                        else:
                        	print('\t  ', stack[num]['changes'][change][0], stack[num]['changes'][change][1],'->', stack[num]['changes'][change][2])
            else:	# Если файл удалён
                print('-', change)
    else:
        if not os.path.exists(var.users_destination + username + '/'):
            print('В VCS нет пользователя', username)
        else:
            print('У пользователя', username, 'нет проекта с именем', project_name)

        return

def show_not_pushed(username,project_name):
	global_stack = sc.load_g(project_name)
	local_stack = sc.load_l(username,project_name)
	list_of_changes = []
	for stack_element in reversed(local_stack):
		if stack_element not in global_stack:
			list_of_changes.append(stack_element)
		else:
			break
	print(list_of_changes)
	return list_of_changes

def del_couple_commits(username,project_name):
	local_stack = sc.load_l(username,project_name)
	list_of_changes = show_not_pushed(username,project_name)
	pushed_commits = []
	for stack_element in reversed(local_stack):
		if stack_element not in list_of_changes:
			pushed_commits.append(stack_element)
	sc.dump_l(username,project_name,pushed_commits)

def make_project_local(username, project_name):
	global_stack=sc.load_g(project_name)
	if global_stack == 0:
		return 0
	try:
		os.mkdir(var.users_destination+"/"+username+"/"+project_name+"/")
	except:
		return
	f = open(var.users_destination+username+"/"+project_name+"/stack.txt","wb")
	pickle.dump([global_stack[0]],f)
	f.close()
	return 
