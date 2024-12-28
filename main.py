from telegram_class import *
from pool_50m import * 

#client = Telegram(USER, API_ID, API_HASH)
#chats = client.get_chats()


file = os.listdir('PDF Results')[0]
results = Pool_50m(file)
print(results.coords_distance)



#results = get_results("PDF Results/50 freestyle Men's Final.pdf") 
#print(results)

#for pdf in get_pdf():
#	print(f"World Cup I Stage 18.10-20.10.2024/{pdf}")
#	results = get_results(f"World Cup I Stage 18.10-20.10.2024/{pdf}")
#	print(print_results(results), sep='\n')
#	print()