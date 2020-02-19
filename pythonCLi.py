import subprocess as cmd
cp = cmd.run("git add *", check = True, shell  = True)
cp  = cmd.run("git commit - m 'This is a fake commit'", check = True, shell = True)
cp = cmd.run("git push origin master", check = True, shell = True)