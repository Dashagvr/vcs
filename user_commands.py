import os
import pickle
path = 'C:\\Users\\User\\Desktop\\Project\\local\\'

def commit(username):
	stack = get_stack()
	stack.append(updates)
	f = open("stack.txt","wb")
	pickle.dump(stack,f)
	f.close()



def push(username):
	check = check_updates()
	if check:
		f = open(var.global_destination+project_name+"/stack.txt","rb")
		global_stack = pickle.load(f)
		f.close()
		f = open()



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
						shutil.rmtree(var.users_destination+"/"+username+"/"+project_name)
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
	path = 'C:\\Users\\User\\Desktop\\Project\\local\\'
	dirs_in_user = os.listdir(path+username)
	isEmpty = True
	for dir_in_user in dirs_in_user:
		isEmpty = False
		if os.path.isdir(path+username+'\\'+dir_in_user+'\\') == True and project_name == dir_in_user:
			psth_to_project = path + username + '\\' + project_name + '\\'
			os.chdir(psth_to_project)
			f = open('stack.txt', 'rb')
			stack = pickle.load(f)
			print('Изменения в проекте', project_name, 'были сделаны пользователем', stack[num]['user'])
			f.close()
			return stack[num]['user']
	if isEmpty:
		print('В VCS ещё не зарегистрирован ни один пользователь')
		return
def show_com_date_time(username, project_name, num):
	path = 'C:\\Users\\User\\Desktop\\Project\\local\\'
	dirs_in_user = os.listdir(path+username)
	isEmpty = True
	for dir_in_user in dirs_in_user:
		isEmpty = False
		if os.path.isdir(path+username+'\\'+dir_in_user+'\\') == True and project_name == dir_in_user:
			psth_to_project = path + username + '\\' + project_name + '\\'
			os.chdir(psth_to_project)
			f = open('stack.txt', 'rb')
			stack = pickle.load(f)
			print('Проект ', project_name, 'был изменён', stack[num]['date-time'], 'пользователем', stack[num]['user'])
			f.close()
			return stack[num]['date-time']
	if isEmpty:
		print('В VCS ещё не зарегистрирован ни один пользователь')
		return
def show_commit(username, project_name, num):
    path = 'C:\\Users\\User\\Desktop\\Project\\local\\'
    dirs_in_user = os.listdir(path + username)
    isEmpty = True
    for dir_in_user in dirs_in_user:
        isEmpty = False
        if os.path.isdir(path + username + '\\' + dir_in_user + '\\') == True and project_name == dir_in_user:
            path_to_project = path + username + '\\' + project_name + '\\'
            os.chdir(path_to_project)
            f = open('stack.txt', 'rb')
            stack = pickle.load(f)
            f.close()
            if len(stack) < num:
                print('Коммита с таким номров нет!')
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
        if isEmpty:
            print('В VCS ещё не зарегистрирован ни один пользователь')
            return


def show_commit_new(username, project_name, num):
    print('Выберите, что вы хотите узнать о пректе:')
    print('\tusername - Имя пользователя, сделавшего коммит под определённым номером')
    print('\tdate_time - Дату создания коммита под определённым номером')
    print('\tcommit_info - Всю информацию о коммите под определённым номером')
    print('\tall_info - Вывести информацию о всех коммитах проекта')
    choice = input()

	
    dirs_in_user = os.listdir(path + username)
    isEmpty = True
    for dir_in_user in dirs_in_user:
        isEmpty = False
        if os.path.isdir(path + username + '\\' + dir_in_user + '\\') == True and project_name == dir_in_user:
            path_to_project = path + username + '\\' + project_name + '\\'
            os.chdir(path_to_project)
            f = open('stack.txt', 'rb')
            stack = pickle.load(f)
            f.close()
            if len(stack) < num:
                print('Коммита с таким номров нет!')
                return
            elif len(stack) == 1:
                print('Коммит пуст!')
                return
            if choice == 'username':
                print('Изменения в проекте', project_name, 'были сделаны пользователем', stack[num]['user'])
                return stack[num]['user']
            elif choice == 'date_time':
                print('Проект ', project_name, 'был изменён', stack[num]['date-time'], 'пользователем', stack[num]['user'])
                return stack[num]['date-time']
            elif choice == 'commit_info':
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
            elif choice == 'all_info':
                print('Изменения в проекте', project_name, 'были сделаны ', stack[num]['date-time'])
                print()
                print('Изменения:')
                print()
                isSmthChange = False
                for num in range(len(stack)-1):
                    num += 1
                    print('Коммит номер', str(num)+':')
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
        if isEmpty:
            print('В VCS ещё не зарегистрирован ни один пользователь')
            return
            isSmthChange = False
#show_commit('Ivan', 'my_new_project', 0)
show_commit_new('Ivan', 'my_new_project', 0)