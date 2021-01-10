import Pyro4
import json
from typing import Dict, List, Any
from modules.decorators import calc_time, calc_plot

"""
terminal 03: python client.py
	type: server
"""

# use name server object lookup uri sshortcut
server = Pyro4.Proxy("PYRONAME:server")


# USING SERVER OBJECT

# # Hello World
message = input("What is your message? ").strip()
print(server.hello(message))

# operations

# # 01 - ok
profiles_engcomp = server.list_profiles_of_a_course(course='Engenharia da Computação')
print(profiles_engcomp)

# # # 02 - ok
# skills_ananindeua = server.list_skills_of_profiles_of_a_city(address="Ananindeua")
# print(skills_ananindeua)

# # # 03 - ok
# bruno_experiences: List[str] = server.list_experiences_from_email_profile(\
# 	email='bruno@email.com')
# print('Bruno experiences before add experience: {}'.format(bruno_experiences))

# server.put_new_experience_in_a_profile(\
# 	email='bruno@email.com', \
# 	experience='Engenharia de Software')

# bruno_experiences: List[str] = server.list_experiences_from_email_profile(\
# 	email='bruno@email.com')
# print('Bruno experiences after add experience: {}'.format(bruno_experiences))

# # # 04 - ok
# print('Getting experiences from profile which owns to {}'.format("cassio@email.com"))
# print(server.list_experiences_from_email_profile(email='cassio@email.com'))

# # # 05 - ok
# di_all_informations = server.list_all_informations_of_all_profiles()
# print(di_all_informations)

# # 06 - ok
# email_informations = server.list_all_informations_of_profile_by_its_email(email="renato@email.com")
# print(email_informations)

# # display photo
# server.display_photo(email='bruno@email.com')