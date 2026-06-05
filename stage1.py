import heapq
import time

class Notification:
    def __init__(self, nid, title, ntype, timestamp, unread=True):
        self.id = nid
        self.title = title
        self.type = ntype
        self.timestamp = timestamp
        self.unread = unread

    def score(self):
        weights = {
            "PLACEMENT": 3,
            "RESULT": 2,
            "EVENT": 1
        }

        return weights[self.type] * 1000000000 + self.timestamp


class PriorityInbox:

    def __init__(self, k=10):
        self.k = k
        self.heap = []

    def add_notification(self, notification):

        if not notification.unread:
            return

        score = notification.score()

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, (score, notification.id, notification))
        else:
            if score > self.heap[0][0]:
                heapq.heapreplace(
                    self.heap,
                    (score, notification.id, notification)
                )

    def get_top_notifications(self):

        result = sorted(
            self.heap,
            key=lambda x: x[0],
            reverse=True
        )

        return [item[2] for item in result]


inbox = PriorityInbox(10)

current = int(time.time())

notifications = [
    Notification(1,"Amazon Placement Drive","PLACEMENT",current-500),
    Notification(2,"Mid Exam Results","RESULT",current-400),
    Notification(3,"Coding Event","EVENT",current-300),
    Notification(4,"Microsoft Placement","PLACEMENT",current-100),
    Notification(5,"Semester Results","RESULT",current-50),
]

for n in notifications:
    inbox.add_notification(n)

print("\nTOP PRIORITY NOTIFICATIONS\n")

for n in inbox.get_top_notifications():
    print(f"{n.id} | {n.title} | {n.type}")