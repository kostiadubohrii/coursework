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
          {"product": 1,
          "quantity": 1},
          {"product": 3,
          "quantity": 2}
         ],
         "totalPrice": 308
    }
}

```

### `"orderData"`
* `"userId"` type of the field can be string or digit.
* `"orderOn"` type of the field must be string and must be in form of `YYYY-MM-DD` and must not be in the past date.

### `"orderLineData"`
* `"products"` type of the field must be an array of objects. Each objects has two properties: `"product"` and `"quantity"`.
* * `"product"` is an ID of product, whose type can be string or digit.
* * `"quantity"` type of the field can be string or digit.
* `"totalprice"` type of the field can be string or digit.


## Commit "mean review added to product endpoint" (October 01, 2023)

### Product
* New field `meanReview` is added to product endpoint. The new field contains a mean value of reviews about a product.

When you update or add review, a function called `updateMeanReview` calculates mean review and updates record in product model. <br>
`updateMeanReview` runs after any changes have been done to review. Such as deleted, changed and added.

URL of the reviews endpoint http://127.0.0.1:8000/products/reviews/ <br>
* `GET` and `POST` requests are allowed. 
* Json file must contain three fields: "product", "user", "review". An example of it you can find further below<br>
```json 
{
    "product": 3,
    "user": 5,
    "review": 4.5
}
```
* `product` type of the field can be string or digit. 
* `user` type of the field can be string or digit. 
* `review` type of the field must be digit. Also, it must be in 0 to 5. 

Futhermore, you can request to each of reviews by http://127.0.0.1:8000/products/reviews/`reviewId`.
* `GET`, `POST`, `PUT` and `DELETE` requests are allowed.
* For `PUT` and `POST` requests a json file must have the same structure as in the example above.
* In `PUT` request `review` field must be changed only.
