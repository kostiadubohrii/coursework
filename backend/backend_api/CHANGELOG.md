## January 21, 2024 Update

In this update the whole application api has been finished.
This is the list of things that have been done:

### Statistics Page:

> The page has been deleted from server.

### Routes to the endpoint have been changed:

> The main route to the api is `http://127.0.0.1:8000/api/`.

#### Product:

> http://127.0.0.1:8000/api/v1/products/

> http://127.0.0.1:8000/api/v1/products/`id` - returns product by id.

```json
    "status": String,
    "data": [{
            "id": Number,
            "name": String,
            "description": String,
            "price": Number,
            "oldPrice": Number,
            "isApple": Boolean,
            "isActive": Boolean,
            "category": String,
            "mainImage": String(url to image),
            "images": [
                {
                    String(url to image)
                }
            ],
            "meanReview": Number,
            "created_at": String
        }]
```

#### Product's reviews:

> http://127.0.0.1:8000/api/v1/products/reviews/

For`GET` ->

```json
    "status": String,
    "data": [{
        "id": Number,
        "product": Number,
        "user": Numer,
        "review": Number
        }]
```

For `POST` ->

```json
    {
        "product": Number,
        "user": Numer,
        "review": Number
    }
```

> http://127.0.0.1:8000/api/v1/products/reviews/`id` - pass id parameter into url.

Allowed methods: `GET`, `PUT`, `DELETE`

#### Add a new order:

> http://127.0.0.1:8000/api/v1/processorder/

Allowed methods: `POST`

```json
{
  "orderData": {
    "userId": String,
    "orderOn": "yyyy-mm-dd"
  },
  "orderLineData": {
    "products": [
      { "product": Number, "quantity": Number },
    ],
    "totalPrice": Number
  }
}
```

#### Statistics:

> http://127.0.0.1:8000/api/v1/statdata/

Allowed methods: `GET`

```json
    "status": "success",
    "data": [
        {
            "id": Number,
            "name": Name,
            "2024": {
                "revenue": [],
                "sold": []
            }
        }]
```

`revenue` and `sold` store data for each month, starting from Jan to Dec. So there are 12 entities in each of arrays.

> http://127.0.0.1:8000/api/v1/years/

Allowed methods: `GET`

```json
    "status": "success",
    "data": [
        String
        ]
```

## Commit "Orders Validation" (November 15, 2023)

The validation of orders was enhanced and responses to errors were modified.
Main work was focused on validation of orders requests.

Here is an example of the structure of a json file. Explanation is further below.

```json
{
  "orderData": {
    "userId": "2",
    "orderOn": "2023-12-01"
  },
  "orderLineData": {
    "products": [
      { "product": 1, "quantity": 1 },
      { "product": 3, "quantity": 2 }
    ],
    "totalPrice": 308
  }
}
```

### `"orderData"`

- `"userId"` type of the field can be string or digit.
- `"orderOn"` type of the field must be string and must be in form of `YYYY-MM-DD` and must not be in the past date.

### `"orderLineData"`

- `"products"` type of the field must be an array of objects. Each objects has two properties: `"product"` and `"quantity"`.
- - `"product"` is an ID of product, whose type can be string or digit.
- - `"quantity"` type of the field can be string or digit.
- `"totalprice"` type of the field can be string or digit.

## Commit "mean review added to product endpoint" (October 01, 2023)

### Product

- New field `meanReview` is added to product endpoint. The new field contains a mean value of reviews about a product.

When you update or add review, a function called `updateMeanReview` calculates mean review and updates record in product model. <br>
`updateMeanReview` runs after any changes have been done to review. Such as deleted, changed and added.

URL of the reviews endpoint http://127.0.0.1:8000/products/reviews/ <br>

- `GET` and `POST` requests are allowed.
- Json file must contain three fields: "product", "user", "review". An example of it you can find further below<br>

```json
{
  "product": 3,
  "user": 5,
  "review": 4.5
}
```

- `product` type of the field can be string or digit.
- `user` type of the field can be string or digit.
- `review` type of the field must be digit. Also, it must be in 0 to 5.

Futhermore, you can request to each of reviews by http://127.0.0.1:8000/products/reviews/`reviewId`.

- `GET`, `POST`, `PUT` and `DELETE` requests are allowed.
- For `PUT` and `POST` requests a json file must have the same structure as in the example above.
- In `PUT` request `review` field must be changed only.
