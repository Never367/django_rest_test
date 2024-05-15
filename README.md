# Mini-app for test task

To start the project, run the `docker-compose up` command in the root folder of the project.

1. The files are parsed when the `docker-compose up` command is executed. The data is saved to the database ;
2. When querying on url `http://localhost:8000/api/products/<int:pk>/` you can get json data of a product by its id (ASIN, Title) and Reviews of this product with pagination.
This request is cached ;
3. When requesting at url `http://localhost:8000/api/create_review_for_product/<int:pk>/` a POST request is sent to the database to write a new Review for the product (for its id) .

Thanks for a good test assignment.