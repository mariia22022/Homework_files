files = ['1.txt','2.txt','3.txt']
all_files_information =[]
for element in files:
    with open(element,encoding='utf-8') as file:
        count = 0
        text = file.readlines()
        for i in text:
            count += 1

    list_of_information =[count,element,text]
    all_files_information.append(list_of_information)
    all_files_information = sorted(all_files_information)
for i in range(len(all_files_information)):
    with open('4.txt','a',encoding='utf-8') as t:
        t.write(all_files_information[i][1] + '\n')
        t.write(str(all_files_information[i][0]) + '\n')
        for line in all_files_information[i][2]:
            t.write(line)
        t.write('\n')