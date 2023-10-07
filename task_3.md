## CLI Tool for Obtaining Information by BIN

___

### Objective
> You need to write a CLI tool that allows interaction with an external service at the link https://stat.gov.kz/api/juridical/counter/api/?bin=bin&lang=ru  
> Write a wrapper around this service.
> You need to pass 2 args:  
>   1. biniin (client's BIN)
>   2. fieldnames (fields that you need to display on the screen)

### Example of Running Your CLI Program
```shell
./searcher.exe --biniin 011240009242 --fieldnames bin okedName
```

### Expected Response from Your CLI Tool
P.S: Output to the terminal (can be done through regular `print` or `pprint.pprint`)
```json
{
  "bin": "011240009242",
  "okedName": "Construction of pipelines for water supply and sewage systems"
}
```

**Example Website Request**  
> https://stat.gov.kz/api/juridical/counter/api/?bin=011240009242&lang=ru

**Example Website Response**
```json
{
    "success": true,
    "obj": {
        "id": 0,
        "bin": "011240009242",
        "name": "TOO \"DAUREN BUILD\"",
        "registerDate": "2001-12-12T18:00:00.000+0000",
        "okedCode": "42212",
        "okedName": "Construction of pipelines for water supply and sewage systems",
        "secondOkeds": "43310,43910,43390,43220,47999,43330",
        "krpCode": "150",
        "krpName": "Small enterprises (41-50)",
        "krpBfCode": "150",
        "krpBfName": "Small enterprises (41-50)",
        "kseCode": "1122",
        "kseName": "National private non-financial corporations – NGOs",
        "kfsCode": "19",
        "kfsName": "Ownership of enterprises without state and foreign participation",
        "katoCode": "751310000",
        "katoId": 268027,
        "katoAddress": "Almaty, Auezov district, Sadovnikova street, house 54",
        "fio": "Smagulova Alfira Taufikovna",
        "ip": false
    },
"description": null
}
```

### Implementation Requirements
> 1. Cache the results of requests (save the result of the request execution to a file).   
> That is, if a BIN is passed that already exists in this file, do not send a request to the external service (https://stat.gov.kz/api/juridical/counter/api/). Immediately return the result, based on the local file.
>   
> 2. If a request to the external service fails with an error, resend the request with an 8-second delay. No more than 3 attempts.  
> If after three attempts you still don't receive a response, raise a ValueError exception.
> 
> 3. Turn your code into an executable (.exe) file with name `searcher`.  
> Write a command that converted your code into an executable file.
