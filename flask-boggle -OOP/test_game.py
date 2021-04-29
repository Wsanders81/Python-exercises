from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!



    def test_homepage(self): 
        with app.test_client() as client: 
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('playtimes'))
            self.assertIn("High Score", html)
            self.assertIn("Score", html)
            self.assertIn("Tries", html)


    def test_if_word_is_valid(self): 
        with app.test_client() as client:
            with client.session_transaction() as change_session: 
                
                change_session["board"] = [['E', 'K', 'U', 'Y', 'C'], ['A', 'N', 'K', 'R', 'N'], ['J', 'G', 'A', 'K', 'K'], ['X', 'V', 'E', 'L', 'M'], ['U', 'M', 'L', 'N', 'B']]
                
        res = client.get('/check-for-answer',query_string={"word":"lake"})        
        self.assertEqual(res.status_code, 200)
        #* Route returns a json response so we need to check for it.
        self.assertEqual(res.json['result'], 'ok')



#test_invalid_word(self)
    def test_for_invalid_word(self): 
        with app.test_client() as client: 
            with client.session_transaction() as change_session: 
                change_session["board"] = [['E', 'K', 'U', 'Y', 'C'], ['A', 'N', 'K', 'R', 'N'], ['J', 'G', 'A', 'K', 'K'], ['X', 'V', 'E', 'L', 'M'], ['U', 'M', 'L', 'N', 'B']]

        res = client.get('/check-for-answer',query_string={"word":"ball"}) 
        self.assertEqual(res.json['result'], 'not-on-board') 

    def test_if_not_a_word(self): 
         with app.test_client() as client: 
            with client.session_transaction() as change_session: 
                change_session["board"] = [['E', 'K', 'U', 'Y', 'C'], ['A', 'N', 'K', 'R', 'N'], ['J', 'G', 'A', 'K', 'K'], ['X', 'V', 'E', 'L', 'M'], ['U', 'M', 'L', 'N', 'B']]

         res = client.get('/check-for-answer',query_string={"word":"asdfsa"}) 
         self.assertEqual(res.json['result'], 'not-word') 