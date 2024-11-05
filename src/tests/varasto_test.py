import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.neg_varasto = Varasto(-10, -10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_tyhjan_kun_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.neg_varasto.saldo, 0)

    def test_saldo_taysi_kun_alkusaldo_tilavuutta_suurempi(self):
        varasto = Varasto(1, 2)
        self.assertAlmostEqual(varasto.saldo, 1)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_oikea_tilavuus_kun_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.neg_varasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_ei_lisaa_kun_negatiivinen_arvo(self):
        alkuarvo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, alkuarvo)

    def test_lisays_ei_ylitayta_varastoa(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 10)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivisen_ottaminen_palauttaa_oikein(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0)

    def test_negatiivisen_ottaminen_ei_muuta_saldoa(self):
        alkusaldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, alkusaldo)

    def test_saldoa_suuremman_ottaminen_nollaa_saldon(self):
        self.varasto.ota_varastosta(self.varasto.saldo + 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldoa_suuremman_ottaminen_palauttaa_oikein(self):
        saldo = self.varasto.saldo
        self.assertAlmostEqual(
            self.varasto.ota_varastosta(saldo + 10),
            saldo
            )

    def test_string_muunnos_toimii_oikein(self):
        saldo = self.varasto.saldo
        tilaa = self.varasto.paljonko_mahtuu()
        self.assertEqual(
            str(self.varasto),
            f"saldo = {saldo}, vielä tilaa {tilaa}"
        )

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
