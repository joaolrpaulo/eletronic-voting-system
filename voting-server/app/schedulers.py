from apscheduler.schedulers.background import BackgroundScheduler
from app import db
import time
import json
from app import rsa_utils
from app import models


def check_for_new_polls():
    conn = db.connect()
    result = conn.execute(
        "SELECT * FROM POLLS WHERE already_counted = 0 and end_ts < ?",
        [int(time.time())]
    )

    for res in result.fetchall():
        poll_id = res[0]
        fraud = 0

        messages = conn.execute(
            "SELECT message FROM messages WHERE poll_id = ?",
            [poll_id]
        )

        votes = [rsa_utils.decrypt(message[0]) for message in messages.fetchall()]

        items_poll = conn.execute(
            "SELECT item_id FROM polls_items WHERE poll_id = ?",
            [poll_id]
        )

        items = [item[0] for item in items_poll.fetchall()]

        items_votes = {}
        for vote in votes:
            vote = models.Vote(json.loads(vote))

            if vote.item in items:
                if vote.item not in items_votes:
                    items_votes[vote.item] = {
                        'count': 0,
                        'identifiers': []
                    }

                items_votes[vote.item]["count"] += 1
                items_votes[vote.item]["identifiers"].append(vote.identifier)

            else:
                fraud += 1

        for key in items_votes:
            with db.begin() as conn2:
                conn2.execute(
                    "UPDATE polls_items SET votes = ? WHERE item_id = ?",
                    [items_votes[key]["count"], key]
                )
                conn2.execute(
                    "UPDATE polls SET already_counted = 1, frauds = ? WHERE poll_id = ?",
                    [fraud, poll_id]
                )
                for identifier in items_votes[key]["identifiers"]:
                    conn2.execute(
                        "INSERT INTO item_votes(item, identifier) VALUES(?, ?)",
                        [key, identifier]
                    )

scheduler = BackgroundScheduler()

scheduler.add_job(check_for_new_polls, 'interval', seconds = 5)