from pyrogram import Client, filters 
from pyrogram.types import Message


api_hash = "" #api hash 
api_id = 111111 #api id 
phone_number = "+9890000000" #shomare
from_chat_id = 111111 #chat id ke az aan ersal shavad
to_chat_id = 111111 #chat id ke be aan ersal shavad


app = Client("meysam", api_id, api_hash)

    #baraye login kardan mitonid in ghesmat ro az comment dar biarid
# app.connect()
# sent_code_info = app.send_code(phone_number)
# phone_code = input("Please enter your phone code: ")  # Sent phone code using last function
# app.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)


@app.on_message(filters.me)
async def channel(c:Client, m:Message):
    if m.text == "S": #dar saved message khod S(bozorg) ersal konid ta robat kar konad

        # in ghesmat niazi be dar ovordan az comment nisst(serfan baraye kasani ke baladan)
        # async for message in app.get_chat_history(-1001978825114):
        #     print(message.text)
        for i in range(1000): 
            try:
                print(i)
                await app.copy_message(to_chat_id, from_chat_id, i, reply_to_message_id=16)
                #tozihat in ghesmat dar: https://github.com/hossein504/channel-to-topic_group
            except:
                pass

app.run()