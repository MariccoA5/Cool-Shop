function add2Cart(product_id) {
  alert(`Added item to the cart!`);
  
  axios.post(`http://127.0.0.1:8000/add-product/${product_id}`)
}