import Pyro4
import json
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

# remote object calss
print(server.hello(message))
# print(p1.email)

# operations

# # call profile objects by using server object
# obj = server.call_profile_objects()
# print(obj.email)

# 01 - ok
# profiles_engcomp = server.list_profiles_of_a_course(course='Engenharia da Computação')
# print(profiles_engcomp)

# # 02 - ok
# skills_ananindeua = server.list_skills_of_profiles_of_a_city(address="Ananindeua")
# print(skills_ananindeua)

# # 03
# print('Bruno experiences: {}'.format(db_li_profiles[0].experiences)) # will not work on client
# db_li_profiles[0].experiences.append('Engenharia de software')
# print('Bruno experiences: {}'.format(db_li_profiles[0].experiences)) # will not work on client

# # 04 - ok
# print('Getting experiences from profile which owns to {}'.format("cassio@email.com"))
# print(server.list_experiences_from_email_profile(email='cassio@email.com'))

# # 05 - ok
# di_all_informations = server.list_all_informations_of_all_profiles()
# print(di_all_informations)

# # 06 - ok
# email_informations = server.list_all_informations_of_profile_by_its_email(email="renato@email.com")
# print(email_informations)
# email_informations['photo'].show()