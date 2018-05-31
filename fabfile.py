from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO='https://github.com/cc1061361123/blog.git'

env.user='chenchen'
env.password='Wan,.521'

env.hosts=['www.gongchunyu.cc']
env.port='22'
def deploy():
    source_folder='C:/Users/Xie/sites/www.gongchunyu.cc/django-blog-tutorial'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-www.gongchunyu.cc')
    sudo('service nginx reload')
