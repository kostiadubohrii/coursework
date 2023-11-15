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
1. Products statistic: 
* Top 5 popular products(rated by frequecy of purchases)
* The most reliable products (products with high rating). Such products will be rated, once they get more then 5 rivews.
* Number of products. Are they in stock. What is out of stock. 


### Validation
* Products validation - done
* Orders validation:
* * Add validation to post request of the review on the product must be between 0 and 5 - done 
* * validate a date of order on. Must not be past date, must loop line 4digit-2digit-2digit. - done
* * Validate User id must be a digit. Dont bother whether it is sting or number. Also, userID must exist in db - done 
* * Validation of a price of a product - done


### Responses 
* Products - done 
* Orders - done
