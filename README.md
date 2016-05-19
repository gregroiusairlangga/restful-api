# restful-api

# this is simple restful api using python,flask,postgresql.

doc api:

	obscure-journey-25836.herokuapp.com/api/v1/product.json (product list) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/product/{id}.json (product list with id) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/product/getbysize/{id_size}.json (product list with id size) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/product/getbycolor/{id_color}.json (product list with id color) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/product/filterprice/{pricemin}-{pricemax}.json (product list with id color) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/product.json (insert product list) [POST]
	obscure-journey-25836.herokuapp.com/api/v1/product/{id}.json (patch product list) [PATCH]
	obscure-journey-25836.herokuapp.com/api/v1/product/{id}.json (delete product list) [DELETE]
	obscure-journey-25836.herokuapp.com/api/v1/category.json (category list) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/category/{id}.json (category list with id) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/category.json (insert category product list) [POST]
	obscure-journey-25836.herokuapp.com/api/v1/category/{id}.json (patch category product list) [PATCH]
	obscure-journey-25836.herokuapp.com/api/v1/category/{id}.json (delete category product list) [DELETE]
	obscure-journey-25836.herokuapp.com/api/v1/color.json (color list) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/color/{id}.json (color list with id) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/color.json (insert color product list) [POST]
	obscure-journey-25836.herokuapp.com/api/v1/color/{id}.json (patch color product list) [PATCH]
	obscure-journey-25836.herokuapp.com/api/v1/color/{id}.json (delete color product list) [DELETE]
	obscure-journey-25836.herokuapp.com/api/v1/size.json (size list) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/size/{id}.json (size list with id) [GET]
	obscure-journey-25836.herokuapp.com/api/v1/size.json (insert size product list) [POST]
	obscure-journey-25836.herokuapp.com/api/v1/size/{id}.json (patch size product list) [PATCH]
	obscure-journey-25836.herokuapp.com/api/v1/size/{id}.json (delete size product list) [DELETE]


Local:
	use host:http://127.0.0.1:5000
	http://127.0.0.1:5000/api/v1/product.json

Raw Json to Post and Patch, example:
{
  "data": {
    "type": "users",
    "attributes": {
      "name": "angga",
      "email": "gregorius.airlangga@gmail.com",
      "is_active": "true"
      }
     }
}

{
  "data": {
    "type": "color",
    "attributes": {
      "color": "lavender"
    }
  }  
}

{
  "data": {
    "type": "category",
    "attributes": {
      "category": "seragam batik"
    }
  }  
}

{
  "data": {
    "type": "size",
    "attributes": {
      "color": "LL"
    }
  }  
}

{
  "data": {
    "type": "product",
    "attributes": {
      "name": "baju batik 1",
      "id_size":1,
      "id_color":1,
      "price":90000,
      "id_category":1,
      "gambar":"bajubatik1.jpg"
    }
  }  
}

