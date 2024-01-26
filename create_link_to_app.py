#!/usr/bin/python3  

import click
from os.path import abspath, basename

@click.command()
@click.option('--file', help='Path to file', type=click.Path(exists=True), required=True)
@click.option('--name', help='App name', required=True)
def main(file, name):
    """Simple program that creates desktop image for specified executable file"""

    abs_path = abspath(file)

    content = f"""[Desktop Entry]
    Version=0.13.23
    Type=Application
    Name={name}
    Comment=Application Description
    TryExec={abs_path}
    Exec={abs_path}
    Icon=
    Actions=Editor"""

    filename = basename(abs_path)

    with open(f'/home/majo/.local/share/applications/generated_{name}.desktop', 'w') as f:
        f.write(content)


    click.echo(f'Created link to AppImage')



if __name__ == '__main__':
    main()
