import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pptpd_running_and_enabled(host):
    svc = host.service('pptpd')
    assert svc.is_enabled
    assert svc.is_running


def test_pptpd_is_listen(host):
    socket = host.socket('tcp://127.0.0.1:1723')
    assert socket.is_listening
