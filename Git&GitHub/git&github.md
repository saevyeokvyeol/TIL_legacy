## 버전 확인 및 이름 설정

```bash
git --version # 버전 확인

git config --global user.name "이름" # 이름 설정
git config --global user.email "이메일" # 이름 설정

git config --global user.name # 설정된 이름 확인
git config --global user.email # 설정된 이메일 확인

git config --global init.defaultBranch 변경브랜치명 # 기본 브랜치 이름 변경: 기본 브랜치는 보통 'main'을 사용
```

## git 초기화, 업로드, 커밋

```bash
git init # 초기화(git 기본 설정)

git add 파일이름 # 특정 파일 스테이지에 올리기
git add . # 변화한 전체 파일 스테이지에 올리기

git commit -m "커밋메시지" # 커밋하기
git log # 로그 확인
```

## git-github 연동

- 이전에 git을 초기화 하지 않았을 경우
    
    ```bash
    echo "# 프로젝트 이름">> README.md
    git init
    git add README.md
    git commit -m "커밋 메세지"
    git remote add origin https://github.com/깃허브사용자명/레퍼지토리명.git
    git push -u origin main
    ```
    
- 이전에 git을 초기화했을 경우
    
    ```bash
    git remote add origin https://github.com/깃허브사용자명/레퍼지토리명.git
    git push -u origin main
    ```