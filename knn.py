from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import tls_client

NEIGHBORS = 1
X_AUTH_TOKEN = ""

class KNN:
    client = tls_client.Session(client_identifier="Chrome_104")

    def __init__(self, games):
        self.predict = games

    @classmethod
    def get_games(cls):
        cl = cls.client.get("https://api.bloxflip.com/games/towers/history?size=6&page=0", headers={
            'x-auth-token': X_AUTH_TOKEN
        }).json()
        if not cl['success']: return False
        get = [x for x in cl['data']]
        get_not_exploded = sorted(get, key=lambda i: i['exploded'], reverse=False)[0]['towerLevels']
        return cls(get_not_exploded)

    def predict_1(self):
        # generate x
        x_generate = [[0 for i in range(3)] for i in range(8)]
        x = np.array(x_generate)
        y = np.array(self.predict)
        k = KNeighborsClassifier(n_neighbors=NEIGHBORS)
        k.fit(x, y)
        return k.predict(x_generate)


x = KNN.get_games()
print(x.predict_1())
