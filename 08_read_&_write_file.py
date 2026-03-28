f = open("c://Python_AI//funny.txt", "w")

f.write("hello world\n")
f.close()

f = open("c://Python_AI//funny.txt", "r")
f_out = open("c://Python_AI//funny_wc.txt", "w")
# print(f.read())

for line in f:
    token = line.split(" ")
    # print(str(token))
    f_out.write("wordcount:" + str(len(token)) + line)
    print(len(token))
    # print(line)

f.close()
f_out.close()
