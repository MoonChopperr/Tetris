class Timer:
    def __init__(self, duration, repeated = False, func = None):
        self.repeated = repeated
        self.func = func
        self.duration = duration
        # there is not inbuilt way to create timer in pygame, we check how much time has passed since started
        
