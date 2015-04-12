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


def client_can_run(name):
    try:
        exec('from . import %s as client; client.can_run()' % name)
        print('%s client OK' % name)
        return True
    except ClientException as e:
        print('%s client error %s' % (name, str(e)))
    except Exception as e:
        print('%s client exception %s' % (name, str(e)))

def run_client(name):
    try:
        exec('from . import %s as client; client.can_run()' % name)
    except ClientException as e:
        print('%s client error %s' % (name, str(e)))
    except Exception as e:
        print('%s client exception %s' % (name, str(e)))


def run(client=None):
    if client is not None:
        client_can_run(client)
        run_client(client)
    else:
        client_errors = []
        clients = []
        # Find the first working client
        for name in list(CLIENT_ORDER):
            try:
                client_can_run(name)
                break
            except ClientException as e:
                client_errors.append(client, e)
        else:
            if not clients:
                print('Could not start any clients.')
                print('HINT:')
                print('  Install client dependencies with melange clientinstall %client')
                print('  e.g')
                print('  melange clientinstall pypy')
                for client in list(CLIENT_ORDER):
                    print('    %s' % client)
