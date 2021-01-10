import Pyro4
import json
from typing import Dict, List, Any
from modules.decorators import calc_time, calc_plot
# j = {'alfbeto': ['a', 'b'], 'numeros': '1'}
# print(json.dumps(j), type(json.dumps(j)))

"""
terminal 03: python client.py
	type: server
"""
# uri not beeing used, but could be
# uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
# print(f"uri: {uri, type(uri)}")

message = input("What is your message? ").strip()
# use name server object lookup uri sshortcut
server = Pyro4.Proxy("PYRONAME:server")

"""
BGIN
REGISTERING PROFILE OBJECT
"""
# p1 = Pyro4.Proxy("PYRONAME:p1")

"""
END
REGISTERING PROFILE OBJECT
"""

# class Client(object):	
# 	"""Decorate server operations
# 	with @calc_time and @calc_plot
# 	to plot the time that each one
# 	of the operations takes to
# 	execute
# 	"""		

# 	@calc_plot
# 	@calc_time(debug=True)
# 	def hello(self, msg: str) -> str:
# 		return server.hello(msg)

	# @calc_plot
	# @calc_time(debug=True)
	# def list_profiles_of_a_course(*args, **kwargs) -> Any:
	# 	server.list_profiles_of_a_course(args, kwargs)

	# @calc_plot
	# @calc_time(debug=True)
	# def list_profiles_of_a_course(*args, **kwargs) -> str:
	# 	return server.list_profiles_of_a_course(args, kwargs)

# USING SERVER OBJECT


# remote object calss
# print(server.hello(message))
# print(p1.email)

# operations

# # 01 - ok
profiles_engcomp = server.list_profiles_of_a_course(course='Engenharia da Computação')
print(profiles_engcomp)

# # 02 - ok
# skills_ananindeua = server.list_skills_of_profiles_of_a_city(address="Ananindeua")
# print(skills_ananindeua)

# # 03
# bruno_experiences: List[str] = server.list_experiences_from_email_profile(\
# 	email='bruno@email.com')
# print('Bruno experiences before add experience: {}'.format(bruno_experiences))

# server.put_new_experience_in_a_profile(\
# 	email='bruno@email.com', \
# 	experience='Engenharia de Software')

# bruno_experiences: List[str] = server.list_experiences_from_email_profile(\
# 	email='bruno@email.com')
# print('Bruno experiences after add experience: {}'.format(bruno_experiences))

# # 04 - ok
# print('Getting experiences from profile which owns to {}'.format("cassio@email.com"))
# print(server.list_experiences_from_email_profile(email='cassio@email.com'))

# # 05 - ok
# di_all_informations = server.list_all_informations_of_all_profiles()
# print(di_all_informations)

# 06 - ok
# email_informations = server.list_all_informations_of_profile_by_its_email(email="renato@email.com")
# print(email_informations)

# display photo
server.display_photo(email='bruno@email.com')


# USING CLIENT OBJECT

# # Creating the client object
# client = Client()

# # Hello - ok
# message = input("What is your message? ").strip()
# client.hello(msg=message)

# 01
# @calc_plot
# @calc_time	
# def o1(course):
# 	server.list_profiles_of_a_course(course)

# o1(course='Engenharia da Computação')