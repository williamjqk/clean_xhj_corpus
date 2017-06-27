from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# 載入(簡體)中文的基本語言庫
chatbot.train("chatterbot.corpus.chinese")

# 載入(簡體)中文的問候語言庫
chatbot.train("chatterbot.corpus.chinese.greetings")
print('over trained file: chinese.greetings')

# 載入(簡體)中文的對話語言庫
chatbot.train("chatterbot.corpus.chinese.conversations")
print('over trained file: chinese.conversations')

# 所谓的小黄鸡的语料
# chatbot.train("chatterbot.corpus.chinese.xiaohuangji")

for i in range(45):
    name = "chatterbot.corpus.chinese.xhj45.xiaohuangji" + str(i+1)
    chatbot.train(name)
    print('over trained file: {}'.format(name))

# %%
# Get a response to an input statement
# chatbot.get_response("Hello, how are you today?")
print(chatbot.get_response("傻逼"))


# %%
