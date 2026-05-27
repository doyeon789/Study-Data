# WSL이란 무엇인가

- Window환경에서 리눅스를 실행할 수 있도록 도와주는 도구
- 윈도우에서 별도의 전통적인 VM을 직접 설치하지 않고도 실행 가능
- 명령어, 파일시스템, 리눅스 도구 사용 가능

# WSL 설치방법

- window10/11 필요
  wsl --install

- 기능 활성화

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

- wsl2기본설정

```
wsl -set-default-version2
```
