import os
from distutils.dir_util import copy_tree
from glob import glob1
import jinja2 as j

CONTENT_FOLDER='.\\content'
BUILD_FOLDER='.\\build'
GALLERY_WEB_PATH='.\\assets\\gallery\\'

def generate_imgs_src(content_folder=CONTENT_FOLDER):
    """Generate web-ready list of full filepaths for jinja2.

    Args:
        content_folder (string): path to content folder
    """
    result = []
    for root, dirs, files in os.walk(CONTENT_FOLDER):
        for filename in files:
            result.append(os.path.join(GALLERY_WEB_PATH, filename))
            # result.append(filename)
    print('log: generated file paths for', len(result), 'images')
    return result

def copy_content(origin=CONTENT_FOLDER, destination=os.path.join(BUILD_FOLDER, GALLERY_WEB_PATH)):
    """Copy content to build folder for deployment on the web.

    Args:
        origin ([type]): [description]
        destination ([type]): [description]
    """
    copy_tree(origin, destination)

def generate_HTML(images):
    file_loader = j.FileSystemLoader('./src/templates')
    env = j.Environment(loader=file_loader)

    template = env.get_template('nano.template.html')
    stream = template.render(
        title        = 'Pics2Web Gallery',
        itemsBaseURL = GALLERY_WEB_PATH,
        images       = images,
    )

    with open(
        os.path.join(BUILD_FOLDER, 'index.html'), 'w', encoding='utf-8'
    ) as out:
        out.write(stream)
    print('log: generated HTML')


def procedure():

    """
    copy contents of CONTENT_FOLDER to GALLERY_WEB_PATH
    generate web-ready paths to images generate_imgs_src() -> [src] (./assets/gallery/filename.extension)
    pass [src] back to generator
    generate HTML and save to DESTINATION

    """

    copy_content()
    generate_HTML(images=generate_imgs_src())


   
procedure()