## REST APIs

应用程序接口基本上公开为一系列的函数或者property,我们可以使用这些函数或者属性从该系统接收和发送数据，应用程序只是一个黑盒子。

```json
{
  "firstName": "Davey",
  "lastName": "Jones",
  "ship": "Flying Dutchman",
  "lastSeen": 2017,
  "nationality": null
}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <firstName>Davey</firstName>
    <lastName>Jones</lastName>
    <lastSeen>2017</lastSeen>
    <nationality/>
</root>
```

```shell
GET https://.../customer/12345/account/5523?query=balance
→ {"balance": 2123.45, "asOf": "2020-04-05T15:35:45+00:00"}

POST https://.../customer/12345/account/5523
+ {"action": "withdraw", "amount": 100.0}
→ {"balance": 2023.45, "asOf": "2020-04-05T16:00:00+00:00"}
```

### HTTP Status Codes

| 状态码 (Status Code) | 名称 / 含义 (Name / Meaning)             | 描述 (Description)                                           |
| -------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| **2xx**              | **成功 (Success)**                       | **请求已成功处理。**                                         |
| `200`                | OK (成功)                                | 请求已成功。                                                 |
| `201`                | Created (已创建)                         | 资源已成功创建。                                             |
| `202`                | Accepted (已接受)                        | 请求已被接受，但处理尚未完成（异步处理）。                   |
| **4xx**              | **客户端错误 (You did something wrong)** | **请求中存在错误，问题出在客户端。**                         |
| `400`                | Bad Request (错误请求)                   | 服务器无法理解该请求。                                       |
| `401`                | Unauthorized (未认证)                    | 技术上指“**未认证**”(not authenticated)，即用户未登录或未提供有效凭证。 |
| `403`                | Forbidden (禁止访问)                     | 指“**未授权**”(not authorized)，即服务器知道你是谁，但你没有权限访问该资源。 |
| `404`                | Not Found (未找到)                       | 服务器找不到请求的指定资源。                                 |
| **5xx**              | **服务器错误 (Server had an issue)**     | **服务器端出现问题。通常不是你的错！**                       |

------

**注意:** 这只是其中一部分常见的状态码。还有更多状态码，完整的列表可以在维基百科上找到：[List of HTTP status codes](https://www.google.com/url?sa=E&q=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FList_of_HTTP_status_codes)