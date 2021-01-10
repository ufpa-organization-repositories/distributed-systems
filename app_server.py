from modules.profile import Profile
import Pyro4
from typing import List, Dict
import json
import jsonify
from bottle import run
from modules.decorators import calc_time, calc_plot


"""
in terminal 01:
python -m Pyro4.naming

in terminal 02:
python app_server.py
"""


db_li_profiles: List[Profile] = []
p1 = Profile(first_name='Bruno', last_name='Conde Costa da Silva', \
	photo='bruno.png', address='Ananindeua', email='bruno@email.com', \
	academic_education='Engenharia da Computação', skills=['Python'], \
	experiences=['Ciencia de dados', 'Desenvolvimento Web'])

# p1.photo.show()
p2 = Profile(first_name='Renato', last_name='Sousa da Silva', \
	photo='renato.png', address='Ananindeua', email='renato@email.com', \
	academic_education='Engenharia da Computação', skills=['Cobol'], \
	experiences=['infra'])
p3 = Profile(first_name='Cassio', last_name='Sousa da Silva', \
	photo='cassio.png', address='Bragança', email='cassio@email.com', \
	academic_education='Educação Física', skills=['Cobol'], \
	experiences=['xadrez na praça'])

db_li_profiles.append(p1)
db_li_profiles.append(p2)
db_li_profiles.append(p3)

# for profile in db_li_profiles:
	# print('\n--------------------')
	# print(profile.__dict__)	

@Pyro4.expose # wihtout this line the client doesn't run properly
class Server:
	"""
	Class Server to create exposed server object
	Tips: to debug this class, run the client code at this module
	(app_server.py), 'cause here we have more details than just
	the line of client code which raises an error
	"""	
	# db_li_profiles: List[Profile] = db_li_profiles


	def __init__(self): pass		
	
	@staticmethod
	@calc_plot
	@calc_time
	def hello(msg: str) -> str:		
		print('client message: {}'.format(msg))
		return 'Message processed sucessfully by the server application'

	# 01 - ok	
	@staticmethod
	@calc_plot
	@calc_time
	def list_profiles_of_a_course(course: str) -> Dict:
		"""
		List all profiles of a course
		"""

		di_profiles_of_a_course = {}
		for profile in db_li_profiles:			
			if profile.academic_education == course:
				email = profile.email
				di_profiles_of_a_course[email] = profile.__dict__ # [CLIENT] TypeError: Object of type bytes is not JSON serializable
				"""
				So, i remove the p1, p2 and p3 from deamon and not register too
				I just share the server object
				"""
		
		# return str(db_li_profiles_of_a_course).encode(encoding='utf-8', errors='strict')
		# return jsom.dumps(di_profiles_of_a_course.__dict__) # working, but [CLIENT] TypeError: Object of type bytes is not JSON serializable
		# return jsonify(db_li_profiles_of_a_course) # TypeError: Object of type Daemon is not JSON serializable

		# return "['p1', 'p2']" # FALSE
		# return "profiles of a course" # TRUE

		# TRUE
		# string = 'profiles'
		# return f"[{string}]"

		# TRUE
		# profs = {'a': '0'}
		# print(profs)
		# print(type(profs))
		# return profs

		# print(di_profiles_of_a_course)
		# print(type(di_profiles_of_a_course))
		return di_profiles_of_a_course


	# 02 - ok
	@staticmethod
	def list_skills_of_profiles_of_a_city(address: str) -> list:
		"""
		List the skills of the profiles of a specific city
		"""

		li_skills_of_profiles_of_a_address = []
		for profile in db_li_profiles:
			if profile.address == address:
				if type(profile.skills) == list:
					for skill in profile.skills:
						if not skill in li_skills_of_profiles_of_a_address:
							li_skills_of_profiles_of_a_address.append(skill)
				else:
					return [profile.skills]

		return li_skills_of_profiles_of_a_address

	# 03
	@staticmethod
	def put_new_experience_in_a_profile(email: str, experience: str) -> None:
		"""
		Addding a new experience in a registrated profile
		:email:	str -> id of the profile
		:experience: str
		"""

		for i, profile in enumerate(db_li_profiles):
			if profile.email == email:
				db_li_profiles[i].experiences.append(experience)


	# 04 - ok
	@staticmethod
	def list_experiences_from_email_profile(email: str):
		"""
		Get experiences from an email profile of registered profiles		
		"""
		li_email = [profile.email for profile in db_li_profiles]			

		if len(li_email) == 0:
			print(f"{email} email does'n belong to any users")
			return None

		if email in li_email:
			for profile in db_li_profiles:
				if profile.email == email:
					return profile.experiences

	# 05 - ok
	@staticmethod
	def list_all_informations_of_all_profiles() -> Dict:
		"""Get all informations of all profiles
		:db_li_profiles: List[Profiles]
		return: Dict -> Dictionary of all profiles
		"""
		di_all_profiles = {}

		for profile in db_li_profiles:
			email = profile.email
			di_all_profiles[email] = {}

			for key, value in profile.__dict__.items():
				if not key == 'email':
					di_all_profiles[email][key] = value			

		return di_all_profiles

	# 06 - ok
	def list_all_informations_of_profile_by_its_email(self, email: str) -> Dict:
		"""Get all informations of a profile by passing its email
		:db_li_profiles: List(Profile)
		:email: str -> The email profile
		return: Dict -> Return the profile informations in a dictionary
		"""
		try:
			return self.list_all_informations_of_all_profiles()[email]
		except Exception as e:
			print('Email {} not found:\n\n {}'.format(email, e))
			raise e

	# display profile photo
	@classmethod
	def display_photo(cls, email):
		for i, profile in enumerate(db_li_profiles):
			if profile.email == email:
				profile.display_photo()


def start_server():
    server = Server()

    # make a Pyro daemon to listen remote calls
    # all pyro objects are registered in one or more deamons
    daemon = Pyro4.Daemon(host='127.0.0.2', port=8080) # works on 127.0.0.2 ok, but need tests    

    # locate the name server running
    # usually there is just one name server running in your network
    ns = Pyro4.locateNS()

    # register the server as a Pyro object
    # uri is unique resource identifier (the same idea of url - unique resource location)
    uri = daemon.register(server)  
    
    # register the object with a name in the name server
    ns.register("server", uri)   
    
    # print the uri so we can use it in the client later
    print("Ready. Object uri =", uri)
    
    # # creating uri for each profile objects
    # uri_1, uri_2, uri_3 = daemon.register(p1), daemon.register(p2), daemon.register(p3)

    # # resgistering each uri profile object (IT CAN BE DISCARTED)
    # ns.register("p1", uri_1)
    # ns.register("p2", uri_2)
    # ns.register("p3", uri_3)

    # start the event loop of the server to wait for calls
    daemon.requestLoop()    


if __name__ == '__main__':
	start_server()

# -------------------------------------------------

# # testing (client code)
# server = Server() # don't do this in client

# 01 - ok
profiles_engcomp = server.list_profiles_of_a_course(course='Engenharia da Computação')
print(profiles_engcomp['bruno@email.com']['first_name'])
# for profile_key in profiles_engcomp:
# 	print(profile_key)
# 	print(profiles_engcomp[profile_key], '\n')

# # 02
# skills_ananindeua = server.list_skills_of_profiles_of_a_city(address="Ananindeua")
# print(skills_ananindeua)

# # 03
# print('Bruno experiences: {}'.format(db_li_profiles[0].experiences)) # will not work on client
# db_li_profiles[0].experiences.append('Engenharia de software')
# print('Bruno experiences: {}'.format(db_li_profiles[0].experiences)) # will not work on client

# # 04
# print('Getting experiences from profile which owns to {}'.format("cassio@email.com"))
# print(server.list_experiences_from_email_profile(email='cassio@email.com'))

# # 05 - ok
# di_all_informations = server.list_all_informations_of_all_profiles()
# print(di_all_informations)

# # 06
# email_informations = server.list_all_informations_of_profile_by_its_email(email="renato@email.com")
# print(email_informations)
# email_informations['photo'].show()

# display photo
# server.display_photo(email='bruno@email.com')