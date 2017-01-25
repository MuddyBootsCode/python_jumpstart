import os

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    # display cats


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count):
        print(i)

    cat_service.get_cat(folder, "")


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def print_header():
    print('----------------------------------------------------')
    print('                      LoL Cats')
    print('----------------------------------------------------')
    print()


if __name__ == '__main__':
    main()
