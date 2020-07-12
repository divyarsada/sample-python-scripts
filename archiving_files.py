import os
import shutil

archive_name = os.path.expanduser(os.path.join('~','myarchive'))
root_dir = os.path.expanduser(os.path.join('~','.ssh'))
archivedfile=shutil.make_archive(archive_name, "zip", root_dir)
print(archivedfile)
shutil.unpack_archive(archivedfile,'/home/ec2-user/python_scripts')
