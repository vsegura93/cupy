from unittest import TestCase
from linear_model import LinearModel
from chainer.optimizers import AdaDelta

class TestAdaDelta(TestCase):
    def setUp(self):
        self.optimizer = AdaDelta()
        self.model = LinearModel(self.optimizer)

    def test_linear_model_cpu(self):
        self.assertGreater(self.model.accuracy(False), 0.8)

    def test_linear_model_gpu(self):
        self.assertGreater(self.model.accuracy(True), 0.8)
