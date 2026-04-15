import os


def create_folder(path):
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except OSError as e:
        print(f"Error creating directory '{path}': {e}")


def remove_folder(path):
    if len(os.listdir(path)) == 0:
        os.rmdir(path)


def create_file(path):
    with open(path,'w',encoding='utf-8') as f:
        f.write("")


def append_text_file(path,text):
    with open(path,"a",encoding='utf-8') as f:
        f.write(text)


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("no such file")


def show_items_in_folder(path):
    # os.environ.get('HOMEPATH')
    os.chdir(path)
    print(os.listdir())


def show_full_path_current():
    print(os.getcwd())


def show_full_path(path):
    curr_path=os.getcwd()
    os.chdir(path)
    print(os.getcwd())
    os.chdir(curr_path)

