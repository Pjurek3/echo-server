import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)
            print(sock)
            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # TODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting
                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))
                    
                    # TODO: Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))
                    
                    if len(data) < 16:

                        break
                
                print('Just Broke the server!')

            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                conn.shutdown(1)
                conn.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        print('quitting echo server', file=log_buffer)
        raise

if __name__ == '__main__':
    server()
    sys.exit(0)
