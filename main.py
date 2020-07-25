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
    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()
    session.login("javacheckerpython@gmail.com", "Python37")
    session.sendmail("javacheckerpython@gmail.com", email_receiving, message)
    session.quit()


# Main function
def main():
    while 1 > 0:

        print("What do you want to do?")

        print("java\t\tCheck if Java is installed")
        print("ver\t\tCheck what version of Java is installed")
        print("[version]\tInstall Java with version (ie. 11, 13, 14, etc.)")
        print("exit\t\tExit process")

        x = input()

        if x == "java":
            print("Java Exists: " + str(is_installed()))

        elif x == "ver":
            print("Java Version: " + str(get_version()))

        elif x == "exit":
            print("Goodbye")
            exit()

        else:
            print("Enter email to receive status:")
            email = input()

            print("Installing Java " + str(x))
            install_java(x)

            send_status_email(email, "Process complete")
            exit()


if __name__ == "__main__":
    main()
