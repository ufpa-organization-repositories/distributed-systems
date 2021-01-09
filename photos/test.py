from PIL import Image
import base64
import io


###########################
# Serializing/encoding (Server)

image = open('bruno.png', 'rb')
print(image)
print('image type: ', type(image))

# # optional at the server side and usefull in client side
# # It does not work at the same time that client
# with Image.open(image) as image_pillow_server:
# 	print(type(image_pillow_server))
# 	image_pillow_server.show()

print('\n\n' + 30 * '-')
image_read = image.read()
print('image_read: ', image_read)
print('image_read (type): ', type(image_read))

print('\n\n' + 30 * '-')
image_64_encode = base64.encodebytes(image_read)
print('image_64_encode: ', image_64_encode)
print('image_64_encode (type): ', type(image_64_encode))

###############################
# Deserializing/Decoding (Client)

image_64_decode = base64.decodebytes(image_64_encode)
print(type(image_64_decode))

# optional at the server side and usefull in client side
image_pillow_client = Image.open(io.BytesIO(image_64_decode))
print(type(image_pillow_client))
image_pillow_client.show()

# # or

# with Image.open(io.BytesIO(image_64_decode)) as image_pillow_client:
# 	image_pillow_client.show()