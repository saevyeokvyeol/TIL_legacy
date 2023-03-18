# Log4j

## 특징

- 자바 어플리케이션을 쉽고 빠르게 로깅할 수 있도록 도와주는 오픈소스

## properties 파일 형식

```java
log4j.rootLogger = debug, dailyfile, consoleOut

// 콘솔 출력 형식
log4j.appender.consoleOut = org.apache.log4j.ConsoleAppender

log4j.appender.consoleOut.layout = org.apache.log4j.PatternLayout

log4j.appender.consoleOut.layout.ConversionPattern=%5p ({%t} %F[%M]:%L) [%d] - %m%n

// 파일 기록 형식
log4j.appender.dailyfile = org.apache.log4j.DailyRollingFileAppender

log4j.appender.dailyfile.File = 경로/파일명.log
// 파일 저장 위치와 파일 이름 

log4j.appender.dailyfile.Append = true
// true일 경우 파일 이어쓰기, false일 경우 덮어쓰기

log4j.appender.dailyfile.DatePattern='.'yyyy-MM-dd

log4j.appender.dailyfile.layout = org.apache.log4j.PatternLayout

log4j.appender.dailyfile.layout.ConversionPattern=%5p ({%t} %F[%M]:%L) [%d] - %m%n

```