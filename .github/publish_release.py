import os
import platform
import re
import subprocess
import sys


def call(*args, shell=False):
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell, check=False)
    if proc.returncode:
        print('Error: ', *args)
        print('STDOUT:', proc.stdout, file=sys.stdout)
        proc.check_returncode()
    return proc.stdout.decode('utf8').strip()


def get_bins():
    path = 'dist'
    binaries = os.listdir(path)
    binaries = ['-a "{}/{}"'.format(path, it) for it in binaries if it.endswith('.whl') or platform.system() == 'Linux']
    return ' '.join(binaries)


def main():
    trigger = os.getenv('GITHUB_REF_NAME', '')
    trigger = trigger.split('/')[0]
    if not re.match(r'v\d+(\.\d+){2,}', trigger):
        version = call('python', 'setup.py', '--version')
        commit = call('git', 'describe', '--always', '--abbrev=8')
        trigger = 'v{}-{}'.format(version, commit)
    print(trigger)

    binaries = get_bins()
    try:
        output = call('hub release create {} -m "{}" "{}"'.format(binaries, trigger, trigger), shell=True)
    except subprocess.CalledProcessError:
        output = call('hub release edit {} -m "" "{}"'.format(binaries, trigger), shell=True)
    print(output)


if __name__ == '__main__':
    main()
