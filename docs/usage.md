# 사용법

1. 검사는 저장소 루트에서 `./check` 하나다. 로컬과 CI가 같은 명령을 쓴다.
2. `./check`는 `python3 -m unittest discover -s tests -t . -v`를 실행한다.
3. 표준 라이브러리만 쓴다. 따로 설치할 것이 없다.
4. 코드는 `src/`에 둔다. (아직 코드가 없어 폴더도 없다.)
5. 시험은 `tests/`에 둔다. 파일 이름은 `test_*.py`, 방식은 unittest다.
6. 한 파일만 돌리려면 `python3 -m unittest tests.test_boards -v`를 쓴다.
7. 변경은 PR로만 합친다. 자기 PR을 승인하거나 우회 병합하지 않는다.
8. `.github/`, `.agentkit/`, `check`, `AGENTS.md`를 바꾸는 PR은 제목 첫머리에 `[울타리]`를 붙인다.
9. 인증 정보를 저장소·로그·CI에 남기지 않는다.
10. 더 자세한 규칙은 `AGENTS.md`에 있다.
