# 비트코인 가격 예측

환율, 금리, 외부적 요인, 알트코인 가격과 비트코인 가격을 비교하여 연관이 있을 법한 변수들을 찾아내고자 하였다. 


## 데이터 수집

https://github.com/sharebook-kr/pyupbit  
![1_1](https://user-images.githubusercontent.com/89456014/134462838-3186390a-799f-4b8a-ae1a-82e5f2939117.png)

Pyupbit 패키지를 이용해서 비트코인, 질리카, 코스모스, 에이다, 카이버네트워크, 스트라디스, 온톨로지가스, 밀크, 룸네트크, 모스코인의 일별 가격 데이터를 수집하였다. 코인 선정 기준은
대표 코인인 비트코인과 환화로 구매가 가능한 코인을 시가총액별로 상/중/하 그룹으로 나누고 무작위로 3개씩 추출하였다.

## 데이터 분석

### Part1. 예측 모형을 이용한 비트코인 가격 예측
![2](https://user-images.githubusercontent.com/89456014/134504112-8f3708b7-f3af-4b29-9d76-33af3dc81eff.png)
![3](https://user-images.githubusercontent.com/89456014/134504114-2c710911-b766-41b0-88f1-efe08e0ce0c8.png)
![4](https://user-images.githubusercontent.com/89456014/134504118-edadc0c1-2386-4cdd-a75e-e9a5b27281c1.png)
![5](https://user-images.githubusercontent.com/89456014/134504123-83bdaadd-a312-4eb9-ae84-851af8b980fb.png)
![6](https://user-images.githubusercontent.com/89456014/134504126-e8a04640-e0d9-4397-8df4-45e50c2ac7d6.png)

Facebook에서 공개한 Prophet 모델을 사용하여 6개월 간격으로 비트코인을 예측한 결과이나 예측 결과가 굉장히 불안정함을 알 수 있다.
비트코인 가격 그래프가 예측 가능한 경향성을 보이지 않아 가격 예측이 어려웠던 것으로 판단된다.
***
### Part2. 금리와 코인의 상관관계 분석
![9](https://user-images.githubusercontent.com/89456014/134508367-b81ccf6f-1478-4c5c-a3a7-10e7b7e1719f.png)
![7](https://user-images.githubusercontent.com/89456014/134507681-4033dcb1-bdd0-4ccf-94a8-51dbf6d82bec.png)
![8](https://user-images.githubusercontent.com/89456014/134507690-1e4697a2-2e83-4fb4-818a-6a54c2d77e81.png)

금리가 낮으면 사람들이 돈을 은행에 맡기기보다는 투자를 할 것이라고 예측하여 금리와 비트코인의 상관관계를 분석해 보았으나 상관계수가 굉장히 낮게 나오느 것으로 나타나 큰 연관은 없는 것으로 나타났다.
***

### Part3. 머스크의 트위터 언급과 비트코인 가격 분석
![10](https://user-images.githubusercontent.com/89456014/134553836-2747f5fa-65e5-4e8e-bdcd-79958d566d5e.png)   

네이버와 매일경제 뉴스 기사에서 '일론 머스크 코인'을 키워드로 검색하여 나타나는 모든 기사의 제목, 날짜 URL을 크롤링 하여 전처리하여 엑셀로 저장하였다.   

![11](https://user-images.githubusercontent.com/89456014/134554313-4fa01d35-5962-45fc-b731-b7c51535b2b9.PNG)   

![12](https://user-images.githubusercontent.com/89456014/134554320-ca3f5781-ae24-4b27-9d68-66ecc147e6e9.PNG)   

비트코인, 도지코인 일별 가격 변동 그래프에서 가격이 크게 변동한 일자의 전후 기사를 비교하여 일론 머스크의 발언이 가격에 영향을 미치는지 분석해 보았고, 머스크의 발언이 어느정도 영향이 판단했다.

***
### Part3. 비트코인과 알트코인의 상관관계

![13](https://user-images.githubusercontent.com/89456014/134560342-140ac740-6909-400a-9096-147792f287f5.PNG)   

![14](https://user-images.githubusercontent.com/89456014/134560348-c9fe3700-4f1b-4c31-8acf-4cae5466ad27.PNG)   

![15](https://user-images.githubusercontent.com/89456014/134560351-0d15d181-12aa-4f53-9492-937609fc6a17.PNG)   

비트코인과 거래량을 기준으로 한 상/중/하 각 3개 코인과의 상관관계를 분석하였으나 Ada를 제외하고는 거의 상관이 없다고 나타났다.

