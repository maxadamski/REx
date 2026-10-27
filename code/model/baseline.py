import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class baseline(object):
    def get_baseline_value(self):
        pass
    def update(self, target):
        pass

class ReactiveBaseline(baseline):
    def __init__(self, l):
        self.l = l
        #self.b = tf.Variable( 0.0, trainable=False)
        # Ported to not use tensorflow
        self.b = 0.0
    def get_baseline_value(self):
        # returns the current baseline value
        return self.b
    def update(self, target):
        # updates the baseline value based on the target value reward
        #self.b = tf.add((1-self.l)*self.b, self.l*target)
        # Ported to not use tensorflow
        self.b = (1 - self.l) * self.b + self.l * target