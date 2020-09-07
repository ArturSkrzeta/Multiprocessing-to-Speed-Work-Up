import time
from os import walk
import concurrent.futures
from PIL import Image

size = (300,300)
images_dir = './products'
done_dir = './done'

def get_files(dir):
    files = []
    for (dirpath, dirnames, filenames) in walk(dir):
        files.append(filenames)
    print(str(len(files[0])) + ' files')
    return files[0]

def process_img(img_name):
    img = Image.open(images_dir + '/' + img_name)
    img.thumbnail(size)
    img.save(f'./done/{img_name}')

def  main():

    files = get_files(images_dir)

    t1 = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_img, files)

    # for file in files:
    #     process_img(file)

    t2 = time.perf_counter()

    files = get_files(done_dir)

    print(f'Finished in {t2-t1} seconds.')

if __name__ == '__main__':
    main()
