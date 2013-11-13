#!/usr/bin/env bash
touch /tmp/installscript
chmod +x /tmp/installscript

function install_os {
    apt-get update
    
    cat > /etc/rc.local <<EOF
#!/usr/bin/env bash
dhclient eth0
uwsgi /etc/uwsgi/apps-enabled/pescator.ini
exit 0
EOF
    
    cat >> /home/vagrant/.bashrc <<EOF
export DJANGO_SETTINGS_MODULE=pescator.settings.vagrant
cd /vagrant
source env/bin/activate 

echo 'Server reload: kill -HUP \$(</tmp/uwsgi_pescator.pid)'
echo 'Server stop: kill -INT \$(</tmp/uwsgi_pescator.pid)'
echo 'Server start: uwsgi /etc/uwsgi/apps-enabled/pescator.ini'
echo Server logs: tail -f /vagrant/uwsgi.log
echo
if [[ -f /tmp/uwsgi_pescator.pid ]]; then
    kill -0 \$(</tmp/uwsgi_pescator.pid)

    if [[ \$? -eq 0 ]]; then
        echo Server is currently running
    else
        echo Server is dead, starting server
    fi
else
    echo Server is **not** running, starting
    uwsgi /etc/uwsgi/apps-enabled/pescator.ini
fi
EOF
}

function install_db {
    sudo apt-get install -y postgresql-9.1

    cat > /tmp/installscript <<EOF
#!/usr/bin/env bash
psql -f /vagrant/docs/examples/postgresql_utf8_template.sql
createuser -wsrd vagrant
createdb -E UTF8 -O vagrant django
EOF
    su postgres -c /tmp/installscript
        
    cat > /tmp/installscript <<EOF
export DJANGO_SETTINGS_MODULE=pescator.settings.vagrant
source /srv/pescator/env/bin/activate
cd /srv/pescator
./manage.py syncdb --noinput
./manage.py migrate
EOF
    su vagrant -c /tmp/installscript
}

function install_http {
    apt-get install -y nginx uwsgi uwsgi-plugin-python nodejs npm memcached
    npm install -g coffee-script recess

    ln -sfn /vagrant/docs/examples/nginx.conf /etc/nginx/nginx.conf
    /etc/init.d/nginx start
    
    ln -sfn /vagrant/docs/examples/pescator.ini /etc/uwsgi/apps-enabled/
    
    cat > /tmp/installscript <<EOF
export DJANGO_SETTINGS_MODULE=pescator.settings.vagrant
source /srv/pescator/env/bin/activate
cd /srv/pescator
./manage.py collectstatic -l --noinput
EOF
    su vagrant -c /tmp/installscript
    
    uwsgi /etc/uwsgi/apps-enabled/pescator.ini
}

function install_project {
    echo DJANGO_SETTINGS_MODULE=pescator.settings.vagrant >> /etc/bash.bashrc
    
    apt-get install -y git python-virtualenv python-imaging python-psycopg2 python-pylibmc

    ln -sfn /vagrant /srv/pescator
    chown vagrant /srv/pescator

    cat > /tmp/installscript <<EOF
#!/usr/bin/env bash
virtualenv --system-site-packages /srv/pescator/env
source /srv/pescator/env/bin/activate
pip install django
pip install -r /srv/pescator/requirements/base.txt
EOF
    su vagrant -c /tmp/installscript
}

install_os
install_project
install_db
install_http
