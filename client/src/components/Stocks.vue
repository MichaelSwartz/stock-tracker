<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Stocks</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Stock</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">SYMB</th>
              <th scope="col">CurrPrice</th>
              <th scope="col">YestPrice</th>
              <th scope="col">Recc.</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(stock, index) in stocks" :key="index">
              <td>{{ stock.symb }}</td>
              <td>{{ stock.curr_price }}</td>
              <td>{{ stock.yest_price }}</td>
              <td>{{ stock.curr_price - stock.yest_price }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-danger btn-sm">Sell</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      stocks: [],
    };
  },
  methods: {
    getStocks() {
      const path = 'http://localhost:5000/stocks';
      axios.get(path)
        .then((res) => {
          this.stocks = res.data.stocks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getStocks();
  },
};
</script>
