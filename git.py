#Import needed libraries
import subprocess, os, shutil
#Menu to display
menu = {}
menu['1'] = "Create Repository."
menu['2'] = "Clone Repository."
menu['3'] = "Add Files."
menu['4'] = "Commit Repository."
menu['5'] = "Push Repository."
menu['6'] = "Pull Repository."
menu['7'] = "Get Log."
menu['8'] = "More Info."
menu['9'] = "Exit."

#Check operating system and then clear screen before menu
if os.name == "nt":
    os.system('cls')
else:
    os.system('clear')

#Run menu
while True:
    try:
        subprocess.call(["git"], stdout=subprocess.PIPE)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print "Git Not Installed"
            break
        else:
            print "Something went wrong while trying to test git"
            break
            raise
    options = menu.keys()
    options = sorted(options, key=int)
    for item in options:
        print "[" + item + "] - " + menu[item]
    print "\n"

    response = raw_input("What Would You Like To Do: ")
    if response == '1':
        #Create Repository
        response = raw_input("Name of Repository? ")
        if not os.path.exists(response):
            os.makedirs(response)
        subprocess.check_call(["git", "init"], cwd=response)
    elif response == '2':
        #Clone Repository
        response = raw_input("What is the URL To the Repository?\nIf Folder Exists, It Will Overwrite\neg: https://github.com/GettingGodlyInThisGame/githelp: ")
        folder = response.split('/')[-1]
        if os.path.isdir(folder) == True:
            print "Deleting " + folder + "/"
            shutil.rmtree(folder)
        subprocess.check_call(["git", "clone", response])
    elif response == '3':
        #Add Files
        runagan = 1
        repo = ""
        while runagan == 1:
            if not repo:
                repo = raw_input("What Repository Do You Want To Work In? ")
                if not os.path.isdir(repo):
                    print "Invalid Repository."
                    break
            files = raw_input("What File Do You Want To Add? ")
            if os.path.isfile(repo + "/" + files):
                subprocess.check_call(["git", "add", files], cwd=repo)
            else:
                print "Invalid File."
            run = raw_input("Do you want to add more files? Y/N ")
            if run.lower() == "y":
                runagan = 1
            elif run.lower() == "n":
                askcommit = raw_input("Do you want to commit? Y/N ")
                if askcommit.lower() == y:
                    commitmsg = raw_input("Commit Message? ")
                    subprocess.check_call(["git", "commit", "-m", "\""+commitmsg+"\""], cwd=repo)
                runagan = 0
            else:
                print "Invalid Option"
    elif response == '4':
        #Commit Repository
        repo = raw_input("What Repository Do You Want To Work In? ")
        if not os.path.isdir(repo):
            print "Invalid Repository."
            break
        commitmsg = raw_input("Commit Message? ")
        subprocess.check_call(["git", "commit", "-m", "\""+commitmsg+"\""], cwd=repo)
    elif response == '5':
        #Push Repository
        branch = ""
        repo = raw_input("What Repository Do You Want To Work In? ")
        if not os.path.isdir(repo):
            print "Invalid Repository."
            break
        branch = raw_input("Which Branch? ")
        if not branch:
            branch = "master"
        subprocess.check_call(["git", "push", "origin", branch], cwd=repo)
    elif response == '6':
        #Pull Repository
        repo = raw_input("What Repository Do You Want To Work In? ")
        if not os.path.isdir(repo):
            print "Invalid Repository."
            break
        subprocess.check_call(["git", "pull"], cwd=repo)
    elif response == '7':
        #Get Log
        repo = raw_input("What Repository Do You Want To Work In? ")
        if not os.path.isdir(repo):
            print "Invalid Repository."
            break
        subprocess.check_call(["git", "log"], cwd=repo)
    elif response == '8':
        #More Info
        print "Created By: GettingGodlyInThisGame - https://github.com/GettingGodlyInThisGame"
        print "Version: v1.0"
        print "Date of Release: 10th of October 2016"
    elif response == '9':
        #Exit
        break
    else:
        print "Unknown Options Selected!"
