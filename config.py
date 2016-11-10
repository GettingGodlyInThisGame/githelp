try:
    subprocess.call(["git"])
except OSError as e:
    if e.errno == os.errno.ENOENT:
        print "Git Not Installed"
        break
    else:
        print "Something went wrong while trying to test git"
        break
        raise

name = ""
email = ""

name = raw_input("Name: ")
email = raw_input("Email: ")

if not name:
    print "Invalid Name"
if not email:
    print "Invalid Email"

subprocess.check_call(["git", "config", "--global", "user.name", "\""+name+"\""]
subprocess.check_call(["git", "config", "--global", "user.email", email]
