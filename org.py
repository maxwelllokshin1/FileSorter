import os
import shutil

def moveToFinalLoc(root, loc):
    for folder, subFolder, filenames in os.walk(root):
        for filename in filenames:
            # file_path = os.path.join(folder, filename)
            # new_path = os.path.join(loc, filename)

            file_path = folder + '/' + filename
            new_path = loc + '/' + filename

            if not os.path.exists(new_path):
                shutil.move(file_path, new_path)

def moveToDesignatedFolders(loc):
    for filename in os.listdir(loc):
        file_path = loc + '/' + filename

        if os.path.isfile(file_path):
            file_extention = filename.split('.')[-1].lower()
            folder = loc + '/' + file_extention

            if not os.path.exists(folder):
                os.makedirs(folder)
            
            target = folder + '/' + filename

            shutil.move(file_path, target)
            
if __name__ == "__main__":
    loc = os.path.expanduser("~/OneDrive/Desktop")

    # moveToFinalLoc(loc, loc)
    moveToDesignatedFolders(loc)