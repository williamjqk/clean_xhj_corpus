from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# 載入(簡體)中文的基本語言庫
chatbot.train("chatterbot.corpus.chinese")
print('over trained file: chinese')

# 載入(簡體)中文的問候語言庫
chatbot.train("chatterbot.corpus.chinese.greetings")
print('over trained file: chinese.greetings')

# 載入(簡體)中文的對話語言庫
chatbot.train("chatterbot.corpus.chinese.conversations")
print('over trained file: chinese.conversations')

# 所谓的小黄鸡的语料
# chatbot.train("chatterbot.corpus.chinese.xiaohuangji")
chatbot.train("chatterbot.corpus.chinese.xhj45.xiaohuangji4")
print('over trained file: chinese.xhj45.xiaohuangji4')

# %%
# Get a response to an input statement
# chatbot.get_response("Hello, how are you today?")
chatbot.get_response("傻逼")


# %%
