
#import selenium
import csv
import requests

#get auth token with selenium
def get_session():
    # https://docs.python-requests.org/en/master/user/advanced/
    quizletSession = requests.Session()

    quizletSession.get('https://quizlet.com/583027395/list-41-flash-cards/')
    getQuizletSession = quizletSession.get('https://quizlet.com/cookies')

    print(getQuizletSession.text)
    # '{"cookies": {"sessioncookie": "123456789"}}'

get_session()





#
def get_quizlet_data():
    #grab the data in the quizlet list
    print("done")

get_quizlet_data()