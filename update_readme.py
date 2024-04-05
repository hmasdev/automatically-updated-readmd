from datetime import datetime as dt
from jinja2 import FileSystemLoader, Environment
readme = Environment(loader=FileSystemLoader('.')).get_template('README.md.j2')
print(readme.render(now=dt.now().strftime('%Y-%m-%d %H:%M:%S')))
