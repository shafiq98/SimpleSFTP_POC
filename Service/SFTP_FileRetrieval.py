from dotenv import load_dotenv
import logging
import paramiko
import os

from Utilities.FileHelper import getMostRecentFiles

log = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
log.setLevel(logging.DEBUG)

load_dotenv()

USERNAME = os.getenv("SFTP_USERNAME")
PASSWORD = os.getenv("SFTP_PASSWORD")
HOST = os.getenv("HOST")
PORT = int(os.getenv("SFTP_PORT"))
DATA_STORE = os.getenv("DATA_STORE")
RESOURCE_FOLDER = os.getenv("RESOURCE")
DIVIDER_SUBSTRING = os.getenv("DIVIDER_SUBSTRING")

def sftpFileRunner():
    fileList = getFileList(host=HOST, port=PORT, username=USERNAME, password=PASSWORD, source_directory=DATA_STORE)
    log.debug("Complete File List = {file_list}".format(file_list=fileList))
    sortedFileList = sorted(fileList, reverse=True)
    log.debug("Sorted File List = {file_list}".format(file_list=sortedFileList))
    chosenFileList = getMostRecentFiles(sortedFileList, DIVIDER_SUBSTRING)
    log.debug("Chosen File List = {file_list}".format(file_list=chosenFileList))
    downloadFiles(host=HOST, port=PORT, username=USERNAME, password=PASSWORD, source_directory=DATA_STORE, target_directory=RESOURCE_FOLDER, fileList=chosenFileList)

def downloadFiles(host: str, port: int, username: str, password: str, source_directory: str, target_directory: str,
                  fileList: list[str]):
    ssh = paramiko.SSHClient()
    # automatically add keys without requiring human intervention
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host, username=username, password=password, port=port)
    ftp = ssh.open_sftp()
    ftp.chdir(source_directory)

    for file in fileList:
        source_file_path = "{directory}/{file_name}".format(directory=source_directory, file_name=file)
        destination_file_path = "{directory}/{file_name}".format(directory=target_directory, file_name=file)
        log.info("Trying to download {source_path} into {destination_path}".format(source_path=source_file_path, destination_path=destination_file_path))
        # log.debug(ftp.stat(source_file_path))
        ftp.get(source_file_path, destination_file_path)

    return None


def getFileList(host: str, port: int, username: str, password: str, source_directory: str) -> list[str]:
    ssh = paramiko.SSHClient()
    # automatically add keys without requiring human intervention
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host, username=username, password=password, port=port)
    ftp = ssh.open_sftp()
    ftp.chdir(source_directory)
    fileList = ftp.listdir()

    return fileList
