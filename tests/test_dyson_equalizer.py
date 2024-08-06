import unittest

import numpy as np

from dyson_equalizer.dyson_equalizer import DysonEqualizer
from dyson_equalizer.examples import generate_Y_with_correlated_noise


class DysonEqualizerTestCase(unittest.TestCase):
    def test_fig_2(self):
        Y = generate_Y_with_correlated_noise()
        de = DysonEqualizer(Y)
        de.compute()

        self.assertEqual(20, de.r_hat)

    def test_transpose(self):
        Y = generate_Y_with_correlated_noise()

        de = DysonEqualizer(Y)
        de.compute()
        det = DysonEqualizer(Y.T)
        det.compute()

        self.assertEqual(20, det.r_hat)
        np.testing.assert_array_almost_equal(de.x_hat, det.y_hat)
        np.testing.assert_array_almost_equal(de.y_hat, det.x_hat)
        np.testing.assert_array_almost_equal(de.Y_hat, det.Y_hat.T)
        np.testing.assert_array_almost_equal(de.X_bar, det.X_bar.T)
        self.assertEqual(de.r_hat, det.r_hat)
        np.testing.assert_array_almost_equal(de.S, det.S)
        np.testing.assert_array_almost_equal(de.S_hat, det.S_hat)


if __name__ == '__main__':
    unittest.main()
