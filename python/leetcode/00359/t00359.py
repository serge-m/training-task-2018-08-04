"""
359. Logger Rate Limiter
Easy

s=14
"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.recent = dict()
        self.dt = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        print(self.recent, message, timestamp)
        old_t = self.recent.get(message, -2 * self.dt)
        result = timestamp >= old_t + self.dt
        if result:
            self.recent[message] = timestamp

        return result

    # Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
