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
                print('Проект ', project_name, 'был изменён', stack[num]['date-time'], 'пользователем',
                      stack[num]['user'])
                return stack[num]['date-time']
            elif choice == 'commit_info':
                print('Изменения в проекте', project_name, 'были сделаны ', stack[num]['date-time'])
                print()
                print('Изменения:')
                print()
                isSmthChange = False
                for change in stack[num]['changes']:  # ['changes'][1:] -> Error: unhashable type: 'slice'
                    isSmthChange = True
                    print(stack[num]['changes'][change][0], change)
                    if change[0] == '+' or change[0] == '...':  # Если файл добавлен или изменён
                        if stack[num]['changes'][change][0] == '+' or stack[num]['changes'][change][0] == '-':
                            for line_in_change in stack[num]['changes'][change][1]:
                                if line_in_change[0] == '+' or line_in_change[0] == '-':
                                    print('\t  ', stack[num]['changes'][change][0], stack[num]['changes'][change][1])
                                else:
                                    print('\t  ', stack[num]['changes'][change][0], stack[num]['changes'][change][1],
                                          '->', stack[num]['changes'][change][2])
                    else:  # Если файл удалён
                        print('-', change)
            elif choice == 'all_info':
                print('Изменения в проекте', project_name, 'были сделаны ', stack[num]['date-time'])
                print()
                print('Изменения:')
                print()
                isSmthChange = False
                for num in range(len(stack) - 1):
                    num += 1
                    print('Коммит номер', str(num) + ':')
                    for change in stack[num]['changes']:  # ['changes'][1:] -> Error: unhashable type: 'slice'
                        isSmthChange = True
                        print(stack[num]['changes'][change][0], change)
                        if change[0] == '+' or change[0] == '...':  # Если файл добавлен или изменён
                            if stack[num]['changes'][change][0] == '+' or stack[num]['changes'][change][0] == '-':
                                for line_in_change in stack[num]['changes'][change][1]:
                                    if line_in_change[0] == '+' or line_in_change[0] == '-':
                                        print('\t  ', stack[num]['changes'][change][0],
                                              stack[num]['changes'][change][1])
                                    else:
                                        print('\t  ', stack[num]['changes'][change][0],
                                              stack[num]['changes'][change][1], '->', stack[num]['changes'][change][2])
                        else:  # Если файл удалён
                            print('-', change)
        if isEmpty:
            print('В VCS ещё не зарегистрирован ни один пользователь')
            return
            isSmthChange = False