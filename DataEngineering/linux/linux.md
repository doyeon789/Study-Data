# 유닉스(UNIX)

- 리눅스가 탄생하기 이전 운영체제
- 라이선스 비용이 비쌌음

# 리눅스(Linux)

- 무료 유닉스 개념
- 유닉스와 거의 동일한 운영체제
- 오픈소스 기반 운영체제

---

# 커널(Kernel)

- 운영체제의 핵심 구성요소
- 하드웨어와 응용 프로그램 사이를 중재하는 역할

---

# 장점

- 무료 & 오픈소스
- 가볍고 빠른 성능
- GUI 없이 CLI 중심 운영 가능
- 서버 점유율이 높음
- 개발환경(`git`, `docker`, `python`, `node.js` 등)이 대부분 리눅스 친화적

---

# root 사용자란?

- 최고 권한(Superuser)을 가진 계정
- 시스템의 모든 파일, 설정, 사용자 계정 등에 제약 없이 접근 가능

| 기능 | 일반 사용자 | root 사용자 |
|---|---|---|
| 시스템 파일 수정 | X | O |
| 새로운 프로그램 설치 | X | O |
| 다른 사용자 계정 관리 | X | O |
| 커널 모듈 수정 | X | O |

## root 권한 사용 시 주의점

- 실수로 중요한 시스템 파일 삭제 가능
- 잘못된 명령어로 OS 자체를 망가뜨릴 위험 존재
- 외부 공격자가 root 권한을 얻으면 시스템 전체 장악 가능
- 실무에서는 root로 직접 작업하지 않고, 필요한 경우에만 `sudo` 사용

## root 사용자 권한 전환

```bash
sudo -i
```

---

# Linux 기본 명령어

## 파일 생성, 편집, 복사, 삭제

| 명령어 | 설명 | 예시 | 비고 | 약자 의미 |
|---|---|---|---|---|
| pwd | 현재 디렉토리 경로 확인 | `pwd` | 터미널 기준 작업 위치 파악 | Print Working Directory |
| ls | 현재 디렉토리 목록 보기 | `ls -l`, `ls -a` | `-l`: 자세히, `-a`: 숨김 포함 | List |
| cd | 디렉토리 이동 | `cd ~`, `cd ..` | `..`: 상위 디렉토리 | Change Directory |
| mkdir | 새 폴더 생성 | `mkdir my_folder` | 여러 개 생성 가능: `mkdir a b c` | Make Directory |
| rmdir | 빈 폴더 삭제 | `rmdir my_folder` | 폴더가 비어 있어야 함 | Remove Directory |
| rm -r | 폴더 포함 삭제 | `rm -r my_folder` | 실수 방지 필요 | Remove (recursive) |
| touch | 빈 파일 생성 | `touch test.txt` | 새 파일 생성 | Touch |
| cp | 파일/폴더 복사 | `cp a.txt b.txt` | `-r` 옵션으로 폴더 복사 | Copy |
| mv | 파일/폴더 이동 및 이름 변경 | `mv a.txt dir/` | 파일 이름 변경 가능 | Move |
| cat | 파일 내용 출력 | `cat test.txt` | 간단한 파일 확인 | Concatenate |
| clear | 터미널 화면 정리 | `clear` | 화면 초기화 | Clear Screen |

## 명령어 연결 & 데이터 흐름

| 명령어 | 설명 | 예시 | 비고 | 약자 의미 |
|---|---|---|---|---|
| touch | 빈 파일 생성 | `touch test.txt` | 수정 시간 갱신용으로도 사용됨 | touch = 접촉하다(시간 변경) |
| echo | 문자열 출력 / 파일에 저장 | `echo "Hello" >> hi.txt` | `>>` : 이어쓰기 | echo = 메아리처럼 출력 |
| cat | 파일 내용 출력 | `cat file.txt` | 대용량 파일은 `less`, `more` 추천 | Concatenate |
| head, tail | 처음 / 끝 일부 출력 | `head -n 3 file.txt` | 로그 확인에 유용 | Head/Tail (머리/꼬리) |
| cp | 파일 / 폴더 복사 | `cp a.txt b.txt`<br>`cp -r dir1 dir2` | 디렉토리 전체 복사 가능 | Copy |
| mv | 이동 또는 이름 변경 | `mv a.txt new.txt` | 파일 위치 이동에도 사용 | Move |
| rm | 파일 삭제 | `rm test.txt` | `rm -rf` 사용 주의 | Remove |


## 검색과 필터링

| 구분 | 기호 | 역할 | 동작 방식 | 예시 | 설명 |
|---|---|---|---|---|---|
| 파이프 | `\|` | 데이터 전달 | stdout->stdin | `cat log.txt \| grep ERROR` | 앞 결과를 뒤 명령어 입력으로 전달 |
| AND | `&&` | 조건 실행(성공 시) | 성공하면 다음 실행 | `mkdir test && cd test`| 앞 명령 성공 시만 실행
| OR | `\|\|` | 조건 실행(실패 시) | 실패하면 실행 | `mkdir test \|\| echo fail`| 실패 시 대체 실행 |
| 세미콜론 | `;` | 무조건 실행|`cmd1; cmd2`|성공 여부와 관계없이 실행|

| 명령어 | 설명 | 예시 | 비고 | 약자 의미 |
|---|---|---|---|---|
| grep | 특정 문자열 검색| `grep "ERROR" log.txt` | 로그 분석에 필수 | Global Regular Expression Print|
| find | 파일 검색 | `find -name "*.txt"` | 위치별 조건 검색 | Find |
| history | 명령어 기록 확인 | `history` | 이전 명령 복기 | History |


## 시스템 정보 및 프로세스

| 명령어 | 설명 | 예시 | 비고 | 약자 의미 |
|---|---|---|---|---|
| ps aux | 전체 프로세서 확인 `ps aux`, `ps aux grep python` | 자원 소비 확인 | `PS - process`,`A - All users`, `U - User-oriented format`, `X - No controlling terminal` |
| kill | 프로세스 종류 | `kill 1234` | -9 옵션은 강제 종료 | Kill |
| top | 실시간 자원 모니터링 | top, q로 종료 | htop은 GUI버전 | Top of Process|
| uptime | 시스템 가동 시간 | uptime | 부팅 이후 시간확인 | Up Time | 
| whoami | 현재 사용자 확인 | whoami | 스크립트에서 유용 | Who am I | 
| hostname | 호스트명 확인 | hostname | 네트워크 확이네 사용 |  Host Name | 


## 사용자 권한 및 보안
| 명령어 | 설명 | 예시 | 비고 | 약자 의미 |
|---|---|---|---|---|
| sudo | 관리자 권한 명령 | sudo apt update | root 권한 필요 시 | Superuser Do |
| sudo -i | root 전환 | sudo -i, su -root | 환경 유지하며 root전환, su -root는 root pw 지정 후 이용| Interactive shell |
| chmod | 파일 권한 변경 | chmode 755 run.sh | 실행 권한 등 설정, 조심해서 사용 | Change Mode |
| chown | 파일 소유자 변경 | sudo chown user file.txt | 조심해서 사용 | Change Owner | 


### chmod (Change Mode)
- 리눅스에서는 각 파일/디렉토리이ㅔ 대래 다음 3가지 주체에 대한 권한을 따로 설정할 수 있다.

- 주체
 - u(user) - 파일의 소유자
 - g(group) - 파일이 속한 그룹
 - o(other) - 그 외 사용자

- 권한 
 - r(read) - read(내용 보기 가능)
 - w(write) - write(수정, 삭제 가능)
 - x(excute) - execute (실행 가능, 디렉토리 접근 포함)

예시:
|U|||G|||O|||
|---|---|---|---|---|---|---|---|---|
|r|w|x|r|w|x|r|w|x|
|r|w|-|r|-|-|r|-|-|
|4|2|0|4|0|0|4|0|0|

데이터는 644권한을 가지고 있으며
사용자는 읽기와 쓰기,
그룹은 읽기 전용
기타 사용자도 읽기 전용

## CLI 환경 관련 유용 명령어

| 명령어 | 설명 | 예시 | 비고 | 약자 의미 |
|---|---|---|---|---|
| clear | 터미널 화면 초기화 | clear | 화면 정리용 | Clear |
| man | 매뉴얼 보기 | man grep, q로 종료 | 대부분 명령어 지원 | Manual |