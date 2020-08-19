import asyncio
from socket import gethostbyname
from cprint import *


class portscanner:
    def __init__(self, host,fullscan=False):
        self.host = host
        self.fullscan = fullscan
        self.open = []

    async def runner(self):
        if self.fullscan:
            x = 21845
            for i in range(3):
                if i == 1 or i == 2:
                    x = x + 21845
                task = [self.open_socket(ports) for ports in range(x - 21845 ,x)]
                await asyncio.gather(*task)
        else:
            task = [self.open_socket(ports) for ports in range(5000)]
            await asyncio.gather(*task)
            taskx = [self.open_socket(ports) for ports in range(5000,10000)]
            await asyncio.gather(*taskx)
            
    async def open_socket(self,port):
        socket_connection = asyncio.open_connection(self.host, port, loop=self.loop)
        try:
            _, writer  = await asyncio.wait_for(socket_connection, timeout=5)
            writer.close()
            self.open.append(port)
        except Exception as e:
            cprint.err(e)
        
    async def main(self):
        await self.runner()
        return self.open

if __name__ == "__main__":
    portscan = portscanner("127.0.0.1")
    open = portscan.main()
    cprint.info(open)
    
