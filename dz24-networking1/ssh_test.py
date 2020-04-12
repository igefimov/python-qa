import paramiko


def ssh_client():
    host = '192.168.0.122'
    username = 'igor'
    password = 'igor'
    port = 22
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(hostname=host, username=username, password=password, port=port)
    return sshClient


def test_01_verify_apache_is_running():
    ssh = ssh_client()
    stdin, stdout, stderr = ssh.exec_command('systemctl status apache2 | grep "active (running)"')
    assert not stdout.channel.recv_exit_status(), 'Apache is up and running'
    ssh.close()


def test_02_restart_and_verify_mariadb():
    ssh = ssh_client()
    stdin, stdout, stderr = ssh.exec_command('sudo -S systemctl restart mariadb', get_pty=False)
    stdin.write('igor\n')
    assert not stdout.channel.recv_exit_status(), 'MariaDB was restarted'
    stdin, stdout, stderr = ssh.exec_command('systemctl status mariadb | grep -o ";.*ago$"')
    assert not 'min' in stdout.readline(), 'MariaDB is up and running'
    ssh.close()
