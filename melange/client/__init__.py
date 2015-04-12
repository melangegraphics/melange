from enum import Enum

# If no client is specified try these in order
CLIENT_ORDER=['pyglet', 'web']

class ClientReason(Enum):
    dependencies = 1

class ClientException(Exception):
    def __init__(self, msg, reason):
        self.msg = msg
        self.reason = reason
    
    def __str__(self):
        return self.msg


def run_client(name):
    exec('import %s as client' % name)
    try:
        client.init()
    except ClientException as e:
        print('Client error %s' % str(e))


def run(client=None):
    if client is not None:
        run_client(client)
    else:
        clients = list(CLIENT_ORDER)
        client_errors = []
        # Find the first working client
        for client in clients:
            try:
                client.init()
            except ClientException as e:
                client_errors.append(client, e)
        else:
            print('Could not start any clients.')
            print('HINT:')
            print('  Install client dependencies with melange clientinstall %client')
            print('  e.g')
            print('  melange clientinstall pypy')
            for client in clients:
                print('    %s' % client)
