import subprocess as cmd

cmd.run("git add *", check = True, shell = True)
cmd.run("ls", check = True, shell = True)
cmd.run("git commit -m 'it is a fake commit'", check = True, shell = True)
cmd.run("pwd", check = True, shell = True)
cmd.run("git push origin master", check = True, shell = True)