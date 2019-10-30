import requests


def test_web(host):
    """Ensure web server is reachable on port 9090"""
    ip_addr = host.ansible.get_variables()['ansible_host']
    # 'verify=False' is set in this call to avoid the current SSL verification
    # error that occurs due to the current lack of a local certificate for
    # allowing HTTPS connections to the cockpit web interface
    response = requests.get('https://{}'.format(ip_addr), verify=False)
    # check for expected status code from the cockpit webserver
    assert response.status_code == 200
