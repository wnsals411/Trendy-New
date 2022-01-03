- **Python3** 와 **Django**를 통해 제작한 웹페이지입니다.
- 실시간으로 DB에 따라 실시간 검색어, 인기 게시물 순위가 변경되는 **동적인 웹사이트**이며,
- **AWS EC2 Ubuntu Linux 18.08** 버전에서 작업했습니다.
- **RESTful API** 형식을 준수했습니다.

<img width="1427" alt="스크린샷 2021-12-30 오후 5 06 54" src="https://user-images.githubusercontent.com/78847555/147734397-45620ae4-8bc6-442c-997b-6c9575cad706.png">
메인페이지 화면입니다.<br>
좌측에 사이트 내 원하는 페이지로 이동할 수 있는 네비게이션바가 위치하고,<br>
상단부터 구글검색이 가능한 검색바, 구글트렌드, 실시간 검색순위, 게시판 내 인기 게시물이 노출됩니다.
<br><br><br>
<img width="1427" alt="스크린샷 2021-12-30 오후 5 10 18" src="https://user-images.githubusercontent.com/78847555/147734406-c1575bd4-30d8-4227-9bda-522400282d48.png">
검색창에 크리스마스를 검색한 결과입니다.<br>
현재는 네이버와 유튜브 내에서 검색어에 대한 결과만 가져오도록 설정되어있습니다.
<br><br>
<img width="503" alt="스크린샷 2021-12-30 오후 5 12 00" src="https://user-images.githubusercontent.com/78847555/147734409-cc6ff85a-e796-42e7-9b61-94166a05da69.png">
<br>
<img width="1440" alt="스크린샷 2021-12-30 오후 5 13 33" src="https://user-images.githubusercontent.com/78847555/147734410-f9fee86d-7eb4-40c9-a868-05b3c9d0a301.png">
Q&A는 사용자들끼리 익명으로 소통할 수 있는 공간입니다.<br>
사용자는 본인이 원하는 닉네임으로 게시물을 등록할 수 있고 제목, 내용, 닉네임 필터로 원하는 게시물을 검색할 수 있습니다.<br><br>
<img width="1440" alt="스크린샷 2021-12-30 오후 5 16 25" src="https://user-images.githubusercontent.com/78847555/147734412-049a1384-215e-42fc-9d91-52cc7c12b6cc.png">
게시물에 간단한 이미지도 첨부 가능하고 작성시 입력한 비밀번호를 통해 본인의 게시물을 삭제할 수 있습니다.<br><br><br>
<img width="718" alt="스크린샷 2021-12-30 오후 5 17 09" src="https://user-images.githubusercontent.com/78847555/147734413-376a2486-3f49-47b0-a03b-4195df4e874d.png">
관리자는 Django에서 제공하는 관리자 페이지를 통해 사이트 내 모든 내역을 관리할 수 있습니다.
