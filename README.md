# Board_crawler

## Requirement & Version
python 3.9.6 <br>
selenium 3.141.0

## Implementation

```
python sitename.py "URL"

## IMPORTANT!! The first argument URL must contain quotes
## ex) python naver.py "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259"
```

### URL condition
Naver news : 카테고리의 카테고리 까지 들어가서 ㅇㅇ <br>
Velog : 특정 저자의 홈페이지 (저자 이름 링크 눌렀을때)

## Result Data Structure

Crawling data is stored as a json file in the data repository.

### Naver
{ <br>
  "title" : String, <br>
  "summary" : String, <br>
  "link" : String, <br>
  "img_link: String, <br>
  "headline": String, <br>
  "img_text": String, <br>
  "content": String <br>
}
 
 ### Velog
 { <br>
  "title" : String, <br>
  "summary" : String, <br>
  "link" : String, <br>
  "img_link: String, <br>
  "content": String <br>
}





