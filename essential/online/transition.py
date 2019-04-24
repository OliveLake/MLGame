"""
The interface for coomunicating with the message server
"""

from asgiref.sync import async_to_sync
from channels_redis.core import RedisChannelLayer

class RedisTransition:
	def __init__(self, channel_name):
		"""Constructor

		@param channel_name Specify the name of the channel in the Redis server
		       to be communicated.
		"""
		# TODO Get the host from the environment variable
		self._redis_server = RedisChannelLayer(hosts = [("redis_server", 6379)])
		self._channel_name = channel_name

	def send(self, message_object):
		async_to_sync(self._redis_server.send)(self._channel_name, message_object)
