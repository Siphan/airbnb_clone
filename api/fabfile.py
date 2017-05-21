from fabric.api import *

dist = "airbnb_clone"
maintenance_file = "maintenance.trigger"
env.roledefs = {
    'deploy_siphan': ['siphan@192.168.0.45', 'admin@158.69.84.193']
}


@roles('deploy_siphan')
def deploy_siphan():
    '''Clone airbnb_clone repo and create a zipfile.'''
    local('git clone https://github.com/Siphan/airbnb_clone/')
    local("cd airbnb_clone ; tar --exclude='*.tar.gz' -czf %s.tar.gz ." % dist)

    '''Unpack the tarfile and copy into the site's root on the webserver.'''
    put('airbnb_clone/%s.tar.gz' % dist, '/tmp/%s.tar.gz' % dist)
    run('sudo mkdir /tmp/%s' % dist)
    run('sudo tar -xzf /tmp/%s.tar.gz -C /var/www/html' % dist)
    run('sudo rm -rf /tmp/%s /tmp/%s.tar.gz' % (dist, dist))
    local('sudo rm -rf mywebapp.tar.gz airbnb_clone')


def maintenance_on():
    '''Add maintenance.trigger file to redirect users to maintenance.html and
    return a 503 status. See .htaccess file.
    '''
    run('sudo touch /var/www/html/%s' % maintenance_file)


def maintenance_off():
    '''Remove maintenance.trigger file to redirect users to maintenance.html
    and return a 200 status. See .htaccess file.
    '''
    run('sudo rm /var/www/html/%s' % maintenance_file)
