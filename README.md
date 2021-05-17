# NLP_Review_Classifier

Source Code From https://github.com/kh-kim/simple-ntc in Fastcampus

## 2021년 춘계공동학술대회 발표 _ 대한산업공학회

### 연구 제목 : 딥러닝 기반 텍스트 분류 모델을 활용한 국내 이커머스 사용자 리뷰 분석

#### 연구 순서 정리

1. Data Scrapping
    - Corpus 수집을 위한 데이터 스크래핑
    1. For Modeling _ Sentiment Classifier
    2. For Evaluation _ Sentiment Classifier & For Modeling _ Topic Classifier

2. Labeling
    - Sentiment Classifier Modeling에 필요한 Corpus만 Labeling진행

3. Cleaning
    - Regular Expression을 이용한 전각문자 및 불필요한 특수문자 제거

4. Tokenization
    - mecab을 활용한 tokenize

5. Modeling