import unittest

import numpy as np

from dyson_equalizer.algorithm import marchenko_pastur, marchenko_pastur_cdf


class AlgorithmTestCase(unittest.TestCase):
    def test_marchenko_pastur_cdf(self):
        gamma = .25
        sigma = 2.0

        x = np.linspace(start=0, stop=10, num=1000)
        mp = marchenko_pastur(x, gamma, sigma=sigma)
        mc = marchenko_pastur_cdf(x, gamma, sigma=sigma)

        delta = mp.cumsum() / mp.cumsum()[-1] - mc
        self.assertLess(delta.max(), 0.005 )

        self.assertEqual(0, mc.min())
        self.assertEqual(1, mc.max())



if __name__ == '__main__':
    unittest.main()
