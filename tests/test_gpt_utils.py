from rewiser.gpt.utils import split_numbered_lines


class TestGPTUtils:
    # TODO: use pytest parameterize to test with more examples
    def test_split_numbered_lists(self):
        text = """1. hello world
        2. hello"""
        splits = split_numbered_lines(text)

        assert splits[0] == "hello world"
        assert splits[1] == "hello"
