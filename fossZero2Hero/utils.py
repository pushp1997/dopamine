
import subprocess

def p2c(project: str) -> str:
    commits = []
    cmd = ' {  echo ' + " ; echo ".join(l) + " ; } " + ' | ~/lookup/getValues p2c'
    try:
        commits = subprocess.check_output(cmd, shell=True)
        commits = commits.decode('utf-8')
        commits = commits.split(";")
    except:
        print("Warning: Skipping due to unexpected error in shell command.")
    return commits


def c2data(commit_hash: str) -> str:
    data = ""
    cmd = "echo "+commit_hash+" | ~/lookup/getValues c2dat"
    try:
        data = subprocess.check_output(cmd, shell=True).decode('utf-8')
    except Exception as e:
        print(e)
        print("Warning: Skipping due to unexpected error in shell command.")
    return data


def a2c(author: str) -> list:
    commits = []
    cmd = 'echo "'+author+'" | ~/lookup/getValues a2c'
    try:
        commits = subprocess.check_output(cmd, shell=True).decode('utf-8')
        commits = commits.split(";")
        print(type(commit))
    except:
        print("Warning: Skipping due to unexpected error in shell command.")
    return commits

ssh_exchange_identification: Connection closed by remote host
Command 'echo 03fa88799dd0ed7ca08d0eca3a4e664d9a00043a | ~/lookup/getValues c2dat' returned non-zero exit status 255.


def convert_to_int(value: any)->any:
    try:
        value = int(value)
    except:
        value = None
    return value