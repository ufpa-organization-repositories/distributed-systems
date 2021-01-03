# from abc import ABC, abstractmethod
from typing import List
import os
from PIL import Image


class Profile():
	"""
	A user profile in object database
	"""
	def __init__(self, first_name, last_name, photo, address, email, academic_education, skills, experiences):
		self.first_name: str = first_name
		self.last_name: str = last_name
		self.photo = Image.open(os.path.join(os.sep.join(os.path.dirname(__file__).split()[:-1]), 'photos', photo))
		self.address: str = address
		self.email: str = email
		self.academic_education: str = academic_education
		self.skills: List[str] = skills
		self.experiences: List[str] = experiences