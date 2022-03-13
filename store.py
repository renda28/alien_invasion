class Store():
    """A class to save the all time high score"""

    def __init__(self):
        self.all_time_high_score_filename = "all_time_high_score.txt"

    def save_high_score(self, stats):
        filename = self.all_time_high_score_filename
        with open(filename, 'w') as file_object:
            high_score = str(stats.high_score)
            file_object.write(high_score)

    def read_high_score(self):
        filename = self.all_time_high_score_filename
        with open(filename) as file_object:
            contents = file_object.read()
            return contents
