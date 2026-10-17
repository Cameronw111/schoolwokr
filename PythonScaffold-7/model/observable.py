class Observable:
    def __init__(self):
        self.__subscribers = []
    
    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
    
    # Note, the way subscribers are invoked changes from Study 9 to Study 10
    # If you are only up to Study 9, line 17 should be familiar
    # If you are up to Study 10, line 18 is an improvement, and is encouraged
    # You are free to change this method to suit whichever technique you are using
    def notify(self):
        for subscriber in self.__subscribers:
            # subscriber.handle()
            subscriber()
