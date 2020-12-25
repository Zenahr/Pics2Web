import os
from glob import glob1
import jinja2 as j

DESTINATION='./build'

def procedure():
    file_loader = j.FileSystemLoader('./src/templates')
    env = j.Environment(loader=file_loader)

    template = env.get_template('index.template.html')
    stream = template.render(
        images=[1,2,3,4,5],
    )

    with open(
        os.path.join(DESTINATION, 'index.html'), 'w', encoding='utf-8'
    ) as out:
        out.write(stream)

procedure()