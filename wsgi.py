#whereas this file seems to be where you put any code / functions
from app.main import app
 
if __name__ == "__main__":
        app.run_server(debug=True)

        
wordle_words = pd.read_csv('data/wordle_words.csv')
word_frequency = pd.read_csv('data/unigram_freq.csv')
