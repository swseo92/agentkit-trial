"""이 저장소가 적은 판마다 정의 파일이 있고 그 안의 이름이 같다."""
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class BoardFiles(unittest.TestCase):
    def test_each_board_has_its_definition(self):
        boards = tomllib.loads((ROOT / ".agentkit/repo.toml").read_text(encoding="utf-8"))["board"]
        self.assertTrue(boards)
        for board in boards:
            definition = tomllib.loads((ROOT / f".agentkit/boards/{board['name']}.toml").read_text(encoding="utf-8"))
            self.assertEqual(definition["name"], board["name"])


if __name__ == "__main__":
    unittest.main()
