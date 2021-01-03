import Pyro4

"""
terminal 03: python client.py
	type: server
"""
uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
print(f"uri: {uri, type(uri)}")

message = input("What is your message? ").strip()
# use name server object lookup uri sshortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.hello(message))
