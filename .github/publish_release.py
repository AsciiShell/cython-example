import os
import platform
import re
import subprocess


def call(*args):
    proc = subprocess.run(args, stdout=subprocess.PIPE, shell=True, check=True)
    return proc.stdout.decode('utf8').strip()


def get_bins():
    binaries = os.listdir('dist')
    binaries = [it for it in binaries if it.endswith('.whl') or platform.system() == 'Linux']
    return binaries


def main():
    trigger = os.getenv('GITHUB_REF_NAME', '')
    trigger = trigger.split('/')[0]
    if not re.match(r'v\d+(\.\d+){2,}', trigger):
        version = call('python3 setup.py --version')
        commit = call('git describe --always --abbrev=8')
        trigger = 'v{}-{}'.format(version, commit)
    print(trigger)

    binaries = get_bins()
    binaries = ' '.join(['-a ' + it for it in binaries])
    try:
        output = call('hub release create {} {}'.format(binaries, trigger))
    except subprocess.CalledProcessError:
        output = call('hub release edit {} {}'.format(binaries, trigger))
    print(output)


if __name__ == '__main__':
    main()
