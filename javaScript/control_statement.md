

# 제어문

## 조건문

- if문
    
    ```jsx
    // 자바와 if문 구성이 동일함

    if(조건문 1) { // 조건문 1이 true이면 실행문 1 실행
        실행문 1;
    } else if(조건문 2) { // 조건문 1이 false고 실행문 2가 true면 실행문 2 실행
        실행문 2;
    } else { // 조건문 1과 2 모두 false면 실행문 3 실행
        실행문 3;
    }
    ```
    
- switch문
    
    ```jsx
    // 자바와 switch문 구성이 동일함
    
    switch(변수) {
    	case 값: // 변수와 값이 같으면 아래의 실행문 실행
    		실행문 1;
    		break;
    	case 값:
    		실행문 2;
    		break;
    	default: // 변수와 같은 값이 없으면 default 아래의 실행문 실행
    		실행문 3;
    }
    ```
    
## 반복문

- for문
    
    ```jsx
    // 자바와 for문 구성이 동일함
    
    for(초기값; 조건식; 증감식) { // 조건식이 true인 동안 실행
    	실행문;
    }
    ```

- 개선된 for문
    
    ```jsx
    // 자바와 달리 undefined가 아닌(=값이 들어있는) 인덱스의 숫자를 하나씩 꺼내옴
    
    for(let i in 배열명) { // 배열의 인덱스를 하나씩 꺼내옴
    	document.write(배열명[i]); // 배열의 값을 하나씩 꺼내 출력
    }
    ```

- do-while문
    
    ```jsx
    // 자바와 do-while문 구성이 동일함
    
    do { // 조건식이 true인 동안 실행하되, 조건식이 false여도 한 번은 실행
    	실행문;
    } while(조건식)
    ```
    
- switch문
    
    ```jsx
    // 자바와 switch문 구성이 동일함
    
    switch(변수) {
    	case 값:
    		실행문 1;
    		break;
    	case 값:
    		실행문 2;
    		break;
    	default:
    		실행문 3;
    }
    ```