# 비트코인 가격 예측

환율, 금리, 외부적 요인, 알트코인 가격과 비트코인 가격을 비교하여 연관이 있을 법한 변수들을 찾아내고자 하였다. 


## 데이터 수집

https://github.com/sharebook-kr/pyupbit  
![1_1](https://user-images.githubusercontent.com/89456014/134462838-3186390a-799f-4b8a-ae1a-82e5f2939117.png)

Pyupbit 패키지를 이용해서 비트코인, 질리카, 코스모스, 에이다, 카이버네트워크, 스트라디스, 온톨로지가스, 밀크, 룸네트크, 모스코인의 일별 가격 데이터를 수집하였다. 코인 선정 기준은
대표 코인인 비트코인과 환화로 구매가 가능한 코인을 시가총액별로 상/중/하 그룹으로 나누고 무작위로 3개씩 추출하였다.

## 데이터 분석
* Part1. 예측 모형을 이용한 비트코인 가격 예측

![2](https://user-images.githubusercontent.com/89456014/134503181-a2a14da8-72cd-478c-8682-27a8213080a7.png)
![3](https://user-images.githubusercontent.com/89456014/134503186-078f01b6-f066-4b60-a826-132c9ce1afcb.png)
![4](https://user-images.githubusercontent.com/89456014/134503190-afb7229d-7008-459e-9fc8-57ebb178574b.png)
![5](https://user-images.githubusercontent.com/89456014/134503195-86796131-31c4-476a-9b5c-493e7a09404d.png)
![6](https://user-images.githubusercontent.com/89456014/134503199-48e02f7c-97b0-4eb0-8564-d8e0a1ee3c90.png)
