import os
import shutil

FileExtentions = {'jpg': 'Image',
                  'png': 'Image',
                  'gif': 'Image',
                  'bnp': 'Image',
                  'mp3': 'Audio',
                  'wma': 'Audio',
                  'wav': 'Audio',
                  'ra': 'Audio',
                  'ram': 'Audio',
                  'rm': 'Audio',
                  'mid': 'Audio',
                  'ogg': 'Audio',
                  'avi': 'Video',
                  'asf': 'Video',
                  'mov': 'Video',
                  'avchd': 'Video',
                  'flv': 'Video',
                  'swv': 'Video',
                  'mpg': 'Video',
                  'mp4': 'Video',
                  'wmv': 'Video',
                  'psd': 'Photoshop Files',
                  'prproj': 'Premiere Projects',
                  'aep': 'After Effects Comps'}


def get_desktop_location():
    deskpath = 'C:' + os.getenv('HOMEPATH') + '\\Desktop'
    os.chdir(deskpath)
    return deskpath


def make_directories(files):
    m_directories = list(set(files.values()))
    a_directories = [item for item in os.listdir(os.getcwd()) if os.path.isdir(item)]
    c_directories = set(m_directories).difference(set(a_directories))
    for file in list(c_directories):
        os.mkdir(file)


def get_files():
    DesktopFiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    return DesktopFiles


def copy_files(FileList):
    TempList = []
    FinalList = []
    for item in FileList:
        TempList.append((item.rsplit('.', 1)))
    for item2 in TempList:
        try:
            if item2[1] in FileExtentions.keys():
                FinalList.append(item2)
        except:
            continue
    for item in FinalList:
        shutil.move(item[0] + '.' + item[1], os.getcwd() + '\\' + FileExtentions.get(item[1]))


get_desktop_location()
make_directories(FileExtentions)
copy_files(get_files())
