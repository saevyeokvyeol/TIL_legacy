# 객체-테이블 매핑

```java
@Entity // hibernate.hbm2ddl.auto 설정에 따라 객체와 대응하는 테이블 생성
@Table(name = "table_test") // 생성할 테이블 이름 변경
public class Table {
	
	@Id // Primary Key 설정
	
	/*
	 * @GeneratedValue: 생성된 컬럼에 자동으로 값을 넣어줄 때 사용
	 * 
	 * strategy: persistence provider가 엔티티 기본키를 생성할 때 사용할 PK 생성 전략
	 *           GenerationType.AUTO - 벤더에 맞춰 hibernate 내부에서 시퀀스를 생성해 할당(기본값)
	 *                                 동일한 hibernate로 생성한 모든 테이블에서 같은 시퀀스 공유
	 *                                 Oracle-SEQUENCE, MySQL-AUTOINCREMENT, MSSQL-IDENTITY
	 *           GenerationType.SEQUENCE - Oracle 시퀀스 사용(Oracle 전용)
	 *                                     반드시 @SequenceGenerator와 함께 사용하지 않으면 
	 *           GenerationType.TABLE - 테이블이 직접 키를 만들어 사용하는 방법(MySQL, MSSQL 전용)
	 *           GenerationType.IDENTITY - MySQL, MSSQL의 IDENTITY 사용(MySQL, MSSQL 전용)
	 * */
	@GeneratedValue(strategy = GenerationType.AUTO)

	/*
	 * @SequenceGenerator: 시퀀스를 생성하는 어노테이션
	 * name: SequenceGenerator 이름
	 *       @GeneratedValue의 strategy 속성이 GenerationType.SEQUENCE일 경우
   *       @GeneratedValue의 generator 속성에 SequenceGenerator 이름을 동일하게 주어야 시퀀스 작동
	 * allocationSize: 시퀀스 숫자 증가치
	 * sequenceName: 실제로 생성될 시퀀스 이름
	 * */
	@SequenceGenerator(name = "SequenceGenerator 이름", allocationSize = 증가치, sequenceName = "시퀀스명")
	private Long pk;

	// 컬럼명, null 허용 여부, 컬럼의 데이터 크기 등 컬럼 설정 변경
	@Column(name = "field_column", nullable = false, length = 100)
	private String fieldColumn;

	/*
	 * @@UpdateTimestamp: insert, update될 때 자동으로 현재 날짜와 시간 설정
	 *                    Date와 LocalDateTime 형식 사용 가능 -> Oracle에 생성될 때는 둘 다 timestamp 타입으로 생성
	 * */
	@CreationTimestamp
	private Date dateColumn;
	
	@UpdateTimestamp // insert, update될 때 자동으로 현재 날짜와 시간 설정, Date와 LocalDateTime 형식 사용 가능
	private LocalDateTime dateColumn; // JAVA LocalDateTime(JDK 1.8 추가) == Oracle timestamp	

	/*
	 * @Temporal: 특정 날짜 입력 시 사용 가능, Date 형식만 사용 가능
	 *            TemporalType.DATE - Date 타입(연/월/일만 입력)으로 컬럼 생성
	 *            TemporalType.TIMESTAMP - TIMESTAMP 타입(연/월/일 시:분:초 입력)으로 컬럼 생성
	 * */
	@Temporal(TemporalType.DATE)
	private Date dateColumn;

	/*
	 * 연관관계 생성 어노테이션: 테이블끼리의 연관관계를 생성하는 어노테이션
	 * 
	 * @ManyToOne - 다:1 연관관계, 즉시 로딩(select 할 때 연관관계 테이블 자동 조인)
	 * @OneToOne - 1:1 연관관계, 즉시 로딩
	 * @OneToMany - 1:다 연관관계, 지연 로딩(필요할 때만 연관관계 테이블 조인, 권장)
	 *              mappedBy = "부모 테이블명=현재 객체의 테이블명" 속성 입력해야 조인 가능
	 * 
	 * 즉시 로딩을 지연 로딩으로 만들기: fetch = FetchType.LAZY 속성 입력(권장)
	 * 지연 로딩을 즉시 로딩으로 만들기: fetch = FetchType.EAGER 속성 입력
	 * */
		@OneToMany(mappedBy = "자식 객체에 생성된 부모 객체 필드명") // 1:다 연관관계 생성
	@JoinColumn(name = "컬럼명") // Foreign Key 이름 변경
	private List<ChildTable> list;

	@ManyToOne(fetch = FetchType.LAZY) // 다:1 연관관계 생성, 지연 로딩 설정
	private Team team;
}
```