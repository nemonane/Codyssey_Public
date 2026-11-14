## 1. Docker 설치
``` powerShell
docker --version

windget install -e --id Docker.DockerDesktop #안깔려있으면 설치 -e는 exact약자

docker --version #버전확인
docker info
docker run hello-world

#안되면 위도우에서 DockerDesktop 실행(Skip만 해도 run됨)
Settings
> Enable integration with default WSL distro >> ON
> Enable integration with additional distro >> UBUNTU
>> Apply & Restart Engine

sudo usermod -aG docker $USER #현재 사용자를 docker 그룹에 추가
exit
wsl --shutdown
wsl

docker run hello-world
```

## 2. 이미지 만들기
```
mkdir DockerTest && cd DockerTest
touch Dockerfile
>> FROM ngnix:latest
>> COPY Index.html /usr/share/nginx/html/Index.html
> 저장(Ctrl + s)
cat Dockerfile

touch Index.html
>> <h1>안녕하세요 Docker!</h1>
>> <p>내가 만든 첫 번째 컨테이너입니다.</p>
> 저장(Ctrl + s)

docker build -t myfirst-image . 
	#현재 폴더에 있는 Dockerfile로 이미지를 만들고 이름은 `myfirst-image`로 해줘
docker images

```

## 3. 컨테이너 실행하기
- 이제 만든 이미지로 실제 실행해보기
```
docker images

docker run -d -p 8080:80 --name myfirst-container myfirst-image

```
- `docker run` : 컨테이너 실행
- `-d` : 백그라운드에서 실행
- `-p 8080:80` : 내 컴퓨터의 8080번 포트를 컨테이너의 80번 포트와 연결
- `--name myfirst-container` : 컨테이너 이름 지정
- `myfirst-image` : 실행할 이미지 이름
- 
```
docker ps #실행된 컨테이너 확인하기
docker ps -a
http://localhost:8080
```

- 자주 쓰는 기본 명령어
```
docker images
docker run -d -p 8080:80 --name myfirst-container myfirst-image
docker ps
docker ps -a
docker stop myfirst-container #컨테이너 중지
docker start myfirst-container #컨테이너 다시 시작
docker rm myfirst-container #컨테이너 삭제
docker rmi myfirst-image

docker logs myfirst-container #컨테이너 로그 확인
docker stats myfirst-container --no-stream # 컨테이너의 cpu,메모리,네트웍사용량을 보여준다.  --no-stream 한번만 측정
```

## 4. 바인드 마운트
- 내 컴퓨터(호스트)의 폴더/파일을 컨테이너 안에 연결해서, 서로 같은 데이터를 보게 하는 것
- docker run -v 내컴퓨터경로: 컨테이너경로 이미지이름
```
docker run -d -p 8080:80 -v $(pwd)/site:/usr/shared/nginx/html nginx:alpine
```
- `$(pwd)/site` : 현재 폴더 안의 `site` 폴더 (내컴퓨터경로)
- `/usr/share/nginx/html` : nginx가 웹 파일을 읽는 폴더 (컨테이너경로)
-  nginx:alpine (이미지이름)
- 즉, **내 컴퓨터의 site 폴더를 nginx 웹 폴더에 연결**
### 결과
- `site/index.html` 을 수정하면
- 브라우저에서 `localhost:8080` 새로고침 시 바로 반영될 수 있어요
이게 바운드 마운트의 가장 큰 장점입니다.