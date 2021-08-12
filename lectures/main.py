import argparse

parser = argparse.ArgumentParser(description='File statistics')

parser.add_argument('file_path', help="Dateipfad der Datei, die analysiert werden soll")
parser.add_argument('--verbose', '-V', action='store_true', default=False, help="Zeige den Inhalt der Datei")

args = parser.parse_args()

print('Hallo main.py running...')
print(f'Open file: {args.file_path}...', end='')

with open(args.file_path, 'r') as f:
    content = f.read()
    print('done.')

print(f'I found {len(content)} bytes.\n')

if args.verbose:
    print('Content:\n')
    print(content)