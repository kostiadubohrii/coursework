## Commit "CHANGELOG added and some small modifications" (October 01, 2023)

### Change log
* This file contains history of all updates of the this API.


## Commit "mean review added to product endpoint" (October 01, 2023)

### Product
* New field `meanReview` is added to product endpoint. The new field contains a mean value of reviews about a product.

When you update or add review, a function called `updateMeanReview` calculates mean review and updates record in product model. <br>
`updateMeanReview` runs after any changes have been done to review. Such as deleted, changed and added.

The endpoint has url http://127.0.0.1:8000/products/reviews/ <br>
* `GET` and `POST` requests are allowed. 
* Json file must contain three fiels: "product", "user", "review" and loop like this <br>
```json 
{
    "product": 3,
    "user": 5,
    "review": 4.5
}
```
"product" must contain an ID of product to which the new review is added. <br>
"user" must containt as ID of user which leaves that review. <br>
"review" must containt review and a digit. Must be between 0 to 5. <br>


Also, you can request to each of reviews by http://127.0.0.1:8000/products/reviews/"id of review you what to get".
* `GET`, `POST`, `PUT` and `DELETE` requests are allowed.
* Json file must loop the same as the file which is above.
* If you what to make `PUT` request. You need to change only "review" field.
