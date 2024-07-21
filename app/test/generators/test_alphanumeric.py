from ...generators.alphanumeric import AlphaNumeric

class AlphaNumericGeneratorTest:
    def test_generate_params(self):
        parameters = { 'length': 9 }
        assert len(AlphaNumeric().generate(parameters)) == 9

    def test_generate_defaults(self):
        assert len(AlphaNumeric().generate({})) == 32

    def test_generate_negative(self):
        assert len(AlphaNumeric().generate({ 'length': -1 })) == 32
