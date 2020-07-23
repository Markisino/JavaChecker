import subprocess

#Get Java version and return string
def get_version():
    versionstr = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT).decode('utf-8')

    outputstr = versionstr[versionstr.find('\"')+1:versionstr.find('\"',versionstr.find('\"')+1)]

    return outputstr


# Check if Java is installed
def check_installed():

    try:
        get_version()

    except:
        return False

    return True


