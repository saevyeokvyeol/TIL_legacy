# Web Storage

## localStorage

- 만료 기간이 없어 평생 유지됨
- 저장
    
    ```jsx
    localStorage.setItem(key, value);
    // 로컬 스토리지에 키와 밸류 저장
    ```
    
- 호출
    
    ```jsx
    localStorage.length;
    // 로컬 스토리지에 저장된 키와 밸류 갯수 가져오기
    
    localStorage.key(i);
    // i번째 키값 가져오기
    
    localStorage.getItem(key);
    // key에 해당하는 밸류값 가져오기
    ```
    
- 삭제
    
    ```jsx
    localStorage.removeItem(key);
    // key값에 해당하는 키와 밸류 삭제
    
    localStorage.clear();
    // 로컬 스토리지에 저장된 키와 밸류 모두 삭제
    ```
    

## sessionStorage

- 세션이 유지되는 동안(해당 탭이나 창을 완전히 종료할 때까지) 유지됨
- 저장
    
    ```jsx
    sessionStorage.setItem(key, value);
    // 세션 스토리지에 키와 밸류 저장
    ```
    
- 호출
    
    ```jsx
    sessionStorage.length;
    // 세션 스토리지에 저장된 키와 밸류 갯수 가져오기
    
    sessionStorage.key(i);
    // i번째 키값 가져오기
    
    sessionStorage.getItem(key);
    // key에 해당하는 밸류값 가져오기
    ```
    
- 삭제
    
    ```jsx
    sessionStorage.removeItem(key);
    // key값에 해당하는 키와 밸류 삭제
    
    sessionStorage.clear();
    // 세션 스토리지에 저장된 키와 밸류 모두 삭제
    ```