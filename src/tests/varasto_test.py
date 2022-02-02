import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_initialized_with_value_less_than_zero(self):
        self.varasto = Varasto(-10)

        # the tilavuus should be zero
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_initialized_with_saldo_less_than_zero(self):
        self.varasto = Varasto(10, alku_saldo=-10)

        #the saldo should be zero
        self.assertAlmostEqual(self.varasto.saldo, 0)


    def test_alku_saldo_is_greater_than_tilavuus(self):
        self.varasto = Varasto(10, alku_saldo=20)

        #the saldo should equal the tilavuus
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_with_negative_value(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0)

    def test_lisaa_varastoon_negative_value(self):
        self.varasto.lisaa_varastoon(-10)

        #the saldo should not have changed with a negative number
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_value_greater_than_tilavuus(self):
        self.varasto.lisaa_varastoon(20)

        #the saldo should be the same size as tilavuus
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_more_than_saldo(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(20), 10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_self_str(self):
        self.assertEquals(str(self.varasto), "saldo = 0, vielä tilaa 10")
