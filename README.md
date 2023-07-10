# Pre-requisites
1. Set up a local SFTP Server if you do not have one to connect to
   ```bash
    docker run --name client-sftp-orion -p 2222:22 -v C:\Users\pcadmin\sftp\root-folder:/home/pcadmin/root-folder/ -d atmoz/sftp root:password:1001
    ```
2. Install all dependencies
   ```bash
   pip install -r requirements.txt 
   ```