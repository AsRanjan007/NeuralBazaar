from subprocess import run
cmd = [
    'git', 'filter-repo', '--force',
    '--commit-callback',
    'commit.author_name = b Ashutosh Ranjan; commit.author_email = barj.muz@gmail.com; commit.committer_name = bAshutosh Ranjan; commit.committer_email = barj.muz@gmail.com'
]
print(Running:, cmd)
run(cmd, check=True)
