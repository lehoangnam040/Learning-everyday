from multiprocessing import Pipe, Process


def pingpong(i, conn, send_first: bool):

    value = 0
    if send_first:
        conn.send(1)

    while True:
        recv_val = conn.recv()
        value += recv_val
        print(f"process {i} value={value}")
        conn.send(value)
        if value > 100:
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe(duplex=True)

    player1 = Process(target=pingpong, args=(1, conn1, True))
    player2 = Process(target=pingpong, args=(2, conn2, True))

    player1.start()
    player2.start()
    player1.join()
    player2.join()
