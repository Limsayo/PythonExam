import os
import json

class ScoreSaver:
    def __init__(self):
        self.score_file = os.path.join(os.path.dirname(__file__), "../ressources/score.json")

    def add_point(self, user_id: int):
        # Read current scores
        try:
            with open(self.score_file, mode='r', encoding='utf-8') as f:
                data = f.read()
                scores = json.loads(data) if data else {}
        except FileNotFoundError:
            scores = {}
        except Exception:
            scores = {}

        # Update score
        user_id_str = str(user_id)
        scores[user_id_str] = scores.get(user_id_str, 0) + 1

        # Write back to file
        with open(self.score_file, mode='w', encoding='utf-8') as f:
            json.dump(scores, f, indent=4)