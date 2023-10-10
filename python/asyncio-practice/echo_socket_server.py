import asyncio
import socket


async def echo(conn: socket.socket, loop: asyncio.AbstractEventLoop):
    while data := await loop.sock_recv(conn, 1024):
        await loop.sock_sendall(conn, data)

async def listen_for_connection(server_socket: socket.socket, loop: asyncio.AbstractEventLoop):
    while True:
        conn, addr = await loop.sock_accept(server_socket)
        conn.setblocking(False)
        asyncio.create_task(echo(conn, loop))

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.setblocking(False)
    server_socket.bind(("0.0.0.0", 8000))
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())

if __name__ == "__main__":
    asyncio.run(main())