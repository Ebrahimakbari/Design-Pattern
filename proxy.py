"""
Proxy Design Pattern:
    The Proxy pattern is a structural design pattern that provides 
    a placeholder or surrogate for another object to control access to it. 
    The proxy acts as an intermediary between the client and the real object, 
    allowing you to perform something either before
    or after the request gets through to the original object.

Key Components:
    Subject - Common interface for RealSubject and Proxy
    RealSubject - The actual object that performs the real work
    Proxy - Controls access to the RealSubject and may perform additional operations
    Client - Uses the Subject interface
Types of Proxies:
    Virtual Proxy - Controls access to expensive objects
    Protection Proxy - Controls access based on permissions
    Remote Proxy - Represents objects in different address spaces
    Caching Proxy - Provides caching for expensive operations
    Smart Reference - Performs additional actions when object is accessed
"""

from abc import ABC, abstractmethod
from datetime import datetime
import time

#subject
class AbstractServer(ABC):
    @abstractmethod
    def receive(self):
        pass

#real subject
class Server(AbstractServer):
    def receive(self):
        print('request received .. starting process..')
        time.sleep(1)
        print('done')

#proxy
class ProxyServer(AbstractServer):
    def __init__(self, server):
        self._server = server
    
    def receive(self):
        self.logging()
        self._server.receive()
    
    def logging(self):
        with open('log.log', 'a') as f:
            f.write(f'request time : {datetime.now()} \n')

#client
def client(server, proxy):
    s = server()
    p = proxy(s)
    p.receive()

client(Server, ProxyServer)
