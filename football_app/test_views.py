from django.test import Client, TestCase


class ViewsTestCase(TestCase):

    client = Client()
    league_name = "Premier League"
    home_team = "Home Team"
    opp_team = "Opponents Team"

    def test_create_league(self):
        response = self.client.post('/league/{}/'.format(self.league_name))
        print("Response: {}".format(response.content))
        self.assertEqual(200, response.status_code)
        print("----- End of Test -----\n")

    def test_create_team(self):
        self.client.post('/league/{}/'.format(self.league_name))
        response = self.client.post('/team/{}/{}/'.format(self.league_name, self.home_team))
        print("Response: {}".format(response.content))
        self.assertEqual(200, response.status_code)
        print("----- End of Test -----\n")

    def test_create_match(self):
        self.client.post('/league/{}/'.format(self.league_name))
        self.client.post('/team/{}/{}/'.format(self.league_name, self.home_team))
        self.client.post('/team/{}/{}/'.format(self.league_name, self.opp_team))
        response = self.client.post('/match/{}/{}/{}/{}/'.format(self.home_team, self.opp_team, 1, 0))
        print("Response: {}".format(response.content))
        self.assertEqual(200, response.status_code)
        print("----- End of Test -----\n")

    def test_min_goals(self):
        self.client.post('/league/{}/'.format(self.league_name))
        self.client.post('/team/{}/{}/'.format(self.league_name, self.home_team))
        self.client.post('/team/{}/{}/'.format(self.league_name, self.opp_team))
        self.client.post('/match/{}/{}/{}/{}/'.format(self.home_team, self.opp_team, 2, 1))
        response = self.client.post('/minGoals/{}/'.format(self.league_name))
        print("Response: {}".format(response.content))
        self.assertEqual(200, response.status_code)
        print("----- End of Test -----\n")

    def test_max_wins(self):
        self.client.post('/league/{}/'.format(self.league_name))
        self.client.post('/team/{}/{}/'.format(self.league_name, self.home_team))
        self.client.post('/team/{}/{}/'.format(self.league_name, self.opp_team))
        self.client.post('/match/{}/{}/{}/{}/'.format(self.home_team, self.opp_team, 2, 1))
        response = self.client.post('/maxWins/{}/'.format(self.league_name))
        print("Response: {}".format(response.content))
        self.assertEqual(200, response.status_code)
        print("----- End of Test -----\n")

