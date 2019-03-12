import os
import zipfile
import shutil

def package_lambdas():

    folder = 'lambdas/'
    zipped_folder = 'zipped_' + folder
    
    if os.path.exists(zipped_folder):
        shutil.rmtree(zipped_folder)
    
    os.makedirs(zipped_folder)
    for root, dirs, files in os.walk(folder):
        for file in files:
            print('Zipping file `' + file + '` ...')
            zipf = zipfile.ZipFile(zipped_folder + file + '.zip', 'w', zipfile.ZIP_DEFLATED)
            path = os.path.join(root, file)
            base_path = os.path.basename(path)
            zipf.write(path, base_path)
            zipf.close()
            
if __name__ == "__main__":
    package_lambdas()