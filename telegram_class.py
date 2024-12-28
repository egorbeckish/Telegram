from utils import *

class Telegram:

	def __init__(self, user: str, api_id: str=None, api_hash: str=None) -> None:
		self.connect = TelegramClient(user, api_id, api_hash)
		self.connect.start()		
	
	def self_info(self) -> dict[str: int | str]:
		info = self.connect.get_me()
		return {
			'first_name': info.first_name,
			'last_name': info.last_name,
			'user_name': info.username,
			'id': info.id,
			'phone': info.phone,
		}

	def get_chats(self) -> dict[str: dict[str: int | str]]:
		return [
			{
				'title': dialog.title,
				'id':dialog.id
			} 
			for dialog in self.connect.get_dialogs()
		]
	
	def get_messages(self, chat=None, count_message:int=None) -> None:
		for i, item in enumerate(self.connect.iter_messages(chat)):
			if not item.message:
				continue
			
			#print(i, item.message, item.stringify())

			if i == count_message:
				break
			print(item.message)