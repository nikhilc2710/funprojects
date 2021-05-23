import os
from datetime import datetime
import subprocess
import shutil,stat
import os
import time
from apiclient.http import MediaFileUpload
from Google import main
from colorama import init
from colorama import Fore, Back, Style  
init()
service=main()
currtime=lambda : datetime.now().strftime("%Y_%m_%d")
def on_rm_error( func, path, exc_info):
    os.chmod( path, stat.S_IWRITE )
    os.unlink( path )


try:
    proc=subprocess.Popen(["git","clone","gitrepoURL"])
    proc.wait()
    zip_name=f"serverbackup_upto{currtime()}"
    shutil.make_archive(zip_name, 'zip', "reponame")
    print(Fore.RED + 'Zip created....')
    file_metadata = {'name': zip_name+".zip"}
    media = MediaFileUpload(zip_name+".zip", mimetype='application/zip')
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    print(Fore.GREEN + 'File Uploaded....')
    media.__del__()
except Exception as e:
    print(e)
finally:
    shutil.rmtree("reponame", onerror = on_rm_error )
    os.remove(zip_name+".zip")
print(Fore.RED + 'Job Completed')

