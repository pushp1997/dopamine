
import subprocess

def p2c(project: list) -> str:
    commits = []
    cmd = ' {  echo ' + " ; echo ".join(project) + " ; } " + ' | ~/lookup/getValues p2c'
    try:
        commits = subprocess.check_output(cmd, shell=True)
        commits = commits.decode('utf-8')
        commits = commits.split(";")
    except:
        print("Warning: Skipping due to unexpected error in shell command.")
    return commits


def c2data(commit_hash: list) -> str:
    data = ""
    cmd = ' {  echo ' + " ; echo ".join(commit_hash) + " ; } " + ' | ~/lookup/getValues c2dat'
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


def convert_to_int(value: any)->any:
    try:
        value = int(value)
    except:
        value = None
    return value