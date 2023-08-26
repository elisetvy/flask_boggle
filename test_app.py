from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            # test that you're getting a template
            self.assertEqual(response.status_code, 200)
            self.assertIn('<table class="board"', html)
            self.assertIn(
                'Test to determine if the board is loaded properly upon game start.', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:

            response = client.post('/api/new-game')
            json = response.get_json()
            id = json.get('gameId')  # should be string
            board = json.get('board')  # should be list

            self.assertIsInstance(id, str)
            self.assertIsInstance(board, list)
            self.assertIn(id, games)

            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # test that the game_id is a string
            # test that the board is a list
            # test that the game_id is in the dictionary of games (imported from app.py above)

    def test_score_word(self):
        """Test if word is valid"""

        with self.client as client:
            ...
            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # find that game in the dictionary of games (imported from app.py above)

            # manually change the game board's rows so they are not random

            # test to see that a valid word on the altered board returns {'result': 'ok'}
            # test to see that a valid word not on the altered board returns {'result': 'not-on-board'}
            # test to see that an invalid word returns {'result': 'not-word'}

    def test_new_game_integration(self):
        """Test """
        with self.client as client:

            response = client.post('/api/new-game')
            json = response.get_json()
            gameId = json.get('gameId')  # should be string
            game = games[gameId]
            games[gameId].board = [
                [
                    "L",
                    "E",
                    "S",
                    "G",
                    "M"
                ],
                [
                    "R",
                    "A",
                    "T",
                    "U",
                    "P"
                ],
                [
                    "W",
                    "G",
                    "L",
                    "K",
                    "I"
                ],
                [
                    "E",
                    "K",
                    "A",
                    "U",
                    "O"
                ],
                [
                    "S",
                    "T",
                    "E",
                    "F",
                    "R"
                ]
            ]

            resp = client.post('/api/score-word',
                        json={'gameId': gameId, 'word': 'RAT'})
            data = resp.get_json()

            self.assertEqual({"result": "ok"}, data)

            resp = client.post('/api/score-word',
            json={'gameId': gameId, 'word': 'sdufshdfjhsd'})
            data = resp.get_json()

            self.assertEqual({"result": "not-word"}, data)
