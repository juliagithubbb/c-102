import os 
from importlib.resources import path
import shutil

from_dir ="C:/Users/julia/Downloads"
to_dir = "C:/Users/julia/Downloads/Python/PRO_1-1_C102_AtividadeDoAluno1-main"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == "":
        continue
    
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir +'/'+ file_name
        path2 = to_dir +'/'+ 'Arquivos_imagem'
        path3 = to_dir +'/'+ 'Arquivos_imagem' +'/'+ file_name
        print("path1", path1)
        print("path3", path3)
        
        if os.path.exists(path2):
            print(f'movendo{file_name}...')
            shutil.move (path1, path3)
        else:
            os.makedirs(path2)
            print(f'movendo{file_name}...')
            shutil.move (path1, path3)