## TODO 

- Unable POST and GET requests to some of the endpoints what are not supposed to get such requests.
- Rename url for orderline and order enpoint 
- Add responses of error to endpoints.
- Add validation to post request of the review on the product must be between 0 and 5
- Validation must be added, when we try to delete a review in Reviews which refers to a product, but there is not any orderline with that product. (So review exists, but orderline does not know about that, and when review is deleted, we update the orderline but we can not find any product with that review)