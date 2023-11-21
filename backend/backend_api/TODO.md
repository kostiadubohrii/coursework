## TODO 

- Validation must be added, when we try to delete a review in Reviews which refers to a product, but there is not any orderline with that product. (So review exists, but orderline does not know about that, and when review is deleted, we update the orderline but we can not find any product with that review)
- Represent date time in products endpoint in normal form

### User api 
- User have a number of favourites product(liked products)
- User have a number of orders
- User have a number of products in basket
- Information about single user that has addresses, passwork, name, phonenumber, email, postcode.
- Validation must be providedto all of these attributes.

### Display statistics
1. Products statistics
2. Orders statistics
3. Users statistics 