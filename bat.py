import os
#-----------------------------------------------------
# MAIN
#-----------------------------------------------------

print("\033c\033[47;30m")
print("give me file .class ?")
print()

filename = input().strip()

classname = filename.replace(".class", "")

#-----------------------------------------------------
# CONVERTER CLASS -> JASM
#-----------------------------------------------------

cmd = "/usr/bin/openjdk-asmtools-jdis $1 -w ./"

cmd = cmd.replace("$1", filename)

os.system(cmd)

jasm_name = "./" + classname + ".jasm"

if not os.path.exists(jasm_name):

    print("cannot create jasm file")
    exit(1)
