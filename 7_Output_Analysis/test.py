from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 한글 폰트 패스로 지정
import matplotlib.font_manager as fm
import re
import collections

text = """지금 알고 있는 걸 그때도 알았더라면
내 가슴이 말하는 것에 더 자주 귀를 기울였으리라.
더 즐겁게 살고, 덜 고민했으리라.
금방 학교를 졸업하고 머지않아 직업을 가져야 한다는 걸 때달았으리라.
아니, 그런 것들은 잊어 버렸으리라.
다른 사람들이 나에 대해 말하는 것에는
신경쓰지 않았으리라.
그 대신 내가 가진 생명력과 단단한 피부를 더 가치있게 여겼으리라.

더 많이 놀고, 덜 초조해 했으리라.
진정한 아름다움은 자신의 인생을 사랑하는 데 있음을 기억했으리라.
부모가 날 얼마나 사랑하는가를 알고
또한 그들이 내게 최선을 다하고 있음을 믿었으리라.

사랑에 더 열중하고
그 결말에 대해선 덜 걱정했으리라.
설령 그것이 실패로 끝난다 해도
더 좋은 어떤 것이 기다리고 있음을 믿었으리라.

아, 나는 어린아이처럼 행동하는 걸 두려워하지 않았으리라.
더 많은 용기를 가졌으리라.
모든 사람에게서 좋은 면을 발견하고
그것들을 그들과 함께 나눴으리라.

지금 알고 있는 걸 그때도 알았더라면
나는 분명코 춤추는 법을 배웠으리라.
내 육체를 있는 그대로 좋아했으리라.
내가 만난 사람을 신뢰하고
나 역시 누군가에게 신뢰할 만한 사람이 되었으리라.

입맞춤을 즐겼으리라.
정말로 자주 입을 맞췄으리라.
분명코 더 감사하고,
저 많이 행복해 했으리라.
지금 알고 있는 걸 그때도 알았더라면.
"""

spwords = set(STOPWORDS)
# 워드 클라우드를 설정합니다. 한글폰트 사용
# text string 사용
wc1 = WordCloud(max_font_size=200, stopwords=spwords, font_path='C:/Windows/Fonts/NanumGothic.ttf',
                background_color='white', width=800, height=800)
wc1.generate(text)

plt.figure(figsize=(10, 8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()
