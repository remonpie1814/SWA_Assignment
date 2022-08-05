# 📝 bicsubi_core_api


###### API Reference
<details markdown="1">
<summary>현재 날씨</summary>

<details markdown="1" style="margin-left:14px">
<summary>/weather</summary>

**현재 날씨 보기**
----
현재 기온과 바람세기를 표시합니다.

* **URL**

  /weather

* **Method:**

  `GET`


* **Data Params**

  **Required:**

  `API KEY=[String] - API KEY`  
  `lat=[Float] - 위도`  
  `lon=[Float] - 경도`  


* **Response**

  `current_region=[String] - 현재 지역`  
  `current_temperture=[Float] - 현재 기온(섭씨)`  
  `current_windspeed=[Float] - 현재 바람 세기(m/s)`  
 

* **Success Response:**
```
HTTP/1.1 200 OK
```
</details>
</details>

<details markdown="1">
<summary>무기</summary>

<details markdown="1" style="margin-left:14px">
<summary>/weapon</summary>

**무기 일람**
----
빅수비가 갖고 있는 무기의 일람을 조회합니다.

* **URL**

  /weapon

* **Method:**

  `GET`

* **Response**

  `weapon_view.html` 
 

* **Success Response:**
```
HTTP/1.1 200 OK
```
</details>

<details markdown="1" style="margin-left:14px">
<summary>/weapon/create</summary>

**무기 추가**
----
무기 일람에 무기를 추가합니다.
추가하는 내용은 Form 형식으로 입력합니다.

* **URL**

  /weapon/create

* **Method:**

  `POST`

* **Data Params**

  **Form Required:**
 
  `name=[String] - 무기 이름`  
  `stock=[Integer] - 수량`  


* **Success Response:**
```
"POST /weapon/create/ HTTP/1.1" 302
"GET /weapon/ HTTP/1.1" 200
```

</details>

<details markdown="1" style="margin-left:14px">
<summary>/weapon/update</summary>

**무기 수정**
----
무기의 이름이나 수량을 수정합니다.
수정하는 내용은 Form 형식으로 입력합니다.

* **URL**

  /weapon/update/{weapon_id}

* **Method:**

  `POST`

* **Data Params**

  **Form Required:**
 
  `name=[String] - 수정할 무기 이름`  
  `stock=[Integer] - 수정할 수량`  
 

* **Success Response:**
```
"POST /weapon/update/{weapon_id} HTTP/1.1" 302
"GET /weapon/ HTTP/1.1" 200
```

</details>

<details markdown="1" style="margin-left:14px">
<summary>/weapon/delete/{weapon_id}</summary>


**무기 삭제**
---- 
특정한 무기를 삭제합니다.

* **URL**

  /weapon/delete/{weapon_id}

* **Method:**

  `POST`

* **Success Response:**
```
"POST /weapon/delete/{weapon_id} HTTP/1.1" 302
"GET /weapon/ HTTP/1.1" 200
```

</details>
</details>


<details markdown="1">
<summary>echo</summary>

<details markdown="1" style="margin-left:14px">
<summary>/echo</summary>

**문자열 표시**
----
문자열을 표시합니다.

* **URL**

  /echo?string={string}

* **Method:**

  `GET`

* **Data Params**

  **Required:**
 
  `string=[String] - 표시할 내용` 
 
* **Response**

  **Required:**

  `value=[String] - 입력받은 문자열`


* **Success Response:**
```
"GET /echo?string={string} HTTP/1.1" 200
```
</details>
</details>

<details markdown="1">
<summary>whoami</summary>

<details markdown="1" style="margin-left:14px">
<summary>/whoami</summary>

**github id**
----
github id를 표시합니다.

* **URL**

  /whoami

* **Method:**

  `GET`
 
* **Response**

  `{"name": "yeji1814"}`


* **Success Response:**
```
"GET /whoami/ HTTP/1.1" 200
```
</details>
</details>