from scr.questionAnswerHelp import QuestionHelper


class GameManager:

    def __init__(self):
        self.questioner = QuestionHelper('static/riddles.json')
        self.currentRiddle = self.questioner.get_random()
        self.solved = True

    def update_cur_riddle(self):
        self.currentRiddle = self.questioner.get_random()

    def check_if_correct(self, text):
        if self.currentRiddle['a'] in str(text).lower():
            return True
        return False


