## 🐱 씨의 문제를 해결하기 위한 아이디어

### 고양이씨의 문제 정의
  - 이벤트 URL을 각종 SNS에 공유를 통해 많은 사람들의 유입
  - 여기서 문제는 긴 URL을 공유하려고 함! 따라서 특정 SNS에 업로드 불가 (글자 제한 이슈)
  - 또한 자신이 만든 단축 url 정보들을 가지고 목록을 확인할 수 있어야하며 각 url의 클릭수 정보를 조회하고 싶어함

**👉 단축 URL을 만들어주는 서비스는 위의 기능을 유료로 제공하고 있는 상태**

### 요구사항 정의
  - 긴 URL을 짧게 **단축** 시킬 수 있어야 함.
  - 단축된 URL을 오래 **유지**시킬 수 있어야 함.
  - 만들어진 모든 단축 URL에 대한 목록을 **조회**할 수 있어야 함.
  - 동시에 효과 분석 즉, 모든 공유된 단축 url의 유효 클릭수 및 어디서 유입이 되었는지를 **조회**할 수 있어야 함.

### ☝️ 전제 조건
  - 사용자는 고양이씨 한명이라고 가정
    - 인증 불필요
    - 단축 Url 생성 시 어떤 사용자에 의해서 만들어졌는지에 대한 추가 정보 불필요

### 👊 아이디어
1. 원본 URL을 단축 URL로 변경 프로세스
    - 사용자가 서버에게 "url 단축 요청(post)" 전송
    - 서버는 입력으로 온 url을 단축하여 원본 url과 mapping
    - DB에서는 원본 url과 단축 url 그리고 추가로 만료기간을 포함하여 저장 및 유지
    - 서버는 변환된 단축 url을 사용자에게 응답으로 반환

2. 고양이씨의 단축된 모든 url 정보 조회 프로세스
    - 모든 단축된 url 정보를 보기위해 서버에게 요청(get) 전송
    - 서버는 요청을 받고, DB에 접근해  데이터 반환
    - 예시

저장된 순서(고유ID) | 원본 URL | 단축 URL | 유효 클릭 수 | 공유된 SNS | 만료 기간
-- | -- | -- | -- | -- | --
1 | ... | ... | 23 | kakao | 2022.04.05

3. 짧은 url 클릭 시 실제 url 확인하는 방법
    - 짧게 줄인 url을 get 요청 시 응답으로 'HTTP 30x' 리턴
    - 헤더 'Location :' 정보에 실제 url이 들어가있음.
    - 따라서 전체 body를 리턴하지 말고 HTTP Header Request를 이용하여 헤더의 'Location' 정보만 파싱
    - 불필요한 리소스 사용 감소

4. 원본 url을 단축 url로 인코딩하기
    - DB 저장 시 저장된 순서 즉, int 자료형 고유 ID를 사용해 Base62 또는 Base64로 인코딩
    - 만약 5개의 문자로 단축 url을 만든다면 62^5(64^5)의 크기를 가질 수 있음.
    - base62와 base64의 차이는 ```-```와 ```_```의 포함 유무

5. 단축된 url을 원본 url로 디코딩하기
    - 단축된 url을 디코딩하여나온 10진수 값으로 DB에서 해당 고유ID를 검색 후 원본 url 정보 매핑


