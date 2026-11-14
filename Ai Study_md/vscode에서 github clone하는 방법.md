좋아요! 아래처럼 메모해두면 나중에 다시 할 때 헷갈리지 않습니다.

# GitHub Repository를 VS Code로 Clone하는 방법

## 1. GitHub에서 Repository 주소 복사

1. GitHub에서 가져올 repository 페이지로 이동
2. 초록색 **Code** 버튼 클릭
3. **HTTPS** 선택
4. 주소 복사

예시:

```text
https://github.com/본인아이디/Repository이름.git
```

예:

```text
https://github.com/nemonane/Codyssey_Public.git
```

---

## 2. VS Code 열기

VS Code를 실행합니다.

터미널을 엽니다.

```text
Terminal > New Terminal
```

또는 단축키:

```text
Ctrl + `
```

---

## 3. 저장할 위치로 이동

Repository를 저장하고 싶은 폴더로 이동합니다.

예시:

```powershell
cd D:\codyssey 01
```

현재 위치 확인:

```powershell
pwd
```

폴더 안의 내용 확인:

```powershell
dir
```

---

## 4. GitHub Repository Clone하기

복사한 주소를 사용해서 clone합니다.

```powershell
git clone https://github.com/본인아이디/Repository이름.git
```

예시:

```powershell
git clone https://github.com/nemonane/Codyssey_Public.git
```

성공하면 이런 메시지가 나옵니다.

```text
Cloning into 'Codyssey_Public'...
Receiving objects: 100%, done.
```

---

## 5. Clone된 폴더로 이동

clone이 완료되면 repository 이름과 같은 폴더가 생깁니다.

```powershell
cd Repository이름
```

예시:

```powershell
cd Codyssey_Public
```

현재 위치가 이렇게 바뀌면 성공입니다.

```powershell
PS D:\codyssey 01\Codyssey_Public>
```

---

## 6. GitHub 연결 확인

아래 명령어로 GitHub repository와 연결되었는지 확인합니다.

```powershell
git remote -v
```

정상 예시:

```text
origin  https://github.com/nemonane/Codyssey_Public.git (fetch)
origin  https://github.com/nemonane/Codyssey_Public.git (push)
```

이렇게 나오면 GitHub와 연결된 상태입니다.

---

## 7. VS Code에서 Clone한 폴더 열기

### 방법 A: 명령어로 열기

clone된 폴더 안에서:

```powershell
code .
```

`code .`는 “현재 폴더를 VS Code로 열기”라는 뜻입니다.

---

### 방법 B: 메뉴로 열기

VS Code 상단 메뉴에서:

```text
File > Open Folder...
```

그다음 clone된 폴더를 선택합니다.

예시:

```text
D:\codyssey 01\Codyssey_Public
```

---

## 8. 주의할 점

### Clone과 Publish 차이

| 기능 | 의미 |
|---|---|
| Clone | GitHub에 있는 repository를 내 컴퓨터로 가져오기 |
| Publish Branch | 내 컴퓨터의 로컬 작업물을 GitHub에 올리기 |

기존 GitHub repository를 가져올 때는 **Clone**을 사용합니다.

---

## 자주 쓰는 명령어 정리

```powershell
pwd
```

현재 위치 확인

```powershell
dir
```

현재 폴더 안의 파일/폴더 확인

```powershell
cd 폴더명
```

해당 폴더로 이동

```powershell
git clone GitHub주소
```

GitHub repository 가져오기

```powershell
git remote -v
```

GitHub 연결 주소 확인

```powershell
code .
```

현재 폴더를 VS Code로 열기

---

## 전체 예시

```powershell
cd D:\codyssey 01
git clone https://github.com/nemonane/Codyssey_Public.git
cd Codyssey_Public
git remote -v
code .
```

---

여기까지 하면 **GitHub repository를 VS Code로 가져오기(Clone)** 완료입니다.  
잘 정리해두면 다음부터는 정말 빠르게 할 수 있어요.