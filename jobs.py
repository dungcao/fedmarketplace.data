import subprocess


def start_client(server, config, data, runth):
    subprocess.run(["docker", "run", "dungcao1979/fedmarketplace.fraud.vm", server, config, data, runth])


def remove_all_container():
    subprocess.run(["docker", "rm", "-f", "$(docker ps -a -q)"])