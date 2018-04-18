from protocol import YoteServerProtocol
from factory import YoteServerFactory

if __name__ == "__main__":
    import asyncio

    ServerFactory = YoteServerFactory
    factory = YoteServerFactory(u"ws://localhost:10000")
    factory.protocol = YoteServerProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, "localhost", 10000)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
