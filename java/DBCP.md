# DBCP 기술을 이용한 DB 연동

## 특징

- 연결 객체를 확보해두고 필요 시마다 Client에게 연결해줌
- 미리 Connection을 연결해두기 때문에 속도가 빠름

## 사용 방법(오라클 기준)

- lib에 ojdbc jar 파일 추가
- context.xml 파일에 코드 추가
    
    ```java
    <Resource name="db이름" auth="Container"
    	type="javax.sql.DataSource" driverClassName="드라이버 종류"
    	url="jdbc:oracle:thin:@127.0.0.1:1521:ORCL | xe"
    	username="db계정" password="db계정비밀번호" maxTotal="20" maxIdle="10"
    	maxWaitMillis="-1"/>
    
    /*
    	특정 프로젝트만 적용하고 싶으면 META_INF에 context.xml 파일을 복사해 설정함
    */
    ```
    
- DB를 로드해 사용함