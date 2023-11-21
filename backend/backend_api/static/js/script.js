const ctx = document.getElementById('orders-month-chart');
const ctxx = document.getElementById('products-income-chart');
const ctxxx = document.getElementById('produts-ordered-chart');


fetch('http://127.0.0.1:8000/statistics_data/')
    .then(response => response.json())
    .then(data => setChart(data))
    .catch(error => console.error('Error:', error));



const setChart = (data) => {

    const {products, orderedProduts} = data;
    const ordersData = [];

    orderedProduts.forEach((order) => {
        products.forEach(product => {
            if (product.id === order.product_id){
                ordersData.push({
                    'name': product.name,
                    'quantity': order.quantity
                })
            }
        })
    })

    const mergeQuantities = (array) => {
        const result = {};
        array.forEach((item) => {
          const key = item.name;
          if (result[key]) {
            result[key].quantity += item.quantity;
          } else {
            result[key] = { ...item };
          }
        });
        return Object.values(result);
      };
      

    new Chart(ctx, {
        type: 'bar',
        data: {
            datasets: [{
                label: '№ of product has been ordered',
                data: mergeQuantities(ordersData),
                borderWidth: 0
            }]
        },
        options: {
            parsing: {
                xAxisKey: 'name',
                yAxisKey: 'quantity'
            },
        }
    })


    new Chart(ctxx, {
        type: 'pie',
        data: {
            labels: [
                'Red',
                'Blue',
                'Yellow'
              ],
              datasets: [{
                label: 'My First Dataset',
                data: [300, 50, 100],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)',
                  'rgb(255, 205, 86)'
                ],
                hoverOffset: 4
              }]
        }
    })

    new Chart(ctxxx, {
        type: 'pie',
        data: {
            labels: [
                'Red',
                'Blue',
                'Yellow'
              ],
              datasets: [{
                label: 'My First Dataset',
                data: [300, 50, 100],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)',
                  'rgb(255, 205, 86)'
                ],
                hoverOffset: 4
              }]
        }
    })
}
