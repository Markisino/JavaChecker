import subprocess
import smtplib
import os

# Get Java version and return string
def get_version():
    in_str = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT).decode('utf-8')

    out_str = in_str[in_str.find('\"') + 1:in_str.find('\"', in_str.find('\"') + 1)]

    return out_str

# Check if Java is installed
def is_installed():
    try:
        get_version()

    except:
        return False

    return True

# Install Java with version as parameter
def install_java(version):
    os.system("sudo -S apt-get install openjdk-" + str(version) + "-jre")

# Send email with status message
def send_status_email(email_receiving, message):
    # TODO Implement use cases (Results for every process)
    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()
    session.login("javacheckerpython@gmail.com", "Python37")
    session.sendmail("javacheckerpython@gmail.com", email_receiving, message)
    session.quit()