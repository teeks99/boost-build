import tempfile
import os
import subprocess

check_file="python_ntfs_junction_test.bat"

def _build_test(full_check_file):
    if not os.path.isfile(full_check_file):
        with open(full_check_file, 'w') as fobj:
            fobj.write("REM Tests if a directory is a symlink/junction\n\n")
            fobj.write("SET /A IS_A_LINK=0\n")
            fobj.write("SET /A NOT_A_LINK=1\n\n")
            fobj.write('SET Z=&&   FOR %%A IN (%1) DO SET Z=%%~aA')
            fobj.write("\n\n\t")
            fobj.write(r'IF "%Z:~8,1%" == "l" GOTO :IS_A_LINK')
            fobj.write("\n\n")
            fobj.write("EXIT /B %NOT_A_LINK%\n\n")
            fobj.write(":IS_A_LINK\n")
            fobj.write("EXIT /B %IS_A_LINK%\n")


def isjunction(path_to_dir):
    """Checks if the given path is a link.

    This will return true for windows junction
    Will also return true for symlinks on python2...looking for a way to fix this.
    """

    if not os.path.isdir(path_to_dir):
        return False

    if os.path.islink(path_to_dir):
        # In python3 windows symlinks are found
        return False

     full_check_file = os.path.join(tempfile.gettempdir(), check_file)
     _build_test(full_check_file)

     result = subprocess.call([full_check_file, path_to_dir],
                              stdout=subprocess.PIPE)

     if not result:
         return True
     return False


def junction(src_dir, link_name):
    if not os.path.isdir(src_dir):
        raise Exception("Source must be a directory")

    if os.path.exists(link_name):
        raise Exception(
            "Cannot create a junction where something already exists")

    subprocess.call(['mklink', '/J', link_name, src_dir], shell=True,
                    stdout=subprocess.PIPE)


def unlink(link):
    os.rmdir(link)

