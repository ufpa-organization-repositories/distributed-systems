# from abc import ABC, abstractmethod
from typing import List
import os
from PIL import Image
import base64
import jsonify
import Pyro4
import numpy as np
import base64
import io

@Pyro4.expose
class Profile():
	"""
	A user profile in object database
	"""
	def __init__(self, first_name: str, last_name: str, \
		photo: str, address: str, email: str, \
		academic_education: str, \
		skills: List[str], experiences: List[str]):

		self.first_name: str = first_name
		self.last_name: str = last_name
		self.photo: str = Profile.serialize_image(photo=photo)		
		self.address: str = address
		self.email: str = email
		self.academic_education: str = academic_education
		self.skills: List[str] = skills
		self.experiences: List[str] = experiences		

	@classmethod
	def serialize_image(self, photo: str) -> str:
		"""[SERVER] Serialize a photo (read bytes -> encode 64 -> str (utf-8))
		to send it through the network
		:photo: str
		return: str
		"""

		abs_path_to_photo_name: str = Profile.calc_path_image(photo=photo)
		image: _io.BufferedReader = open(abs_path_to_photo_name, 'rb')
		image_read: bytes = image.read()
		image_64_encode: bytes = base64.encodebytes(image_read)
		image_str: str = image_64_encode.decode(encoding="utf-8")
		return image_str


	def deserialize_image(self, image_str: str) -> bytes:
		"""[CLIENT] Serialize/Encode image
		:image_str: bytes
		return: str
		"""		
		image_64_encode: bytes = image_str.encode()
		image_bytes: bytes = base64.decodebytes(image_64_encode)
		return image_bytes


	@classmethod
	def calc_path_image(cls, photo) -> str:
		"""[SERVER] Calculate the absolute path to image
		:photo: str
		return: str
		"""
		return os.path.join(os.sep.join(\
			os.path.dirname(__file__).split()[:-1]), 'photos', photo)


	def display_photo(self) -> None:
		"""[CLIENT] Display image using PILLOW		
		return: None -> just displays the photo
		"""
		image_bytes: bytes = self.deserialize_image(image_str=self.photo)
		with Image.open(io.BytesIO(image_bytes)) as image_pillow_client:
			image_pillow_client.show()