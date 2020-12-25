import os
from glob import glob1
import jinja2 as j

CONTENT_FOLDER='.\\content'
DESTINATION='.\\build'
GALLERY_WEB_PATH='.\\assets\\gallery'

def generate_imgs_src(content_folder):
    """Generate web-ready list of full filepaths for jinja2

    Args:
        content_folder (string): path to content folder
    """

    result = []
    for root, dirs, files in os.walk(CONTENT_FOLDER):
        for filename in files:
            result.append(os.path.join(GALLERY_WEB_PATH, filename))
    print(result[0])


generate_imgs_src(CONTENT_FOLDER)



def procedure():

    """
    copy contents of CONTENT_FOLDER to GALLERY_WEB_PATH
    generate web-ready paths to images generate_imgs_src() -> [src] (./assets/gallery/filename.extension)
    pass [src] back to generator
    generate HTML and save to DESTINATION

    """



    # file_loader = j.FileSystemLoader('./src/templates')
    # env = j.Environment(loader=file_loader)

    # template = env.get_template('index.template.html')
    # stream = template.render(
    #     images=[1,2,3,4,5],
    # )

    # with open(
    #     os.path.join(DESTINATION, 'index.html'), 'w', encoding='utf-8'
    # ) as out:
    #     out.write(stream)

# procedure()