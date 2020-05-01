import json
import os
from chatterbot import ChatBot


basedir = os.path.abspath(os.path.dirname(__file__))


class PrivateBot(object):

	def __init__(self, bot_name, basedir=basedir):
		if __name__ == '__main__':
			from chatterbot.trainers import ListTrainer
			from chatterbot.trainers import ChatterBotCorpusTrainer
			
			self.slash = '/'
			self.basedir = basedir
			self.path_to_massanger = basedir+self.slash+'data/massanger'
			self.path_to_dialogues = basedir+self.slash+'data/dialogues'
			self.sub_directories = [ f.name for f in os.scandir(self.path_to_massanger) if f.is_dir() ]
			self.list_trainer = ListTrainer(self.bot)
			self.chatterbot_corpus_trainer = ChatterBotCorpusTrainer(self.bot)

		self.bot = ChatBot(bot_name,
			logic_adapters=[
				'chatterbot.logic.MathematicalEvaluation',
				{'import_path': 'chatterbot.logic.BestMatch',
				'default_response': 'I am sorry, but I do not understand.',
				'maximum_similarity_threshold': 0.90},
				'chatterbot.logic.BestMatch'
			],
			preprocessors=[
				'chatterbot.preprocessors.clean_whitespace', 
				'chatterbot.preprocessors.convert_to_ascii'
				]
			)


	def get_massanger_files(self, directory):
		return sorted([f.name for f in os.scandir(
			self.path_to_massanger+self.slash+directory) if f.is_file() and f.endswith('.json') ])


	def get_dialogue_files(self):
		return sorted([f.name for f in os.scandir(
			self.path_to_dialogues) if f.is_file() and f.endswith('.txt') ])


	def load_json(self, path):
		with open(path, 'r') as f:
			return json.load(f)


	def load_txt(self, path):
		with open(path, 'r') as f:
			return f.readlines()


	def parse_json(self, file_obj):
		previous_participant = None
		previous_message = None
		chat = []
		for m in reversed(file_obj['messages']):
			if 'content' in m:
				if previous_participant == m['sender_name'] and previous_message != None:
					previous_message = previous_message +". "+ m['content']
				else:
					if previous_message != None:
						chat.append(previous_message)
					previous_participant = m['sender_name']
					previous_message = m['content']
			pass
		return chat


	def parse_txt(self, file_obj):
		cleaned_file = []
		for l in file_obj:
			cleaned_file.append(l.rstrip('\n'))
		return cleaned_file


	def train_chatterbot_corpus(self):
		trainer = self.chatterbot_corpus_trainer
		trainer.train("chatterbot.corpus.english")
		print("Training with dataset 'chatterbot.corpus.english' ")


	def train_massanger_corpus(self):
		for d in self.sub_directories:
			print("Loading directory", d)
			for f in reversed(self.get_massanger_files(d)):
				print("Processing file", f)
				chat = self.parse_json(
					self.load_json(self.path_to_massanger+self.slash+d+self.slash+f
					)
				)
				print("Finished processing file", f)
				trainer = self.list_trainer
				print("Training with dataset {} ".format(f))
				trainer.train(chat)
				print("Trained with dataset {} ".format(f))


	def train_dialogues_corpus(self):
		for f in self.get_dialogue_files():
			print("Loading file", f)
			print("Processing file", f)
			chat = self.parse_txt(
				self.load_txt(self.path_to_dialogues+self.slash+f
				)
			)
			print("Finished processing file", f)
			trainer = self.list_trainer
			print("Training with dataset {} ".format(f))
			trainer.train(chat)
			print("Trained with dataset {} ".format(f))


	def console_run_bot(self):

		print('Type something to begin...')

		# The following loop will execute each time the user enters input
		while True:
			try:
				user_input = input()

				bot_response = self.bot.get_response(user_input)

				print(bot_response)

			# Press ctrl-c or ctrl-d on the keyboard to exit
			except (KeyboardInterrupt, EOFError, SystemExit):
				break


	def web_run_bot(self, message):
		return self.bot.get_response(message)

	def get_response(self, message):
		try:
			return self.bot.get_response(message)
		except (KeyboardInterrupt, Exception, EOFError, SystemExit):
			return "I have issues"
