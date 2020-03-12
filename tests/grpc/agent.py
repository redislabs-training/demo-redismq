import signal
import threading

from message_queue_client import Receivers, send_message


def sender(service_name, func_name):

    while True:

        rsp = send_message(service_name, func_name, "poaylaod")

        print(rsp)


def test_func(req_params):

    rsp = {
        "result": req_params + "_processed"
    }

    return rsp


threading.Thread(target=sender, args=('test-service', 'test_func')).start()

rs = Receivers('test-service', [test_func]).start()


def signal_handler(signum, sighdl):
    rs.stop()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

rs.wait()
