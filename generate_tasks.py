def generate_tasks(filename, TaskG):
    with open(filename, 'w') as tasks:
        taskL = TaskG.generate_tasks()
        i = 0
        for task in taskL:
            i = i + 1
            tasks.write("Задание " + str(i) + ":\n")
            tasks.write('m: ' + str(task.m) + ' n: ' + str(task.n) + '\n')
            tasks.write('C:' + str(task.C) + '\n')
            tasks.write('D:' + str(task.D) + '\n')
            tasks.write('\n')